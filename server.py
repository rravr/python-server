import socket
import threading

PORT = 4848
HEADER = 90
SERVER = socket.gethostbyname(socket.gethostname())
DECODE= 'utf-8'
ADDRESS = (SERVER, PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDRESS)

def handle(conn, addr):
    print(f"+ Connection + {addr} connected ")
    connection = True
    while connection:
        msg_length = conn.recv(HEADER).decode(DECODE)
        msg_length = int(msg_length)
        message = conn.recv(msg_length).decode(DECODE)
        print (f"{addr} {message}")
        






def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target= handle, args=(conn, addr))
        thread.start()
        print(f"+Active Clients {threading.activeCount() -1 }")


print ("server started...")
start()
