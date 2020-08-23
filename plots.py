from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import csv
import pandas as pd

#https://www.youtube.com/watch?v=XDv6T4a0RNc
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist
#https://www.youtube.com/watch?v=XFZRVnP-MTU
#https://www.youtube.com/watch?v=zZZ_RCwp49g&


plt.style.use('fivethirtyeight')

df = pd.read_csv('irisds.csv')

#Create array for each variable
sepal_l = df['sepal_length'].array
sepal_w = df['sepal_width'].array
petal_l = df['petal_width'].array
petal_w = df['petal_length'].array


filtsetosa_df= df[(df['species'] == 'setosa')]
filtversicolor_df = df[(df['species'] == 'versicolor')]
filtvirginica_df = df[(df['species'] == 'virginica')]

#Create array of each column per species & add to dictionary
#Setosa
setosas_l = filtsetosa_df['sepal_length'].array
setosas_w = filtsetosa_df['sepal_width'].array
setosap_l = filtsetosa_df['petal_length'].array
setosap_w = filtsetosa_df['petal_width'].array

#Sepal Length Plots
plt.hist(setosas_l, bins = 15, edgecolor = 'black')
plt.title('')
plt.xlabel('Length(cm)')
plt.ylabel('# of Occurances')

plt.hist(setosas_w, bins = 15, edgecolor = 'black')
plt.title('')
plt.xlabel('Length(cm)')
plt.ylabel('# of Occurances')

plt.hist(setosap_l, bins = 15, edgecolor = 'black')
plt.title('')
plt.xlabel('Length(cm)')
plt.ylabel('# of Occurances')

plt.hist(setosap_w, bins = 15, edgecolor = 'black')
plt.title('')
plt.xlabel('Length(cm)')
plt.ylabel('# of Occurances')

#Versicolor
versicolors_l = filtversicolor_df['sepal_length'].array
versicolors_w = filtversicolor_df['sepal_width'].array
versicolorp_l = filtversicolor_df['petal_length'].array
versicolorp_w = filtversicolor_df['petal_width'].array

plt.hist(versicolors_l, bins = 15, edgecolor = 'black')
plt.title('')
plt.xlabel('Length(cm)')
plt.ylabel('# of Occurances')

plt.hist(versicolors_w, bins = 15, edgecolor = 'black')
plt.title('')
plt.xlabel('Length(cm)')
plt.ylabel('# of Occurances')

plt.hist(versicolorp_l, bins = 15, edgecolor = 'black')
plt.title('')
plt.xlabel('Length(cm)')
plt.ylabel('# of Occurances')

plt.hist(versicolorp_w, bins = 15, edgecolor = 'black')
plt.title('')
plt.xlabel('Length(cm)')
plt.ylabel('# of Occurances')

#Virginica
virginicas_l = filtvirginica_df['sepal_length'].array
virginicas_w = filtvirginica_df['sepal_width'].array
virginicap_l = filtvirginica_df['petal_length'].array
virginicap_w = filtvirginica_df['petal_width'].array

plt.hist(virginicas_l, bins = 15, edgecolor = 'black')
plt.title('')
plt.xlabel('Length(cm)')
plt.ylabel('# of Occurances')

plt.hist(virginicas_w, bins = 15, edgecolor = 'black')
plt.title('')
plt.xlabel('Length(cm)')
plt.ylabel('# of Occurances')

plt.hist(virginicap_l, bins = 15, edgecolor = 'black')
plt.title('')
plt.xlabel('Length(cm)')
plt.ylabel('# of Occurances')

plt.hist(virginicap_w, bins = 15, edgecolor = 'black')
plt.title('')
plt.xlabel('Length(cm)')
plt.ylabel('# of Occurances')