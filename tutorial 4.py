#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *

root = Tk()


# In[2]:


root.geometry("934x234")

root.title("GUI - BLACK HOLE")


# In[3]:


# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE



title_label = Label(text = '''A black hole is a region of spacetime where gravity is so strong that nothing, 
\nincluding light or other electromagnetic waves, has enough energy to escape it.
\nThe theory of general relativity predicts that a sufficiently compact mass can deform spacetime to form a black hole.
\nThe boundary of no escape is called the event horizon. 
\nAlthough it has a great effect on the fate and circumstances of an object crossing it, 
\nit has no locally detectable features according to general relativity.''',
                    
                   bg= "red", fg="blue", font= "comicsansms 10 bold",
                    padx= 23, pady=19,borderwidth=23, relief=SUNKEN
                    
                   )


# In[4]:


# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady





#title_label.pack(anchor= 'sw') #default is side=TOP

#title_label.pack(side= BOTTOM, anchor= 'sw', padx=13, pady=8)
title_label.pack(side=LEFT, fill=Y, padx=13, pady=8)


# In[5]:


root.mainloop()


# In[ ]:




