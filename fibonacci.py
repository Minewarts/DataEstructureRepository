'''def fibonacci(numero:int)->int:
    if numero <=0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero-1)+fibonacci(numero-2)
    
numero = int(input('Escriba un numero: '))

print(f'el numero {numero} de la serie de fibonacci es {fibonacci(numero)}')'''


'''def fibonacci(numero:int)->int:
    if numero<=1:
        return (numero,0)
    else:
        (a,b)=fibonacci(numero-1)
        return (a+b,a)
    

numero = int(input('Escriba un numero: '))
print(f'el numero {numero} de la serie de fibonacci es {fibonacci(numero)[0]}')'''

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(numero:int)->int:
    if numero<=0:
        return numero
    elif numero == 1:
        return numero
    else:
        return fibonacci(numero-1)+fibonacci(numero-2)
    
numero = int(input('Escriba un numero: '))
print(f'el numero {numero} de la serie de fibonacci es {fibonacci(numero)}')