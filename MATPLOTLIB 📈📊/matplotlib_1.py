import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.array([1,2,3])
y = np.array([2,4,6])

plt.plot(x,y)

plt.title('Line Graph')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()