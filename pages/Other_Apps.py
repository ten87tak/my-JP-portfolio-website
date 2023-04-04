import streamlit as st

st.set_page_config(layout="wide")

column_1, column_2 = st.columns(2)

with column_1:
    st.header("GEOMETRY GAME")

    st.subheader("This is a CLI game where a player will be given random "
                 "coordinates that make two points, which produces a rectangle.")

    st.subheader("The player is then asked to type in a set of X and Y coordinates "
                 "which they think is located within that rectangle. Also, the "
                 "player will be asked to enter an area they guess. ")

    st.subheader("Finally, the program draws the rectangle and the guessed "
                 "point in the graphic window.")

    # content = """
    #
    #     """
    # st.info(content)

with column_2:
    st.image("images/OOP_App1.PNG")

    st.write("[Source Code](https://github.com/ten87tak/OOP_App1_GeoGame)")
