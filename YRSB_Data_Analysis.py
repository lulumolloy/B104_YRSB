# Developers: Doherty, Hailey & Holdt, Lucy
# Class: B104
# Group: Non-Major
# Project: YRSB Data Analysis- Final Project

import pandas as pd
# import spreadsheet
dataSet=pd.read_excel("B104_YRBS.xlsx", sheet_name="b104") #import spreadsheet

# create lists for each relevant column 
# empty value = nan
breakfast =dataSet["q75"].to_list() 
activity =dataSet["q76"].to_list()
age =dataSet["q1"].to_list()
sex =dataSet["q2"].to_list()
height =dataSet["q6"].to_list()
weight =dataSet["q7"].to_list()


