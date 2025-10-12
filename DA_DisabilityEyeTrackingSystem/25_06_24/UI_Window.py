from tkinter import *

def onClick1():
    print("clicked Option1")
   
def onClick2():
    print("clicked Option2") 
 
master = Tk()
Button(master, text='Option1',width=33, height=20, bg="azure", command=onClick1).grid(row=0, column=0)
Label(master, text='Neutral',width=33, height=20).grid(row=0, column=1)
Button(master, text='Option2',width=33, height=20, bg="beige", command=onClick2).grid(row=0, column=2)
mainloop()