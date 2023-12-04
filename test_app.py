import streamlit as st
import csv
import cv2
import pandas as pd
import numpy as np
from datetime import datetime

from src.pipelines.pipeline_preprocessing import preprocess_pipeline
from src.pipelines.pipeline_ocr import pipeline_ocr
from src.pipelines.pipeline_translation import translation_pipeline

from src.utils import load_random_image


if not "csv_file" in st.session_state: 
    st.session_state["csv_file"] = ""



def generate_csv_button_callback(): 

    if not input_image: 
        st.warning("Please provide a image")
        return

    if not src_lang:
        st.warning("Please provide a source language")
        return 
    
    if not dst_lang: 
        st.warning("Please provide a destination language")
        return
    
    image_data = input_image.read() 
    image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_UNCHANGED)


    st.session_state["csv_file"] = image_to_csv(image)
    st.warning("Your image has been generated successfully, please click the 'Download' button")


def image_to_csv(image): 

    preprocess_image = preprocess_pipeline(image)
    data = pipeline_ocr(preprocess_image)
    output = translation_pipeline(data)

    return output




st.title("Anki .CSV Generator")


input_image = st.file_uploader(
    label='IMAGE',
    type=['png','jpg'],
    accept_multiple_files=False,
)

src_lang = st.text_input(
    label='Source Language',
    value='french',
)

dst_lang = st.text_input(
    label='Destination Language',
    value='spanish'
)

st.markdown("### Download .CSV Generated")
st.download_button(
    label="Download",
    data=st.session_state["csv_file"],
    file_name=f"MyDeck_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.csv"
)

st.button(
    label="Generate .CSV", 
    on_click=generate_csv_button_callback,
)




