import socket
import sys
from threading import Thread

host ='192.168.43.40'
port = 8081

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

try:
    server.bind((host,port))

except socket.error:
    print("Binding failed")
    sys.exit()

print("Socket has been bounded")

server.listen(10)

print("Socket is ready")

connectedlist = []

class Clientthread(Thread):
    def __init__(self, conn, addr):

        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
    def run(self):
        welcomemessage = "Welcome to the server. Press Enter to write"
        self.conn.send(welcomemessage.encode())

        while 1:
            try:
                data=self.conn.recv(2048)
                data = data.decode()
                if data:
                    print("<"+addr[0]+">"+data)

                    datatosend = "<"+addr[0]+">"+data
                    self.broadcast(datatosend,self.conn)

                else:
                    self.remove(self.conn)
            except:
                conn.close()
                break


    def broadcast(self, data, conn):
        for client in connectedlist:
            if client != conn:
                try:
                    client.send(data.encode())
                except:
                    client.close()
                    self.remove(client)

    def remove(self,conn):
        if conn in connectedlist:
            connectedlist.remove(conn)




while 1:
    conn, addr = server.accept()
    connectedlist.append(conn)
    print("Connected with " + addr[0] + ":" + str(addr[1]))
    client = Clientthread(conn, addr)
    client.start()


conn.close()
server.close()