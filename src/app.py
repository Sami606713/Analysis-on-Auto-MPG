import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv("notebook/Clean_data.csv")  # Adjust the path as necessary
st.title("Auto-Mpg Dashboard")
palettes = ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind',
            'viridis', 'plasma', 'inferno', 'magma', 'cividis',
            'coolwarm', 'RdBu', 'vlag', 'icefire']

sns.set_palette(palettes[2])
with st.container(border=True):
    col1,col2=st.columns(2)
    with col1:
        st.write("num col")
        with st.container(border=True):
            col,graph=st.columns(2)
            with col:
                col_select=st.selectbox("",options=data.describe().columns.tolist())
            with graph:
                graph_select=st.selectbox("",options=["Histogram","Density Plot","Boxplot"])
        with st.container(border=True):
            st.write("Gragh num here")
            st.set_option('deprecation.showPyplotGlobalUse', False)
            if(graph_select=="Histogram"):
                plt.figure(figsize=(8, 6))
                sns.histplot(data[col_select])
                st.pyplot()
            elif(graph_select=="Density Plot"):
                plt.figure(figsize=(8, 6))
                sns.kdeplot(data[col_select])
                st.pyplot()
            elif(graph_select=="Boxplot"):
                plt.figure(figsize=(8, 6))
                sns.boxplot(data[col_select])
                st.pyplot()
    
    with col2:
        st.write("catcol")
        with st.container(border=True):
            col,graph=st.columns(2)
            with col:
                # st.write(data.describe().columns.tolist())
                col_select=st.selectbox("",options=data.describe(exclude="number").columns.tolist())
            with graph:
                graph_select=st.selectbox("",options=["Barlot","Pie Chart"])
        with st.container(border=True):
            if(graph_select=="Barlot"):
                plt.figure(figsize=(8,6))
                sns.barplot(x=data[col_select].value_counts().index,y=data[col_select].value_counts())
                st.pyplot()

            elif(graph_select=="Pie Chart"):
                plt.figure(figsize=(8,6))
                plt.pie(data[col_select].value_counts(normalize=True),labels=data[col_select].value_counts().index,autopct="%.2f")
                st.pyplot()


with st.container():
    col1,col2=st.columns(2)
    with col1:
        st.write("num-num")
        with st.container(border=True):
            col,graph=st.columns(2)
            with col:
                col_select=st.selectbox("",options=data.describe().columns.tolist())
            with graph:
                graph_select=st.selectbox("",options=["Histogram","Density Plot","Boxplot"])
        with st.container(border=True):
            st.write("Gragh num here")
            st.set_option('deprecation.showPyplotGlobalUse', False)
            if(graph_select=="Histogram"):
                plt.figure(figsize=(8, 6))
                sns.histplot(data[col_select])
                st.pyplot()

    
    with col2:
        st.write("num-cat")

# with st.container():
#     col1=st.columns(1)
    
#     with col1:
#         st.write("multivariate")
