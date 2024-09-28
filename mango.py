import streamlit as st
import pandas as pd
import plotly.express as px

url = 'https://drive.google.com/file/d/1PlQaDOb2Ys0yOVZK_WcNbCIAVklTYw7f/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
data = pd.read_csv(url)
data

sns.histplot(data['Units Sold'], kde = True)
plt.title("Distribution of Units Sold")
