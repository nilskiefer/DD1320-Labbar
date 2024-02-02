from bintreeFile import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()
gamla = Bintree()
queue = LinkedQ()


def readfile(filename = "word3.txt"):
    with open(filename, "r", encoding = "utf-8") as file:
        tree = Bintree()
        for line in file:
            line=line.strip()
            if line in tree:
                gamla.put(line)
                pass
            svenska.put(line)
    return tree
def makechildren(startord):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
    for i in range(len(startord)):
        for j in alfabet:
            neword = startord[:i] + j + startord[i+1:] # Byter ut bokstaven i startord på plats i mot bokstaven j
            if neword in svenska and neword not in gamla:
                queue.enqueue(neword)
                gamla.put(neword)
def main():
    readfile()
    startord = input("Ange startord: ")
    slutord = input("Ange slutord: ")
    queue.enqueue(startord)
    while not queue.isEmpty():
        ordet = queue.dequeue()
        if ordet == slutord:
            print("Det finns en väg till", slutord)
            break
        else:
            makechildren(ordet)
                     
if __name__ == "__main__":
    main()
