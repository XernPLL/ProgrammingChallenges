import socket
import sys
import select
from threading import Thread
import time
host = "192.168.43.40"
port = 8081

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # init socket

except socket.error:
    print("Failed do connect")
    sys.exit()

print("Socket Created")


server.connect((host, port))

print("Socket Connected to " + host)

class Typing(Thread):
    def run(self):
        while True:
            input()
            message = input("<You>: ")
            server.send(message.encode())
            time.sleep(1)

class Getting(Thread):
    def run(self):
        while 1:
            sockets_list = [server]

            read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

            for socks in read_sockets:
                if socks == server:
                    message = socks.recv(2048)
                    print(message)


Typing().start()
Getting().start()
