import pandas as pd 
import numpy as np 
import plotly.express as px 
import streamlit as st 

st.set_page_config(page_title='movie',page_icon="🎥",layout='wide')

df=pd.read_csv('cleaned_data.csv')

year_range=st.sidebar.slider('Year range',int(df['year'].min()),int(df['year'].max()),(int(df['year'].min()),int(df['year'].max())))

rating_range=st.sidebar.slider('rating range',float(df['rating'].min()),float(df['rating'].max()),(float(df['rating'].min()),float(df['rating'].max())))

filtered_df=df[
    (df['year'].between(year_range[0],year_range[1]))
    &(df['rating'].between(rating_range[0],rating_range[1]))
               ]

st.title('Movies dashboard')
tab1,tab2=st.tabs(['overview','analysis'])

with tab1:

    col1,col2=st.columns(2)
    col1.metric('Total movies',len(filtered_df))
    col2.metric('Average runtime',filtered_df['runtime'].mean())

    st.dataframe(filtered_df)
with tab2:
    temp=filtered_df.groupby('year')['runtime'].mean().reset_index().sort_values(by='year')
    fig1=px.line(temp,x='year',y='runtime')
    st.plotly_chart(fig1,use_container_width=True)

    fig2=px.histogram(filtered_df,x='year')

    st.plotly_chart(fig2,use_container_width=True)

