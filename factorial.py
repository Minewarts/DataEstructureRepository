def Factorial(numero:int)->int:
    if numero==0:
        return 1
    else:
        factorial=numero*Factorial(numero-1)
        return factorial
    

print(f'Escoja un numero')
numero=int(input())
print(f'el factorial de {numero} es:{Factorial(numero)}')
