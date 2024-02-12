def utskrift(lista):
    if len(lista) > 0:
        print(lista[0])
        utskrift(lista[1:])


def utskriftSist(lista):
    if len(lista) > 0:
        utskriftSist(lista[1:])
        print(lista[0])


def main():
    lista = [1, 2, 3, 4, 5]
    utskrift(lista)
    print("\n")
    utskriftSist(lista)


if __name__ == "__main__":
    main()
