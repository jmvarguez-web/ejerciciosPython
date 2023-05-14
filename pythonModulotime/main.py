from jornadaLaboral import JornadaLaboral
import time
import datetime


def main():


    horaentrada = datetime.time(9, 14, 0)  # 9 horas mañana
    horasalida=datetime.time(19, 0, 0) #19 horas 7 de la nuche salida
    while True:
        hora = datetime.datetime.now()# generamos hora actual
        horaactual = datetime.time(hora.hour, hora.minute, hora.second)
        jornadaLaboral = JornadaLaboral(horaactual,horaentrada,horasalida)
        esLaboral = jornadaLaboral.esHorarioLaboral()
        calculoTiemporespuesta=jornadaLaboral.tiempoFinTrabajo()
        if  esLaboral == 0:
            print(calculoTiemporespuesta)
        if  esLaboral == 1:
            print(calculoTiemporespuesta)
            break
        if esLaboral == -1:
            print(calculoTiemporespuesta)
            break
        time.sleep(1*60) #repite cada minuto
        #time.sleep(1 * 3600) # repite cada hora





if __name__ == "__main__":
    main()

