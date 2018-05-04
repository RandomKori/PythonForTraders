//+------------------------------------------------------------------+
//|                                                          Ops.mqh |
//|                        Copyright 2018, MetaQuotes Software Corp. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "Copyright 2018, MetaQuotes Software Corp."
#property link      "https://www.mql5.com"
//+------------------------------------------------------------------+
//| defines                                                          |
//+------------------------------------------------------------------+
// #define MacrosHello   "Hello, world!"
// #define MacrosYear    2010
//+------------------------------------------------------------------+
//| DLL imports                                                      |
//+------------------------------------------------------------------+
// #import "user32.dll"
//   int      SendMessageA(int hWnd,int Msg,int wParam,int lParam);
// #import "my_expert.dll"
//   int      ExpertRecalculate(int wParam,int lParam);
// #import
//+------------------------------------------------------------------+
//| EX5 imports                                                      |
//+------------------------------------------------------------------+
// #import "stdlib.ex5"
//   string ErrorDescription(int error_code);
// #import
//+------------------------------------------------------------------+

double add(double a1,double a2)
{
   return a1+a2;
}

double sub(double a1,double a2)
{
   return a1-a2;
}

double mul(double a1,double a2)
{
   return a1*a2;
}

double div(double a1,double a2)
{
   if(a2==0.0) return 0.0;
   return a1/a2;
}

double pwr(double a1,int a2)
{
   return MathPow(a1,a2);
}

double osqrt(double a1)
{
   return MathSqrt(a1);
}

double osin(double a1)
{
   return MathSin(a1);
}

double ocos(double a1)
{
   return MathCos(a1);
}

double otan(double a1)
{
   return MathTan(a1);
}

double olog10(double a1)
{
   if(a1==0.0) return 0.0;
   return MathLog10(a1);
}

double neg(double a1)
{
   return 0.0-a1;
}

double if_then_else(bool a1,double a2,double a3)
{
   double rez=a3;
   if(a1) rez=a2;
   return rez;
}

bool ravno(double a1,double a2)
{
   return a1==a2;
}

bool bolshe(double a1,double a2)
{
   return a1>a2;
}

bool menshe(double a1,double a2)
{
   return a1<a2;
}

bool oand(bool a1,bool a2)
{
   return a1 && a2;
}

bool oor(bool a1,bool a2)
{
   return a1 || a2;
}

bool onot (bool a)
{
   return ~a;
}

double avr(double a1,double a2)
{
   return (a1+a2)/2.0;
}