#!/usr/bin/env python3
import socketserver
from queue import Queue
from time import sleep
from time import sleep,time,strftime,localtime
def timestamp():
    style="%a %I:%M:%S %p"
    return strftime(style,localtime(time()))


q=Queue()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class broadcastHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        if 'space' in data:
            print(f"[{timestamp()}] Recieved a space from {self.client_address[0]}")
            q.put(data)
        else:
            self.index=q.qsize()
            print(f"[{timestamp()}] New connection from {self.client_address[0]} at index: {self.index}")
            self.request.sendall(bytes(f'{self.index}','ascii'))
            while True:
                if q.qsize() > self.index:
                    self.index+=1
                    print(f"[{timestamp()}] Sending a space to {self.client_address[0]}; index {self.index}")
                    self.request.sendall(bytes(str(self.index),'ascii'))
                sleep(.5)
        
def run():
    HOST,PORT='',6699
    with ThreadedTCPServer((HOST,PORT),broadcastHandler) as server:
        print(f"[{timestamp()}] Server started at {HOST}:{PORT}")
        server.serve_forever()
        
if __name__=='__main__':
    run()
