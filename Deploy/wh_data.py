import pandas as pd
import numpy as np


def get_wh_data(df,wh_name):
    data_pt=df.reset_index().pivot_table(index=['Date','Warehouse','Product_Category','Product_Code'],values=['Order_Demand'],aggfunc='sum')
    data_pt=data_pt.reset_index().set_index(['Date'])
    df_whse_prod=data_pt[data_pt['Warehouse']==wh_name].reset_index().pivot_table(index=['Date'],columns=['Product_Code'],values=['Order_Demand'],aggfunc='sum',fill_value=0)
    df_whse_month=df_whse_prod.resample('m').sum()
    df_whse_month=df_whse_month.droplevel([0],axis=1).reset_index().set_index(['Date'])
    return df_whse_month
