import pandas as pd
import HData.HistoryData as dt

f=dt.ReadTickBidAsk('./History/EURUSD.m_Ticks.csv')
print(f.head())
print(f.info())
input("Нажмите ентер")

