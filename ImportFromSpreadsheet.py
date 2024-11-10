# Developers: Doherty, Hailey & Holdt, Lucy
# Class: B104
# Group: Non-Major
# Project: YRSB Data Analysis- Final Project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

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

# import spreadsheet & convert to numpy 
dataSet=np.array(pd.read_excel("B104_YRBS.xlsx", sheet_name="b104"))

makeSexBarGraph(dataSet)
