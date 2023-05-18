#Crea un script que le pida al usuario una lista de países (separados por comas).
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
#paises = ["Estados Unidos", "Canadá", "México", "Brasil", "Argentina", "Francia", "España", "Italia", "Alemania", "China", "Japón", "India"]
#Estados Unidos, Canadá, México, Brasil, Argentina, Francia, España, Italia, Alemania, China, Japón, India,México
paises2 = ["Estados Unidos", "Canadá", "México", "México", "Brasil", "Argentina", "Francia", "España", "Italia", "Alemania", "China", "Japón", "India"]
def listapaises():

    lista_paises=[pais.strip() for pais in paises2]
    lista_paises = list(set(lista_paises))
    lista_paises.sort()
    return lista_paises

def pedir_paises():
    paises = input("Ingrese una lista de países (separados por comas): ")
    lista_paises = paises.split(",")
    lista_paises=[pais.strip() for pais in lista_paises]
    lista_paises = list(set(lista_paises))
    lista_paises.sort()
    return lista_paises
print("==================ordena lista forma 1=====================\n")
paises_ordenar = listapaises()
paises_string1 = ", ".join(paises_ordenar)
print("Lista de países ordenados alfabéticamente:")
print(paises_string1)

print("\n=======================================\n")
paises_ordenados= pedir_paises()
paises_string = ", ".join(paises_ordenados)
print("Lista de países ordenados alfabéticamente:")
print(paises_string)