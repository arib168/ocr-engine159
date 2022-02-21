import streamlit as st 
import numpy as np
import pytesseract
from PIL import Image  

st.title("OPTICAL CHARACTER RECOGNITION")
st.text("Upload the image :")

pytesseract-pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'

uploaded_file = st.sidebar.file_uploader("Choose an image :", type = ["jpg","jpeg","png"])   # create a file uploader in the sidebar 
if uploaded_file is not None: #if there is some file uploaded, then run the following conditions 
  img = Image.open(uploaded_file)  #open the file and display the image 
  st.image(img,caption='Uploaded Image',use_column_width=True)

  st.write("")

  if st.button('PREDICT'):
    st.write("OCR OUTPUT :")
    op = pytesseract.image_to_string(img)
    st.subheader(op)
