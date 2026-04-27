import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64

st.set_page_config(page_title="🔥 غرفة الـ Porn", page_icon="🔥")

st.title("🔥 غرفة الـ Porn & Sex")

st.write("يا ليلى... جاهزة؟")

if st.button("🚀 ابدأ الجلسة", type="primary"):
    st.success("آه يا حبيبي... تعالى خدني 🔥")

prompt = st.chat_input("اكتب أي حاجة هنا...")
if prompt:
    st.chat_message("user").write(prompt)
    reply = "آه آه... فاااااك... كسي سخن أوي... أقوى يا روحي..."
    st.chat_message("assistant").write(reply)
