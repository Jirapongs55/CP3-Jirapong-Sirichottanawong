from forex_python.converter import CurrencyRates
from datetime import *
from math import *
from tkinter import *


class FutureValue:
    pv = 0
    fv = 0
    interest = 0
    year = 0
    print("Input your start date".center(42,"-"))
    day_start = int(input("Day number :"))
    month_start = int(input("Month number :"))
    year_start = int(input("Year number :"))
    date_start = datetime(year_start,month_start,day_start,00,00,00,00)
    print("Start date : ",date_start)

    def convert_currency(self):
        c = CurrencyRates()
        self.pv = c.convert(input("Input based currency :"),
                          input("Input destinated currency :"),
                          int(input("Input amount :")),
                          self.date_start)
        print("Present Value : %d" % (self.pv))
        return self.pv


    def calculation_fv(self):
        self.convert_currency()
        self.interest = int(input("%Interest rate per year :")) / 100
        self.year = int(input("Input year duration :"))
        for index in range(self.year + 1):
            self.fv = self.pv * pow(1 + self.interest,index)
            print("Future Value (year->%d) : %d" %(index,int(self.fv)))
        print("Future Value in last year : %d" %(int(self.fv)))

fv1 = FutureValue()
print(fv1.calculation_fv())






