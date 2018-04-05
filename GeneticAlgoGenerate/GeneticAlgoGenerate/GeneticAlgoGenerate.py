import pandas as pd
import HData.HistoryData as dt
import Tester.Tester as ts
from deap import base, creator, gp, tools, algorithms
import operator
import math
import random
import numpy


print("Загрузка данных")
f=dt.ReadTickBidAsk('./History/BR Splice_Ticks.csv')
st=ts.CTester()
st.TickHistory=f[f.columns[:]].values.tolist()
st.N=10
st.Point=0.01
print("Обучение ГА")
set=gp.PrimitiveSetTyped('main',[float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float],float)
set.addPrimitive(operator.add,[float,float],float,name='add')
set.addPrimitive(operator.sub,[float,float],float,name='sub')
set.addPrimitive(operator.mul,[float,float],float,name='mul')
def protectedDiv(left, right):
    if right==0.0:
        return 0.0
    return left / right
def osqrt(a):
    if a<=0.0:
        return 0.0
    return math.sqrt(a)
set.addPrimitive(protectedDiv,[float,float],float,name='div')
set.addPrimitive(operator.pow,[float,int],float,name='pow')
set.addPrimitive(osqrt,[float],float,name='sqrt')
set.addPrimitive(math.cos,[float],float,name='cos')
set.addPrimitive(math.sin,[float],float,name='sin')
set.addPrimitive(math.tan,[float],float,name='tan')
def olog10(a):
    if a<=0.0:
        return 0.0
    return math.log10(a)
set.addPrimitive(olog10,[float],float,name='log10')
def neg(a):
    return 0.0-a
set.addPrimitive(neg,[float],float,name='neg')
def if_then_else(input, output1, output2):
    rz=output2
    if input:
        rz=output1
    return rz
set.addPrimitive(if_then_else, [bool, float, float], float,name='if_then_else')
set.addPrimitive(operator.eq,[float,float],bool,name='равно')
set.addPrimitive(operator.gt,[float,float],bool,name='больше')
set.addPrimitive(operator.lt,[float,float],bool,name='меньше')
def oand(a1,a2):
    return a1 and a2
def oor(a1,a2):
    return a1 or a2
def onot(a1):
    return not a1
set.addPrimitive(oand,[bool,bool],bool,name='oand')
set.addPrimitive(oor,[bool,bool],bool,name='oor')
set.addPrimitive(onot,[bool],bool,name='onot')
def avr(a1,a2):
    return (a1+a2)/2
set.addPrimitive(avr,[float,float],float,name='avr')
set.addEphemeralConstant('const',lambda: random.normalvariate(0.0, 100.0),float)
set.addTerminal(True, bool)
set.addTerminal(False, bool)
set.addTerminal(2, int)
set.addTerminal(3, int)
set.addTerminal(4, int)
set.addTerminal(5, int)

set.renameArguments(ARG0="bid1")
set.renameArguments(ARG1="ask1")
set.renameArguments(ARG2="last1")
set.renameArguments(ARG3="volume1")
set.renameArguments(ARG4="type1")
set.renameArguments(ARG5="bid2")
set.renameArguments(ARG6="ask2")
set.renameArguments(ARG7="last2")
set.renameArguments(ARG8="volume2")
set.renameArguments(ARG9="type2")
set.renameArguments(ARG10="bid3")
set.renameArguments(ARG11="ask3")
set.renameArguments(ARG12="last3")
set.renameArguments(ARG13="volume3")
set.renameArguments(ARG14="type3")
set.renameArguments(ARG15="bid4")
set.renameArguments(ARG16="ask4")
set.renameArguments(ARG17="last4")
set.renameArguments(ARG18="volume4")
set.renameArguments(ARG19="type4")
set.renameArguments(ARG20="bid5")
set.renameArguments(ARG21="ask5")
set.renameArguments(ARG22="last5")
set.renameArguments(ARG23="volume5")
set.renameArguments(ARG24="type5")
set.renameArguments(ARG25="bid6")
set.renameArguments(ARG26="ask6")
set.renameArguments(ARG27="last6")
set.renameArguments(ARG28="volume6")
set.renameArguments(ARG29="type6")
set.renameArguments(ARG30="bid7")
set.renameArguments(ARG31="ask7")
set.renameArguments(ARG32="last7")
set.renameArguments(ARG33="volume7")
set.renameArguments(ARG34="type7")
set.renameArguments(ARG35="bid8")
set.renameArguments(ARG36="ask8")
set.renameArguments(ARG37="last8")
set.renameArguments(ARG38="volume8")
set.renameArguments(ARG39="type8")
set.renameArguments(ARG40="bid9")
set.renameArguments(ARG41="ask9")
set.renameArguments(ARG42="last9")
set.renameArguments(ARG43="volume9")
set.renameArguments(ARG44="type9")
set.renameArguments(ARG45="bid10")
set.renameArguments(ARG46="ask10")
set.renameArguments(ARG47="last10")
set.renameArguments(ARG48="volume10")
set.renameArguments(ARG49="type10")

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=set, min_=1, max_=16)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=set)

sl=7
tp=7
func=None
def syst():
    global st
    pz=0
    if len(st.position)==0:
        
        p=0.0
        p=func(st.dat[0][1],st.dat[0][2],st.dat[0][3],st.dat[0][4],st.dat[0][5],st.dat[1][1],st.dat[1][2],st.dat[1][3],st.dat[1][4],st.dat[1][5],st.dat[2][1],st.dat[2][2],st.dat[2][3],st.dat[2][4],st.dat[2][5],st.dat[3][1],st.dat[3][2],st.dat[3][3],st.dat[3][4],st.dat[3][5],st.dat[4][1],st.dat[4][2],st.dat[4][3],st.dat[4][4],st.dat[4][5],st.dat[5][1],st.dat[5][2],st.dat[5][3],st.dat[5][4],st.dat[5][5],st.dat[6][1],st.dat[6][2],st.dat[6][3],st.dat[6][4],st.dat[6][5],st.dat[7][1],st.dat[7][2],st.dat[7][3],st.dat[7][4],st.dat[7][5],st.dat[8][1],st.dat[8][2],st.dat[8][3],st.dat[8][4],st.dat[8][5],st.dat[9][1],st.dat[9][2],st.dat[9][3],st.dat[9][4],st.dat[9][5])
        if p>0.5:
            pz=1
        if p<(-0.5):
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
    return 1,pz

st.System=syst

def evalSymbReg(individual):
    global func
    func = toolbox.compile(expr=individual)
    st.Test()
    if st.TradeCount==0:
        return -1000.0,
    return st.Profit,

toolbox.register("evaluate", evalSymbReg)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=16)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=set)

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

pop = toolbox.population(n=30)
hof = tools.HallOfFame(1)
stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
stats_size = tools.Statistics(len)
mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
mstats.register("avg", numpy.mean)
mstats.register("std", numpy.std)
mstats.register("min", numpy.min)
mstats.register("max", numpy.max)
pop, log = algorithms.eaSimple(pop, toolbox, 0.5, 0.1, 30, stats=mstats, halloffame=hof, verbose=True)
record = mstats.compile(pop)
print(record)
expr = hof[0]
tree = gp.PrimitiveTree(expr)
rez=str(tree)
print(rez)
fl=open('./Rez/tree.txt','w')
fl.write(rez)
fl.close()
input("Нажмите ввод")
