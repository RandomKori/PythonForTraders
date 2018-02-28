import pandas as pd
import HData.HistoryData as dt
import Tester.Tester as ts

print("Загрузка данных")
f=dt.ReadTickBidAsk('./History/EURUSD.m_Ticks.csv')
st=ts.CTester()
st.TickHistory=f[f.columns[:]].values.tolist()
st.N=10
print("Обучение ГА")

input("Нажмите ввод")
