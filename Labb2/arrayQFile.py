from array import array

class ArrayQ:
    def __init__(self):
        self.queue = array('i')
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
