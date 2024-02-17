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


def main():
    # Läs in listan
    indata = input().strip()
    the_list = indata.split()
    # Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()


if __name__ == "__main__":
    main()
