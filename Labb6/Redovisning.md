Tänk igenom vilket attribut passar bäst (annars får man massor av konstiga siffror). Kolla tidskomplexiteten stämmer överens.

# Timeit-modulen i Python

## Parametrar i Timeit

- `stmt`: Detta är det påstående du vill mäta exekveringstiden för. Det kan vara en sträng som kan exekveras av Python, eller ett anropbart objekt som en funktion. I det här fallet är det en `lambda`-funktion som anropar `linsok(lista, random.choice(lista))`. Detta innebär att timeit kommer att mäta tiden det tar att exekvera detta funktionsanrop.


- `number`: Anger hur många gånger `stmt` ska exekveras. Det är ett heltal som standardinställs till 1000000.

## Vad Timeit Tar Tid På

Timeit mäter exekveringstiden för koden specificerad i `stmt` över antalet iterationer angivet av `number`.

## Utskrift från Timeit

Timeit skriver ut totala exekveringstiden (i sekunder) för koden i `stmt` över de `number` antal iterationer som utförts.

# Sökningsmetoder
Linjärsökning tidskomplexitet: $O(n)$
Binärsökningstid: $O(n\ln(n))$
Hastabellsökning: $O(1)$

| Liststorlek (n) | Linjärsökningstid (s) | Binärsökningstid (s) | Hashtabellsökningstid (s) |
|-----------------|-----------------------|----------------------|---------------------------|
| 250 000         | 5.2810                | 0.3476               | 0.0760                    |
| 500 000         | 7.5831                | 0.3638               | 0.0852                    |
| 1 000 000       | 9.6254                | 0.3998               | 0.1149                    |
| ALL               | 10.2317               | 0.3785               | 0.0999                    |

![[538dafad-2f73-48df-bacd-b4904722fa56 1.jpeg]]
# Sorteringsalgoritmer
Bubblesort tidskomplexitet: $O(n^2)$
Bogosort tidskomplexitet: $O(∞)$

| Liststorlek (n) | Bubble Sort Tid (s)   | BogoSort Tid (s)       |
|-----------------|-----------------------|------------------------|
| 10 | 2.3959e-05            | 7.25e-06               |
| 100             | 0.0018963             | 3.2417e-05             |
| 1000            | 0.18335               | 0.00034                |
| 10000           | 19.1982               | 0.02047                |

![[2a8aa996-211f-4073-9577-558a9da351f2.jpeg]]
