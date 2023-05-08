print('Se dice que un año es bisiesto si: \nes divisible entre 4 \ny (no es divisible entre 100 o sí es divisible entre 400).')

def esBiciesto(anio: int):
    if anio % 4==0 and (anio %4 != 0 or anio %400==0):
     return True
    else: return False

anioes    = input("\nDame el año:XXXX:")
resultado = esBiciesto(int(anioes))
if resultado==True:
        print("\nEl año:",anioes," Es bisiesto")
else:
        print("\nEl año:",anioes," No es bisiesto")