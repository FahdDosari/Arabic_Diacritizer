import streamlit as st
from logic import expert_system_diacritizer

st.set_page_config(page_title="المُشكِّل الهجين", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .main-title {
        font-size: 35px;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 20px;
    }
    .result-box {
        background-color: #F0F4F8;
        border-right: 5px solid #1E3A8A;
        padding: 20px;
        font-size: 28px;
        font-weight: bold;
        color: #2D3748;
        border-radius: 5px;
        margin-top: 20px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>🌟 تطبيق المُشكِّل العربي الذكي</div>", unsafe_allow_html=True)

input_text = st.text_area("أدخل النص العربي (بدون حركات):", height=150, placeholder="مثلاً: إن العلم نور")

if st.button("شَكِّلِ النَّصَّ"):
    if input_text.strip():
        with st.spinner('جاري معالجة النص...'):
            output = expert_system_diacritizer(input_text)
            st.markdown("### النتيجة:")
            st.markdown(f"<div class='result-box'>{output}</div>", unsafe_allow_html=True)
    else:
        st.warning("يرجى إدخال نص أولاً.")

st.sidebar.title("عن المشروع")
st.sidebar.info("نظام هجين للتشكيل الآلي يجمع بين القواعد النحوية والقاموس الذكي.")