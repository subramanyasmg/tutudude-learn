import socket
from tkinter import *

def send(listbox, entry):
    message = entry.get()
    listbox.insert(END, message)
    entry.delete(0, END)
    s.send(bytes(message, "utf8"))
    receive(listbox)

def receive(listbox):
    message_from_server = s.recv(1024)
    listbox.insert(END, "Server:" + message_from_server.decode("utf8"))

root = Tk()
root.title('Client')
root.geometry("300x300")
root.resizable(width=0, height=0)
root.wm_attributes("-topmost", True)
root.wm_attributes("-topmost", False)

entry = Entry(root)
entry.pack(side=BOTTOM)
listbox = Listbox(root)
listbox.pack(side=LEFT)

buton = Button(root, text="Send", command=lambda: send(listbox, entry))
buton.pack(side=BOTTOM)

rbutton = Button(root, text="Receive", command=lambda: receive(listbox))
rbutton.pack(side=BOTTOM)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 8080
s.connect((HOST_NAME, PORT))

root.mainloop()