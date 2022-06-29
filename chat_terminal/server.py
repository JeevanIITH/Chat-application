import socket
import select
import threading



PORT= 2020
IP=socket.gethostbyname(socket.gethostname())
ADDRESS=(IP,PORT)
format="utf-8"

clients,names =[],[]


server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(ADDRESS)

def startChat():
    print("server is working on " + IP)

    server.listen()

    while True:

        client,addr =server.accept()
        client.send("NAME".encode(format))

        name= client.recv(1024).decode(format)

        names.append(name)
        clients.append(client)

        print(f"Name is : {name}")
        broadcastMessage(f"{name} has joined the chat !".encode(format),client)
        client.send('connection successful!'.encode(format))
        thread=threading.Thread(target=handle,args=(client,addr))
        thread.start()

        print(f"active connections {threading.active_count()-1}")



def broadcastMessage(message,client_t):
    for client in clients:
        if client!=client_t:
           client.send(message)


def handle(client,addr):

    print(f"new connection {addr}")
    connected = True
    while connected:
        message = client.recv(1024).decode(format)
        if message=='close':
            
            print(f"closing connection with {names[clients.index(client)]} ")
            names.remove(names[clients.index(client)])
            clients.remove(client)
            break
        broadcastMessage(message.encode(format),client)
    client.close()

startChat()