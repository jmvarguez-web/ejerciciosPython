#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
#lo abráis y escribáis dentro del archivo.
#Para ello, tendréis que acceder dos veces al archivo creado.
import os


def main():
    nombreArchivo="Archivo.txt"
    textoArchivo='algunos ejemplos de texto narrativo. Ejemplo de texto narrativo: Lo dejo suelto,\n' \
                 ' y se va al prado, y acaricia tibiamente con su hocico, rozándolas apenas,\n ' \
                 'las florecillas rosas, celestes y gualdas\n'

    textoAgregar='Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.\n ' \
                 'Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impreso\n'
    if os.path.isfile(nombreArchivo):
        print("El archivo ",nombreArchivo," existe. Se escribira al final de la linea el siguente texto\n",textoAgregar)
        agregatextofinal(nombreArchivo,textoAgregar)


    else:
        print("El archivo ",nombreArchivo," no existe. Se creara y se escribira la siguiente linea\n",textoArchivo)
        crearArchivo(nombreArchivo,textoArchivo)

    print("Leer contenido de archivo ",nombreArchivo,".......\n")
    leerArchivo(nombreArchivo)

def crearArchivo(nombrearchivo,texto):
    f=open(nombrearchivo,'wt')
    f.write(texto)
    f.close()
def agregatextofinal(nombrearchivo,texto):
    f = open(nombrearchivo, 'at')
    f.write(texto)
    f.close()

def agregatextoLista(nombrearchivo,lista):
    f = open(nombrearchivo, 'at')
    f.write(lista)
    f.close()
def leerArchivo(nombrearchivo):
    f = open(nombrearchivo, 'r')
    datos=None
    while datos != '':
        datos=f.read()
        print(datos)
    f.close()


if __name__ == '__main__':
    main()