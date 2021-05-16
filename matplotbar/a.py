import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

plt.style.use('fivethirtyeight')
a = np.array([[4,8,5,7,6],[2,3,4,2,6],[4,7,4,7,8],[2,6,4,8,6],[2,4,3,3,2]])
df1 = pd.DataFrame(a, columns=['a','b','c','d','e'], index=[2,4,6,8,10])

df1.plot(kind='bar')

# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

plt.show()