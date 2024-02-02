# Binärträd Förklaringar

## 1. Rita och Berätta Hur Binärträdet Byggs Upp
Ett binärträd är en datastruktur som består av noder, där varje nod har upp till två barn. Här är de grundläggande koncepten:
- **Rotnod**: Överst i trädet finns rotnoden.
- **Barn**: Varje nod i trädet kan ha en vänster och en höger barnnod.
- **Binära Sökträd**: Används ofta som binära sökträd där varje nod innehåller ett nyckelvärde. För varje nod är alla värden i dess vänstra underträd mindre än nodens värde, och alla värden i dess högra underträd är större.
- **Tillägg av Noder**: Vid tillägg av en ny nod, jämförs dess värde med rotnodens värde och placeras därefter lämpligt i vänster eller höger underträd.

## 2. Visa Hur Du Testat Din Klass för Binära Träd
För att säkerställa att en klass för binära träd fungerar korrekt, bör du utföra enhetstester:
- **Grundläggande Operationer**: Testa lägga till, söka, och ta bort element.
- **Edge-Cases**: Inkludera tester för tomma träd, träd med en nod, och träd med många noder.
- **Balanseringstester**: Om trädklassen stöder balansering, testa för att säkerställa effektivitet i operationer.

## 3. Förklara Varför Det Går Snabbt Att Söka i Ett Binärträd
Sökning i binära träd är effektiv tack vare deras struktur:
- **Halvering Vid Sökning**: Med varje jämförelse kan man utesluta halva trädet, vilket gör sökprocessen snabb.
- **Tidskomplexitet**: För ett välbalanserat träd är söktiden $O(\log n)$ där n är antalet noder.
- **Förutsättning**: Effektiviteten beror på att trädet är välbalanserat.

## 4. Förklara Idén Bakom Att Ha `put` Som Anropar `putta`
Denna designmetod används för att förenkla användandet av en klass:
- **Abstraktion och Kapsling**: Användaren interagerar med den enklare `put` metoden, medan `putta` innehåller den faktiska logiken.
- **Modularitet och Underhåll**: Separationen av gränssnitt (`put`) och implementering (`putta`) gör koden mer modulär och lättare att underhålla.
