#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#Color
#Ruedas
#Puertas
#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
#Velocidad
#Cilindrada
#Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.*/

class Vehículo:
    _color ="rojo"
    _ruedas=4
    _puertas=4
class Coche(Vehículo):
    Velocidad =120
    Cilindrada=2


ver=Coche()
ver._color
ver._ruedas
ver._puertas
ver.Velocidad
ver.Cilindrada
print(dir(ver))
print("\nEl coche es de color ",ver._color,",tiene ",ver._ruedas," ruedas ,",ver._puertas," ruedas\n y su velocidad es de ",ver.Velocidad,"y Cilindrada de ",ver.Cilindrada)


