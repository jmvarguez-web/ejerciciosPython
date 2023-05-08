print('El range() genera una secuencia de números que van desde 0 por defecto '
      'hasta el número que se pasa como parámetro menos 1. \n En realidad, se '
      'pueden pasar hasta tres parámetros separados por coma, donde el primer '
      'es el inicio de la secuencia,\n el segundo el final y el tercero el salto '
      'que se desea entre números. Por defecto se empieza en 0 y el salto es de 1.\n')
print(" EJEMPLO:\n#range(inicio, fin, salto)")

for valor in range(100,0,-1):
      print("Valor actual",valor)

