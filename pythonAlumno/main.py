print("En este segundo ejercicio, tendréis','que crear un programa que tenga una clase llamada"+
" Alumno \nque tenga como atributos su nombre y su nota.\n"+
"Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje\n"+
"con el resultado de la nota y si ha aprobado o no.")
class Alumno:
    nombre = "none"
    nota = 0
    def __int__(self):
        self.nombre = "falta nombre"
        self.nota = 0
    def inicia (self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    def imprimirNota(self):
        print("Datos del Alumno:\n")
        print("Nombre",self.nombre)
        print("Nota:",self.nota)
    def validaNota(self):
        if self.nota < 6:
            print("Aprobado:\n")
        else:
            print("No Aprobado:\n")

#creamos objetos
alumno1=Alumno()
alumno2=Alumno()
alumno3=Alumno()

#iniciamosy pasamos valores
alumno1.inicia("Jesus",10)
alumno2.inicia("Manuel",5.9)

#imprimimos notas y resultado de validacion de nota

alumno1.imprimirNota();
alumno1.validaNota();
alumno2.imprimirNota();
alumno2.validaNota();
#como no se pasaron o se inicializaron valoresel contructor inicializa valores por defaul
alumno3.imprimirNota();
alumno3.validaNota();
