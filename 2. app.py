# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18

@author: EdgarJJ
"""
#importing the libraries
#!pip install streamlit

from PIL import Image
import pandas as pd
import glob
import re
import numpy as np
import cv2

import time
import os  
from keras.models import load_model
from keras.preprocessing import image
import tempfile
from keras.preprocessing.image import load_img

import tensorflow as tf
import keras_preprocessing
from keras.applications import densenet  
from keras import regularizers  
from keras.layers import Conv2D, MaxPooling2D
from keras_preprocessing.image import ImageDataGenerator
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.models import Sequential, Model, load_model  
from keras.applications.resnet50 import preprocess_input 
from keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint, Callback
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint 

from pathlib import Path
import matplotlib.pyplot as plt

import streamlit as st
import joblib
import warnings
warnings.filterwarnings('ignore')

#import imutils

# Carga del modelo entrenado
model=load_model("Bestmodel.h5")


# Inicio diseño de interfaz
st.title("Hands Signs Classification App")


st.write('\n') # Nueva linea
image = Image.open('cover\hand.png') # Imagen que aparece en la parte inicial
show = st.image(image, use_column_width=True)

st.sidebar.title("Please, upload a hand image")

# Desactivar warning
st.set_option('deprecation.showfileUploaderEncoding', 
              False)

# Seleccion de la imagen
uploaded_file = st.sidebar.file_uploader(" ",
                                         type=['png', 'jpg', 'jpeg'] ) #Fomrato img



if uploaded_file is not None:
    hand = Image.open(uploaded_file)
    show.image(hand, 'This is the image that you have successfully uploaded', use_column_width=True)
    
    # Procesamiento para keras    
    x = np.asarray(hand, dtype='float32')
    x = np.expand_dims(x, axis=0)
    x= tf.keras.applications.imagenet_utils.preprocess_input(x)

# For newline
st.sidebar.write('\n')
    
if st.sidebar.button("Click to see your image classification"):
    
    if uploaded_file is None:
        
        st.sidebar.write("Please upload an Image")
    
    else:
        
        with st.spinner('Wait, we are working on your image . . .'):
            
            prediction = model.predict(x)
            answer = "{:.0f}".format(float(np.argmax(prediction)))
            time.sleep(2)
            st.success('¡Well Done!')
            
        st.sidebar.header("Result of the model: ")
        st.sidebar.write("The number in the hand is", answer)
    