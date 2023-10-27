# Python-uppgifter

Ni kan använda https://python.microbit.org/v/3 för att programmera. 


## Problem 1: LED-mönster

### Uppgiftsbeskrivning:
Skapa ett mönster av LED-lampor som rör sig från den vänstra kolumnen till den högra kolumnen på micro:bitens display.


### Steg:
* Initiera programmet: Importera microbit-biblioteket.
* Starta loopen: Skapa en oändlig loop med while True:
* Skapa mönstret: Använd nästlade loopar för att iterera genom varje kolumn och tända LED-lamporna.
* Rensa displayen: Rensa displayen innan du går vidare till nästa kolumn.
* Pausa: Lägg till en kort fördröjning mellan varje mönsterförskjutning.



## Problem 2: Knappsekvens

### Uppgiftsbeskrivning:
Tryck på knapp A och B i en valfri sekvens för att visa ett leende ansikte/lösenord på micro:bitens display.


### Steg:
* Initiera programmet: Importera microbit-biblioteket och initiera en tom lista som kallas sequence.
* Starta loopen: Skapa en oändlig loop med while True:.
* Knapptryckningar: Kontrollera om knapp A eller B är tryckt och lägg till knappetiketten i sequence.
* Kontrollera sekvensen: Om sekvensen matchar mönstret, visa ett leende ansikte.
* Återställ: Rensa sekvensen och displayen.



## Problem 3: Temperaturvarning

### Uppgiftsbeskrivning:
Visa en varning om temperaturen går över 30°C eller under 10°C.


### Steg:
* Initiera programmet: Importera microbit-biblioteket.
* Starta loopen: Skapa en oändlig loop med while True:.
* Mät temperaturen: Använd temperature() för att få den aktuella temperaturen.
* Kontrollera temperaturen: Visa en varning baserat på temperaturområdet.
* Pausa: Lägg till en fördröjning innan nästa avläsning.



## Problem 4: Sten, sax, påse-spel

### Uppgiftsbeskrivning:
Skapa ett "Sten, sax, påse"-spel där knapp A representerar sten, knapp B representerar sax, och skakning av micro:bit representerar påse. Spelet ska slumpmässigt välja en av dessa tre och jämföra med användarens val, sedan visa om användaren vann, förlorade eller om det blev oavgjort.


### Steg:
* Initiera programmet: Importera microbit-biblioteket och initiera variabler för att hålla reda på användarens och datorns val.
* Starta loopen: Skapa en oändlig loop med while True:.
* Användarens val: Använd knapp A för sten, knapp B för sax, och skakning för påse. Spara användarens val.
* Datorns val: Använd en slumpmässig generator för att låta datorn välja sten, sax eller påse.
* Jämför valen: Jämför användarens och datorns val och avgör vem som vinner.
* Visa resultatet: Visa en lämplig bild eller text för att indikera om användaren vann, förlorade eller om det blev oavgjort.
* Återställ: Rensa displayen och förbered för nästa omgång.



## Problem 5. Sten, Sax, Påse mellan två micro:bits

### Uppgiftsbeskrivning:
Skapa ett "Sten, sax, påse"-spel där två micro:bits kan spela mot varandra. Knapp A ska representera sten, knapp B ska representera sax, och en skakning av micro:biten ska representera påse. Varje micro:bit ska kunna skicka sitt val till den andra micro:biten och visa om användaren vann, förlorade eller om det blev oavgjort.


Du kan modifiera ditt program från uppgift 4 eller börja på nytt


### Steg:
* Initiera programmet: Importera microbit- och radio-biblioteken. Ställ in en radiokanal för kommunikation mellan de två micro:bitsen.
* Starta loopen: Skapa en oändlig loop med while True:.
* Användarens val: Använd knapp A för sten, knapp B för sax, och skakning för påse. Skicka användarens val till den andra micro:biten via radio.
* Motståndarens val: Ta emot det inkommande valet från den andra micro:biten via radio.
* Bekräftelse: Skicka en bekräftelse ('ack') till den andra micro:biten för att bekräfta att meddelandet har mottagits.
* Jämför valen: Jämför användarens och motståndarens val och avgör vem som vinner.
* Visa resultatet: Visa en lämplig bild eller text för att indikera om användaren vann, förlorade eller om det blev oavgjort.
* Återställ: Rensa displayen och förbered för nästa omgång.