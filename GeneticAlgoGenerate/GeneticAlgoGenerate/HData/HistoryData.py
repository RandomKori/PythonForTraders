import pandas as pd
import datetime

# Чтение тиковой истории форекс в таблицу pfndas и возвращение таймсерий для Bid и Ask
def ReadTickBidAsk(name):
    rz=pd.read_csv(name,sep=',')
    Bid=pd.Series(rz['Bid'].values, pd.to_datetime(rz['DateTime']))
    Ask=pd.Series(rz['Ask'].values,pd.to_datetime(rz['DateTime']))
    return Bid,Ask