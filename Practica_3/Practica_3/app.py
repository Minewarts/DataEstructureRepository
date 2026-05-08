# Sanet Correa Y Cristian Escobar
"""-incluir prioridad, insumos pediatricos
   -Erorr analisis 15% regresa al proceso:
   -Cierre Ventanilla, ejecuta numero determinado de turnos en area toma de muestras
   -Capacidad Dinamica x congestion: Un area debe ajustar su capacidad por congestion, si el area tiene en espera mas de 2 pacientes el area actual no debe de procesar ningun paciente
   """

from Iniciadores import Queue, Stack, Node
import random

class Patient:
    def __init__(self, name, patient_type):
        self.name = name
        self.patient_type = patient_type
        self.error = random.randint(1, 100)


class Area:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = Queue()


def initialize_system():
    stack_areas = Stack()
    stack_areas.push(Area("Result delivery", 2))
    stack_areas.push(Area("Result validation", 1))
    stack_areas.push(Area("Analysis", 2))
    stack_areas.push(Area("Sample collection", 3))
    return stack_areas


def add_patient(stack_areas, name, patient_type):
    if stack_areas.is_empty():
        print("System is empty")
        return
    top_area = stack_areas.pop()
    top_area.patients.enqueue(Patient(name, patient_type))
    stack_areas.push(top_area)


def process_shift(stack_areas, shift_max=4, shift=1):
    aux_stack = Stack()
    transfer_queue = Queue()
    
    attended_report = ""
    waiting_report = ""
    
    while not stack_areas.is_empty():


        area = stack_areas.pop()
        new_transfer_queue = Queue()
        attended_count = 0
        attended_names = ""
        
        
        while attended_count < area.capacity and not area.patients.is_empty():
            
            patient = area.patients.dequeue()
            if shift <= shift_max and area.name == "Sample collection": 
                if patient.error >= 15: 
                    new_transfer_queue.enqueue(patient)
                    attended_names += patient.name + " "
                    attended_count += 1
                    print(f'La muestra del paciente {patient.name} no esta contaminada, puede continuar. Valor = {patient.error}')
                else: 
                    add_patient(stack_areas, patient.name, patient.patient_type)
                    print(f'La muestra ha sido contaminada, favor retomar muestras. Valor = {patient.error}')

            
        if attended_names == "":
            attended_names = "None"
            
        attended_report += area.name + ": " + attended_names + "\n"
        
        while not transfer_queue.is_empty():
            area.patients.enqueue(transfer_queue.dequeue())
            
        transfer_queue = new_transfer_queue
        aux_queue = Queue()
        waiting_names = ""
        
        while not area.patients.is_empty():
            patient = area.patients.dequeue()
            waiting_names += patient.name + " "
            aux_queue.enqueue(patient)
            
        if waiting_names == "":
            waiting_names = "None"
            
        waiting_report += area.name + ": " + waiting_names + "\n"
        
        while not aux_queue.is_empty():
            area.patients.enqueue(aux_queue.dequeue())
            
        aux_stack.push(area)
        shift=shift+1 
        
    while not aux_stack.is_empty():
        stack_areas.push(aux_stack.pop())
        
    print("--- PROCESSED PATIENTS ---")
    print(attended_report)
    print("--- WAITING PATIENTS ---")
    print(waiting_report)
    
    left_system = ""
    while not transfer_queue.is_empty():
        left_system += transfer_queue.dequeue().name + " "
    if left_system != "":
        print("Patients who left the system: " + left_system + "\n")


def has_patients(stack_areas):
    aux_stack = Stack()
    patient_exists = False
    while not stack_areas.is_empty():
        area = stack_areas.pop()
        if not area.patients.is_empty():
            patient_exists = True
        aux_stack.push(area)
    while not aux_stack.is_empty():
        stack_areas.push(aux_stack.pop())
    return patient_exists

def automate(stack_areas, shift_max=4):
    index=1
    shift_number = 4 
    while has_patients(stack_areas):
        index= index+1
        print("\n=== SHIFT " + str(shift_number) + " ===")
        process_shift(stack_areas, shift_max, index)
        shift_number += 1


def check_status(stack_areas):
    aux_stack = Stack()
    print("\n--- SYSTEM STATUS ---")
    while not stack_areas.is_empty():
        area = stack_areas.pop()
        aux_queue = Queue()
        names = ""
        while not area.patients.is_empty():
            patient = area.patients.dequeue()
            names += patient.name + " "
            aux_queue.enqueue(patient)
        while not aux_queue.is_empty():
            area.patients.enqueue(aux_queue.dequeue())
        if names == "":
            names = "Empty"
        print(area.name + " (Cap. " + str(area.capacity) + ") -> In queue: " + names)
        aux_stack.push(area)
    while not aux_stack.is_empty():
        stack_areas.push(aux_stack.pop())
    print("--------------------------\n")


if __name__ == "__main__":
    stack_areas = initialize_system()

    add_patient(stack_areas, "P1", "Adult")
    add_patient(stack_areas, "P2", "Adult")
    add_patient(stack_areas, "P3", "Child")
    add_patient(stack_areas, "P4", "Child")
    add_patient(stack_areas, "P5", "Adult")
    add_patient(stack_areas, "P6", "Child")
    add_patient(stack_areas, "P7", "Adult")

    print("--- INITIAL PATIENT ENTRY ---")
    check_status(stack_areas)

    print("\n=== SHIFT 1 ===")
    process_shift(stack_areas)
    check_status(stack_areas)

    print("\n=== SHIFT 2 ===")
    process_shift(stack_areas)
    check_status(stack_areas)

    print("\n=== SHIFT 3 ===")
    process_shift(stack_areas)
    check_status(stack_areas)

    print("\n=== AUTOMATING REMAINING SHIFTS ===")
    automate(stack_areas)
