import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('slr02.xls')

cricket_chirps = df['X']
temp = df['Y']

colors = (0,0,0)
area = np.pi*3

# Plot
plt.scatter(cricket_chirps, temp, s=area, c=colors, alpha=0.5)
plt.title('Scatter')
plt.xlabel('Cricket Chirps')
plt.ylabel('Temp')

# Compute best fit line
sum_x = sum(cricket_chirps)
mean_x = sum_x / len(cricket_chirps)

sum_y = sum(temp)
mean_y = sum_y / len(temp)

sum_x_squared = 0
for x in cricket_chirps:
    sum_x_squared += (x - mean_x)**2

sum_x_y = 0
for ind in df.index: 
     sum_x_y += (df['X'][ind] - mean_x) * (df['Y'][ind] - mean_y)

slope = sum_x_y / sum_x_squared
intercept = mean_y - (slope * mean_x)

print("best fit line: y = " + str(slope) + "x + " + str(intercept) )

x = np.linspace(min(cricket_chirps),max(cricket_chirps), 500)
y = slope * x + intercept

plt.plot(x, y, '-r')

plt.show()