import pandas as pd
import HData.HistoryData as dt
import Tester.Tester as ts
import matplotlib.pyplot as plt
import random as rnd

print('Загрузка данных')
f=dt.ReadTickBidAsk('./History/EURUSD.m_Ticks.csv')
print(f.head())
f.plot('DateTime','Bid')
plt.show()
print('Тестирование')
st=ts.CTester()
st.TickHistory=f[f.columns[:]].values.tolist()
sl=50
tp=70
def syst():
    global st
    pz=0
    if len(st.position)==0:
        p=rnd.random()
        if p>0.5:
            pz=1
        else:
            pz=-1
    else:
        if st.posirion[2]==1:
            if st.position[3]-sl*st.Point<=dat[len(dat)-1,1]:
                pz=-1
            if st.position[3]+tp*st.Point>=dat[len(dat)-1,1]:
                pz=-1
        else:
            if st.position[3]+sl*st.Point>=dat[len(dat)-1,2]:
                pz=-1
            if st.position[3]-tp*st.Point<=dat[len(dat)-1,2]:
                pz=-1
    return 0.1,pz
st.System=syst
st.Test()
plt.plot(st.ProfitHistory[0],st.ProfitHistory[1])
plt.show()
input("Нажмите ентер")

