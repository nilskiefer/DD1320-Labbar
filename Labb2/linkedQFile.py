class LinkedQ:
    def __init__(self):
        self.first = None
        self.last = None
    def enqueue(self, data):
        node = Node(data)
        if self.first == None:
            self.first = node
            self.last = node
        else:
            self.last.setNext(node)
            self.last = node
    def dequeue(self):
        if self.first == None:
            return None
        
        temp = self.first
        self.first = self.first.next
        return temp.data
        
    def isEmpty(self):
        return self.first == None
    
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    def __int__(self):
        return self.data
    
    def __iter__(self):
        return self.data
    
    def __next__(self):
        return self.next
    def setNext(self, next):
        self.next = next
        
