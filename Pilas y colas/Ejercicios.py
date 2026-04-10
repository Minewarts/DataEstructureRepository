import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from Queue import Queue, QueueNode

custom_queue = Queue()
custom_queue.generate(10, 1, 50)
print("Cola generada:")
print(custom_queue)

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



