import socket
import pickle
import time

def read_data(file_dir):
    file = open(file_dir, 'r')
    s = file.read()
    data = s.split('\n')

    return data

def run_client(host='127.0.0.1', port=7788):
    with socket.socket() as sock:
        sock.connect((host, port))

        i = 0
        while True:
            data = read_data('Sieve\\Sieve\\2d_int_int.txt')
            print(data)

            data = pickle.dumps(data[i])
            sock.send(data)

            time.sleep(1)

            if len(data) == i:
                break
            i += 1

if __name__ == '__main__':
    run_client()



