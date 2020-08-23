#Import necessary modules
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import csv
import pandas as pd
import statistics


def average(x):
    ans = float(round(sum(x)/len(x),3))
    return ans

def stddev(x):
    sdev = float(round(statistics.stdev(x),3))
    return sdev



#Open csv as df
df= pd.read_csv('irisds.csv')


#Seperate df by species
filtsetosa_df= df[(df['species'] == 'setosa')]
filtversicolor_df = df[(df['species'] == 'versicolor')]
filtvirginica_df = df[(df['species'] == 'virginica')]

#Create lists of each column per species & add to dictionary
#Setosa
setosas_l = filtsetosa_df['sepal_length'].tolist()
setosas_w = filtsetosa_df['sepal_width'].tolist()
setosap_l = filtsetosa_df['petal_length'].tolist()
setosap_w = filtsetosa_df['petal_width'].tolist()
setosa = {'sepal length' : setosas_l, 'sepal width' : setosas_w, 'petal length': setosap_l, 'petal width': setosap_w}

setosares = []
for key in setosa:
    setosares.append(key)

setosares2 = []
for val in setosa.values():
    ans = average(val)
    setosares2.append(ans)

#merge setosares lists into dictionary
setosaresult = dict(zip(setosares, setosares2))

setosares2 = []
for val in setosa.values():
    sdev = stddev(val)
    setosares2.append(sdev)

setosasdev = dict(zip(setosares, setosares2))

#Versicolor
versicolors_l = filtversicolor_df['sepal_length'].tolist()
versicolors_w = filtversicolor_df['sepal_width'].tolist()
versicolorp_l = filtversicolor_df['petal_length'].tolist()
versicolorp_w = filtversicolor_df['petal_width'].tolist()
versicolor = {'sepal length' : versicolors_l , 'sepal width' : versicolors_w, 'petal length': versicolorp_l, 'petal width': versicolorp_w}

versicolorres = []
for key in versicolor:
    versicolorres.append(key)

versicolorres2 = []
for val in versicolor.values():
    ans = average(val)
    versicolorres2.append(ans)

#merge setosares lists into dictionary
versicolorresult = dict(zip(versicolorres, versicolorres2))

versicolorres2 = []
for val in versicolor.values():
    sdev = stddev(val)
    versicolorres2.append(sdev)

versicolorsdev = dict(zip(versicolorres, versicolorres2))

#Virginicadef average:
virginicas_l = filtvirginica_df['sepal_length'].tolist()
virginicas_w = filtvirginica_df['sepal_width'].tolist()
virginicap_l = filtvirginica_df['petal_length'].tolist()
virginicap_w = filtvirginica_df['petal_width'].tolist()
virginica = {'sepal length' : virginicas_l , 'sepal width' : virginicas_w, 'petal length': virginicap_l, 'petal width': virginicap_w}

virginicares = []

for key in virginica:
    virginicares.append(key)

virginicares2 = []
for val in virginica.values():
    ans = average(val)
    virginicares2.append(ans)

#merge setosares lists into dictionary
virginicaresult = dict(zip(virginicares, virginicares2))

virginicares2 = []
for val in virginica.values():
    sdev = stddev(val)
    virginicares2.append(sdev)

virginicasdev = dict(zip(virginicares, virginicares2))

print(versicolorresult)
print(setosaresult)
print(virginicaresult)

print(versicolorsdev)
print(setosasdev)
print(virginicasdev)