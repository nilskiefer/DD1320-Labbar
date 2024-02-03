from bintreeFile import Bintree
from linkedQFile import LinkedQ

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


def makechildren(startord):
    alfabet = "qwertyuiopåasdfghjklöäzxcvbnm"
    gamla.put(startord)
    for i in range(len(startord)):
        for j in alfabet:
            neword = startord[:i] + j + startord[i + 1 :]
            if neword in svenska and neword not in gamla:
                print(neword)  # Print the new word on the screen
                gamla.put(neword)  # Add the new word to gamla


def find_path(startord, slutord):
    queue.enqueue(startord)
    while not queue.isEmpty():
        current_word = queue.dequeue()
        if current_word == slutord:
            return True  # Found the path
        makechildren(current_word)
    return False  # No path found


def main():
    readfile()
    startord = input("Startord: ")
    slutord = input("Slutord: ")
    if find_path(startord, slutord):
        print("There is a path from", startord, "to", slutord)
    else:
        print("No path found")
    print("done")


if __name__ == "__main__":
    main()
