# Nils Kiefer och Oscar Persson
import unittest
import sys
from linkedQFile import LinkedQ


class TestQueue(unittest.TestCase):

    def test_isEmpty(self):
        #isEmpty ska returnera True för tom kö, False annar
        q = LinkedQ()
        self.assertTrue(q.isEmpty(), "isEmpty på tom kö")
        q.enqueue(17)
        self.assertFalse(q.isEmpty(), "isEmpty på icke-tom kö")

    def test_order(self):
        #Kontrollerar att kö-ordningen blir rätt
        q = LinkedQ()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)

def sphagettifiArray(array):
    q = LinkedQ()
    for i in array:
        q.enqueue(i)
    return q
        
def trollkarlsprogram(kort):
    temp = []
    while not kort.isEmpty():
        kort.enqueue(kort.dequeue())
        temp.append(kort.dequeue())
    return temp

def main():
    userInput = sys.stdin.readline().split()
    inmatning = sphagettifiArray(userInput)
    q = LinkedQ()
    while not inmatning.isEmpty():
        inmatning.enqueue(inmatning.dequeue())
        q.enqueue(inmatning.dequeue())
    while not q.isEmpty():
        print(q.dequeue()+" ", end="")
    
if __name__ == "__main__":
    #unittest.main()
    main()