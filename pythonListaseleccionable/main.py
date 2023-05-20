#En este segundo ejercicio, tendréis que crear una interfaz
# sencilla la cual debe de contener una lista de elementos seleccionables,
# también debe de tener un label con el texto que queráis.

import tkinter

def mostrar_seleccion():
    seleccion = seleccionado.get()
    label_seleccion.config(text="Selección: "+seleccion)
def inserta_listaradio():
    seleccion = seleccionado.get()
    label_seleccion.config(text="Insertar valor de radio a lista: "+seleccion)
    listbox.insert(tkinter.END, seleccion)
def mostrar_seleccionbutton():
    seleccion = seleccionado.get()
    label_seleccion.config(text="Selección boton: "+seleccion)
def mostrar_seleccionlista():

    seleccion =  listbox.curselection()#items_lista.get()
    if seleccion:
        index_selecion=seleccion[0]
        valor_seleccion=listbox.get(index_selecion)
        labelseleccionlista.config(text="Selección de la lista: " + valor_seleccion)
        print(valor_seleccion)
    else:
        label_seleccion.config(text="Selección de la lista: Ninguna ")
def elimina_valor_seleccionado():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
def reinicia_seleccion():
    seleccionado.set(None)
    #listbox.delete(0, tkinter.END)
    label_seleccion.config(text="Selección: ")

ventana = tkinter.Tk()
ventana.title("Lista de RadioButton")



# Configura el contenido de la ventana aquí

ventana.columnconfigure( 0, weight=1)
ventana.columnconfigure( 0, weight=1,minsize=100)



opciones_radio = ["Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5"]

opciones_lista = ["Lista 1", "Lista 2", "Lista 3", "Lista 4", "Lista 5"]
i=0
seleccionado=tkinter.StringVar()
for  radioes in opciones_radio:
    r1 = tkinter.Radiobutton(ventana, text=radioes, value=radioes, variable=seleccionado, command=mostrar_seleccion)
    r1.grid(column=0, row=i, pady=5, padx=5 ,sticky=tkinter.W)
    i+=1
    r1.select()
    #print(radioes)

items_lista = tkinter.StringVar(value=opciones_lista)
listbox=tkinter.Listbox(ventana,height=10,listvariable=items_lista)
listbox.grid(column=0,row=10,sticky=tkinter.W)

# mostrar la selección
label_seleccion = tkinter.Label(ventana, text="Selección: ")
label_seleccion.grid(column=0,row=5,padx=5,pady=5,sticky=tkinter.W)

# mostrar la selección Lista
labelseleccionlista = tkinter.Label(ventana, text="Lista Selección: ")
labelseleccionlista.grid(column=0,row=11, sticky=tkinter.N)


# mostrar la selección
boton_mostrar = tkinter.Button(ventana, text="Mostrar", width=20, height=2, command=mostrar_seleccionbutton)
boton_mostrar.grid(column=1,row=0, sticky=tkinter.W,padx=5,pady=5)

# reiniciar la selección
boton_reiniciar = tkinter.Button(ventana, text="Reiniciar", width=20, height=2, command=reinicia_seleccion)
boton_reiniciar.grid(column=1,row=1, sticky=tkinter.W,padx=5,pady=5)

boton_mostrarlista = tkinter.Button(ventana, text="Mostrar Valor Lista", width=20, height=2, command=mostrar_seleccionlista)
boton_mostrarlista.grid(column=1,row=2, sticky=tkinter.W,padx=5,pady=5)

boton_insertalista = tkinter.Button(ventana, text="Inserta valor radio a lista", width=20, height=2, command=inserta_listaradio)
boton_insertalista.grid(column=1,row=3, sticky=tkinter.W,padx=5,pady=5)

boton_insertalista = tkinter.Button(ventana, text="Elimina de la lista", width=20, height=2, command=elimina_valor_seleccionado)
boton_insertalista.grid(column=1,row=5, sticky=tkinter.W,padx=5,pady=5)

ventana.mainloop()
