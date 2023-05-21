#En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:
# la columna id de tipo entero, la columna nombre que será de tipo texto
# y la columna apellido que también será de tipo texto.

#Una vez creada la tabla, tenéis que insertarle datos,
# como mínimo tenéis que insertar 8 alumnos a la tabla.
#Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
class basedatos:
    def datostabla():
        # Conectarse a la base de datos (o crearla si no existe)
        conexion = sqlite3.connect('base_datos.db')

        # Crear un cursor para ejecutar las consultas
        cursor = conexion.cursor()
        # Realizar una búsqueda de un alumno por nombre
        #nombre_buscado = 'Pedro'
        cursor.execute('SELECT * FROM Alumnos ')
        alumno_encontrado = list(cursor)
        #print(alumno_encontrado)
        pass

        # Mostrar los datos del alumno por consola
        if alumno_encontrado:
            print('Datos encontrados.')
        else:
            print('No se encontró ningún alumno con ese nombre.')

        # Cerrar la conexión con la base de datos
        conexion.close()
        return list(alumno_encontrado)
    def Busqueda(nombre):
        # Conectarse a la base de datos (o crearla si no existe)
        conexion = sqlite3.connect('base_datos.db')

        # Crear un cursor para ejecutar las consultas
        cursor = conexion.cursor()
        nombre_buscado = nombre
        cursor.execute('SELECT * FROM Alumnos WHERE nombre = ?', (nombre_buscado,))

        alumno_encontrado = list(cursor)
        print(alumno_encontrado)
        # Mostrar los datos del alumno por consola
        if alumno_encontrado:
            print('Datos encontrados.')
        else:
            print('No se encontró ningún alumno con ese nombre.')

        # Cerrar la conexión con la base de datos
        conexion.close()
        return list(alumno_encontrado)

    def insertaAlumno(alumnos):
        alumnosreg=alumnos
        # Conectarse a la base de datos (o crearla si no existe)
        conexion = sqlite3.connect('base_datos.db')

        # Crear un cursor para ejecutar las consultas
        cursor = conexion.cursor()

        # Insertar datos en la tabla

        cursor.executemany('INSERT INTO Alumnos (nombre,apellido) VALUES ( ?, ?)', alumnosreg)

        # Guardar los cambios en la base de datos
        conexion.commit()
        conexion.close()


class Inicio:

    def ventana():
        def insertaAlumno():
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()

            if nombre and apellido:
                messagebox.showinfo("Registro Exitoso", "¡Registro completado!")
                alumnos = [
                    (nombre, apellido),
                ]
                basedatos.insertaAlumno(alumnos)
                entry_nombre.delete(0, tk.END)
                entry_apellido.delete(0, tk.END)
                tabla.delete(*tabla.get_children())
                datosactualizados = basedatos.datostabla()
                for i, datosactualizados in enumerate(datosactualizados, start=1):
                    tabla.insert(parent="", index="end", iid=i, text=str(i), values=datosactualizados)
            else:
                messagebox.showwarning("Campos Vacíos", "Por favor, completa todos los campos.")
        def buscaAlumno():
            busqueda = entry_buscar.get()
            if busqueda :

                entry_nombre.delete(0, tk.END)
                entry_buscar.delete(0, tk.END)
                entry_buscar.delete(0, tk.END)
                tabla.delete(*tabla.get_children())
                resultadobusqueda = basedatos.Busqueda(busqueda)
                for i, resultadobusqueda in enumerate(resultadobusqueda, start=1):
                    tabla.insert(parent="", index="end", iid=i, text=str(i), values=resultadobusqueda)
            else:
                messagebox.showwarning("Campos Vacíos", "Por favor, completa el campo de busqueda.")
                tabla.delete(*tabla.get_children())
                datostabla = basedatos.datostabla()
                for i, datostabla in enumerate(datostabla, start=1):
                    tabla.insert(parent="", index="end", iid=i, text=str(i), values=datostabla)


        ventana = tk.Tk()
        ventana.title("Alumnos")
        fuente = font.Font(size=14)

        # Configura el contenido de la ventana aquí

        ventana.columnconfigure(0, weight=1)
        ventana.columnconfigure(1, weight=2)
        ventana.columnconfigure(2, weight=3)

        label_nombre = tk.Label(ventana, text="Nombre:")
        label_nombre.grid(column=0,row=1,sticky=tk.W,padx=10,pady=5)
        entry_nombre = tk.Entry(ventana, width=30,font=fuente)
        entry_nombre.grid(column=0,row=2,sticky=tk.W,padx=10,pady=5)

        label_apellido = tk.Label(ventana, text="Apellido:")
        label_apellido.grid(column=0, row=3,sticky=tk.W,padx=10,pady=5)

        entry_apellido = tk.Entry(ventana, width=30,font=fuente)
        entry_apellido.grid(column=0, row=4, sticky=tk.W,padx=10,pady=5)

        boton_mostrar = tk.Button(ventana, text="Registrar", width=20, height=2,command=insertaAlumno )
        boton_mostrar.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)

        entry_buscar = tk.Entry(ventana, width=30,font=fuente,)
        entry_buscar.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)

        label_busqueda = tk.Label(ventana, text="Buscar por nombre:")
        label_busqueda.grid(column=0, row=7, sticky=tk.W, padx=10, pady=0)

        boton_mostrar = tk.Button(ventana, text="BUSCAR ALUMNO", width=20, height=2, command=buscaAlumno)
        boton_mostrar.grid(column=0, row=8, sticky=tk.E, padx=5, pady=5)

        # Crear el árbol de la tabla
        tabla = ttk.Treeview(ventana, columns=("Clave","Nombre", "Apellido"))

        datos = basedatos.datostabla()
        #print(registros)


        # Definir encabezados de columnas

        tabla.heading("Clave", text="clave")
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Apellido", text="Apellido")

        # Insertar los datos en la tabla
        for i, dato in enumerate(datos, start=1):
            tabla.insert(parent="", index="end", iid=i, text=str(i), values=dato)

        # Ajustar el ancho de las columnas automáticamente

        tabla.column("Clave", width=200)
        tabla.column("Nombre", width=200)
        tabla.column("Apellido", width=200)

        tabla.grid(column=0, row=9, sticky=tk.W, padx=5, pady=5)


        ventana.mainloop()


if __name__ == '__main__':
    #basedatos.datostabla()
    Inicio.ventana()