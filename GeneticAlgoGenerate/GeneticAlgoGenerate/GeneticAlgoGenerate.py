import pandas as pd
import HData.HistoryData as dt
import Tester.Tester as ts
import deap
import operator
import math
import random

print("Загрузка данных")
f=dt.ReadTickBidAsk('./History/EURUSD.m_Ticks.csv')
st=ts.CTester()
st.TickHistory=f[f.columns[:]].values.tolist()
st.N=10
print("Обучение ГА")

input("Нажмите ввод")
set=deap.gp.PrimitiveSetTyped('main',[float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float],float)
set.addPrimitive(operator.add,[float,float],float,name='+')
set.addPrimitive(operator.sub,[float,float],float,name='-')
set.addPrimitive(operator.mul,[float,float],float,name='*')
def protectedDiv(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1
set.addPrimitive(protectedDiv,[float,float],float,name='/')
set.addPrimitive(operator.pow,[float,float],float,name='^')
set.addPrimitive(math.cos,[float],float,name='cos')
set.addPrimitive(math.sin,[float],float,name='sin')
set.addPrimitive(math.tan,[float],float,name='tan')
set.addPrimitive(math.log10,[float],float,name='log10')
def if_then_else(input, output1, output2):
    rz=output2
    if input:
        rz=output1
    return rz
set.addPrimitive(if_then_else, [bool, float, float], float,name='if_then_else')
set.addPrimitive(operator.eq,[float,float],bool,name='==')
set.addPrimitive(operator.gt,[float,float],bool,name='>')
set.addPrimitive(operator.lt,[float,float],bool,name='<')
set.addPrimitive(operator.and_,[bool,bool],bool,name='and')
set.addPrimitive(operator.or_,[bool,bool],bool,name='or')
set.addPrimitive(operator.not_,[bool],bool,name='not')


