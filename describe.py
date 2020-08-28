#Import necessary modules
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import csv
import pandas as pd


#Open csv as df
df= pd.read_csv('irisds.csv')

alldata = df.describe().to_dict()

#Seperate df by species
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
#https://www.youtube.com/watch?v=daefaLgNkw0&t=466s
filtsetosa = df[(df['species'] == 'setosa')].describe().to_dict()
filtversicolor = df[(df['species'] == 'versicolor')].describe().to_dict()
filtvirginica = df[(df['species'] == 'virginica')].describe().to_dict()

print(alldata)
print(filtsetosa)
print(filtversicolor)
print(filtvirginica)


