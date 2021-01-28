import numpy as np
import seaborn as sns
import csv
import datetime as dt
import matplotlib.pyplot as plt
from random import *
import time
from socket import *
import pandas as pd
import pickle
import sys
import plotly_express as px
import plotly.graph_objects as go
import plotly.io as pio

HOST_NEXT = '127.0.0.1'
PORT_NEXT = 8080
INTERVAL = 0.5

next_client = socket(AF_INET, SOCK_STREAM)
next_client.connect((HOST_NEXT, PORT_NEXT))

file = open('2d_int_int.txt', 'r')
s = file.read()
data = s.split('\n')

#df = pd.read_csv('2d_int_int.csv')
#pio.renderers.default = "browser"
i = 0

while True :
    if i == len(data) :
        i = 0
    row = data[i].split('\n')
    #fig = go.Figure([go.Scatter(y=df['Column1'])])
    fig = px.line(data)


    try :
        send_data = pickle.dumps(row)
        next_client.sendall(send_data)

    except :
        next_client.close()

    i = i+1




