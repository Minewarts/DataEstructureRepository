'''def ReversaPalabra(palabra:str)->str:
    if len(palabra)==1:
        return palabra
    
    return palabra[-1]+ReversaPalabra(palabra[:-1])

word=str(input('Escriba una palabra: '))
print(f'el reverse de {word} es {ReversaPalabra(word)}')'''

'''def ReversaPalabra(palabra:str, index:int=0)->str:
    if index == len(palabra):
        return ""
    
    return ReversaPalabra(palabra,index+1)+palabra[index]

word=str(input('Escriba una palabra: '))
print(f'el reverse de {word} es {ReversaPalabra(word)}')'''

'''def ReversaPalabra(palabra:str, index:int=0,palabra_reversa:str='')->str:
    if index == len(palabra):
        return palabra_reversa
    
    print('palabra reversa : ',palabra_reversa)
    print('palabra indice:',palabra[index])
    
    return ReversaPalabra(palabra,index+1,palabra[index]+palabra_reversa)

word=str(input('Escriba una palabra: '))
print(f'el reverse de {word} es {ReversaPalabra(word)}')'''