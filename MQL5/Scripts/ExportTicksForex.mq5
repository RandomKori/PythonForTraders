//+------------------------------------------------------------------+
//|                                                  ExportTicks.mq5 |
//|                                                           Рэндом |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "Рэндом"
#property link      "https://www.mql5.com"
#property version   "1.00"
#property script_show_inputs
//--- input parameters
input datetime Date=D'2016.10.21';

//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+

void OnStart()
  {
//---
   MqlTick t[];
   int rz=COPY_TICKS_ALL;
   CopyTicksRange(Symbol(),t,rz,(ulong)(Date*1000),(ulong)(TimeCurrent()*1000));
   int ot=FileOpen(Symbol()+"_Ticks.csv",FILE_WRITE|FILE_ANSI,",");
   string hdr="DateTime,Bid,Ask";
   FileWrite(ot,hdr);
   int limit=ArraySize(t);
   for(int i=0;i<limit;i++)
   {
      string dt=TimeToString((ulong)(t[i].time),TIME_DATE|TIME_SECONDS);
      int rep=StringReplace(dt,".","-");
      string d=dt+","+DoubleToString(t[i].bid,Digits())+","+DoubleToString(t[i].ask,Digits());
      FileWrite(ot,d);
   }
   FileClose(ot);
  }
//+------------------------------------------------------------------+
