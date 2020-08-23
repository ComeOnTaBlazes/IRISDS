#Import necessary modules
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import csv
import pandas as pd

#Open csv as df
df= pd.read_csv('irisds.csv')

#Seperate df by species
filtsetosa_df= df[(df['species'] == 'setosa')]
filtversicolor_df = df[(df['species'] == 'versicolor')]
filtvirginica_df = df[(df['species'] == 'virginica')]

#Create lists of each column per species
#Setosa
setosas_l = filtsetosa_df['sepal_length'].tolist()
setosas_w = filtsetosa_df['sepal_width'].tolist()
setosap_l = filtsetosa_df['petal_length'].tolist()
setosap_w = filtsetosa_df['petal_width'].tolist()

#Versicolor
versicolors_l = filtversicolor_df['sepal_length'].tolist()
versicolors_w = filtversicolor_df['sepal_width'].tolist()
versicolorp_l = filtversicolor_df['petal_length'].tolist()
versicolorp_w = filtversicolor_df['petal_width'].tolist()

#Virginica
virginicas_l = filtvirginica_df['sepal_length'].tolist()
virginicas_w = filtvirginica_df['sepal_width'].tolist()
virginicap_l = filtvirginica_df['petal_length'].tolist()
virginicap_l = filtvirginica_df['petal_width'].tolist()