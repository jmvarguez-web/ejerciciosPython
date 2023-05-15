#En este segundo ejercicio, tendréis que crear un archivo py y
# dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle


class Vehiculo:
    def __init__(self, marca, modelo, color, precio) -> None:
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.velocidad = 0
        self.encendido = False

    def getMarca(self):
        return self.marca
    def getModel(self):
        return self.modelo
    def getColor(self):
        return self.color
    def getPrecio(self):
        return self.precio

    def getVelocidad(self):
        return self.velocidad

    def getencendido(self):
        return self.encendido
    def encender(self):
        self.encendido = True
        print("El vehículo ha sido encendido.")

    def apagar(self):
        self.encendido = False
        self.velocidad = 0
        print("El vehículo ha sido apagado.")

    def acelerar(self, velocidad):
        if self.encendido:
            self.velocidad += velocidad
            print("El vehículo está acelerando a {} km/h.".format(self.velocidad))
        else:
            print("El vehículo está apagado.")

    def frenar(self, velocidad):
        if self.encendido:
            self.velocidad -= velocidad
            print("El vehículo está frenando a {} km/h.".format(self.velocidad))
        else:
            print("El vehículo está apagado.")

    def girar_izquierda(self):
        print("El vehículo está girando a la izquierda.")

    def girar_derecha(self):
        print("El vehículo está girando a la derecha.")

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print("El vehículo ahora es de color {}.".format(self.color))


class Serializador:
    def __init__(self, path) -> None:
        self.path = path

    def serializar(self, object) -> None:
        f = open(self.path, 'wb') #escibir erchivo en binario
        pickle.dump(object, f)
        f.close()

    def deserializar(self) -> object:
        f = open(self.path, 'rb') #leer erchivo binario
        object = pickle.load(f)
        f.close()
        return object


class Inicio:
    def main():
        serializador = Serializador('vehiculo.bin')
        auto = Vehiculo("Ford", "Mustang", "negro", 40000)
        auto.encender()
        auto.acelerar(60)
        auto.girar_derecha()
        auto.frenar(10)
        auto.cambiar_color("Rojo")

        print("El vehiculo creado es:\n")
        print(auto)

        serializador.serializar(auto)
        vehiculo = serializador.deserializar()

        print("\nVehiculo deserializado:\n")
        #print(type(vehiculo))
        print(vehiculo.marca)
        print(vehiculo.modelo)
        print(vehiculo.color)
        print(vehiculo.precio)
        print(vehiculo.velocidad)
        print(vehiculo.encendido)



if __name__ == '__main__':
    Inicio.main()