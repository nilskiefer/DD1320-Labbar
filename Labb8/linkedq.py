class LinkedQueue:
    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = self.Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Kön är tom")
        data = self.front.data
        self.front = self.front.next
        if self.is_empty():
            self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Kön är tom")
        return self.front.data

    def __len__(self):
        return self.size()

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count
