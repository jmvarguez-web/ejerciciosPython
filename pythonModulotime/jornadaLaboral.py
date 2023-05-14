from time import localtime, time, mktime
import datetime
class JornadaLaboral:
    def __init__(self, hora_actual, hora_entrada, hora_fin):
        self.hora_actual = hora_actual
        self.hora_entrada = hora_entrada
        self.hora_fin = hora_fin
        self.esHorasalir = 0

    def esHorarioLaboral(self):
        """
        retorna 0 si esta en hora laboral, si la hora actual es mayor que la hora fin (Salida) se termina horario laboral(1)
        si la hora actual es menor o igual a la hora de entrada -1
        """
        self.esHorasalir = 0
        if self.hora_actual <= self.hora_entrada:
            self.esHorasalir = -1
        if self.hora_actual > self.hora_fin:
            self.esHorasalir = 1
        return self.esHorasalir

    def tiempoFinTrabajo(self):
        """
        Devuelve mensaje con el tiempo faltante parar entrar , parar salir o despues de su jornada laboral
        """
        tiemp_diferencia=0
        result = localtime()
        mensaje=""
        tiempo = datetime.datetime(result.tm_year, result.tm_mon, result.tm_mday, self.hora_entrada.hour,self.hora_entrada.minute, self.hora_entrada.second)
        tiempo1=datetime.datetime(result.tm_year, result.tm_mon,result.tm_mday, self.hora_fin.hour, self.hora_fin.minute, self.hora_fin.second)
        tiempo2 = datetime.datetime(result.tm_year, result.tm_mon, result.tm_mday, result.tm_hour,result.tm_min, result.tm_sec)
        #calculo diferencia

        if self.esHorasalir==0: #calculo el tiempo faltante para salir si esta en jonada laboral
            tiemp_diferencia = tiempo1 - tiempo2
            # calculando tiempo
            horas = int(tiemp_diferencia.total_seconds() // 3600)
            minutos = int((tiemp_diferencia.total_seconds() % 3600) // 60)
            mensaje="Tiempo faltante para salir: {} hora, {} minutos".format(horas, minutos)
        if self.esHorasalir==-1: #calculo el tiempos despues de su hora de salida
            tiemp_diferencia = tiempo - tiempo2
            # calculando tiempo
            horas = int(tiemp_diferencia.total_seconds() // 3600)
            minutos = int((tiemp_diferencia.total_seconds() % 3600) // 60)
            mensaje="Tiempo faltante para entrar: {} hora, {} minutos".format(horas, minutos)
        if self.esHorasalir==1:
            tiemp_diferencia = tiempo2 - tiempo1
            # calculando tiempo
            horas = int(tiemp_diferencia.total_seconds() // 3600)
            minutos = int((tiemp_diferencia.total_seconds() % 3600) // 60)
            mensaje="Tiempo despues de tu jornada es la hora de ir a casa: {} hora, {} minutos".format(horas, minutos)

        return mensaje