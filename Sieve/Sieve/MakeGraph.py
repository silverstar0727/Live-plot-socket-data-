import numpy as np
from matplotlib.animation import FuncAnimation
import seaborn as sns
import csv
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import *
import time

fig = plt.figure()

x = []
y = []

plt.ion()

figure, ax = plt.subplots(figsize=(8,6))
line, = ax.plot(x, y)
while True :
  with open("2d_int_int.txt",'r') as csvfile:
    plots = csv.reader(csvfile, delimiter='\t')
    for row in plots:
      updated_x = x.append(int(row[0]))
      updated_y = y.append(int(row[1]))
      line.set_data(updated_x, updated_y)

      figure.canvas.draw()
      figure.canvas.flush_events()

      plt.plot(x,y)
      figure.show()
      time.sleep(.5)
