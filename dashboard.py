import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
import plotly.figure_factory as ff
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title='Warehouse Optimization',
                   page_icon=':bar_chart:',layout='wide')
st.title(':bar_chart: Warehouse Optimization')
st.subheader('Project Overview: Predict the Product demand in Warehouse')
st.subheader(':chart_with_upwards_trend: Time Series Analysis')

from Deploy.ingest import read_data
from Deploy.clean import clean_data
from Deploy.wh_data import get_wh_data
from Deploy.forecast import forecast

from statsmodels.tsa.seasonal import seasonal_decompose

df=clean_data(read_data('Data/demand_hist_prod.csv'))

st.sidebar.header("Choose your Filter: ")
# Choose the Warehouse
wh_name=st.sidebar.selectbox("Warehouse",df['Warehouse'].unique())
if not wh_name:
    df2=df.copy()
else:
    df2=get_wh_data(df,wh_name)

#Choose the product Code
prod_code=st.sidebar.selectbox("Product Code",df2.columns)


st.subheader('Product demanding for WareHouse '+wh_name[-1])
demand_prod=df[df['Warehouse']==wh_name].drop(['Warehouse', 'Product_Category'],axis=1).groupby('Product_Code').agg('sum').sort_values(by='Order_Demand',ascending=False)
fig=px.bar(demand_prod)
st.plotly_chart(fig,use_container_width=True)

st.subheader('Hierarchical view of Warehouse Products')
df_wh=df[df['Warehouse']==wh_name]
fig=px.treemap(df_wh,path=['Product_Category','Product_Code'],values='Order_Demand',hover_data=['Order_Demand'],color='Product_Category')
st.plotly_chart(fig,use_container_width=True)

st.subheader('Trend of a Product over time')
sd=seasonal_decompose(df2[prod_code])
fig=px.line(df2,y=sd.trend)
st.plotly_chart(fig,use_container_width=True)

st.subheader('Seasonality of the Product over time')
fig=px.line(df2,y=sd.seasonal)
st.plotly_chart(fig,use_container_width=True)

st.subheader('Forcasting for next 20 months')
fig=px.line(df2,y=prod_code)
fig2=px.line(forecast(df2,prod_code))
fig2.update_traces(line_color='#189ab4')
fig.add_trace(fig2.data[0])
st.plotly_chart(fig,use_container_width=True)