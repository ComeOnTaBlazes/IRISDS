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
petal_w = df['petal_width'].array
allspecies = [sepal_l, sepal_w, petal_l, petal_w]

#Isolate data for each species
filtsetosa_df= df[(df['species'] == 'setosa')]
filtversicolor_df = df[(df['species'] == 'versicolor')]
filtvirginica_df = df[(df['species'] == 'virginica')]

#Create array of each column per species
#Setosa
setosas_l = filtsetosa_df['sepal_length'].array
setosas_w = filtsetosa_df['sepal_width'].array
setosap_l = filtsetosa_df['petal_length'].array
setosap_w = filtsetosa_df['petal_width'].array
setosalist = [setosas_l, setosas_w, setosap_l, setosap_w]

#Versicolor
versicolors_l = filtversicolor_df['sepal_length'].array
versicolors_w = filtversicolor_df['sepal_width'].array
versicolorp_l = filtversicolor_df['petal_length'].array
versicolorp_w = filtversicolor_df['petal_width'].array
versicolorlist = [versicolors_l, versicolors_w, versicolorp_l, versicolorp_w]

#Virginica
virginicas_l = filtvirginica_df['sepal_length'].array
virginicas_w = filtvirginica_df['sepal_width'].array
virginicap_l = filtvirginica_df['petal_length'].array
virginicap_w = filtvirginica_df['petal_width'].array
virginicalist = [virginicas_l, virginicas_w, virginicap_l, virginicap_w]

toplvlist = [allspecies, setosalist, versicolorlist, virginicalist]
formattinglist = ['All Species', 'Setosa', 'Versicolor','Virginica',]

#Histogram whole dataframe
#https://www.youtube.com/watch?v=XFZRVnP-MTU
fig, ax2d = plt.subplots(2,2, figsize= (8,6))

ax = np.ravel(ax2d)
#https://youtu.be/fIFDI7bWNpA?t=485

fig.suptitle('Iris Flower Distribution of Variables')

#if count == 0:
#    fig.suptitle('Iris Flower Distribution of Variables')
#else:
#    fig.suptitle('{} Flower Distribution of Variables'.format(i for x,i in enumerate(toplvlist) if x = count):-4)

for count, p in enumerate(allspecies):
    ax[count].hist(p, bins = 15, edgecolor='black')
    ax[count].set(title=df.columns.values[count])
    if count > 1:
        ax[count].set(xlabel = 'cm')
    if count == 0 or 2:
         ax[count].set(ylabel = '# of occurrences')

    for count, q in enumerate(formattinglist):
    [fig.savefig('{z}hist.jpg'.format(z = q))]

setosalist = [setosas_l, setosas_w, setosap_l, setosap_w]

fig2, ax2d = plt.subplots(2,2, figsize= (8,6))

ax = np.ravel(ax2d)

fig.suptitle('Setosa Distribution of Variables')

for count, p in enumerate(setosalist):
    ax[count].hist(p, bins = 15, edgecolor='black')
    ax[count].set(title=df.columns.values[count], xlabel = 'cm')

    fig.savefig('setosahist.jpg')

    
versicolorlist = [versicolors_l, versicolors_w, versicolorp_l, versicolorp_w]

fig2, ax2d = plt.subplots(2,2, figsize= (8,6))

ax = np.ravel(ax2d)

fig.suptitle('Versicolor Distribution of Variables')

for count, p in enumerate(versicolorlist):
    ax[count].hist(p, bins = 15, edgecolor='black')
    ax[count].set(title=df.columns.values[count], xlabel = 'cm')

    fig.savefig('versicolorhist.jpg')

virginicalist = [virginicas_l, virginicas_w, virginicap_l, virginicap_w]

fig2, ax2d = plt.subplots(2,2, figsize= (8,6))

ax = np.ravel(ax2d)

fig.suptitle('Virginica Distribution of Variables')

for count, p in enumerate(virginicalist):
    ax[count].hist(p, bins = 15, edgecolor='black')
    ax[count].set(title=df.columns.values[count])
    if count >1:
        ax[count].set_xlabel = 'cm'

    fig.savefig('virginicahist.jpg')
