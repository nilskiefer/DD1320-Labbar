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


def stalinSort(lista):
    n = len(lista) - 1
    for i in range(n):
        if lista[i] > lista[i + 1]:
            lista.pop(i)
    if isSorted(lista):
        return lista
    return "FAILED"


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
    random.shuffle(lista)
    t_bubbleSort = 0  # timeit.timeit(lambda: bubbleSort(lista), number=1)
    t_bogoSort = timeit.timeit(lambda: bogoSort(lista), number=1)
    t_stalinSort = timeit.timeit(lambda: stalinSort(lista), number=1)
    return t_bubbleSort, t_bogoSort, t_stalinSort


def main():
    list = read_songs("unique_tracks.txt")

    # Print the markdown table
    print("| N | Bubble Sort Time | Bogo Sort Time | Stalin Sort Time |")
    print("|---|------------------|----------------|------------------|")

    for i in range(5):
        n = 10 * 10**i
        t_bubbleSort, t_bogoSort, t_stalinSort = testTimes(list[:n])
        print(f"| {n} | {t_bubbleSort:.8f} | {t_bogoSort:.8f} | {t_stalinSort:.8f} |")


if __name__ == "__main__":
    main()
