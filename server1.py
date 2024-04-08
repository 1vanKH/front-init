import socket
import urllib.parse
import json
from datetime import datetime

UDP_IP = '127.0.0.1'
UDP_PORT = 5000


def run_server(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    sock.bind(server)
    try:
        while True:
            data, address = sock.recvfrom(2048)
            print(f'Received data: {data.decode()} from: {address}')
            data_parse = urllib.parse.unquote_plus(data.decode())
            print(data_parse)
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            data_dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
            data_entry = {current_time: data_dict}
            with open('storage/data.json', 'a') as file:
                json.dump(data_entry, file, indent=2)
                file.write('\n')
            sock.sendto(data, address)
            print(f'Send data: {data.decode()} to: {address}')

    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        sock.close()


if __name__ == '__main__':
    run_server(UDP_IP, UDP_PORT)
