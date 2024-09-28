import streamlit as st
import pandas as pd
import plotly.express as px

# Đường dẫn đến file CSV trên Google Drive
url = 'https://drive.google.com/file/d/1PlQaDOb2Ys0yOVZK_WcNbCIAVklTYw7f/view?usp=sharing'
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]

# Đọc dataset từ Google Drive
data = pd.read_csv(url)

# Hiển thị dữ liệu lên Streamlit để kiểm tra
st.write("Dữ liệu đã tải về:", data.head())

# Lọc dữ liệu theo điều kiện 'region' là 'Albany' và 'year' là 2015
albany_df = data[data['region'] == "Albany"]
al_df = albany_df[albany_df["year"] == 2015]

# Tạo biểu đồ đường với Plotly Express
line_chart = px.line(
    al_df,  # DataFrame chứa dữ liệu cần vẽ
    x="Date",  # Trục X là cột "Date"
    y="Large Bags"  # Trục Y là cột "Large Bags"
)

# Hiển thị tiêu đề và biểu đồ trên giao diện Streamlit
st.header("Biểu đồ Đường (Line Chart) - Large Bags in Albany (2015)")
st.plotly_chart(line_chart)

streamlit run your_script.py
