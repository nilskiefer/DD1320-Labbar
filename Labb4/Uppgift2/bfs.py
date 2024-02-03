from bintreeFile import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()
gamla = Bintree()
queue = LinkedQ()


def readfile(filnamn = "word3.txt"):
    with open(filnamn, "r", encoding = "utf-8") as fil:
        träd = Bintree()
        for rad in fil:
            rad = rad.strip()
            if rad in träd:
                gamla.put(rad)
                pass
            svenska.put(rad)
    return träd
def makechildren(startord):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
    for i in range(len(startord)):
        for j in alfabet:
            neword = startord[:i] + j + startord[i+1:] 
            # startord[:i] hämtar delsträngen av startord från början upp till (men inte inklusive) bokstaven på position i. Detta fångar alla bokstäver före den vi vill ersätta.
            # j representerar den nya bokstaven som vi vill infoga på position i.
            # startord[i+1:] hämtar delsträngen av startord som börjar från bokstaven efter den på position i. Detta fångar alla bokstäver efter den vi vill ersätta.
            if neword in svenska and neword not in gamla:
                queue.enqueue(neword)
                gamla.put(neword)
def main():
    readfile()
    startord = input("Ange startord: ")
    slutord = input("Ange slutord: ")
    queue.enqueue(startord)
    i = 0
    while not queue.isEmpty():
        ordet = queue.dequeue()
        if ordet == slutord:
            print("Det finns en väg till", slutord)
            break
        else:
            i+=1
            makechildren(ordet)
    print()
if __name__ == "__main__":
    main()
