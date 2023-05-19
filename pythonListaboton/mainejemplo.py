#En este ejercicio tenéis que crear una lista de RadioButton
# que muestre la opción que se ha seleccionado y que contenga un botón
# de reinicio para que deje todo como al principio.
#Al principio no tiene que haber una opción seleccionada.

import tkinter

def mostrar_seleccion():
    seleccion = seleccionado.get()
    label_seleccion.config(text="Selección: "+seleccion)

def mostrar_seleccionbutton():
    seleccion = seleccionado.get()
    label_seleccion.config(text="Selección boton: "+seleccion)

def reinicia_seleccion():
    seleccionado.set(None)
    label_seleccion.config(text="Selección: ")

ventana = tkinter.Tk()
ventana.title("Lista de RadioButton")
ventana.columnconfigure( 0, weight=1)
ventana.columnconfigure( 0, weight=5)

opciones_radio = ["Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5"]
i=0
seleccionado=tkinter.StringVar()
for  radioes in opciones_radio:
    r1 = tkinter.Radiobutton(ventana, text=radioes, value=radioes, variable=seleccionado, command=mostrar_seleccion)
    r1.grid(column=0, row=i, pady=5, padx=5 )
    i+=1
    r1.select()
    #print(radioes)

# mostrar la selección
label_seleccion = tkinter.Label(ventana, text="Selección: ")
label_seleccion.grid(column=2,row=3, sticky=tkinter.W,padx=5,pady=5)

# mostrar la selección
boton_mostrar = tkinter.Button(ventana, text="Mostrar", command=mostrar_seleccionbutton)
boton_mostrar.grid(column=4,row=0, sticky=tkinter.W,padx=5,pady=5)

# reiniciar la selección
boton_reiniciar = tkinter.Button(ventana, text="Reiniciar", command=reinicia_seleccion)
boton_reiniciar.grid(column=4,row=1, sticky=tkinter.W,padx=5,pady=5)



ventana.mainloop()
