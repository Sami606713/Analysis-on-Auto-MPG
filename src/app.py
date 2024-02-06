import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="Auto-Mpg Dashboard",
    page_icon=":chart_with_upwards_trend:",  # Emoji or URL
    layout="wide",  # "centered" or "wide"
    initial_sidebar_state="expanded"  # "auto", "expanded", "collapsed"
)

data = pd.read_csv("notebook/Clean_data.csv")  # Adjust the path as necessary
st.title("🚗 Auto-Mpg Dashboard 📊")
palettes = ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind',
            'viridis', 'plasma', 'inferno', 'magma', 'cividis',
            'coolwarm', 'RdBu', 'vlag', 'icefire']

sns.set_palette(palettes[11])
# Apply filter
with st.container():
    filter=st.selectbox("",options=["All"]+data["origin"].unique().tolist())
    if(filter!="All"):
        data=data[data["origin"]==filter]
    else:
        data=data

with st.container(border=True):
    col1,col2=st.columns(2)
    with col1:
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
    col1=st.columns(1)
    with col1[0]:
        with st.container(border=True):
            x,y=st.columns(2)
            with x:
                col_select1=st.selectbox("",options=data.describe().columns.tolist(),key="first_column")
            with y:
                col_select2=st.selectbox("",options=data.describe().columns.tolist(),key="second column")
            with st.container():
                graph=st.selectbox("",options=["Line","Scatter"])
        with st.container(border=True):
            # st.write("Gragh num here")
            # st.set_option('deprecation.showPyplotGlobalUse', False)
            if(graph=="Line"):
                plt.figure(figsize=(20, 6))
                sns.lineplot(data=data,x=col_select1,y=col_select2)
                st.pyplot()
            elif(graph=="Scatter"):
                plt.figure(figsize=(20, 6))
                sns.scatterplot(data=data,x=col_select1,y=col_select2)
                st.pyplot()



with st.container(border=True):
    col1=st.columns(1)
    
    with col1[0]:
        col1,col2,col3=st.columns(3)
        with col1:
            x=st.selectbox("",options=data.describe().columns.tolist(),key="scatter_column1")
        with col2:
            y=st.selectbox("",options=data.describe().columns.tolist(),key="scatter_column2")
        with col3:
            z=st.selectbox("",options=data.describe().columns.tolist(),key="scatter_column3")
        
        with st.container(border=True):
            fig=px.scatter_3d(data,x=x,y=y,z=z,color=x)
            fig.update_layout(title="Multivariate Analysis")
            st.plotly_chart(fig)
        

    with st.container(border=True):
        fig = plt.figure(figsize=(20, 7))
        plt.title("Correation of each  column")
        num_col=data.describe(exclude="O").columns
        sns.heatmap(data[num_col].corr(), annot=True, cmap="coolwarm")
        st.pyplot(fig)