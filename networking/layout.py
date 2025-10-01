from tkinter import *

root = Tk()
root.geometry("300x300")
root.resizable(width=0, height=0)
root.wm_attributes("-topmost", True)
root.wm_attributes("-topmost", False)

entry = Entry(root)
entry.pack(side=BOTTOM)
listbox = Listbox(root)
listbox.pack(side=LEFT)


buton = Button(root, text="Send", command=root.destroy)
buton.pack(side=BOTTOM)
root.mainloop()
