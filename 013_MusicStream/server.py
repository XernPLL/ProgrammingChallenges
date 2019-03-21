import socket
import sys
from threading import Thread
from queue import Queue





################# Connect part #############################
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
################################################

connectedlist = []
queue = Queue(2)

# Accept connections
class Accept(Thread):
    def run(self):
        while 1:
            conn, addr = server.accept()
            connectedlist.append(conn)
            print("Connected with " + addr[0] + ":" + str(addr[1]))

# Cut on pieces
class Cut(Thread):              ###TODO cutting
    def run(self):
        while True:
            name = input("Write name of song (from this directory) ")
            queue.put(SONG)


# Send pieces to connections
class Send(Thread):
    def run(self):
        while 1:
            bits = queue.get()
            if bits:
                for client in connectedlist:
                    if client != server:
                        try:
                            client.send(bits)
                        except:
                            client.close()
                            self.remove(client)

    def remove(self,conn):
        if conn in connectedlist:
            connectedlist.remove(conn)



Accept().start()
Cut().start()
Send().start()

