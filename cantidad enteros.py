def COntarMultiplos(numero:int, contador:int=0):
    if numero==0:
        return contador
    
    digito= numero%10

    if digito%2==0 and digito%4 == 0 and digito!=0:
        return COntarMultiplos(numero//10, contador+1)
    else: return COntarMultiplos(numero//10, contador)


numero= 123324500

print(f'el numero {numero} tiene {COntarMultiplos(numero)} digitos multiplos de 4 y de 2')