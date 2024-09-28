import streamlit as st
import pandas as pd
import plotly.express as px

url = 'https://drive.google.com/file/d/1PlQaDOb2Ys0yOVZK_WcNbCIAVklTYw7f/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
data = pd.read_csv(url)
data

data['Date']=pd.to_datetime(data['Date'])
date_revenue = data.groupby(['Date'])['Total Revenue'].sum().reset_index()
plt.figure(figsize=(14, 8))
sns.lineplot(x='Date', y='Total Revenue', data=date_revenue)
plt.title('Total revenue by month')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()

st.pyplotpyplot(plt)
