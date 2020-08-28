from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import csv
import pandas as pd


#Open csv as df
df= pd.read_csv('irisds.csv')

f= open("analysis.txt","w+")

shape= df.shape

#Seperate df by species

alldata = df.describe().to_string()
setosadesc = df[(df['species'] == 'setosa')].describe().to_string()
versicolordesc = df[(df['species'] == 'versicolor')].describe().to_string()
virginicadesc = df[(df['species'] == 'virginica')].describe().to_string()

with open("analysis.txt", 'w+') as f:
    f.write("The dataset is comprised of {} columns of {} values in each column \n".format(shape[1], shape[0]))
    f.write("All Species \n")
    f.write(alldata)
    f.write("\n Setosa \n")
    f.write(setosadesc) 
    f.write("\n Versicolor \n") 
    f.write(versicolordesc)
    f.write("\n Virginica \n")
    f.write(virginicadesc)
    f.write("\n** Note the median is denoted as 50% in the above tables")

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


#Histogram
for item in toplvlist:
    fig, ax2d = plt.subplots(2,2, figsize= (10,8))
    ax = np.ravel(ax2d)
    fig.suptitle('Iris Flower Distribution of Variables')
    #if count == 0:
      #  fig.suptitle('Iris Flower Distribution of Variables')
    #else:
      #  fig.suptitle('{} Flower Distribution of Variables'.format(i for x,i in enumerate(toplvlist) if x = count):-4)
    for count, p in enumerate(item):
        ax[count].hist(p, bins = 15, edgecolor='black')
        ax[count].set(title=df.columns.values[count])
        if count > 1:
            ax[count].set(xlabel = 'cm')
        if count == 0 or 2:
            ax[count].set(ylabel = '# of occurrences')
        for count, q in enumerate(formattinglist):
            fig.savefig('{z}hist.jpg'.format(z = q))

#Scatter
fig, ax = plt.subplots(1,2, figsize = (10,8))
fig.suptitle('Iris Flower Scatterplot of Variable Pairs')
ax[0].scatter(setosas_l, setosas_w, color = 'r', label = 'Setosa')
ax[0].scatter(versicolors_l, versicolors_w, color = 'g', label = 'Versicolor')
ax[0].scatter(versicolors_l, versicolors_w, color = 'b', label = 'Versicolor')
ax[0].set(xlabel = 'Sepal Length cm')
ax[0].set(ylabel = 'Sepal Width cm')
ax[0].legend()
ax[1].scatter(setosap_l, setosap_w, color = 'r', label = 'Setosa')
ax[1].scatter(versicolorp_l, versicolorp_w, color = 'g', label = 'Versicolor')
ax[1].scatter(virginicap_l, virginicap_w, color = 'b', label = 'Virginica')
ax[1].set(xlabel = 'Petal Length cm')
ax[1].set(ylabel = 'Petal Width cm')
ax[1].legend()
fig.savefig('Scarrterplot.jpg')