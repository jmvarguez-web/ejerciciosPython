import sys
import tkinter
from tkinter import ttk
window=tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(0,weight=3)

seleccionado=tkinter.StringVar()
seleccionado2=tkinter.StringVar()
r1=ttk.Radiobutton(window,text="Si", value="1", variable=seleccionado)
r2=ttk.Radiobutton(window,text="Ni", value="1", variable=seleccionado)
r1.grid(column=0,row=1,pady=5,padx=5)
r2.grid(column=0,row=2,pady=5,padx=5)

checkbox=ttk.Checkbutton(window,text="Acepta condicion", variable=seleccionado2)
checkbox.grid(column=0,row=3)


#frame=ttk.Frame(window)
#label=ttk.Label(frame,text="hola")
#list=["win","Mac","win","Mac","win","Mac","win","Mac"]
#lista_items=tkinter.StringVar(value=list)
#lisbox=tkinter.Listbox(window,height=100,listvariable=lista_items)
#lisbox.grid(column=0,row=0,sticky=tkinter.W)


window.mainloop()
sys.exit(0)


username_label=ttk.Label(window,text="Username:")
username_label.grid(column=0,row=0, sticky=tkinter.W,padx=5,pady=5)
username_label=ttk.Label(window,text="Password:")
username_label.grid(column=0,row=1, sticky=tkinter.W,padx=5,pady=5)

username_entry=ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E,padx=5,ipady=5)

password_entry=ttk.Entry(window,show='*')
password_entry.grid(column=1, row=1, sticky=tkinter.E,padx=5,ipady=5)

login_button=ttk.Button(window)
login_button.grid(column=1,row=3,sticky=tkinter.E,padx=5,pady=5)


window.mainloop()