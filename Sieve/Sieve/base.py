################ base.py (수정)

import sys
import numpy as np
import csv
import time
from socket import *
import pandas as pd
import pickle
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

HOST = '127.0.0.1'
PORT = 8080
INPUT_SCHEMA = 1

BUFSIZE = 1024
ADDR = (HOST, PORT)

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(ADDR)
serverSocket.listen(100)
print('listen : ', PORT)
clientSocket, addr_info = serverSocket.accept()
print('connected')

client_next = socket(AF_INET, SOCK_STREAM)

while True:
    data = clientSocket.recv(8080)  # Feeder 에서 데이터 받음
    if data != "":
        data = pickle.loads(data)  # Feeder에서 받은 데이터 계속 저장
        df = pd.DataFrame(data)
        fig = px.line(df,y=data)
        fig.write_html("Sieve.html")
        # 데이터 수신 근데 여기서 data는 1 row를 그대로 반환
        ## 데이터 처리부분 여긴 볼필요없음
        #print("1")
        try:
            send = pickle.dumps(fig)
            client_next.sendall(send)
        except:
            client_next.close()

