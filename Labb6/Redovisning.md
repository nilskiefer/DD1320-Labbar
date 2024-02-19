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
Binärsökningstid: $O(\ln(n))$
Hastabellsökning: $O(1)$

| Deluppsättning Storlek | Linjärsökningstid | Binärsökningstid | Hashtabellsökningstid |
|------------------------|-------------------|------------------|-----------------------|
| 10 | 0.00000031 | 0.00000089 | 0.00000032 |
| 100 | 0.00000090 | 0.00000137 | 0.00000028 |
| 1000 | 0.00000719 | 0.00000226 | 0.00000032 |
| 10000 | 0.00006174 | 0.00000286 | 0.00000036 |
| 100000 | 0.00034283 | 0.00000395 | 0.00000083 |
| 1000000 | 0.00111350 | 0.00000422 | 0.00000114 |

![[5968fcdc-bf6c-40d5-a6e1-d18de1020e4c.jpeg]]
# Sorteringsalgoritmer
Bubblesort tidskomplexitet: $O(n^2)$
Bogosort tidskomplexitet: $O(∞)$
Stalinsort tidskomplexitet: $O(n)$ (men man förlorar data)

| N | Bubble Sort Time | Bogo Sort Time | Stalin Sort Time |
|---|------------------|----------------|------------------|
| 10 | 0.00001204 | 0.00000275 | 0.00000317 |
| 100 | 0.00061279 | 0.00001442 | 0.00002183 |
| 1000 | 0.06825250 | 0.00013858 | 0.00022954 |
| 10000 | 6.98823908 | 0.00176546 | 0.00243521 |
| 100000 | 1667.88195683 | 0.02953021 | 0.06166462 |

![[cdc32ab0-8360-4a2b-ba84-689b3f014c94.jpeg]]
