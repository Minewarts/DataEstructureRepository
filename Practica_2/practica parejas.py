#Practica 2 en parejas
#Sanet Correa Castaño y Alberto Escobar Taborda

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from Iniciadores import Vehiculo, Via, Queue


def moto_prioridad(avenida):
    current = avenida.head
    while current is not None:
        next_node = current.next

        if current.tipo.lower() == "moto" and current.prioridad == 1 and current != avenida.head:
            # eliminar current de la posición actual
            if current.prev is not None:
                current.prev.next = current.next
            if current.next is not None:
                current.next.prev = current.prev
            else:
                avenida.tail = current.prev

            # insertar en la cabeza
            current.prev = None
            current.next = avenida.head
            if avenida.head is not None:
                avenida.head.prev = current
            avenida.head = current

        current = next_node


def eliminar_camiones(avenida):
    actual = avenida.head
    while actual is not None:
        siguiente = actual.next
        if actual.tipo.lower() == "camion" and actual.prioridad > 3:
            if actual.prev is not None:
                actual.prev.next = actual.next
            else:
                avenida.head = actual.next
            if actual.next is not None:
                actual.next.prev = actual.prev
            else:
                avenida.tail = actual.prev
        actual = siguiente

def simular_accidente(avenida, placa1, placa2):
    nodo1 = None
    nodo2 = None
    actual = avenida.head
    while actual is not None:
        if actual.placa == placa1:
            nodo1 = actual
        if actual.placa == placa2:
            nodo2 = actual
        actual = actual.next
    
    if nodo1 is None or nodo2 is None:
        return
        
    inicio = None
    fin = None
    actual = avenida.head
    while actual is not None:
        if actual == nodo1 or actual == nodo2:
            if inicio is None:
                inicio = actual
            else:
                fin = actual
                break
        actual = actual.next
    
    if inicio == fin or inicio.next == fin:
        return
        
    inicio.next = fin
    fin.prev = inicio

def invertir_via(avenida):
    autos = 0
    motos = 0
    actual = avenida.head
    while actual is not None:
        if actual.tipo.lower() == "auto":
            autos += 1
        elif actual.tipo.lower() == "moto":
            motos += 1
        actual = actual.next
        
    if autos > motos:
        actual = avenida.head
        avenida.tail = avenida.head
        prev = None
        while actual is not None:
            temp = actual.next
            actual.next = actual.prev
            actual.prev = temp
            prev = actual
            actual = temp
        avenida.head = prev

def reorganizar_prioridad(avenida):
    for p in range(5, 0, -1):
        actual = avenida.head
        while actual is not None:
            siguiente = actual.next
            if actual.prioridad == p and actual != avenida.head:
                # quitar actual de su lugar
                if actual.prev is not None:
                    actual.prev.next = actual.next
                if actual.next is not None:
                    actual.next.prev = actual.prev
                else:
                    avenida.tail = actual.prev

                # llevar a cabeza
                actual.prev = None
                actual.next = avenida.head
                if avenida.head is not None:
                    avenida.head.prev = actual
                avenida.head = actual

            actual = siguiente

def simular_semaforo(avenida, cola_semaforo, cola_revision):
    actual = avenida.head
    cont = 0
    while actual is not None and cont < 6:
        cola_semaforo.encolar(actual)
        actual = actual.next
        cont += 1
    
    tiempo = 0
    pasaron = 0
    ultimo_tipo = None
    consecutivos = 0
    
    while pasaron < 6 and not cola_semaforo.esta_vacia():
        v = cola_semaforo.desencolar()
        
        if v.tipo.lower() == "camion" and v.prioridad > 3 and not v.revisado:
            v.revisado = True
            cola_revision.encolar(v)
            print(f"T:{tiempo} | {v.placa} | enviado a revision")
            
            if cola_revision.tamano() == 3:
                while not cola_revision.esta_vacia():
                    revisado = cola_revision.desencolar()
                    cola_semaforo.encolar(revisado)
            continue

        if v.tipo.lower() == ultimo_tipo:
            if consecutivos == 2:
                bloqueado = True
                actual_cola = cola_semaforo.head
                while actual_cola is not None:
                    if actual_cola.dato.tipo.lower() != v.tipo.lower():
                        bloqueado = False
                        break
                    actual_cola = actual_cola.next
                
                if not bloqueado:
                    cola_semaforo.encolar(v)
                    print(f"T:{tiempo} | {v.placa} | pospuesto")
                    continue

        if v.tipo.lower() == ultimo_tipo:
            consecutivos += 1
        else:
            ultimo_tipo = v.tipo.lower()
            consecutivos = 1
            
        print(f"T:{tiempo} | {v.placa} | paso")
        
        temp = avenida.head
        while temp is not None:
            if temp.placa == v.placa:
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    avenida.head = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                else:
                    avenida.tail = temp.prev
                break
            temp = temp.next
            
        pasaron += 1
        if not (v.tipo.lower() == "moto" and v.prioridad == 1):
            tiempo += 30



avenida = Via()

v1 = Vehiculo("AAA111", "auto", 3)
v2 = Vehiculo("BBB222", "moto", 1)
v3 = Vehiculo("CCC333", "camion", 5)
v4 = Vehiculo("DDD444", "moto", 1)
v5 = Vehiculo("EEE555", "auto", 2)
v6 = Vehiculo("FFF666", "camion", 4)
v7 = Vehiculo("GGG777", "auto", 1)

for veh in (v1, v2, v3, v4, v5, v6, v7):
    avenida.append(veh)

print("\nClase Inicial: ")
print(avenida)

print("\n2. Aplicando moto_prioridad :")
moto_prioridad(avenida)
print(avenida)

print("\n3. Eliminando Camiones:")
eliminar_camiones(avenida)
print(avenida)

print("\n4. Simulacion accidente entre 'BBB222' y 'EEE555':")
simular_accidente(avenida, "BBB222", "EEE555")
print(avenida)
print("\n5. Reorganizar prioridad:")
reorganizar_prioridad(avenida)
print(avenida)

print("\n6. Invertir via:")
invertir_via(avenida)
print(avenida)

print("\n7. Simulacion de semafoto:")
c_semaforo = Queue()
c_revision = Queue()
simular_semaforo(avenida, c_semaforo, c_revision)

print("\nAvenida Final:")
print(avenida)
