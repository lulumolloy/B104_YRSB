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
dataFrame= pd.read_excel("B104_YRBS.xlsx", sheet_name="Sheet1")
dataArray= np.array(dataFrame)

# renaming variables for easier access
dataFrame.rename(columns={"q1":"Age","q2":"Sex","q6":"Height","q7":"Weight","q75":"Breakfast","q76":"Activity"}, inplace=True)

#shift data to match responses
dataFrame["Breakfast"]-= 1
dataFrame["Activity"]-= 1

def getBMI():
    bmi=[] #empty list
    height= dataArray[:,2]
    weight= dataArray[:,3]
    # go through list, take height & weight into BMI
    # numpy used for faster processing
    for x in range(len(height)): 
        if weight[x]!= "nan" or height[x]!= "nan": 
            bmi.append(weight[x]/ (height[x]**2))
        else:
            bmi.append("None") 
        #insert bmi into dataframe        
    dataFrame.insert(4, "BMI", bmi)

def getBMIHist():
    #create bmi if it hasn't been created already
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
    plot.show(block=False)
    
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
    plot.show(block=False)

def getBreakfastEaters():
    # make graph
    sns.countplot(dataFrame, x="Breakfast", color= '#f2a2a2', edgecolor="#bf7373", stat="percent") 
    
    # adjust scale of y axis & add grid   
    plot.yticks([0,5,10,15,20,25,30]) #make the numbers a smaller increment
    plot.grid(axis="y", color="#f2bebe") #adds grid only for y axis
    
    # name columns, rows and title 
    plot.title("Numbers of Days The Participants Ate Breakfast")
    plot.xlabel("Days")
    plot.ylabel("Percent of Participants")

    # print
    plot.show(block=False)

def getHeatmap():
    # create bmi if it hasn't been created already
    if ("BMI" in dataFrame.columns)==False:
      getBMI()
    
    # make graph
    correlation_matrix = dataFrame.corr()
    plot.figure(figsize = (8,8))
    sns.heatmap(correlation_matrix, cmap = 'RdPu', annot=True)
    
    # print
    plot.show(block=False)
    
def getCorrelationPlot():
    #make histplot 
    sns.histplot(dataFrame, x="Breakfast", y="Activity", bins=8, cmap="RdPu", thresh=None, stat="percent", discrete=True, cbar=True)

    #get responses per correlation pair
    percentage, var1, var2= np.histogram2d(dataFrame["Breakfast"], dataFrame["Activity"], bins=8) #var1 and var2 are unused but require declaration 

    #convert responses into percentage
    percentage/=14083.0 
    percentage*=100

    #add text for each correlation pair stating percentage 
    for x in range(8):
        for y in range(8):
            if percentage[x][y]<9: #makes 9% white
                plot.text(x-.38, y-.1, (f"{round(percentage[x][y],2)}%"), fontsize=9, color="black")
            else:
                plot.text(x-.38, y-.1, (f"{round(percentage[x][y],2)}%"), fontsize=9, color="white")

    # name columns, rows and title 
    plot.xlabel("Number of Days Breakfast is Eaten (per week)")
    plot.ylabel("Number of Days of Activity (per week)")
    plot.title("Correlation Between Breakfast and Activity")
    
    # print
    plot.show(block=False)
    
    
    
print('\nHello')
print('-----------------------------------------------------------------------')
print('We were curious to see the relation between how often people eat breakfast and their activity levels\nSo, we created some graphs!')

print('\nWould you like to see our graphs?\nNote: Answering anything other than "y" or "Y" will end the script :c')
answer = input('\nY/N: ').lower()
while answer == 'y':
    print('\nHere are your options!')
    print('To choose a graph, please enter its assigned number :) ')
    print('\n1. The Heatgraph\n2. BMI Bar Graph\n3. Activity Bar Graph\n4. Breakfast Bar Graph\n5. Correlation Plot')
    plot.close() #close current graph (nessecary for VScode)
    which_graph = input(('\nPlease enter the assigned number:  '))
    
    if which_graph == '1':
        print('\nHere is a heat graph ')
        getHeatmap()
        answer = input('\nWould you like to see more graphs?  ').lower()
        
    elif which_graph == '2':
        print('\nHere is a bar graph showing the BMI of the participants')
        getBMIHist()
        answer = input('\nWould you like to see more graphs?  ').lower()
        
    elif which_graph == '3':
        print('\nHere is a bar graph showing how many people were active in the last 7 days')
        getActivePeople()
        answer = input('\nWould you like to see more graphs?  ').lower()
        
    elif which_graph == '4':
        print('\nHere is a bar graph showing how many people ate breakfast in the last 7 days')
        getBreakfastEaters()
        answer = input('\nWould you like to see more graphs?  ').lower()
        
    elif which_graph == '5':
        print('\nHere is a graph showing the correlation of people who ate breakfast VS people who were active')
        getCorrelationPlot()
        answer = input('\nWould you like to see more graphs?  ').lower()
        
    else:
        print('\nInvalid input :( Please try again.')
else:
    print('\nThank you for your time :) ')

