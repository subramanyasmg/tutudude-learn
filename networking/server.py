import socket
from tkinter import *

def send(listbox, entry):
    message = entry.get()
    listbox.insert(END, "Server: " + message)
    entry.delete(0, END)
    conn.send(bytes(message, "utf8"))

def receive(listbox):
    try:
        message_from_client = conn.recv(1024)
        if message_from_client:
            listbox.insert(END, "Client: " + message_from_client.decode("utf8"))
    except:
        listbox.insert(END, "Error receiving message")

root = Tk()
root.title('Server')
root.geometry("300x300")
root.resizable(width=0, height=0)
root.wm_attributes("-topmost", True)
root.wm_attributes("-topmost", False)

entry = Entry(root)
entry.pack(side=BOTTOM)
listbox = Listbox(root)
listbox.pack(side=LEFT)

button = Button(root, text="Send", command=lambda: send(listbox, entry))
button.pack(side=BOTTOM)

rbutton = Button(root, text="Receive", command=lambda: receive(listbox))
rbutton.pack(side=BOTTOM)

# Server socket setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 8080

s.bind((HOST_NAME, PORT))
s.listen(1)

listbox.insert(END, "Waiting for connection...")
root.update()

conn, addr = s.accept()
listbox.insert(END, f"Connected to {addr}")

root.mainloop()

# conn.close()
# s.close()