"""
Hacer una función recursiva en Python que 
cuente las vocales minúsculas de un texto. 
"""

def contvoc(tex, x=0):
    if x == len(tex):
        return 0
    else:
        return (1 if tex[x] in "AeioU" else 0) + contvoc(tex, x+1) 


res = input("Ingrese palabra a contar vocales minusculas")
print(contvoc(res)) #1