
class Tester:
    self.TickHistory=[]
    self.TradeHistory=[]
    self.System # Функция реализуящая систему вида lot,trade=f(ticks) где tick список тиков размером N, trade 0 - нет сделки 1 - покупка -1 - продажа
    self.N=20 # Количество тиков передающихся в функцию реализующую систему
    self.Deposit=1000
    self.TickValue=1 # Цена тика на 1 лот
    self.Profit
    self.MaxDropdawn
    self. TradeCount
    self.WinPercent

    def Test(self):
        self.TradeHistory=[]
        i=self.N-1
        last=len(self.TickHistory)
        position=[]
        while i<last:
            lot,trade=self.System(self.TickHistory[i-self.N-1:i])
            if len(pozition)==0:
                if trade==1:
                    t=[self.TickHistory[i,0],lot,trade,self.TickHistoty[i,2]]
                    position=t
                    self.TradeHistory.append(t)
                if trade==-1:
                     t=[self.TickHistory[i,0],lot,trade,self.TickHistoty[i,1]]
                     position=t
                     self.TradeHistory.append(t)
            else:
                if trade==1:
                    t=[self.TickHistory[i,0],lot,trade,self.TickHistoty[i,2]]
                    self.TradeHistory.append(t)
                    if position[1]==t[1] and position[2]==-1:
                        position=[]
                    if position[2]==1:
