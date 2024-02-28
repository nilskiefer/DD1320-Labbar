class HashNode:
    """Noder till klassen Hashtable. Varje nod representerar ett dataelement i hashtabellen."""

    def __init__(self, key, value):
        self.key = key  # Nyckeln för dataelementet
        self.value = value  # Själva datavärdet
        self.next = (
            None  # En pekare till nästa nod i en krocklista (används vid kollisioner)
        )


class Hashtable:
    def __init__(self, size=10):
        self.size = size  # Storleken på hashtabellen, antalet 'slots' i tabellen
        self.table = [None] * size  # Skapar hashtabellen, inledningsvis tomma slots

    def hashfunction(self, key):
        """En enkel hashfunktion som omvandlar en nyckel till ett index i hashtabellen."""
        hash_sum = 0
        for char in str(key):
            hash_sum += ord(
                char
            )  # Omvandlar varje tecken i nyckeln till dess ASCII-värde och summerar
        return (
            hash_sum % self.size
        )  # Använder modulus för att se till att indexet är inom tabellstorleken

    def store(self, key, value):
        """Lagrar ett värde med en specifik nyckel i hashtabellen."""
        index = self.hashfunction(key)  # Beräknar indexet för nyckeln
        node = self.table[index]

        # Om det inte finns något på detta index, lägg till en ny nod här
        if node is None:
            self.table[index] = HashNode(key, value)
            return

        # Om det finns en nod, gå igenom krocklistan för att hitta rätt plats eller uppdatera en befintlig nyckel
        prev = None
        while node is not None:
            if node.key == key:
                node.value = value  # Uppdatera befintlig nyckel
                return
            prev = node
            node = node.next

        # Om nyckeln inte finns, lägg till en ny nod i slutet av krocklistan
        prev.next = HashNode(key, value)

    def search(self, key):
        """Hämtar ett värde baserat på nyckeln. Kastar KeyError om nyckeln inte finns."""
        index = self.hashfunction(key)  # Beräknar indexet för nyckeln
        node = self.table[index]

        # Gå igenom krocklistan på detta index för att hitta noden med rätt nyckel
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        # Om nyckeln inte finns, kasta ett KeyError
        raise KeyError(f"Nyclen '{key}' finns inte i hashtabellen.")

    def __str__(self):
        output = []
        for i in range(self.size):
            node = self.table[i]
            while node is not None:
                output.append(f"{node.key}: {node.value}")
                node = node.next
        return "{" + ", ".join(output) + "}"

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def __len__(self):
        count = 0
        for i in range(self.size):
            node = self.table[i]
            while node is not None:
                count += 1
                node = node.next
        return count
