# -*- coding:utf-8 -*-
import requests
import streamlit as st
from PIL import Image

from sub_app import home_app, store_app, total
def main():

    with st.sidebar:
        sidebar_image_url = 'https://github.com/DongWonC/telecom/Web/image/kt_poster.png'
        response = requests.get(sidebar_image_url)
        sidebar_image = Image.open(BytesIO(response.content))
        st.image(sidebar_image, use_column_width=True)
        
        menu = ['홈', '매장 찾기', '서비스 문자 발송', '서비스 제공자']
        choice = st.sidebar.selectbox("Menu", menu)

    if choice == '홈':
        home_app.main()

    elif choice == '매장 찾기':
        store_app.main()

    elif choice == '서비스 문자 발송':
        total.main()

    elif choice == '서비스 제공자':
        provider_image_url = 'https://github.com/DongWonC/telecom/Web/image/procider.png'
        provider_image_response = requests.get(provider_image_url)
        provider_image = Image.open(BytesIO(provider_image_response.content))
        st.image(provider_image)
    

if __name__ == "__main__":
    main()
