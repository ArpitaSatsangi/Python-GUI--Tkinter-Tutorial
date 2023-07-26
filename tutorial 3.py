#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *

root=Tk()

root.geometry("755x475")

myphoto = PhotoImage(file="flowers.png")

label = Label(image=myphoto)

label.pack()

root.mainloop()


# In[4]:


from tkinter import *
from PIL import Image, ImageTk

root=Tk()

root.geometry("855x575")

#for jpg images
photo = Image.open("peace.jpg")

myphoto = ImageTk.PhotoImage(photo)

label = Label(image=myphoto)

label.pack()

root.mainloop()


# In[ ]:




