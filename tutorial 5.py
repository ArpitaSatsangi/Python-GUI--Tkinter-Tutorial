from tkinter import *

root = Tk()

root.geometry("655x333")

f1 = Frame(root, bg = "pink", borderwidth=8, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, bg="pink", borderwidth=9, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f1, text = "FRAME TEXT EXAMPLE", font = "Helvetica 16 bold", fg="purple")
l.pack(pady = 123)

l = Label(f2, text="HEADING", font = "Helvetica 14 bold", fg="purple")
l.pack()

root.mainloop()
