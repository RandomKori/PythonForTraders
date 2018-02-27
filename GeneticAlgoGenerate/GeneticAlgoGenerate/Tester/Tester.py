
class CTester:
    def __init__(self):
        self.TickHistory=[[]]
        self.TradeHistory=[[]]
        self.ProfitHistory=[[]]
        self.dat=[[]]
        self.position=[]
        self.System=None # Функция реализуящая систему вида lot,trade=f(ticks) где tick список тиков размером N, trade 0 - нет сделки 1 - покупка -1 - продажа
        self.N=20 # Количество тиков передающихся в функцию реализующую систему
        self.Deposit=1000
        self.TickValue=1 # Цена тика на 1 лот
        self.Point=0.00001
        self.Profit=0
        self.MaxDropdawn=0
        self. TradeCount=0
        self.Win=0

    def Test(self):
        self.TradeHistory=[[]]
        self.ProfitHistory=[[]]
        self.position=[]
        self. TradeCount=0
        self.Win=0
        balance=self.Deposit
        i=self.N-1
        last=len(self.TickHistory)
        self.position=[]
        while i<last:
            if self.TickHistory[i][1]==self.TickHistory[i-1][1] and i!=self.N-1:
                i=i+1
                continue
            if balance<=0:
                break
            self.dat=self.TickHistory[(i-self.N-1):(i+1)]
            lot,trade=self.System()
            if len(self.position)==0:
                if trade==1:
                    t=[self.TickHistory[i][0],lot,trade,self.TickHistory[i][2]]
                    self.position=t
                    self.TradeHistory.append(t)
                if trade==-1:
                     t=[self.TickHistory[i][0],lot,trade,self.TickHistory[i][1]]
                     self.position=t
                     self.TradeHistory.append(t)
            else:
                if trade==1:
                    t=[self.TickHistory[i][0],lot,trade,self.TickHistory[i][2]]
                    self.TradeHistory.append(t)
                    if self.position[1]==t[1] and self.position[2]==-1:
                        prof=(self.position[3]-t[3])/self.Point*self.position[1]*self.TivkValue
                        balance=balance+prof
                        self.ProfitHistory.apprnd([t[0],balance])
                        self.TradeCount=self.TradeCount+1
                        if prof>0:
                            self.Win=self.Win+1
                        self.position=[]
                    if self.position[2]==1:
                        self.position=[self.TickHistory[i][0],self.position[1]+t[1],1,(self.position[3]*self.position[1]+t[3]*t[1])/(self.position[1]+t[1])]
                    if self.position[2]==-1 and t[1]<self.position[1]:
                        self.position[1]=position[1]-t[1]
                        self.TradeCount=self.TradeCount+1
                        prof=(self.position[3]-t[3])/self.Point*t[1]*self.TivkValue
                        balance=balance+prof
                        self.ProfitHistory.apprnd([t[0],balance])
                        if prof>0:
                            self.Win=self.Win+1
                    if self.position[2]==-1 and t[1]>self.position[1]:
                        self.TradeCount=self.TradeCount+1
                        prof=(self.position[3]-t[3])/self.Point*self.position[1]*self.TivkValue
                        balance=balance+prof
                        self.ProfitHistory.apprnd([t[0],balance])
                        self.position=[self.TickHistory[i][0],t[1]-position[1],-1,self.TickHistory[i,1]]
                        if prof>0:
                            self.Win=self.Win+1
                if trade==-1:
                    t=[self.TickHistory[i][0],lot,trade,self.TickHistoty[i][1]]
                    self.TradeHistory.append(t)
                    if self.position[1]==t[1] and self.position[2]==1:
                        prof=(t[3]-self.position[3])/self.Point*self.position[1]*self.TivkValue
                        balance=balance+prof
                        self.ProfitHistory.apprnd([t[0],balance])
                        self.TradeCount=self.TradeCount+1
                        if prof>0:
                            self.Win=self.Win+1
                        self.position=[]
                    if self.position[2]==-1:
                        self.position=[self.TickHistory[i][0],self.position[1]+t[1],-1,(self.position[3]*self.position[1]+t[3]*t[1])/(self.position[1]+t[1])]
                    if self.position[2]==1 and t[1]<self.position[1]:
                        prof=(t[3]-self.position[3])/self.Point*t[1]*self.TivkValue
                        balance=balance+prof
                        self.ProfitHistory.apprnd([t[0],balance])
                        self.TradeCount=self.TradeCount+1
                        self.position[1]=self.position[1]-t[1]
                        if prof>0:
                            self.Win=self.Win+1
                    if self.position[2]==1 and t[1]>self.position[1]:
                        self.TradeCount=self.TradeCount+1
                        prof=(t[3]-self.position[3])/self.Point*self.position[1]*self.TivkValue
                        balance=balance+prof
                        self.ProfitHistory.apprnd([t[0],balance])
                        self.position=[self.TickHistoey[i][0],t[1]-self.position[1],1,self.TickHistory[i,2]]
                        if prof>0:
                            self.Win=self.Win+1
            i=i+1
        self.Profit=balance-self.Deposit
