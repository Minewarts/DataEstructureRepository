'''def ReversaLista(lista:list)->list:
    if len(lista)==1:
        return lista
    
    return [lista[-1]]+ReversaLista(lista[:-1])

word=str(input('Escriba una palabra: '))
print(f'el reverse de {word} es {ReversaLista(word)}')'''

def ReversaLista(lista:list, index:int=0)->list:
    if index == len(lista):
        return ""
    
    return ReversaLista(lista,index+1)+[lista[index]]

word=str(input('Escriba una palabra: '))
print(f'el reverse de {word} es {ReversaLista(word)}')