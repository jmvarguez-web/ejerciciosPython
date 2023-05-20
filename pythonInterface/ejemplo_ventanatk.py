
import tkinter
from tkinter import ttk
window=tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(0,weight=3)


label2=tkinter.Label(window,text="Otro Mas",bg="red",fg="yellow")
label2.place(x=25,y=0)



window.mainloop()