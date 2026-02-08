from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from fit_line import my_linfit

plt.legend()
plt.axis([0,2,0,2])
plt.xlabel('height [m]')
plt.grid()
x=plt.ginput(10,show_clicks=TRUE,mouse_add=1,mouse_stop=3)
x_list = []
y_list = []
x_arr = np.array(x_list)
y_arr = np.array(y_list)

for value_pair in x:
    x_i,y_i=value_pair
    x_arr = np.append(x_arr,x_i)
    y_arr = np.append(y_arr,y_i)

plt.plot(x_arr, y_arr, 'kx')
plt.grid()
a,b = my_linfit(x_arr,y_arr)
plt.plot(x_arr,a * x_arr + b, 'r-')
plt.grid()

plt.show()
