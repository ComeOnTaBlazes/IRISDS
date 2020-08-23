#print contents of file
import csv
import pandas as pd

#print the contents of the csv file (below working)
#with open('irisds.csv', newline ='') as csv_file:
 #   reader = csv.reader(csv_file, delimiter=',', quotechar='|')
 #   for row in reader:
 #       print(','.join(row))

#add each row to a dictionary 
#with open('irisds.csv', newline ='') as csv_file:
#    reader = csv.DictReader(csv_file)
#    for row in reader:
#        print(row['ï»¿sepal_length'], row['sepal_width'], row['petal_length'], row['petal_width'])

#using pandas to sum col2
df = pd.read_csv('irisds.csv')

#x= sum(df['sepal_width'])
#print(x)

#print(df)

#working average / push out for each column
#https://www.geeksforgeeks.org/python-pandas-dataframe-sum/
#https://www.youtube.com/watch?v=zmdjNSmRXF4
s_laverage = df['sepal_length'].mean(skipna = True)
print(s_laverage)

s_waverage = df['sepal_width'].mean(skipna = True)
print(s_laverage)

p_laverage = df['petal_length'].mean(skipna = True)
print(p_laverage)

p_waverage = df['petal_width'].mean(skipna = True)
print(p_waverage)

s_lmed = df['sepal_length'].median(skipna = True)
print(s_lmed)

df['sepal_length'].max(skipna = True)
df['sepal_length'].min(skipna = True)