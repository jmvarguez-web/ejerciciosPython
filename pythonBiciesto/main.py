print('Se dice que un año es bisiesto si: \nes divisible entre 4 \ny (no es divisible entre 100 o sí es divisible entre 400).')

def esBiciesto(anio: int):
    if anio % 4==0 and (anio %4 != 0 or anio %400==0):
     return True
    else: return False


resultado = esBiciesto(2000)

print(resultado)