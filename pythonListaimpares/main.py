#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos
# impares de una lista pasada por parámetro con filter y realizará una suma de todos
# estos elementos obtenidos mediante reduce. python
from functools import reduce


def impares(x):
    if x % 2 !=0:
        return True
    return False
def sumaimpar(a,b):
    print(f'a={a} + b={b} ')
    return a+b

Lista_numeros=[1,2,3,4,5,6,7,8,9,10,11,12]
sonimpares= list(filter(impares,Lista_numeros))

print("los impares son ",sonimpares)
sumaes = reduce(sumaimpar,sonimpares)
print("La suma de los impares es:",sumaes)

print("==================================")
sonimparesLamda=list(filter(lambda x:x%2!=0,Lista_numeros))
print("los impares(lamda) son ",sonimparesLamda)
sumalamda = reduce(lambda x, y: x + y ,sonimparesLamda)
print("La suma de los impares es:",sumalamda)