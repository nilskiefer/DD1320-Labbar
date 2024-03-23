import sys

from linkedq import LinkedQueue


# Anpassat undantag för syntaxfel
class Syntaxfel(Exception):
    pass


# Analyserar en molekyl
def parse_molecule(queue):
    parse_atom(queue)  # Parsar en atom
    # Om det finns mer innehåll i kön och nästa tecken är en siffra, parsar ett nummer
    if not queue.is_empty() and queue.peek().isdigit():
        parse_num(queue)


# Analyserar en atom
def parse_atom(queue):
    parse_LETTER(queue)  # Parsar en stor bokstav
    # Om det finns mer innehåll i kön och nästa tecken är en liten bokstav, parsar en liten bokstav
    if not queue.is_empty() and queue.peek().islower():
        parse_letter(queue)


# Analyserar en stor bokstav
def parse_LETTER(queue):
    # Om kön är tom eller nästa tecken inte är en stor bokstav, kasta ett syntaxfel
    if queue.is_empty() or not queue.peek().isupper():
        raise Syntaxfel("Saknad stor bokstav vid radslutet")
    queue.dequeue()  # Tar bort tecknet från kön


# Analyserar en liten bokstav
def parse_letter(queue):
    # Om kön är tom eller nästa tecken inte är en liten bokstav, kasta ett syntaxfel
    if queue.is_empty() or not queue.peek().islower():
        raise Syntaxfel("Saknad liten bokstav vid radslutet")
    queue.dequeue()  # Tar bort tecknet från kön


# Analyserar ett nummer
def parse_num(queue):
    num = ""
    # Samla alla siffror som finns i kön
    while not queue.is_empty() and queue.peek().isdigit():
        num += queue.dequeue()

    # Om inga siffror hittades, kasta ett syntaxfel
    if num == "":
        raise Syntaxfel("Saknad siffra vid radslutet")
    # Om numret börjar med en nolla och är mer än en siffra långt, kasta ett syntaxfel
    elif num[0] == "0" and len(num) > 1:
        num_without_leading_zero = num.lstrip(
            "0"
        )  # Ta bort ledande nollor för felmeddelandet
        raise Syntaxfel("För litet tal vid radslutet " + num_without_leading_zero)
    elif int(num) < 2:
        raise Syntaxfel("För litet tal vid radslutet")


# Läser och analyserar molekyler från användarinmatning
def read_and_parse_molecules():
    while True:
        line = sys.stdin.readline().strip()  # Läs en rad och ta bort whitespace
        if line == "#":
            break  # Avslutar om användaren skriver '#'

        queue = LinkedQueue()
        for char in line:
            queue.enqueue(char)  # Lägger varje tecken i kön

        try:
            parse_molecule(queue)
            if not queue.is_empty():
                raise Syntaxfel("Oväntat tecken vid radslutet")
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as e:
            processed_length = len(line) - queue.size()
            remaining_input = line[
                processed_length:
            ]  # Detta är den obehandlade delen av raden
            print(f"{e} {remaining_input}")


if __name__ == "__main__":
    read_and_parse_molecules()
