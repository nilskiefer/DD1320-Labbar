### Förberedlseuppgifter
##### Rita upp en graf, och skriv upp grannmatris samt grannlista för följande ord: tre öre tri tro trå trä Grafen ska ha kanter (oviktade, oriktade) mellan de ord som bara skiljer sig åt i en bokstav. 
**Första Grafen (Ordnätverk för 'tre', 'öre', 'tri', 'tro', 'trå', 'trä')**
*Antal noder:* 6
*Antal kanter:* 11
*Andel av grannmatrisen som är fylld:* 61.11%
*Grannmatrisen:*
$$
\begin{pmatrix}
0 & 1 & 1 & 1 & 1 & 1 \\
1 & 0 & 0 & 0 & 0 & 0 \\
1 & 0 & 0 & 1 & 1 & 1 \\
1 & 0 & 1 & 0 & 1 & 1 \\
1 & 0 & 1 & 1 & 0 & 1 \\
1 & 0 & 1 & 1 & 1 & 0
\end{pmatrix}
$$
*Grannlista:*
- 'tre': ['öre', 'tri', 'tro', 'trå', 'trä']
- 'öre': ['tre']
- 'tri': ['tre', 'tro', 'trå', 'trä']
- 'tro': ['tre', 'tri', 'trå', 'trä']
- 'trå': ['tre', 'tri', 'tro', 'trä']
- 'trä': ['tre', 'tri', 'tro', 'trå']
![[Pasted image 20240202015009.png]]
##### Rita upp en graf med riktade kanter (bestäm riktningar själv), och skriv upp grannmatris samt grannlista för följande ord: arg ärg agg alg ark arm art arv.
*Antal noder:* 8
*Andel av grannmatrisen som är fylld:* 12.5%
*Finns det cykler i grafen?* Ja
*Grannmatrisen:*
$$
\begin{pmatrix}
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
$$
*Grannlista:*
- 'arg': ['ärg']
- 'ärg': ['agg']
- 'agg': ['alg']
- 'alg': ['ark']
- 'ark': ['arm']
- 'arm': ['art']
- 'art': ['arv']
- 'arv': ['arg']
![[Pasted image 20240202015316.png]]
### Varför Används en Kö i Bredden-först-sökning?
En kö används i bredden-först-sökning (BFS) av flera anledningar:
1. **Systematisk Utforskning:** BFS utforskar grafen nivå för nivå. En kö hjälper till att hålla reda på vilken nod som ska utforskas härnäst, vilket säkerställer att alla noder på en viss nivå utforskas innan man går vidare till nästa nivå.
2. **FIFO (First-In-First-Out) Princip:** Kön följer FIFO-principen, vilket är idealiskt för BFS eftersom det säkerställer att noder utforskas i den ordning de upptäcktes.
### Varför Ger Bredden-först-sökning den Kortaste Lösningen?
Bredden-först-sökning är känd för att ge den kortaste lösningen i termer av antalet kanter från startnoden till målnoden på grund av följande skäl:
1. **Nivåvis Utforskning:** Eftersom BFS utforskar alla noder på en viss nivå innan den går vidare till nästa, garanteras det att den kortaste vägen hittas först om den finns.
2. **Förhindrar Omvägar:** BFS lägger inte till noder i kön som redan har utforskats eller som står i kön för att utforskas, vilket förhindrar omvägar och onödig utforskning av längre vägar.

