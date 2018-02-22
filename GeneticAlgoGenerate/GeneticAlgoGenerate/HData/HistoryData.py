import pandas as pd

# Чтение тиковой истории форекс в таблицу pandas
def ReadTickBidAsk(name):
    rz=pd.read_csv(name,sep=',')
    rz['DateTime']=pd.to_datetime(rz['DateTime'])
    return rz