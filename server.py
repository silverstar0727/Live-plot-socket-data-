import socket
import pickle
import pandas as pd
import time
import matplotlib.pyplot as plt

def graph_setting():
    plt.ion()
    fig, ax = plt.subplots()
    fig.canvas.set_window_title('넘 힘들어.')
    ax.set_title("I'm so tired")

    return ax

def data_get(df, conn, i):
    data = conn.recv(1024)
    data = float(pickle.loads(data))
    print(data)

    df_temp = pd.DataFrame([[data]], columns=['data'])
    df = pd.concat([df, df_temp], axis=0)
    df = df.reset_index(drop = True)
    print(df)

    return df

def run_server(host='127.0.0.1', port=7788):
    ax = graph_setting()

    with socket.socket() as sock:
        sock.bind((host, port))
        sock.listen()
        conn, addr = sock.accept()

        df = pd.DataFrame(columns=['data'])
        i = 0
        while True:
            df = data_get(df, conn, i)

            ax.plot(df)
            plt.show()
            plt.pause(0.01)

            i += 1

if __name__ == '__main__':
    run_server()
