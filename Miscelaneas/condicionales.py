# El ejercicio 1 consta de un codigo que haga un bucle del 1 al 10 y haga la suma de todos los numeros pares y por
# aparte la suma de todos los numeros impares 


inicio=0
fin=0
lista=(inicio,fin)
def sumaPares(inicio,fin):
    sumPares=0
    for a in range(inicio,fin+1):
        if a%2==0:
            print(a)
            sumPares+=a
    print(f'la suma de los numeros pares es: {sumPares}')
def sumaImpares(inicio,fin):
    sumImpares=0
    for a in range(inicio,fin+1):
        if a%2==1:
            print(a)
            sumImpares+=a
    print(f'la suma de los numeros impares es: {sumImpares}')
sumaPares(1,10)
sumaImpares(1,10)