Tänk igenom vilket attribut passar bäst (annars får man massor av konstiga siffror). Kolla tidskomplexiteten stämmer överens.

# Timeit-modulen i Python

## Parametrar i Timeit

- `stmt`: Representerar det uttalande som ska köras och tidtagas. Det är en sträng som innehåller Python-kod.

- `number`: Anger hur många gånger `stmt` ska exekveras. Det är ett heltal som standardinställs till 1000000.

## Vad Timeit Tar Tid På

Timeit mäter exekveringstiden för koden specificerad i `stmt` över antalet iterationer angivet av `number`.

## Utskrift från Timeit

Timeit skriver ut totala exekveringstiden (i sekunder) för koden i `stmt` över de `number` antal iterationer som utförts.


| Liststorlek (n) | Linjärsökningstid (s) | Binärsökningstid (s) | Hashtabellsökningstid (s) |
|-----------------|-----------------------|----------------------|---------------------------|
| 250 000         | 0.3032                | 0.0225               | 0.0010                    |
| 500 000         | 0.3020                | 0.0274               | 0.0010                    |
| 1 000 000       | 0.2974                | 0.0258               | 0.0011                    |
| -       | 0.2984                | 0.0256               | 0.0011                    |
