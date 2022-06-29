import socket
import threading
#from server import *
format="utf-8"
PORT=2020
IP=socket.gethostbyname(socket.gethostname())
ADDRESS=(IP,PORT)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDRESS)

name=input("Enter your name: ")

def listen():
    while True:
        try:
            message=client.recv(1024).decode(format)
            if message=='NAME':
                client.send(f"{name}".encode(format))
                continue
            print("\n"+ message)
        except:
            continue
        
thread=threading.Thread(target=listen)
thread.start()

while True:
    message=input()
    if message=='close':
       client.send(f"{message}".encode(format))
       break
    client.send(f"{name} : {message}".encode(format))
    
client.close()