'''def es_palindromo(palabra:str)->str:
    if len(palabra) == 1:
        return True
    
    if palabra[-1] == palabra[0]:
        #llamado Recursivo
        return es_palindromo(palabra[1:-1])
    else:
        #caso base
        return False
    
palabras='rotor'
palabras2='motor'

print(f'la palabra {palabras} es palindromo?{es_palindromo(palabras)}')
print(f'la palabra {palabras2} es palindromo?{es_palindromo(palabras2)}')'''


