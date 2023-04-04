import streamlit as st

st.set_page_config(layout="wide")

column_1, column_2 = st.columns(2)

with column_1:
    st.header("ジオメトリ・ゲーム")

    st.write("ランダムに生成された２つの座標が作り出す長方形の中に、任意に選んだ座標が"
                 "入っているかどうかを当てるコマンドラインで操作するゲームです。")

    st.write("プロンプトが表示されたら、画面に従って任意の X 座標と Y 座標を入力します。"
                 "また、面積も推測します。")

    st.write("最後にウィンドウが表示され、その中にその長方形と任意に選んだ座標点を表示します。")


with column_2:
    st.image("images/OOP_App1.PNG")

    st.write("[Source Code](https://github.com/ten87tak/OOP_App1_GeoGame)")
