# Developers: Doherty, Hailey & Holdt, Lucy
# Class: B104
# Group: Non-Major
# Project: YRSB Data Analysis- Final Project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import matplotlib as mpl
import seaborn as sns


#make charts pretty
mpl.rcParams['axes.facecolor'] = "#fcf1ee" #sets chart background
mpl.rcParams['figure.facecolor'] = "#fcf1ee" #sets background

# import spreadsheet & convert to numpy (done in 2 steps bc array & frame are used)
dataFrame=pd.read_excel("B104_YRBS.xlsx", sheet_name="Sheet1")
dataArray=np.array(dataFrame)

# variables for ease of access
age=dataArray[:,0]
sex=dataArray[:,1]
height=dataArray[:,2]
weight=dataArray[:,3]
breakfast=dataArray[:,4]
activity=dataArray[:,5]

dataFrame.rename(columns={"q1":"Age","q2":"Sex","q6":"Height","q7":"Weight","q75":"Breakfast","q76":"Activity"}, inplace=True)

#shift data to match responses
dataFrame["Breakfast"]-=1
dataFrame["Activity"]-=1


def getBMIHist():
    bmi=[]
    #calculate bmi, make list
    for x in range(len(height)):
        if weight[x]!="nan" or height[x]!="nan": #remove empty entries
            bmi.append(weight[x]/ (height[x]**2))

    plot.hist(bmi, bins=[10,15,20,25,30,35,40,45,50,55], color= '#ff56a0', edgecolor="#b92e6b") #bins is number of columns, edgecolor is outline of columns 
    plot.xticks([10,15,20,25,30,35,40,45,50,55]) #make the numbers a smaller increment
    plot.grid(axis="y") #adds grid only for y axis
    plot.title("BMI Frequency")
    plot.xlabel("BMI")
    plot.ylabel("Participants")
    plot.show()
    
def ActivePeople():
    # make columns and rows
    plot.hist(activity, bins=[1,2,3,4,5,6,7], color= '#ff56a0', edgecolor="#b92e6b") 
    
    # name columns and rows
    plot.title("Numbers of Days Active")
    plot.xlabel("Days")
    plot.ylabel("Participants")

    # print
    plot.show()

def BreakfastEaters():
    # make columns and rows
    sns.countplot(dataFrame, x="Breakfast", color= '#ff56a0', edgecolor="#b92e6b", stat="percent") 

    # name columns and rows
    plot.title("Numbers of Days The Participants Ate Breakfast")
    plot.xlabel("Days")
    plot.ylabel("Percent of Participants")

    # print
    plot.show()

def getHeatmap():
    bmi=[]
    #calculate bmi, get list
    for x in range(len(height)): #bmi, this time w/empty values!
        if weight[x]!="nan" or height[x]!="nan": 
            bmi.append(weight[x]/ (height[x]**2))
        else:
            bmi.append("none")
    #insert bmi into dataframe        
    dataFrame.insert(4, "BMI", bmi)

    #get correlation and chart
    correlation_matrix = dataFrame.corr()
    plot.figure(figsize = (8,8))
    sns.heatmap(correlation_matrix, cmap = 'RdPu', annot=True)
    plot.show()
    
def getCorrelationPlot():
    #make histplot 
    sns.histplot(dataFrame,x="Breakfast",y="Activity",bins=8,cmap="RdPu",thresh=None, stat="percent", discrete=True, cbar=True)

    #get responses per correlation pair
    percentage, var1, var2= np.histogram2d(breakfast,activity,bins=8) #var1 and var2 are unused but require declaration 

    #convert responses into percentage
    percentage/=14083.0 
    percentage*=100

    #add text for each correlation pair stating percentage 
    for x in range(8):
        for y in range(8):
            if percentage[x][y]<9: #makes 9% white
                plot.text(x-.38,y-.1,(f"{round(percentage[x][y],2)}%"),fontsize=9,color="black")
            else:
                plot.text(x-.38,y-.1,(f"{round(percentage[x][y],2)}%"),fontsize=9,color="white")

    #add labels 
    plot.xlabel("Number of Days Breakfast is Eaten (per week)")
    plot.ylabel("Number of Days of Activity (per week)")
    plot.title("Correlation Between Breakfast and Activity")
    plot.show()

