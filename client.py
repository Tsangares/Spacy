import socket
import pyautogui as gui
import pynput.keyboard as keyboard
from time import sleep
from random import randint
from multiprocessing import Process, Queue
from timestamp import timestamp
index=Queue()
def listener():
    HOST,PORT='localhost',6699
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        s.sendall(bytes('listening','ascii'))
        current_index = int(str(s.recv(1024), 'ascii'))
        while index.qsize() < current_index:
            index.put('space')
        print(f'[{timestamp()}] Spacial positions is {index.qsize()} at ')
        while True:
            response = int(str(s.recv(1024), 'ascii'))
            if response > index.qsize():
                index.put('space')
                print(f"[{timestamp()}] Recieved instruction to hit space")
            elif response == index.qsize():
                print(f"[{timestamp()}] Sucessfully emitted a space request")
            else:
                print(f"[{timestamp()}] You have fallen behind by {response-index.qsize()} steps! HOLY FUCK!")

def send_space():
    HOST,PORT='localhost',6699    
    index.put('space')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        print(f"[{timestamp()}] Broadcasting a space request")
        s.sendall(bytes(f'space','ascii'))

def on_press(key):
    if key == keyboard.Key.space:
        send_space()
        
if __name__=='__main__':
    l=Process(target=listener)
    s=keyboard.Listener(on_press=on_press)
    l.start()
    s.start()
    try:
        s.join()
        l.join()
    except:
        print("closing")
        l.terminate()
