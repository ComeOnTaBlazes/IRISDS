from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import csv
import pandas as pd

plt.style.use('fivethirtyeight')

df = pd.read_csv('irisds.csv')


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

columnlist = [sepal_l, sepal_w, petal_l, petal_w]

#Histogram whole dataframe
#https://www.youtube.com/watch?v=XFZRVnP-MTU
fig, ax2d = plt.subplots(2,2, figsize= (8,6))

ax = np.ravel(ax2d)
#https://youtu.be/fIFDI7bWNpA?t=485

fig.suptitle('Iris Flower Distribution of Variables')

for count, p in enumerate(columnlist):
    ax[count].hist(p, bins = 15)
    ax[count].set(title=df.columns.values[count], xlabel = 'cm')

fig.savefig('fig1.jpg')