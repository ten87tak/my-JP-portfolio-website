import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="form"):
    email_address = st.text_input("メールアドレスをご入力ください： "
                                  "送信ボタンを押したあと、ご入力いただいたメールアドレスに確認メールなどが自動で送信されることはありません。"
                                  "メールアドレスは管理者宛てにメッセージの一部として送信されます。"
                                  "メッセージを受領後、ご連絡させていただきます。")
    raw_message = st.text_area("メッセージ：")
    message = f"""\
    Subject: New email from {email_address}
    
    From: {email_address}
    {raw_message}
    """
    submit_button = st.form_submit_button("送信")
    print(submit_button)

    if submit_button:
        send_email(message)
        st.info("メッセージが送信されました (*^^*)")

