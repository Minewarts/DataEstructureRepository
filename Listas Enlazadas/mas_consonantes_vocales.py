def ContarVocalesConsonantes(palabra:str):

    vocales_list=("aeiou")

    def auxContarVocalesConsonantes(palabra:str,vocales_list, index:int=0, vocales:int=0, consonantes:int=0):
        if index ==len(palabra):
            if vocales == consonantes:
                return "Cantidad igual de vocales y consonantes"
            elif vocales > consonantes:
                return "Hay mas vocales que consonantes"
            else:            
                return "Hay mas consonantes que vocales"
            
        vocales_list=("aeiou")

        if palabra[index].lower().isalpha():
            if palabra[index].lower() in vocales_list:
                return auxContarVocalesConsonantes(palabra,vocales_list, index+1, vocales+1, consonantes)
            else:
                return auxContarVocalesConsonantes(palabra,vocales_list, index+1, vocales, consonantes+1)
            
        else:
            return "Caracter no válido, solo se permiten letras"
        
    return auxContarVocalesConsonantes(palabra,vocales_list)
        



palabra=input("Ingrese una palabra: ")
resultado=ContarVocalesConsonantes(palabra)
print(resultado)
