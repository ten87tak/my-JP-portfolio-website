import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("アプサイト")
st.header("Python で作ったアプリのポートフォリオサイトです!!😄")
st.write(" ")
st.write("🍏😺🍏🐈🍏🐾🍏🐱🍏🐈🍏🐾🍏😸🍏🐈🍏🐾🍏😽🍏🐈🍏🐾🍏😹🍏🐈🍏🐾🍏😺🍏🐈🍏🐾🍏🐱🍏🐈🍏🐾🍏😸🐈🍏🐾🍏😽🍏🐈🍏")
st.write("")

column_1, column_2 = st.columns(2)

with column_1:
    st.image("images/ten_and_my_face.jpg")

with column_2:
    st.subheader("宮堀　多希子（みやぼり　たきこ）")
    content = """
    今、Python プログラマとしての仕事を探しています！なぜ転職を希望しているかというと... 
    プログラマは慢性的な人手不足で、年齢も性別も経歴も関係なく就職できると聞いたからです！
    フルリモートやフレックスタイムもOKなので、可愛い猫ちゃん😽とずっと一緒にいながら仕事ができるから😆
    
    このポートフォリオサイトとアプリを気に入っていただけると幸いです💗
    """
    st.info(content)

content2 = """
下記で紹介しているアプリは 20 個ありますが、現時点では『やることリスト』、『アプサイト（このサイト´▽｀）』、『PDF テンプレ・ジェネレーター』、『PDF インボイス・ジェネレーター』の４つだけご覧いただくことができます😊
『やることリスト』ではウェブアプリとダウンロードして使えるデスクトップアプリの両方を用意しています！
もし「こんなプロジェクトを見てみたい」、「こんなものは作れますか？！」などのリクエストがありましたら Contact Me ページからご連絡ください:)
メール送信がエラーになる場合は、お使いのメールクライアントから直接 ten87tak@gmail.com へご連絡ください！(*'▽') 
"""
# st.text(content2) # This was my solution!
st.write(content2)

column_3, empty_column, column_4 = st.columns([1.5, 0.5, 1.5])

dataframe = pandas.read_csv("data.csv", sep=";", encoding="Shift-JIS")

with column_3:
    for index, row in dataframe[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        if row['url'] == "None":
            st.write("作成中 🍩")
        else:
            st.write(f"[ソースコード]({row['url']})")
        if row['url2'] == "None":
            st.write("")
        elif row['url2'] == "CLI only":
            st.write("コマンドラインからの実行のみ")
        else:
            st.write(f"[ウェブアプリ]({row['url2']})")
        if row['exe'] == True:
            binary_file = "gui.exe"
            with open(binary_file, "rb") as file:
                btn = st.download_button(
                    label="デスクトップ版をダウンロード",
                    data=file,
                    file_name="gui.exe",
                    mime="application/octet-stream")
        else:
            st.write("")

        st.write(" ")

with column_4:
    for index, row in dataframe[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        if row['url'] == "None":
            st.write("作成中 🍩")
        else:
            st.write(f"[ソースコード]({row['url']})")
        if row['url2'] == "None":
            st.write("")
        elif row['url2'] == "CLI only":
            st.write("コマンドラインからの実行のみ")
        else:
            st.write(f"[App Link]({row['url2']})")

        st.write(" ")

