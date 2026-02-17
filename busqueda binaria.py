def busqueda_binaria(lista:list,obj:int, i_low:int=-1, i_high:int=-1 ):
    if i_low==-1 and i_high==-1:
        i_low=0
        i_high=len(lista)-1


    print("i_low : ",i_low)
    print('i_hig : ',i_high)
    i_mid= (i_low + i_high)//2
    print('i_mid : ',i_mid)

    if lista[i_mid]==obj:
        return "el numero se encuentra en la posicion: ",i_mid
    
    if i_low>i_high:
        return "el numero no se encuentra en la lista"
    
    if obj<lista[i_mid]:
        #busqueda en la primera mitad
        print("obj<lista[i_mid]")
        return busqueda_binaria(lista,obj,i_low,i_mid-1)
    elif obj>lista[i_mid]:
        #busqueda en la segunda mitad
        print("obj>lista[i_mid]")
        return busqueda_binaria(lista,obj,i_mid+1,i_high)
    
lista=[1,2,3,4,5,6,7,8,9,10]
busqueda1=3
busqueda2=11
busqueda3=7
print(f'busqueda del numero {busqueda1} : {busqueda_binaria(lista,busqueda1)}')
print(f'busqueda del numero {busqueda2} : {busqueda_binaria(lista,busqueda2)}')
print(f'busqueda del numero {busqueda3} : {busqueda_binaria(lista,busqueda3)}')