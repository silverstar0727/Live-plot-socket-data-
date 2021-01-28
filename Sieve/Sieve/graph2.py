import numpy as np
import pandas as pd
import seaborn as sns
import csv
import datetime as dt
from itertools import count
import time
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import plotly.express as px
import plotly_express as px2
df = pd.read_csv('2d_int_int.csv')
fig = px2.line(df,y='Column2')
fig.write_html("Sieve.html")
time.sleep(.5)
