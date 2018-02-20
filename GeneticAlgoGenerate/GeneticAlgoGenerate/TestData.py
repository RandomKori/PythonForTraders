import pandas as pd
import HData.HistoryData as dt
import matplotlib.pyplot as plt

f=dt.ReadTickBidAsk('./History/EURUSD.m_Ticks.csv')
print(f.head())
f.plot('DateTime','Bid')
plt.show()
input("Нажмите ентер")

