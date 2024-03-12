from pmdarima import auto_arima
import pandas as pd

def forecast(df2,prod_code):
    aa=auto_arima(df2[prod_code], start_p=1, start_q=1,
                    test='adf',
                    max_p=5, max_q=5,             
                    d=1,
                    m=12,         
                    seasonal=True,   
                    start_P=0, 
                    D=None, 
                    trace=True,
                    error_action='ignore',  
                    suppress_warnings=True, 
                    stepwise=True)
    return aa.predict(20)


        