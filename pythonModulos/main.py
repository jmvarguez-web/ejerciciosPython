import operaciones
def main():
    print('En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: \nsumar, restar, multiplicar y dividir.Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.')
    print("\nIniciando main()\n"," a=10 b=15")
    a=10
    b=15
    print("La suma es :",operaciones.sumar(a,b))
    print("La resta es :",operaciones.restar(a,b))
    print("La multiplicacion es :",operaciones.multiplicar(a,b))
    print("La divicion es :",operaciones.dividir(a,b))


if __name__== '__main__':
    main()
