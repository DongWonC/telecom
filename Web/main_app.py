# -*- coding:utf-8 -*-

import streamlit as st
from PIL import Image

from sub_app import home_app, store_app, agree

def main():

    with st.sidebar:
        sidebar_image = Image.open('./image/title.png')
        st.image(sidebar_image, use_column_width=True)
        
        menu = ['홈', '매장 찾기', '서비스 문자 발송', '서비스 제공자']
        choice = st.sidebar.selectbox("Menu", menu)

    if choice == '홈':
        home_app.main()

    elif choice == '매장 찾기':
        store_app.main()

    elif choice == '서비스 문자 발송':
        agree.main()

    elif choice == '서비스 제공자':
        st.image(".\image\procider.png")
    

if __name__ == "__main__":
    main()
