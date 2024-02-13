from bintreeFile import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()
gamla = Bintree()
q = LinkedQ()


def readfile(filename="word3.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line in svenska:
                gamla.put(line)
            else:
                svenska.put(line)


def makechildren(startnode):
    startord = startnode.word
    alfabet = "qwertyuiopåasdfghjklöäzxcvbnm"
    gamla.put(startord)
    for i in range(len(startord)):
        for j in alfabet:
            neword = startord[:i] + j + startord[i + 1 :]
            if neword in svenska and neword not in gamla:
                gamla.put(neword)
                newnode = ParentNode(neword, startnode)
                q.enqueue(newnode)


def find_path(startord, slutord):
    startnode = ParentNode(startord)
    q.enqueue(startnode)
    while not q.isEmpty():
        current_node = q.dequeue()
        if current_node.word == slutord:
            return current_node
        makechildren(current_node)
    return None


def printchain(endnode):
    node = endnode
    while node:
        print(node.word)
        node = node.parent


def main():
    readfile()
    startord = input("Startord: ")
    slutord = input("Slutord: ")
    endnode = find_path(startord, slutord)
    if endnode:
        print("Det finns en väg från", startord, "till", slutord)
        print(startord)
        printchain(endnode)  # Print the chain from the end node
    else:
        print("Ingen väg hittades")
    print("done")


if __name__ == "__main__":
    main()


class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent
