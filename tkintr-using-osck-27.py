# tkinter : GUI 

import tkinter as tk

def showdata():
    xyz = entr.get()
    
    print(xyz)

root = tk.Tk()

root.title("My Tkinter")

width = 400
hight = 300

# root.geometry(f"{width}x{hight}")
root.geometry("400x300")

lable = tk.Label(root, text = "My first tkinter app")
lable.pack()

entr = tk.Entry(root)
entr.pack()

butn = tk.Button(root, text = "submit", command = showdata)
butn.pack()

root.mainloop()
