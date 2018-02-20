import pandas as pd
import datetime

# Чтение тиковой истории форекс в таблицу pfndas
def ReadTickBidAsk(name):
    rz=pd.read_csv(name,sep=',')
    rz['DateTime']=pd.to_datetime(rz['DateTime'])
    return rz