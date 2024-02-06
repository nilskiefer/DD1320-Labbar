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


def makechildren(startord):
    alfabet = "qwertyuiopåasdfghjklöäzxcvbnm"
    gamla.put(startord)
    for i in range(len(startord)):
        for j in alfabet:
            neword = startord[:i] + j + startord[i + 1 :]
            # startord[:i] hämtar delsträngen av startord från början upp till
            # (men inte inklusive) bokstaven på position i. Detta fångar alla
            # bokstäver före den vi vill ersätta.

            # j representerar den nya bokstaven som vi vill infoga på position i.

            # startord[i+1:] hämtar delsträngen av startord som börjar från
            # bokstaven efter den på position i. Detta fångar alla bokstäver
            # efter den vi vill ersätta.
            if neword in svenska and neword not in gamla:
                print(neword)  # Print the new word on the screen
                gamla.put(neword)  # Add the new word to gamla
                q.enqueue(neword)


def find_path(startord, slutord):
    q.enqueue(startord)
    while not q.isEmpty():
        current_word = q.dequeue()
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
