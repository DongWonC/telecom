# -*- coding:utf-8 -*-

import requests
import streamlit as st
from PIL import Image
from io import BytesIO

from sub_app import home_app, store_app, total

token = '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'
headers = {'Authorization': f'token {token}'}

def main():
    with st.sidebar:
        # Fetch the image from GitHub
        image_url = "https://github.com/DongWonC/telecom/raw/main/Web/image/title.png"
        response = requests.get(image_url, headers=headers)

        if response.status_code == 200:
            # If the image is fetched successfully, open it with PIL
            sidebar_image = Image.open(BytesIO(response.content))
            st.image(sidebar_image, use_column_width=True)
        else:
            # If fetching the image fails, display an error message
            st.error("Unable to load the sidebar image.")

        menu = ['홈', '매장 찾기', '서비스 문자 발송', '서비스 제공자']
        choice = st.sidebar.selectbox("Menu", menu)

    if choice == '홈':
        home_app.main()

    elif choice == '매장 찾기':
        store_app.main()

    elif choice == '서비스 문자 발송':
        total.main()

    elif choice == '서비스 제공자':
        provider_image_url = "https://github.com/DongWonC/telecom/raw/main/Web/image/procider.png"
        provider_response = requests.get(provider_image_url, headers=headers)

        if provider_response.status_code == 200:
            provider_image = Image.open(BytesIO(provider_response.content))
            st.image(provider_image, caption="서비스 제공자 이미지", use_column_width=True)
        else:
            st.error("Unable to load the service provider image.")


if __name__ == "__main__":
    main()
