"""
Hacer una funcion recursiva que pedira una 
lista y un numero N y retornara la suma de los 
N ultimos numeros
[2,4,6,3] y N = 2  -> Resultado = 6+3=9
"""

def sumault(lst, n):
    return sumault2(lst, -n)

def sumault2(lst, m):
    if m==0:
        return 0
    else:
        return lst[m] + sumault2(lst, m+1)
    

lista = [2,4,6,3] 
num = 2
print(sumault(lista,3)) #9