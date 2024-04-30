import streamlit as st
import pandas
from send_email import send_email

st.header("Contact Us")

df=pandas.read_csv("C:/Users/Dell/OneDrive/Documents/Python/app-companywebsite/topics.csv")

with st.form(key="contactus"):
    user_email=st.text_input("Your Email Address")
    user_choice=st.selectbox(f"What topic do you want to discuss?", df["topic"])
    raw_message=st.text_area("Text")
    message=f"""\
Subject: New email from {user_email}



From:{user_email}
\
Topic:{user_choice}
{raw_message}
"""
    button=st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your Message is Successfully delivered!")