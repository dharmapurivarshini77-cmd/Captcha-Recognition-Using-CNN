# file_client.py
import socket

HOST = '127.0.0.1'
PORT = 8080

filename = 'example.txt'  # File to request

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(filename.encode())

    data = b''
    while True:
        packet = s.recv(1024)
        if not packet:
            break
        data += packet

    if data.startswith(b"ERROR"):
        print(data.decode())
    else:
        with open("received_" + filename, "wb") as f:
            f.write(data)
        print("File received successfully")