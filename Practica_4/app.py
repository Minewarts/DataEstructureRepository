from iniciadores import BinaryTreeNode, insert_node_bst, delete_node_bst, reverse_in_order

class Medicamento:
    def __init__(self, id_med, nombre, stock, año_vencimiento, precio):
        self.id = id_med
        self.nombre = nombre
        self.stock = stock
        self.año_vencimiento = año_vencimiento
        self.precio = precio


# Variables Globales de Estado
contador_alertas = 0
valor_total_inventario = 0.0
total_operaciones_fusion = 0

# --- FUNCIONES DE BÚSQUEDA ---
def find_node_by_id(root, target_id):
    if root is None:
        return None
    if root.data.id == target_id:
        return root
    elif target_id < root.data.id:
        return find_node_by_id(root.leftchild, target_id)
    else:
        return find_node_by_id(root.rightchild, target_id)

def find_successor(root, target_id):
    succ = None
    curr = root
    while curr is not None:
        if target_id < curr.data.id:
            succ = curr
            curr = curr.leftchild
        elif target_id > curr.data.id:
            curr = curr.rightchild
        else:
            if curr.rightchild is not None:
                temp = curr.rightchild
                while temp.leftchild is not None:
                    temp = temp.leftchild
                return temp
            break
    return succ

def find_predecessor(root, target_id):
    pred = None
    curr = root
    while curr is not None:
        if target_id > curr.data.id:
            pred = curr
            curr = curr.rightchild
        elif target_id < curr.data.id:
            curr = curr.leftchild
        else:
            if curr.leftchild is not None:
                temp = curr.leftchild
                while temp.rightchild is not None:
                    temp = temp.rightchild
                return temp
            break
    return pred

def find_expired_id(root, año_actual):
    if root is None:
        return None
    if root.data.año_vencimiento <= año_actual:
        return root.data.id
    left_res = find_expired_id(root.leftchild, año_actual)
    if left_res is not None:
        return left_res
    return find_expired_id(root.rightchild, año_actual)

def range_query_bst(root, low, high):
    if root is None:
        return
    if root.data.id > low:
        range_query_bst(root.leftchild, low, high)
    if low <= root.data.id <= high:
        print(root.data)
    if root.data.id < high:
        range_query_bst(root.rightchild, low, high)


# --- FUNCIONES CONTROLADORAS (LÓGICA DE NEGOCIO) ---
def registrar_medicamento(root, id_med, nombre, stock, año_vencimiento, precio):
    global CONTADOR_ALERTAS, VALOR_TOTAL_INVENTARIO
    
    if find_node_by_id(root, id_med) is not None:
        print(f"Error: Ya existe un medicamento con el ID {id_med}.")
        return root

    if id_med % 2 == 0:
        precio = precio * 0.90
        print(f"Regla Especial: ID par detectado ({id_med}). Se aplicó un 10% de descuento.")

    nuevo_med = Medicamento(id_med, nombre, stock, año_vencimiento, precio)
    root = insert_node_bst(root, nuevo_med)

    VALOR_TOTAL_INVENTARIO += precio * stock
    if stock < 5:
        CONTADOR_ALERTAS += 1
        
    print(f"Registrado exitosamente: {nombre} (ID: {id_med})")
    return root

def procesar_venta(root, id_venta, cantidad):
    global CONTADOR_ALERTAS, VALOR_TOTAL_INVENTARIO
    
    nodo = find_node_by_id(root, id_venta)
    if nodo is None:
        print(f"Error: Medicamento con ID {id_venta} no encontrado.")
        return root

    if nodo.data.stock == 0:
        print(f"Stock en cero para {nodo.data.nombre} (ID {id_venta}). Buscando sustitutos...")
        succ = find_successor(root, id_venta)
        if succ:
            print(f"Sugerencia Automática (Sucesor): {succ.data.nombre} (ID: {succ.data.id})")
        else:
            pred = find_predecessor(root, id_venta)
            if pred:
                print(f"Sugerencia Automática (Predecesor): {pred.data.nombre} (ID: {pred.data.id})")
            else:
                print("No se encontraron sustitutos disponibles.")
        return root

    if cantidad <= 0 or cantidad > nodo.data.stock:
        print(f"Cantidad inválida o stock insuficiente. Stock actual: {nodo.data.stock}")
        return root

    if nodo.data.stock < 5:
        CONTADOR_ALERTAS -= 1
    VALOR_TOTAL_INVENTARIO -= nodo.data.precio * nodo.data.stock
    
    nodo.data.stock -= cantidad
    
    VALOR_TOTAL_INVENTARIO += nodo.data.precio * nodo.data.stock
    if nodo.data.stock < 5:
        CONTADOR_ALERTAS += 1
        
    print(f"Venta procesada. {cantidad} unidades de {nodo.data.nombre} descontadas.")
    return root

def consolidar_inventario(root, id_origen, id_destino):
    global CONTADOR_ALERTAS, VALOR_TOTAL_INVENTARIO, TOTAL_OPERACIONES_FUSION
    
    nodo_origen = find_node_by_id(root, id_origen)
    nodo_destino = find_node_by_id(root, id_destino)
    
    if nodo_origen is None or nodo_destino is None:
        print("Error en consolidación: Uno o ambos IDs no existen.")
        return root

    stock_origen = nodo_origen.data.stock
    
    if nodo_destino.data.stock < 5:
        CONTADOR_ALERTAS -= 1
    VALOR_TOTAL_INVENTARIO -= nodo_destino.data.precio * nodo_destino.data.stock
    
    nodo_destino.data.stock += stock_origen
    
    VALOR_TOTAL_INVENTARIO += nodo_destino.data.precio * nodo_destino.data.stock
    if nodo_destino.data.stock < 5:
        CONTADOR_ALERTAS += 1

    if nodo_origen.data.stock < 5:
        CONTADOR_ALERTAS -= 1
    VALOR_TOTAL_INVENTARIO -= nodo_origen.data.precio * nodo_origen.data.stock
    
    root = delete_node_bst(root, id_origen)
    TOTAL_OPERACIONES_FUSION += 1
    print(f"Fusión exitosa: El stock del ID {id_origen} se movió al ID {id_destino}.")
    return root

def ejecutar_limpieza_caducidad(root, año_actual):
    global CONTADOR_ALERTAS, VALOR_TOTAL_INVENTARIO
    
    eliminados = 0
    while True:
        expired_id = find_expired_id(root, año_actual)
        if expired_id is None:
            break
        nodo = find_node_by_id(root, expired_id)
        if nodo:
            if nodo.data.stock < 5:
                CONTADOR_ALERTAS -= 1
            VALOR_TOTAL_INVENTARIO -= nodo.data.precio * nodo.data.stock
        root = delete_node_bst(root, expired_id)
        eliminados += 1
        print(f"Eliminado por caducidad automática: ID {expired_id}")
        
    if eliminados == 0:
        print("No se encontraron medicamentos caducados.")
    return root



root = None

print("\n--- 1. REGISTRO DE MEDICAMENTOS QUEMADOS ---")
root = registrar_medicamento(root, 101, "Paracetamol", 20, 2025, 5.0)
root = registrar_medicamento(root, 102, "Ibuprofeno", 4, 2024, 8.0)
root = registrar_medicamento(root, 50, "Amoxicilina", 10, 2023, 15.0)
root = registrar_medicamento(root, 150, "Aspirina", 0, 2026, 3.0)
root = registrar_medicamento(root, 200, "Loratadina", 30, 2027, 12.0)

print("\n--- 2. MOSTRAR INVENTARIO (IN-ORDER INVERSO) ---")
reverse_in_order(root)

print("\n--- 3. ESTADO GLOBAL INICIAL ---")
print(f"Alertas de Stock (< 5 unidades): {CONTADOR_ALERTAS}")
print(f"Valor Total del Inventario: ${VALOR_TOTAL_INVENTARIO:.2f}")

print("\n--- 4. VENDER MEDICAMENTO CON STOCK CERO (DEMOSTRAR SUGERENCIA) ---")
root = procesar_venta(root, 150, 1)

print("\n--- 5. VENDER MEDICAMENTO (RESTA NORMAL Y ALERTAS) ---")
root = procesar_venta(root, 101, 18)

print("\n--- 6. CONSULTAR RANGO DE IDs (50 a 150) ---")
range_query_bst(root, 50, 150)

print("\n--- 7. CONSOLIDACION DE INVENTARIO (FUSION DE 102 HACIA 101) ---")
root = consolidar_inventario(root, 102, 101)

print("\n--- 8. LIMPIEZA POR CADUCIDAD (AÑO ACTUAL: 2024) ---")
root = ejecutar_limpieza_caducidad(root, 2024)

print("\n--- 9. ESTADO GLOBAL FINAL ---")
print("INVENTARIO ACTUALIZADO (Mayor a menor):")
reverse_in_order(root)
print(f"\nAlertas de Stock (< 5 unidades): {CONTADOR_ALERTAS}")
print(f"Valor Total del Inventario: ${VALOR_TOTAL_INVENTARIO:.2f}")
print(f"Total Operaciones de Fusión Exitosas: {TOTAL_OPERACIONES_FUSION}")
