//+------------------------------------------------------------------+
//|                                                   MartGreg_1.mq5 |
//|                                             Copyright 2010, Alf. |
//|         |
//+------------------------------------------------------------------+
#property copyright "Copyright 2010, Alf."
#property link      ""
#property version   "1.00"



//--- input parameters
input double   Lot=1;
input string   SM="BR Splice";
input int      Stop=7;
input int      Tp=7;
input int      Slipage=2;

input double   MaxDropdown=50.0;
input ENUM_ORDER_TYPE_FILLING Isp=ORDER_FILLING_RETURN;

#include <Ops.mqh>

double MaxBalance=0;
//+------------------------------------------------------------------+
//| Open                                                             |
//+------------------------------------------------------------------+
void Open()
  {
   int r=Poz();
   MqlTick last_tick;
   SymbolInfoTick(_Symbol,last_tick);
   MqlTradeResult result;
   MqlTradeRequest request;

   ZeroMemory(result);
   ZeroMemory(request);

   request.symbol=_Symbol;
   request.magic=777;
   request.deviation=Slipage;
   request.action=TRADE_ACTION_DEAL;
   request.type_filling=Isp;
   if(r>0.5)
     {
      request.volume=Lot;
      request.price=last_tick.ask;
      request.type=ORDER_TYPE_BUY;
      request.sl=last_tick.ask-Stop*Point();
      request.tp=last_tick.ask+Tp*Point();
      OrderSend(request,result);
      return;
     }
   if(r<(0.0-0.5))
     {
      request.volume=Lot;
      request.price=last_tick.bid;
      request.type=ORDER_TYPE_SELL;
      request.sl=last_tick.bid+Stop*Point();
      request.tp=last_tick.bid-Tp*Point();
      OrderSend(request,result);
      return;
     }
  }
//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {
//---
   MarketBookAdd(SM);
   if(GlobalVariableCheck("MaxBalance")) MaxBalance=GlobalVariableGet("MaxBalance");
//---
   return(0);
  }
//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
//---
   
  }
//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {
//---
   if(!Risk()) return;
   if(!PositionSelect(Symbol()))Open();

  }
//+------------------------------------------------------------------+
void OnBookEvent (const string& symbol)
{
   
}

bool Risk()
{
   bool rez=true;
   double bl=AccountInfoDouble(ACCOUNT_BALANCE);
   if(bl>MaxBalance)
   {
      MaxBalance=bl;
      GlobalVariableSet("MaxBalance",MaxBalance);
   }
   if(MaxBalance>bl)
   {
      double prs=MaxBalance-bl;
      double prc=MaxBalance/100;
      double p=prs/prc;
      if(p>MaxDropdown) rez=false;
   }
   return rez;
}

double Poz()
{
   double r=0.0;
   MqlTick t[10];
   double type[10];
   CopyTicks(Symbol(),t,COPY_TICKS_ALL,0,10);
   for(int i=0;i<10;i++)
   {
      if((t[i].flags|TICK_FLAG_BUY) && TICK_FLAG_BUY) type[i]=1.0;
      if((t[i].flags|TICK_FLAG_SELL) && TICK_FLAG_SELL) type[i]=-1.0;
   }
   
   double bid1=t[0].bid;
   double ask1=t[0].ask;
   double last1=t[0].last;
   double volume1=t[0].volume;
   double type1=type[0];
   double bid2=t[1].bid;
   double ask2=t[1].ask;
   double last2=t[1].last;
   double volume2=t[1].volume;
   double type2=type[1];
   double bid3=t[2].bid;
   double ask3=t[2].ask;
   double last3=t[2].last;
   double volume3=t[2].volume;
   double type3=type[2];
   double bid4=t[3].bid;
   double ask4=t[3].ask;
   double last4=t[3].last;
   double volume4=t[3].volume;
   double type4=type[3];
   double bid5=t[4].bid;
   double ask5=t[4].ask;
   double last5=t[4].last;
   double volume5=t[4].volume;
   double type5=type[4];
   double bid6=t[5].bid;
   double ask6=t[5].ask;
   double last6=t[5].last;
   double volume6=t[5].volume;
   double type6=type[5];
   double bid7=t[6].bid;
   double ask7=t[6].ask;
   double last7=t[6].last;
   double volume7=t[6].volume;
   double type7=type[6];
   double bid8=t[7].bid;
   double ask8=t[7].ask;
   double last8=t[7].last;
   double volume8=t[7].volume;
   double type8=type[7];
   double bid9=t[8].bid;
   double ask9=t[8].ask;
   double last9=t[8].last;
   double volume9=t[8].volume;
   double type9=type[8];
   double bid10=t[9].bid;
   double ask10=t[9].ask;
   double last10=t[9].last;
   double volume10=t[9].volume;
   double type10=type[9];
   
   bool True=true;
   bool False=false;
   
   r=ocos(neg(div(avr(div(if_then_else(oor(False, True), neg(bid9), osin(volume2)), osqrt(if_then_else(True, last4, ask3))), sub(otan(div(ocos(avr(avr(otan(sub(ask5, ask7)), add(olog10(bid2), div(volume3, bid1))), avr(osqrt(pwr(type9, 2)), otan(osqrt(volume10))))), div(pwr(neg(otan(olog10(last10))), ravno(olog10(div(type3, volume2)), olog10(ocos(last1)))), ocos(ocos(ocos(osin(ask2))))))), neg(olog10(volume5)))), mul(neg(pwr(pwr(div(div(neg(div(osin(if_then_else(False, bid2, last2)), div(if_then_else(True, volume3, 75.94849428051502), neg(last5)))), ocos(mul(neg(otan(bid10)), ocos(mul(45.58307112035175, volume4))))), otan(add(osin(osin(mul(last10, last1))), mul(add(pwr(volume4, oor(bolshe(avr(bid8, bid4), sub(type8, type9)), oand(oor(False, True), ravno(last4, ask10)))), neg(bid5)), osqrt(ocos(ask1)))))), ravno(otan(div(sub(div(mul(bid9, type1), mul(last7, bid5)), olog10(sub(last8, ask7))), if_then_else(menshe(div(volume10, last5), neg(ask4)), div(osin(type3), if_then_else(False, last8, last8)), pwr(pwr(bid4, True), ravno(type7, ask10))))), osqrt(olog10(add(osin(neg(bid1)), olog10(osin(ask4))))))), ravno(neg(mul(avr(mul(mul(avr(volume3, bid9), ocos(ask5)), osqrt(otan(volume5))), neg(mul(avr(neg(div(osin(if_then_else(False, bid2, last2)), div(if_then_else(True, volume3, 75.94849428051502), neg(last5)))), bid1), sub(ask1, volume8)))), otan(ocos(pwr(neg(type2), False))))), if_then_else(bolshe(pwr(osin(osqrt(sub(bid2, type10))), oor(bolshe(avr(bid8, bid4), sub(type8, type9)), oand(oor(False, True), ravno(last4, ask10)))), sub(avr(otan(neg(volume9)), osin(ocos(-106.26276418857661))), osqrt(osqrt(volume5)))), pwr(pwr(if_then_else(bolshe(osin(volume8), sub(ask5, last3)), neg(osqrt(last8)), div(sub(ask5, volume7), sub(last2, volume6))), onot(bolshe(div(volume9, volume9), div(ask10, bid4)))), onot(bolshe(div(volume9, volume9), div(ask10, bid4)))), add(pwr(avr(otan(add(type5, volume7)), olog10(olog10(bid8))), ravno(div(olog10(ask8), otan(type4)), ocos(div(volume6, bid2)))), add(pwr(if_then_else(oor(True, False), pwr(type6, 2), otan(ask6)), oand(True, False)), otan(mul(if_then_else(True, ask1, ask1), neg(last4))))))))), osqrt(ocos(neg(otan(otan(neg(mul(div(div(bid7, type9), avr(45.809299893649204, bid5)), div(last9, div(volume5, last9)))))))))))));
   
   return r;
}
