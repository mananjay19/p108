import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv('data1.csv')
avglist = df['Avg Rating'].tolist()
fig = ff.create_distplot([avglist],['average rating'])
fig.show()