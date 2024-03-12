import pandas as pd

# Date column

def clean_data(df):

# Clean this specific data

    # Strip space from column names
    d={}
    for col in df.columns:
        d[col]=col.strip(' ')
    df.rename(d,axis=1,inplace=True)

    # strip spaces from values inside column
    for col in df.columns[:4]:
        df[col]=df[col].apply(lambda x :x.strip())

    # remove data where date is 'NA'
    df.drop(df.loc[df['Date']=='NA'].index,inplace=True)
    
    # Date as index and sort
    df['Date']=pd.to_datetime(df['Date'],yearfirst=True)
    df=df.set_index(['Date']).sort_index()
    
    
    # Column Order_Demand
    
    # remove '(' and ')' from values in order_demand
    df['Order_Demand']=df['Order_Demand'].apply(lambda x: x.strip('()'))
    
    # change from str type to numeric
    df['Order_Demand']=pd.to_numeric(df['Order_Demand'])
    
    df=df['2012':'2016']
    
    return df
    
    
    

