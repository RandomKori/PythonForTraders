import pandas as pd
import HData.HistoryData as dt
import Tester.Tester as ts
from deap import base, creator, gp, tools, algorithms
import operator
import math
import random
import numpy

print("Загрузка данных")
f=dt.ReadTickBidAsk('./History/EURUSD.m_Ticks.csv')
st=ts.CTester()
st.TickHistory=f[f.columns[:]].values.tolist()
st.N=10
print("Обучение ГА")
set=gp.PrimitiveSetTyped('main',[float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float],float)
set.addPrimitive(operator.add,[float,float],float,name='add')
set.addPrimitive(operator.sub,[float,float],float,name='sub')
set.addPrimitive(operator.mul,[float,float],float,name='mul')
def protectedDiv(left, right):
    return left / right
set.addPrimitive(protectedDiv,[float,float],float,name='div')
set.addPrimitive(operator.pow,[float,float],float,name='pow')
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
set.addPrimitive(operator.eq,[float,float],bool,name='равно')
set.addPrimitive(operator.gt,[float,float],bool,name='больше')
set.addPrimitive(operator.lt,[float,float],bool,name='меньше')
set.addPrimitive(operator.and_,[bool,bool],bool,name='and')
set.addPrimitive(operator.or_,[bool,bool],bool,name='or')
set.addPrimitive(operator.not_,[bool],bool,name='not')
def avr(a1,a2):
    return (a1+a2)/2
set.addPrimitive(avr,[float,float],float,name='avr')
set.addEphemeralConstant('const',lambda: random.uniform(-100, 100),float)
set.addTerminal(1, bool)

set.renameArguments(ARG0="bid1")
set.renameArguments(ARG1="ask1")
set.renameArguments(ARG2="bid2")
set.renameArguments(ARG3="ask2")
set.renameArguments(ARG4="bid3")
set.renameArguments(ARG5="ask3")
set.renameArguments(ARG6="bid4")
set.renameArguments(ARG7="ask4")
set.renameArguments(ARG8="bid5")
set.renameArguments(ARG9="ask5")
set.renameArguments(ARG10="bid6")
set.renameArguments(ARG11="ask6")
set.renameArguments(ARG12="bid7")
set.renameArguments(ARG13="ask7")
set.renameArguments(ARG14="bid8")
set.renameArguments(ARG15="ask8")
set.renameArguments(ARG16="bid9")
set.renameArguments(ARG17="ask9")
set.renameArguments(ARG18="bid10")
set.renameArguments(ARG19="ask10")

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=set, min_=1, max_=3)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=set)

sl=50
tp=70
indiv=None
def syst():
    global st
    pz=0
    if len(st.position)==0:
        func = toolbox.compile(expr=indiv)
        p=func(st.dat[0][1],st.dat[0][2],st.dat[1][1],st.dat[1][2],st.dat[2][1],st.dat[2][2],st.dat[3][1],st.dat[3][2],st.dat[4][1],st.dat[4][2],st.dat[5][1],st.dat[5][2],st.dat[6][1],st.dat[6][2],st.dat[7][1],st.dat[7][2],st.dat[8][1],st.dat[8][2],st.dat[9][1],st.dat[9][2])
        if p>0.9:
            pz=1
        if p<(-0.9):
            pz=-1
    else:
        if st.position[2]==1:
            if st.position[3]-sl*st.Point>=st.dat[len(st.dat)-1][1]:
                pz=-1
            if st.position[3]+tp*st.Point<=st.dat[len(st.dat)-1][1]:
                pz=-1
        else:
            if st.position[3]+sl*st.Point<=st.dat[len(st.dat)-1][2]:
                pz=1
            if st.position[3]-tp*st.Point>=st.dat[len(st.dat)-1][2]:
                pz=1
    return 0.1,pz

st.System=syst

def evalSymbReg(individual):
    global indiv
    indiv=individual
    st.Test()
    if st.TradeCount==0:
        return 0.0,
    rz=(st.Profit*(st.Win/st.TradeCount))
    return rz,

toolbox.register("evaluate", evalSymbReg)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=3)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=set)

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

pop = toolbox.population(n=300)
hof = tools.HallOfFame(1)
stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
stats_size = tools.Statistics(len)
mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)

pop, log = algorithms.eaSimple(pop, toolbox, 0.5, 0.1, 40, stats=mstats, halloffame=hof, verbose=True)

input("Нажмите ввод")
