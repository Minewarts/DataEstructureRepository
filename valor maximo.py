def ValorMaximo(lista:list[int], index:int = 0, maximo: int = None):
    if index == len(lista):
        return maximo

    if maximo is None or lista[index] > maximo:
        maximo = lista[index]

    return ValorMaximo(lista, index+1, maximo)

numeros = [3, 11, 2, 9, 5]
maximo = ValorMaximo(numeros)
print(f"El valor máximo en la lista es: {maximo}")

