from bintreeFile import Bintree
from linkedQFile import LinkedQ
from bintreeFile import Node

svenska = Bintree()
gamla = Bintree()
queue = LinkedQ()


def readfile(filename="word3.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line in svenska:
                gamla.put(line)
            else:
                svenska.put(line)


def makechildren(node):
    startord = node.getVal()
    parent = node  # Nuvarande nod blir parent till de nya noderna
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    gamla.put(startord)
    for i in range(len(startord)):
        for j in alphabet:
            newWord = startord[:i] + j + startord[i + 1 :]
            # startord[:i] hämtar delsträngen av startord från början upp till (men inte inklusive) bokstaven på position i. Detta fångar alla bokstäver före den vi vill ersätta.
            # j representerar den nya bokstaven som vi vill infoga på position i.
            # startord[i+1:] hämtar delsträngen av startord som börjar från bokstaven efter den på position i. Detta fångar alla bokstäver efter den vi vill ersätta.
            if newWord in svenska and newWord not in gamla:
                print(newWord)
                gamla.put(newWord)
                queue.enqueue(Node(newWord, parent))


def find_path(startord, slutord):
    startNode = Node(startord)
    queue.enqueue(startNode)
    while not queue.isEmpty():
        currNode = queue.dequeue()
        if currNode.getVal() == slutord:
            print("Det finns en väg till", slutord)
            return  # Found the path
        makechildren(currNode)
    print("Ingen väg hittades")


def main():
    readfile()
    startord = input("Startord: ")
    slutord = input("Slutord: ")
    find_path(startord, slutord)


if __name__ == "__main__":
    main()
