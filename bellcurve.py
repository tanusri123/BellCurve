import random
import plotly.figure_factory as ff
import pandas as pd
import statistics as st

dice_result=[]
count=[]
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)

std_dev = st.stdev(dice_result)
mean = sum(dice_result)/len(dice_result)
mode = st.mode(dice_result)
median = st.median(dice_result)
print('Median:' + str(median))
print('Mode:' + str(mode))
print('Mean:' + str(mean))

fig = ff.create_distplot([dice_result],['Result'],show_hist=False)
fig.show()