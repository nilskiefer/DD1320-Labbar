class Bintree:
    def __init__(self):
        self.__root = None  # Gör roten privat

    def put(self, newvalue):
        self.__root = self.__putta(self.__root, newvalue)
        # Lägger till ett nytt värde i trädet

    def __contains__(self, value):
        return self.__finns(self.__root, value)
        # Kontrollerar om ett värde finns i trädet

    def __putta(self, p, value):
        # Privat metod för att lägga till ett värde i trädet
        if p == None:
            return Node(value)  # Skapar en ny nod om platsen är tom
        elif value < p.getVal():
            p.setLeft(
                self.__putta(p.getLeft(), value)
            )  # Lägger till värdet i vänstra underträdet
        elif value > p.getVal():
            p.setRight(
                self.__putta(p.getRight(), value)
            )  # Lägger till värdet i högra underträdet
        return p

    def __finns(self, p, value):
        # Privat metod för att kontrollera om ett värde finns
        if p == None:
            return False
        elif value == p.getVal():
            return True  # Hittar värdet
        elif value < p.getVal():
            return self.__finns(p.getLeft(), value)  # Söker i vänstra underträdet
        else:
            return self.__finns(p.getRight(), value)  # Söker i högra underträdet

    def __skriv(self, p):
        # Privat metod för att skriva ut trädet
        if p != None:
            self.__skriv(p.getLeft())  # Besöker vänstra underträdet
            print(p.getVal())  # Skriver ut nodens värde
            self.__skriv(p.getRight())  # Besöker högra underträdet

    def write(self):
        self.__skriv(self.__root)
        print("\n")
        # Offentlig metod för att skriva ut hela trädet


class Node:
    def __init__(self, data, parent=None):
        self.__data = data
        self.__parent = parent
        self.__left = None
        self.__right = None

    def getVal(self):
        return self.__data

    def getParent(self):
        return self.__parent

    def getLeft(self):
        return self.__left

    def getRight(self):
        return self.__right

    def setLeft(self, left):
        self.__left = left

    def setRight(self, right):
        self.__right = right
