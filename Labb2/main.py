from arrayQFile import ArrayQ

def trollkarlsprogram(kort):
    temp = []
    while not kort.isEmpty():
        kort.enqueue(kort.dequeue())
        temp.append(kort.dequeue())
    return temp

def main():
    print("Ange ordningen på korten (exempel: 3 1 4 2 5 stop show stop show stop show...):")
    inmatning = input().split()
    if len(inmatning) != 5:
        print("Du får inte ange fler än 5 kort!")
        main()
    q = ArrayQ()
    for card in inmatning:
        q.enqueue(int(card))
    print("De kommer ut i denna ordning:", " ".join(map(str, trollkarlsprogram(q))))

if __name__ == "__main__":
    main()