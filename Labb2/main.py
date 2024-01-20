import unittest
from linkedQFile import LinkedQ
import sys

class TestQueue(unittest.TestCase):

    def test_isEmpty(self):
        #isEmpty ska returnera True för tom kö, False annars
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
        
def trollkarlsprogram(kort):
    temp = []
    while not kort.isEmpty():
        kort.enqueue(kort.dequeue())
        temp.append(kort.dequeue())
    return temp

def main():
    print("Ange ordningen på korten (exempel: 3 1 4 2 5 stop show stop show stop show...):")
    inmatning = sys.stdin.readline().split()
    if len(inmatning) != 5:
        print("Du får inte ange fler än 5 mojänger!")
        main()
    q = LinkedQ()
    for card in inmatning:
        q.enqueue(card)
    print("De kommer ut i denna ordning:", " ".join(map(str, trollkarlsprogram(q))))

if __name__ == "__main__":
    #unittest.main()
    main()