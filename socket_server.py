import socket
import json
from datetime import datetime

HOST = 'localhost'
PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        while True:
            data, addr = s.recvfrom(1024)
            message = json.loads(data.decode())
            save_to_json(message)

def save_to_json(data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    with open('storage/data.json', 'a') as file:
        json.dump({timestamp: data}, file)
        file.write('\n')

if __name__ == '__main__':
    main()