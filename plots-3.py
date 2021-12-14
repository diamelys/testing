'''
Created on Nov 23, 2021

@author: diame
'''
#%matplotlib inline
import pandas as pd
from glob import glob
from matplotlib import pyplot as plt
import streamlit as st
import os
from PIL import Image
#import tkinter
#import matplotlib
#matplotlib.use("TKAgg")
#import ntpath
#from fpdf import FPDF
#import base64
#from tempfile import NamedTemporaryFile

st.write("""
# Testing
""")
total = []
st.sidebar.header('Testing')
compare = st.sidebar.checkbox('see')
mean = st.sidebar.checkbox('work')
with st.sidebar.form(key ='Form1'):    
    if compare:
        see = st.selectbox('text 1',('Select', '1','2','3'))
        work = st.selectbox('text 2',('Select', '1','2','3'))
    submit = st.form_submit_button(label = 'Submit')