from bintreeFile import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()
gamla = Bintree()
q = LinkedQ()


class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent


def readfile(filename="word3.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line in svenska:
                gamla.put(line)
            else:
                svenska.put(line)


def makechildren(prevNode):
    prevOrd = prevNode.word
    alfabet = "qwertyuiopåasdfghjklöäzxcvbnm"
    gamla.put(prevOrd)
    for i in range(len(prevOrd)):
        for j in alfabet:
            neword = prevOrd[:i] + j + prevOrd[i + 1 :]
            if neword in svenska and neword not in gamla:
                gamla.put(neword)
                newNode = ParentNode(neword, prevNode)
                q.enqueue(newNode)


def find_path(startord, slutord):
    startnode = ParentNode(startord)
    q.enqueue(startnode)
    while not q.isEmpty():
        current_node = q.dequeue()
        if current_node.word == slutord:
            return current_node
        makechildren(current_node)
    return None


def utskriftSist(lista):
    if len(lista) > 0:
        utskriftSist(lista[1:])
        print(lista[0])


def printchain(endnode):
    node = endnode
    list = []
    # Skulle så klart också gå att göra utan att avända utskriftSist
    # Men i mån av att kunna välja så valde jag att använda den
    while node:
        list.append(node.word)
        node = node.parent
    utskriftSist(list)


def main():
    readfile()
    startord = input("Startord: ")
    slutord = input("Slutord: ")
    endnode = find_path(startord, slutord)
    if endnode:
        print("Det finns en väg från", startord, "till", slutord)
        printchain(endnode)  # Print the chain from the end node
    else:
        print("Ingen väg hittades")


if __name__ == "__main__":
    main()
