# Developers: Doherty, Hailey & Holdt, Lucy
# Class: B104
# Group: Non-Major
# Project: YRSB Data Analysis- Final Project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import matplotlib as mpl

#make charts pretty
mpl.rcParams['axes.facecolor'] = "#fac8de" #sets chart background
mpl.rcParams['figure.facecolor'] = "#fce3ee" #sets background

# import spreadsheet & convert to numpy 
dataFrame=pd.read_excel("B104_YRBS.xlsx", sheet_name="Sheet1")
dataArray=np.array(dataFrame)

# variables for ease of access
age=dataArray[:,0]
sex=dataArray[:,1]
height=dataArray[:,2]
weight=dataArray[:,3]
breakfast=dataArray[:,4]
activity=dataArray[:,5]

def getBMIHist(height,weight):
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

def makeSexBarGraph(dataSet):
    """get count of how many participants are male or female"""
    #(sex == 1) is shorthand if statement, if 1, true, else false.
    female = (dataSet[:,1] == 1).sum() #sum counts how many entries are true
    male = (dataSet[:,1] == 2).sum() 

    x= np.array(["females","males"])
    y=[female,male]
    plot.bar(x,y) #creates graph
    plot.show() #shows us the graph
   
    #add additional data for people who didn't respond 
    na= (dataSet[:,1]== "nan").sum() # nan=no response 
    print(f"{na} people didn't respond. That's {round(na/len(dataSet),2)}% of responses")

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
    plot.hist(breakfast, bins=[1,2,3,4,5,6,7], color= '#ff56a0', edgecolor="#b92e6b") 

    # name columns and rows
    plot.title("Numbers of Days The Participants Ate Breakfast")
    plot.xlabel("Days")
    plot.ylabel("Participants")

    # print
    plot.show()

def getHeatmap(dataFrame, height, weight):
    bmi=[]
    #calculate bmi, get list
    for x in range(len(height)): #bmi, this time w/empty values!
        if weight[x]!="nan" or height[x]!="nan": 
            bmi.append(weight[x]/ (height[x]**2))
        else:
            bmi.append("none")
    #rename columns for chart to be clear
    dataFrame.rename(columns={"q1":"Age","q2":"Sex","q6":"Height","q7":"Weight","q75":"Breakfast","q76":"Activity"}, inplace=True)
    dataFrame.insert(4, "BMI", bmi) #insert bmi into dataframe

    #get correlation and chart
    correlation_matrix = dataFrame.corr()
    plot.figure(figsize = (8,8))
    sns.heatmap(correlation_matrix, cmap = 'RdPu', annot=True)
    plot.show()
