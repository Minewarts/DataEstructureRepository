def ContarDigitos(numero:int)->int:
    assert isinstance (numero,int) and numero>=0, 'Error! el numero debe de ser entero positivo' 
    if numero==0:
        return 0
    
    return 1 + ContarDigitos(numero//10)


numero=int(input('ingrese un numero: '))

print(f'el numero de digitos de {numero} es: {ContarDigitos(numero)}')