FATHA = "\u064E"
DAMMA = "\u064F"
KASRA = "\u0650"
TANWEEN_DAMM = "\u064C"

SAFE_PREPOSITIONS = ["من", "إلى", "عن", "على", "في"]
INNA_SISTERS = ["إن", "أن", "كأن", "لكن", "ليت", "لعل"]

AI_MODEL_KNOWLEDGE = {
    "بالبيت": "بِالْبَيْتِ",
    "يذاكر": "يُذَاكِرُ",
    "كتب": "كَتَبَ",
    "حفظ": "حَفِظَ",
    "العلم": "الْعِلْمُ",
    "نور": "نُورٌ",
    "ذهب": "ذَهَبَ",
    "بالسيارة": "بِالسَّيَّارَةِ",
    "المسجد": "الْمَسْجِدُ",
    "كبير": "كَبِيرٌ",
    "الطالب": "الطَّالِبُ",
    "المدرسة": "الْمَدْرَسَةُ",
}

def call_ai_model(word):
    return AI_MODEL_KNOWLEDGE.get(word, word)

def expert_system_diacritizer(sentence):
    words = sentence.split()
    diacritized_words = []
    i = 0 
    while i < len(words):
        current_word = words[i]
        
        if current_word in SAFE_PREPOSITIONS and i + 1 < len(words):
            next_word_raw = words[i+1]
            next_word_formed = call_ai_model(next_word_raw)
            # نستخدم TANWEEN_DAMM هنا للتنظيف
            final_word = next_word_formed.rstrip(FATHA+DAMMA+KASRA+TANWEEN_DAMM) + KASRA
            diacritized_words.append(current_word)
            diacritized_words.append(final_word)
            i += 2 

        elif current_word in INNA_SISTERS and i + 1 < len(words):
            next_word_raw = words[i+1]
            next_word_formed = call_ai_model(next_word_raw)
            final_word = next_word_formed.rstrip(FATHA+DAMMA+KASRA+TANWEEN_DAMM) + FATHA
            diacritized_words.append(current_word)
            diacritized_words.append(final_word)
            i += 2

        else:
            analyzed_word = call_ai_model(current_word)
            diacritized_words.append(analyzed_word)
            i += 1 

    return " ".join(diacritized_words)

if __name__ == "__main__":
    print(expert_system_diacritizer('ذهب الطالب إلى المدرسة بالسيارة'))
    print(expert_system_diacritizer('إن العلم نور'))