# file_server.py
import socket

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Server is listening...")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        filename = conn.recv(1024).decode()
        try:
            with open(filename, 'rb') as f:
                data = f.read()
                conn.sendall(data)
        except FileNotFoundError:
            conn.send(b"ERROR: File not found")