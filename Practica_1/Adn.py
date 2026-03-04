
class SecuenciaADN:
    def __init__(self, id:int, nombre:str, secuencia:str, riesgo:int):

        self._id=id
        self.nombre=nombre
        self.secuencia=secuencia
        self.riesgo=riesgo

    def contar_patron(self, patron:str) -> int:
        len_patron:int=len(patron)
        def contar_patron_recursivo(secuencia:str=self.secuencia) -> int:
            if len(secuencia)<len_patron:
                return 0
            if secuencia[:len_patron]==patron:
                return 1 + contar_patron_recursivo(secuencia[1:])
            return contar_patron_recursivo(secuencia[1:])
        return contar_patron_recursivo()

    def generar_subcadenas(self):
        def generar_subcadenas_recursivo(secuencia:str=self.secuencia, length=1, subcadenas:list[str]=[])-> list[str]:
            if not secuencia:
                return[]
            if length>len(secuencia):
                return generar_subcadenas_recursivo(secuencia[1:], 1, subcadenas)
            
            subcadena_actual=secuencia[:length]
            if subcadena_actual not in subcadenas:
                def agregar_subcadena(lista:list[str]=subcadenas):
                    if not lista:
                        return [subcadena_actual]
                    return [lista[0]] + agregar_subcadena(lista[1:])
                subcadenas = agregar_subcadena(subcadenas)
            return [subcadena_actual] + generar_subcadenas_recursivo(secuencia, length+1, subcadenas)
            
        return generar_subcadenas_recursivo()

    def cantidad_nucleotidos_a_t(self) -> int:
        def cantidad_nucleotidos_recursivo(secuencia:str=self.secuencia) -> int:
            if not secuencia:
                return 0
            if secuencia[0]=='A':
                return 1 + cantidad_nucleotidos_recursivo(secuencia[1:])
            elif secuencia[0]=='T':
                return 1 + cantidad_nucleotidos_recursivo(secuencia[1:])
            else:
                return cantidad_nucleotidos_recursivo(secuencia[1:])
            
        return cantidad_nucleotidos_recursivo()
    
class AlmacenamientoSecuenciaADN:
    def __init__(self):
        self.secuencias:list[SecuenciaADN] = []

        def id_existe(self, id_buscado, acc=0):
            if acc == len(self.secuencias):
                return False
            if self.secuencias[acc]._id == id_buscado:
                return True
            return self.id_existe(id_buscado, acc+1)
    
    def registrar_muestra(self, nueva_muestra):
        if self.id_existe(nueva_muestra._id):
            print("Secuencia ya en uso")
        else:
            self.secuencias.append(nueva_muestra)

    def contar_patron(self, patron:str, id:int) -> int:
        secuencia=self.obtener_secuencia_por_id(id)
        return secuencia.contar_patron(patron)

    def obtener_secuencia_por_id(self, id:int) -> SecuenciaADN:
        def obtener_secuencia_por_id_recursivo(secuencias:list[SecuenciaADN]=self.secuencias, index1:int=0,index2:int=len(self.secuencias)-1) -> SecuenciaADN:
            if index1>index2:
                raise ValueError(f'No se encontró una secuencia con el ID {id}.')
            mid=(index1+index2)//2
            if secuencias[mid]._id==id:
                return secuencias[mid]
            elif secuencias[mid]._id>id:
                return obtener_secuencia_por_id_recursivo(secuencias,index1,mid-1)
            else:
                return obtener_secuencia_por_id_recursivo(secuencias,mid+1,index2)
        return obtener_secuencia_por_id_recursivo()

    def riesgo_promedio(self) -> float:
        if not self.secuencias:
            return 0.0
        def riesgo_promedio_recursivo(secuencias:list[SecuenciaADN]=self.secuencias, suma:int=0) -> float:
            suma+=secuencias[0].riesgo
            if len(secuencias)==1:
                return suma/len(self.secuencias)
            return riesgo_promedio_recursivo(secuencias[1:], suma)
        return riesgo_promedio_recursivo()
    
    def secuencia_mas_larga(self) -> SecuenciaADN:
        if not self.secuencias:
            return None
        def secuencia_mas_larga_recursivo(secuencias:list[SecuenciaADN]=self.secuencias, secuencia_mas_larga:SecuenciaADN=self.secuencias[0]) -> SecuenciaADN:
            if len(secuencias)==1:
                return secuencia_mas_larga
            if len(secuencias[0].secuencia)>len(secuencia_mas_larga.secuencia):
                return secuencia_mas_larga_recursivo(secuencias[1:], secuencias[0])
            return secuencia_mas_larga_recursivo(secuencias[1:], secuencia_mas_larga)
        return secuencia_mas_larga_recursivo()
    
    def generar_secuencia(self, id:int)-> str:
        secuencia=self.obtener_secuencia_por_id(id)
        def generar_secuencia_recursivo(secuencia:str=secuencia.secuencia, secuencia_generada:str='') -> str:
            if not secuencia:
                return secuencia_generada
            if secuencia[0]== 'A':
                return generar_secuencia_recursivo(secuencia[1:], secuencia_generada + 'T')
            elif secuencia[0]== 'T':
                return generar_secuencia_recursivo(secuencia[1:], secuencia_generada + 'A')
            else: 
                return generar_secuencia_recursivo(secuencia[1:], secuencia_generada + secuencia[0])
        return generar_secuencia_recursivo()
    

    

SecuenciaADN1=SecuenciaADN(1,"Secuencia1","AGCTAGCTAG",5)
SecuenciaADN2=SecuenciaADN(2,"Secuencia2","AGCTAGCTAG",3)
SecuenciaADN3=SecuenciaADN(3,"Secuencia3","AGCTAGCTAG",1)
SecuenciaADN4=SecuenciaADN(4,"Secuencia4","AGCTAGCTAG",2)


almacenamiento=AlmacenamientoSecuenciaADN()
almacenamiento.registrar_muestra(SecuenciaADN1)
almacenamiento.registrar_muestra(SecuenciaADN2)
almacenamiento.registrar_muestra(SecuenciaADN3)
almacenamiento.registrar_muestra(SecuenciaADN4)

print(SecuenciaADN1.generar_subcadenas())
