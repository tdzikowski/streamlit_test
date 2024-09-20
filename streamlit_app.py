import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt


st.title('Hello World')
st.write('**Data Science Course 2024 TD**')


df = pd.read_csv('data/Bastar Craton.csv')
#st.dataframe(df)

cat_names = df.columns.tolist()[27:]
col1, col2 = st.columns()

el1 = st.selectbox('x-axis', cat_names)
el2 = st.selectbox('y-axis', cat_names)

with col1:
    el1 = st.selectbox('x-axis', cat_names)
    st.write(el1)

with col2:
    el2 = st.selectbox('y-axis', cat_names)
    st.write(el2)









#plt.scatter(df[0],df[1])
#plt.show()


#jjhg

