import unittest
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


class TestMoleculeParser(unittest.TestCase):
    # Denna metod körs före varje test. Den ställer in förutsättningarna för testen.
    def setUp(self):
        self.queue = LinkedQueue()  # Skapar en ny kö för varje test.

    # En hjälpmetod för att lägga till element i kön. Används för att förbereda data för testen.
    def enqueue_elements(self, elements):
        for element in elements:
            self.queue.enqueue(element)  # Lägger varje element i kön.

    # Testar funktionen parse_LETTER med korrekt data.
    def test_parse_LETTER_correct(self):
        self.enqueue_elements(["C"])  # Lägger till 'C' i kön.
        try:
            parse_LETTER(self.queue)  # Försöker parsa 'C'.
        except Syntaxfel:
            self.fail(
                "Syntaxfel raised unexpectedly"
            )  # Testet misslyckas om ett Syntaxfel kastas.

    # Testar funktionen parse_LETTER med felaktig data.
    def test_parse_LETTER_incorrect(self):
        self.enqueue_elements(["c"])  # Lägger till 'c' (liten bokstav) i kön.
        with self.assertRaises(Syntaxfel):
            parse_LETTER(
                self.queue
            )  # Förväntar sig ett Syntaxfel eftersom 'c' är en liten bokstav.

    # Testar funktionen parse_atom med korrekt data.
    def test_parse_atom_correct(self):
        self.enqueue_elements(["C", "r"])  # Lägger till 'C' och 'r' i kön.
        try:
            parse_atom(self.queue)  # Försöker parsa 'C' följt av 'r'.
        except Syntaxfel:
            self.fail(
                "Syntaxfel raised unexpectedly"
            )  # Testet misslyckas om ett Syntaxfel kastas.

    # Testar funktionen parse_atom med felaktig data.
    def test_parse_atom_incorrect(self):
        self.enqueue_elements(["1"])  # Lägger till '1' i kön.
        with self.assertRaises(Syntaxfel):
            parse_atom(
                self.queue
            )  # Förväntar sig ett Syntaxfel eftersom '1' inte är en bokstav.


if __name__ == "__main__":
    unittest.main()
