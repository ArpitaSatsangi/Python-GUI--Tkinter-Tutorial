#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *

def getvals():
    print(f"the value of username is {uservalue.get()}")
    print(f"the value of password is {passvalue.get()}")
    

root = Tk()
root.geometry("532x285")

user = Label(root, text = "username")
password = Label(root, text="password")

user.grid()
password.grid(row=2)


uservalue = StringVar();
passvalue = StringVar();

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=2, column=1)

Button(root,text="Submit" ,command=getvals).grid(row=3,column=1)

root.mainloop()


# In[ ]:




