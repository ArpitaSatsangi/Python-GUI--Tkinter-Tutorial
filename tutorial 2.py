#!/usr/bin/env python
# coding: utf-8

# In[16]:


from tkinter import *

root = Tk()

root.geometry("845x453") #WidthxHeight

root.minsize(250, 120)

root.maxsize(1000, 567)


text_label = Label(text="Hello, this is a GUI with text.")
text_label.pack()


root.mainloop()


# In[ ]:




