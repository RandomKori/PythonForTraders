import pandas as pd
import HData.HistoryData as dt
import matplotlib.pyplot as plt

Bid,Ask=dt.ReadTickBidAsk('./History/EURUSD.m_Ticks.csv')
print(Bid.head())
Bid.plot()
plt.show()
input("Нажмите ентер")

