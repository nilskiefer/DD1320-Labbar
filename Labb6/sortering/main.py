from song import Song
import timeit, random


def bubbleSort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return


def isSorted(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def bogoSort(lista):
    while not isSorted(lista):
        random.shuffle(lista)
    return


def read_songs(filename):
    songs = []
    with open(filename, encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("<SEP>")
            if len(parts) == 4:
                song = Song(*parts)
                songs.append(song)
            else:
                print("Felaktig rad:", line)
    return songs


def testTimes(lista):
    t_bubbleSort = timeit.timeit(lambda: bubbleSort(lista), number=3)
    t_bogoSort = timeit.timeit(lambda: bogoSort(lista), number=3)
    return t_bubbleSort, t_bogoSort


def main():
    list = read_songs("unique_tracks.txt")
    for i in range(4):
        n = 10 * 10**i
        print("N: " + str(n), testTimes(list[:n]))


if __name__ == "__main__":
    main()
