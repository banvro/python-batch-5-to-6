import tkinter as tk

def myd():
    name = entr1.get()
    p_nu = entr2.get()
    print(name, p_nu)

root = tk.Tk()
root.geometry("400x400")
root.title("My Tkinter")
# root.configure(background = "green")

# lbel = tk.Label(text = "My Data", font = ('Roboto', 16, 'bold'), fg = 'red', bg = "pink")

# lbel.pack(fill = "x",padx = 30, ipadx=10, ipady = 10)

lab1 = tk.Label(root, text = "Enter Name  : ")
entr1 = tk.Entry(root)
lab2 = tk.Label(root, text = "Enter Email : ")
entr2 = tk.Entry(root)
btn = tk.Button(root, text = "Hit Me", command=myd)

lab1.grid(row=1, column=1, ipadx=20, ipady=20)
entr1.grid(row=1, column=2)

lab2.grid(row=2, column=1)
entr2.grid(row=2, column=2)

btn.grid(row=3, column=2, pady=10)




root.mainloop()
