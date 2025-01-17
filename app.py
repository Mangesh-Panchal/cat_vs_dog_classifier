
import numpy as np
import streamlit as st
import tensorflow as tf
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model

from PIL import Image, ImageOps

def import_and_predict(image_data, model):

    size = (64 ,64)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    image = image.convert('RGB')
    image = np.asarray(image)
    image = (image.astype(np.float32) / 255.0)

    img_reshape = image[np.newaxis ,...]

    prediction = model.predict(img_reshape)

    return prediction

model=load_model("DogCat.h5")


file = st.file_uploader("Please upload an image file", type=["jpg", "png"])
#
if file is None:
    st.text("You haven't uploaded an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    if prediction[0]>0.5 :
        st.write("It's a Dog")
    else:
        st.write("It's a Cat")


