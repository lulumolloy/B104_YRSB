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
mpl.rcParams['figure.facecolor'] = "#f7d9d6" #sets background

# import spreadsheet & convert to numpy (done in 2 steps bc array & frame are used)
dataFrame=pd.read_excel("B104_YRBS.xlsx", sheet_name="Sheet1")
dataArray=np.array(dataFrame)

# renaming variables for easier access
dataFrame.rename(columns={"q1":"Age","q2":"Sex","q6":"Height","q7":"Weight","q75":"Breakfast","q76":"Activity"}, inplace=True)

#shift data to match responses
dataFrame["Breakfast"]-=1
dataFrame["Activity"]-=1

def getBMI():
    bmi=[] #empty list
    height=dataArray[:,2]
    weight=dataArray[:,3]
    # go through list, take height & weight into BMI
    # numpy used for faster processing
    for x in range(len(height)): 
        if weight[x]!="nan" or height[x]!="nan": 
            bmi.append(weight[x]/ (height[x]**2))
        else:
            bmi.append("None") 
        #insert bmi into dataframe        
    dataFrame.insert(4, "BMI", bmi)

def getBMIHist():
    if ("BMI" in dataFrame.columns)==False:
       getBMI()
    bmi=dataFrame["BMI"].dropna()
    # make graph
    sns.histplot(x=bmi, bins=[10,15,20,25,30,35,40,45,50], color= '#f2a2a2', edgecolor="#bf7373", stat="percent") #bins is number of columns, edgecolor is outline of columns 
    
    # adjust scale of y axis & add grid
    plot.yticks([0,5,10,15,20,25,30,35,40,45,50]) #make the numbers a smaller increment
    plot.grid(axis="y", color="#f2bebe") #adds grid only for y axis
    
    # name columns, rows and title 
    plot.title("BMI Frequency")
    plot.xlabel("BMI")
    plot.ylabel("Percent of Participants")
    
    # print
    plot.show()
    
def getActivePeople():
    # make graph
    sns.countplot(dataFrame, x="Activity", color= '#f2a2a2', edgecolor="#bf7373", stat="percent") 
    
    # adjust scale of y axis & add grid
    plot.yticks([0,5,10,15,20,25,30]) #make the numbers a smaller increment
    plot.grid(axis="y", color="#f2bebe") #adds grid only for y axis
    
    # name columns, rows and title 
    plot.title("Numbers of Days Active")
    plot.xlabel("Days")
    plot.ylabel("Percent of Participants")

    # print
    plot.show()

def getBreakfastEaters():
    # make graph
    sns.countplot(dataFrame, x="Breakfast", color= '#f2a2a2', stat="percent") 
    
    # adjust scale of y axis & add grid   
    plot.yticks([0,5,10,15,20,25,30]) #make the numbers a smaller increment
    plot.grid(axis="y", color="#f2bebe") #adds grid only for y axis
    
    # name columns, rows and title 
    plot.title("Numbers of Days The Participants Ate Breakfast")
    plot.xlabel("Days")
    plot.ylabel("Percent of Participants")

    # print
    plot.show()

def getHeatmap():
    if ("BMI" in dataFrame.columns)==False:
       getBMI()
    
    #get correlation and chart
    correlation_matrix = dataFrame.corr()
    plot.figure(figsize = (8,8))
    sns.heatmap(correlation_matrix, cmap = 'RdPu', annot=True)
    
    # print
    plot.show()
    
def getCorrelationPlot():
    #make histplot 
    sns.histplot(dataFrame,x="Breakfast",y="Activity",bins=8,cmap="RdPu",thresh=None, stat="percent", discrete=True, cbar=True)

    #get responses per correlation pair
    percentage, var1, var2= np.histogram2d(dataFrame["Breakfast"],dataFrame["Activity"],bins=8) #var1 and var2 are unused but require declaration 

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

    # name columns, rows and title 
    plot.xlabel("Number of Days Breakfast is Eaten (per week)")
    plot.ylabel("Number of Days of Activity (per week)")
    plot.title("Correlation Between Breakfast and Activity")
    
    # print
    plot.show()
