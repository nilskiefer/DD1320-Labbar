import csv
from hashtable import Hashtable


def load_data(filename, hashtable):
    with open(filename, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Hoppa över rubrikraden
        for parts in csv_reader:
            if (
                len(parts) < 10
            ):  # Kontrollera att det finns tillräckligt många delar i raden
                continue
            drama_name = parts[0]
            details = {
                "Rating": parts[1],
                "Actors": parts[2],
                "Viewship Rate": parts[3],
                "Genre": parts[4],
                "Director": parts[5],
                "Writer": parts[6],
                "Year": parts[7],
                "No of Episodes": parts[8],
                "Network": parts[9],
            }
            hashtable.store(
                drama_name, details
            )  # Använd put för att lägga till data i hashtabellen


# Huvudprogrammet
hashtable = Hashtable(size=1000)  # Justera storleken baserat på ditt dataset
filename = "kdrama.csv"

load_data(filename, hashtable)

print(len(hashtable))  # Skriv ut antalet element i hashtabellen
# print(hashtable) # Ta bort kommentaren för denna rad för att se hela hashtabellen
shouldBeInHash = "Legend of the Blue Sea"
shouldntBeInHash = "My love from the star AND A BIG FAT YELLOW CAR"
if shouldBeInHash in hashtable:
    print(hashtable.search(shouldBeInHash))
try:
    print(hashtable.search(shouldntBeInHash))
except KeyError:
    print(f"{shouldntBeInHash} finns inte i hashtabellen.")
