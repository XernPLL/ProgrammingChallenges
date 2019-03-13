import socket
import keyboard
from threading import Thread

host = "chat.freenode.net" #server
port = 6667
nick = "xern"
user = "xern"
name = "Jan Kowalski"


ping = 'PING '.encode()
pong = 'PONG '.encode()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


client.send(('NICK ' + nick + '\r\n').encode())
client.send(('USER ' + user + ' 0 * :' + name + '\r\n').encode())

class Pinger(Thread):
  def run(self):
    while True:
      data = client.recv(1024)
      print(data)

      if data.startswith(ping):
        resp = data.strip(ping);
        client.send(pong + resp)
        print(pong + resp)

class Sender(Thread):
  def run(self):
    while True:
      if keyboard.is_pressed("s"):
        send = input("Wyslij komendę: ")
        client.send((send+ '\n').encode())

Pinger().start()
Sender().start()







