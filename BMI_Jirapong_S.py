from tkinter import *
import math

def BMIPerformance(BMI_Index):
    if BMI_Index >= 30 :
        performance = "Too fat !!!"
        return performance
    elif BMI_Index >= 25 and BMI_Index < 30 :
        performance = "Fat !!!"
        return performance
    elif BMI_Index >= 23 and BMI_Index < 25:
        performance = "Overweight !!!"
        return performance
    elif BMI_Index >= 18.6 and BMI_Index < 23 :
        performance = "Normal weight :)"
        return performance
    else:
        performance = "Too skin !!!"
        return performance

def BMICalculation(event):
    BMI = float(textWeight.get()) / math.pow(float(textHeight.get())/100,2)
    labelResult1.configure(text = str(round(BMI)))
    labelResult2.configure(text = BMIPerformance(round(BMI)))

mainWindow = Tk()
labelTitle = Label(mainWindow,text = "BMI Calculated Program",font = ("Century Gothic",24))
labelTitle.grid(row=0,column=0)
########################End of Title###################################################
labelHeight = Label(mainWindow,text = "Height (cm) : ",font = ("Century Gothic",16),fg="blue",anchor = E)
labelHeight.grid(row=1,column=0)
textHeight = Entry(mainWindow,font = ("Century Gothic",16))
textHeight.grid(row=1,column=1)
########################End of height###################################################
labelWeight = Label(mainWindow,text = "Weight (kg) : ",font = ("Century Gothic",16),fg = "blue",anchor = E)
labelWeight.grid(row=2,column=0)
textWeight = Entry(mainWindow,font = ("Century Gothic",16))
textWeight.grid(row=2,column=1)
########################End of weight###################################################
buttonCal = Button(mainWindow,text = "Click to calculation",font = ("Century Gothic",16),bg = "cyan")
buttonCal.grid(row=3,column=0)
buttonCal.bind("<Button-1>",BMICalculation)
########################End of calculation###################################################
labelResult1 = Label(mainWindow,text = "-> BMI number here !!!",font=("Century Gothic",16))
labelResult1.grid(row=3,column=1)
labelResult2 = Label(mainWindow,text = "-> BMI conclusion here !!!",font = ("Century Gothic",16))
labelResult2.grid(row=3,column=2)
########################End of result###################################################
mainWindow.mainloop()

