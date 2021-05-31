import csv 
import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
count = []
dice_result = []
for i in range (0,100):
    dice1 = random.randint (1,6)
    dice2 = random.randint (1,6)
    dice_result.append(dice1+dice2)
    count.append(i)
df = pd.read_csv("data.csv")
df1 = df ["Avg Rating"].tolist()
fig = ff.create_distplot([df1],["Avg Rating"],show_hist=False)
fig.show()