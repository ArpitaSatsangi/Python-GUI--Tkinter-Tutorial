#!/usr/bin/env python
# coding: utf-8

# In[24]:


from tkinter import *

root=Tk()
root.geometry("355x155")

def hello():
    print("Hello tkinter Buttons")

frame=Frame(root,bg="blue",borderwidth=8, relief=SUNKEN)
frame.pack(side = LEFT, anchor="nw")

b1=Button(frame, bg="red",text="Click here", command=hello)
b1.pack(side=LEFT, padx=23)

b2=Button(frame, bg="yellow" , text="Click here")
b2.pack(side=LEFT, padx=23)


root.mainloop()


# In[ ]:




