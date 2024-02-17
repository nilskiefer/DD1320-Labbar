Tänk igenom vilket attribut passar bäst (annars får man massor av konstiga siffror). Kolla tidskomplexiteten stämmer överens.

# Timeit-modulen i Python

## Parametrar i Timeit

- `stmt`: Representerar det uttalande som ska köras och tidtagas. Det är en sträng som innehåller Python-kod.

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
| -               | 10.2317               | 0.3785               | 0.0999                    |

# Sorteringsalgoritmer
Bubblesort tidskomplexitet: $O(n^2)$
Bogosort tidskomplexitet: $O(∞)$
| Liststorlek (n) | Bubble Sort Tid (s)   | BogoSort Tid (s)       |
|-----------------|-----------------------|------------------------|
| 10              | 2.3959e-05            | 7.25e-06               |
| 100             | 0.0018963             | 3.2417e-05             |
| 1000            | 0.18335               | 0.00034                |
| 10000           | 19.1982               | 0.02047                |

