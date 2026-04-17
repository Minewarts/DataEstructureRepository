import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from Queue import Queue, QueueNode, Stack


'''custom_queue = Queue()
custom_queue.generate(10, 1, 50)
print("Cola generada:")
print(custom_queue)'''

'''def fix_string(input_str):
    corrected_str = Queue()
    index = 0
    while index < len(input_str)-2:
        if input_str[index] != input_str[index + 1]:
            if input_str[index].lower() == input_str[index+1] or input_str[index+1].lower() == input_str[index+2]:
                index += 2
            else:
                corrected_str.inQueue(input_str[index])
                index += 1
        else:
            corrected_str.inQueue(input_str[index])
            index += 1

    print ("index: ", index)
    corrected_str.inQueue(input_str[index])'''


'''def validate_expresion(math_expr):
    open= "{(["
    close= "})]"
    aux_stack = Stack()
    for c in math_expr:
        if c in open:
            aux_stack.push(c)
        elif c in close:
            print ("operador de cierre: ", c)
            print(" indice operador de cierre: ", close.index(c))
            if not aux_stack.is_empty():
                last_open = aux_stack.pop()
            else:
                return False
            print ("ultimo operador de apertura: ", last_open)
            print(" indice operador de apertura: ", open.index(last_open))
            if open.index(last_open) != close.index(c):
                return False
    return aux_stack.is_empty()


exp1 = "({[]})"
exp2 = "({[})]"
exp3 = "({[]})]"
exp4 = "({[]}"

print(validate_expresion(exp1))
print(validate_expresion(exp2))
print(validate_expresion(exp3))
print(validate_expresion(exp4))'''

'''class QueueStack:

    def __init__(self):
        self.in_stack = Stack()
        self.aux_stack = Stack()

    def inQueue(self, elemento):
        self.in_stack.push(elemento)

    def deQueue(self):
        if self.is_empty():
            return 'No hay elementos en la cola'
        else:
            while not self.in_stack.is_empty():
                self.aux_stack.push(self.in_stack.pop())
            

    def is_empty(self):
        return self.in_stack.is_empty() and self.aux_stack.is_empty()
    
    def len(self):
        return self.in_stack.size + self.aux_stack.size
    
    def __str__ (self):
        result = []
        current = self.aux_stack.top
        while current is not None:
            result.append(str(current.dato))
            current = current.next
        current = self.in_stack.top
        while current is not None:
            result.append(str(current.dato))
            current = current.next
        return ' -- '.join(result)
'''

'''def change_positions(stk,i,j):
    aux_stack = Stack()
    index = stk.len() - 1
    value_i = ''
    value_j = ''
    while not stk.is_empty():
        temp_value = stk.pop()

        if index == i:
            value_i = temp_value
        if index == j:
            value_j = temp_value
        else:

        
        aux_stack.push(temp_value)
        index -= 1


custom_stack = Stack()
custom_stack.generate_random_stack(10)

print("Pila generada:", custom_stack)
print("Pila con posiciones 2 y 5 intercambiadas:", change_positions(custom_stack, 2, 5))'''

'''def put_in_queue(queue, element, i):
    aux_queue = queue
    index = 0
    result= Queue()
    if i < 0 or i >= queue.size:
        raise IndexError("La posición es inválida")

    while not queue.is_empty():
        temp_value = queue.deQueue()
        if index == i:
            result.inQueue(element)
        else:
            result.inQueue(temp_value)
        index += 1
    return result 

custom_queue = Queue()
custom_queue.generate(10)
print("Cola generada:", custom_queue)
print("Cola con elemento 99 en la posición 3:", put_in_queue(custom_queue, 99, 3))'''

'''stack1 = Stack()
stack2 = Stack()
stack3 = Stack()
stack4 = Stack()

stack1.generate_random_stack(4)
stack2.generate_random_stack(4)
stack3.generate_random_stack(4)
stack4.generate_random_stack(4)

print("stack 1:", stack1)
print("stack 2:", stack2)
print("stack 3:", stack3)
print("stack 4:", stack4)

stack_of_stacks = Stack()
stack_of_stacks.push(stack1)
stack_of_stacks.push(stack2)
stack_of_stacks.push(stack3)
stack_of_stacks.push(stack4)

def find_min(stack_of_stacks):
    Q_result = Queue()
    while not stack_of_stacks.is_empty():
        temp_stack = stack_of_stacks.pop()
        min_value =temp_stack.top.dato
        while not temp_stack.is_empty():
            temp_value = temp_stack.pop()
            if temp_value < min_value:
                min_value = temp_value
        Q_result.inQueue(min_value)
    return Q_result

print("Q_result:", find_min(stack_of_stacks))'''

stack = Stack()
stack.generate_random_stack(10)
print("stack: ", stack)

def organize_queue_min_Max(stack):
    result_stack = Stack()
    while not stack.is_empty():
        current_value = stack.pop()

        if current_value is None:
            break

        if result_stack.is_empty():
            result_stack.push(current_value)
        elif result_stack.top.dato < current_value:
            result_stack.push(current_value)
        elif result_stack.top.dato > current_value:
            while not result_stack.is_empty() and result_stack.top.dato >= current_value:
                stack.push(result_stack.pop())
            result_stack.push(current_value)
        else:
            result_stack.push(current_value)

    while not result_stack.is_empty():
        stack.push(result_stack.pop())
    return stack

print('stack_result: ', organize_queue_min_Max(stack))
        

        
        
