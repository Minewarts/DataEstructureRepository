def ReversaPalabra(palabra:str)->str:
    if len(palabra)==1:
        return palabra
    
    return palabra[-1]+ReversaPalabra(palabra[:-1])

word=str(input('Escriba una palabra: '))
print(f'el reverse de {word} es {ReversaPalabra(word)}')