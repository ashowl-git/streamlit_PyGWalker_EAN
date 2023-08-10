import streamlit as st 
import streamlit.components.v1 as stc 
import pandas as pd 
import pygwalker as pyg 






# Page Configuration
st.set_page_config(layout="wide", page_title="EAN_data_visual_easy")

# # hide the hamburger menu? hidden or visible
hide_menu_style = """
        <style>
        #MainMenu {visibility: visible;}
        footer {visibility: visible;}
        footer:after {content:'Copyright 2023. EAN R&D Unit. All rights reserved.';
        display:block;
        opsition:relatiive;
        color:orange; #tomato 
        padding:5px;
        top:100px;}

        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True) # hide the hamburger menu?




# Load Data Fxn
def load_data(data):
    return pd.read_excel(data)

def main():
    st.title("데이터 시각화 웹 도구")

    menu = ["시각화", "이건뭐야?"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "시각화":
        st.subheader("Garbage In !, Garbage Out !")
        # Form
        with st.form("upload_form"):
            data_file = st.file_uploader("시각화를 원하는 데이터 파일을 불러오기.",type=["csv","txt","xlsx"])
            submitted = st.form_submit_button("Submit")

        if submitted:
            df = load_data(data_file)
            st.dataframe(df)
            # Visualize
            pyg_html = pyg.walk(df,return_html=True)
            # Render with components
            stc.html(pyg_html,scrolling=True,height=1000)

        
        
    
    else:
        st.subheader("이건뭐야?")

        st.text("게시판에 함께 올려둔 샘플데이터_ test_file.xlsx 처럼 데이터들이 정규화 되어있어야 합니다.")
        st.text("원하는 컬럼명을 X나 Y 축에 끌어다 놓으면 됩니다. 이것저것 눌러 보면 5분안에 모두 이해")

        st.text("아래 링크에서 구경")
        st.text('https://docs.kanaries.net/graphic-walker')

        # img6 = Image.open('data/사용자 메뉴얼_4.jpg')
        # st.image(img6)

        # video_file = open('myvideo.mp4', 'rb')
        # video_bytes = video_file.read()

        # st.video(video_bytes)



        # ddddddd


        


    
if __name__ == "__main__":
    main()