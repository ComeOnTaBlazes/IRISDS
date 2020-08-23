#Averages of the overall DS for each variable
import pandas as pd
import numpy as np

df= pd.read_csv('irisds.csv')

#working average / push out for each column
#https://www.geeksforgeeks.org/python-pandas-dataframe-sum/
#https://www.youtube.com/watch?v=zmdjNSmRXF4
#https://www.youtube.com/watch?v=9Os0o3wzS_I&

def avg(x):
    ans = float(round(df[x].mean(skipna = True),2))
    return ans

print(avg('sepal_length'))

#Average sepal_length
s_laverage = float(round(df['sepal_length'].mean(skipna = True),2))
print(s_laverage)

#Average sepal_width
s_waverage = float(round(df['sepal_width'].mean(skipna = True),2))
print(s_waverage)

#Average petal_length
p_laverage = float(round(df['petal_length'].mean(skipna = True),2))
print(p_laverage)

#Average petal_width
p_waverage = float(round(df['petal_width'].mean(skipna = True),2))
print(p_waverage)

#Filtering the dataframe for each 3 species
#https://www.youtube.com/watch?v=Lw2rlcxScZY&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=4
filtsetosa = (df['species'] == 'setosa')
filtversicolor = (df['species'] == 'versicolor')
filtvirginica = (df['species'] == 'virginica')
df[filtsetosa]

#using .loc
filtsetosas_l = df.loc[filtsetosa, 'sepal_length']

#avg filtsetosas_l
float(round(filtsetosas_l.mean(skipna = True),2))

#Standard Deviation of filtsetosas_l
#https://numpy.org/doc/stable/reference/generated/numpy.std.html
np.std(filtsetosas_l)