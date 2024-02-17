from song import Song
import timeit, random


def binary_search(arr, x):
    # Hjälpfunktion för binärsökning
    def search(low, high):
        if high >= low:
            mid = (high + low) // 2

            if arr[mid] == x:
                return x  # Returnera elementet

            elif arr[mid] > x:
                return search(low, mid - 1)

            else:
                return search(mid + 1, high)

        else:
            return None  # Elementet hittades inte

    # Starta sökningen
    return search(0, len(arr) - 1)


def linsok(lista, other):
    for song in lista:
        if song.artist == other.artist:
            return song
    return None


def create_hash_table(songs):
    hash_table = {}
    for song in songs:
        key = f"{song.artist}-{song.title}"  # Skapar en unik nyckel för varje låt
        hash_table[key] = song
    return hash_table


def hash_search(hash_table, song):
    key = f"{song.artist}-{song.title}"
    return hash_table.get(key)


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
    # Linjärsökning
    linjtid = timeit.timeit(
        stmt=lambda: linsok(lista, random.choice(lista)), number=10000
    )
    # Binärsökning
    lista.sort()
    binjtid = timeit.timeit(
        stmt=lambda: binary_search(lista, random.choice(lista)),
        number=100000,
    )
    # Hashtabellsökning
    hashCreationTime = timeit.timeit(stmt=lambda: create_hash_table(lista), number=1)
    # print("Skapandet av hashtabellen tog", round(hashCreationTime, 10), "sekunder")
    hash_table = create_hash_table(lista)
    hashtid = timeit.timeit(
        stmt=lambda: hash_search(hash_table, random.choice(lista)), number=100000
    )
    return linjtid, binjtid, hashtid


def bubbleSort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def main():
    list = read_songs("unique_tracks.txt")
    print(testTimes(list[:250000]))
    print(testTimes(list[:500000]))
    print(testTimes(list[:1000000]))
    print(testTimes(list))


if __name__ == "__main__":
    main()
