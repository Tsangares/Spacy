#!/usr/bin/env python3
import sys
import socket
import pyautogui as gui
import pynput.keyboard as keyboard
from time import sleep
from random import randint
from multiprocessing import Process, Queue
from time import sleep,time,strftime,localtime
def timestamp():
    style="%a %I:%M:%S %p"
    return strftime(style,localtime(time()))

class Client:
    def __init__(self,HOST,PORT):
        self.index=Queue()
        self.HOST=HOST
        self.PORT=PORT
        
    def run(self):
        print(f"[{timestamp()}] Connecting to server at {HOST}:{PORT}")
        l=Process(target=self.listener)
        s=keyboard.Listener(on_press=self.on_press)
        l.start()
        s.start()
        try:
            s.join()
            l.join()
        except:
            print("closing")
            l.terminate()
        
    def listener(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST,self.PORT))
            s.sendall(bytes('listening','ascii'))
            current_index = int(str(s.recv(1024), 'ascii'))
            while int(self.index.qsize()) < current_index:
                self.index.put('space')
                print(f'[{timestamp()}] Spacial positions is {int(self.index.qsize())}')
            while True:
                response = int(str(s.recv(1024), 'ascii'))
                if response > int(self.index.qsize()):
                    self.index.put('space')
                    print(f"[{timestamp()}] Recieved insteruction to hit space")
                    gui.press('space')
                elif response == int(self.index.qsize()):
                    print(f"[{timestamp()}] Sucessfully emitted a space request")
                else:
                    print(f"[{timestamp()}] You have fallen behind by {response-int(self.index.qsize())} steps! HOLY FUCK!")

    def send_space(self):
        self.index.put('space')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST,self.PORT))
            print(f"[{timestamp()}] Broadcasting a space request")
            s.sendall(bytes(f'space','ascii'))

    def on_press(self,key):
        if key == keyboard.Key.space:
            self.send_space()
        
if __name__=='__main__':
    HOST,PORT='localhost',6699
    if len(sys.argv)>1:
        HOST=sys.argv[1]
        if len(HOST.split(':'))==2:
               HOST,PORT=HOST.split(':')
    if len(sys.argv)==3:
        PORT=sys.argv[2]
    client=Client(HOST,PORT)
    client.run()
