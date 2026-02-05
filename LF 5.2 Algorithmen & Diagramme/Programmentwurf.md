>[!NOTE]
Jedes Programm, das mit Goto-Anweisungen geschrieben werden kann, kann mit einer Kombination aus Sequenzen, Verzweigungen und Schleifen realisiert werden. 
Satz von Böhm und Jacopini

Das heißt: Man braucht zunächst nur drei verschiedene Bausteine zum Programmieren. Deshalb: Schauen wir uns diese Bausteine an:
- (Sequenz)[#Sequenz]
- Verzweigung
- Schleife

## Sequenz

>[!NOTE]
>Programmbefehle, werden hintereinander weg (von oben nach unten) abgearbeitet

![EVA](/Bilder/Screenshot%202026-02-02%20121924_EVA.png)

>[!NOTE]
>Beispiel:
>Es soll eine durch den Nutzer eingegebene Zahl mit 1000 multipliziert werden. Anschließend wird diese Zahl um 1 erhöht, und wieder ausgegeben

### Pseudocode
```
Eingabe: Zahl
Zahl = Zahl * 1000 + 1
Ausgabe: Zahl
```

### "Minipseudo Programmierer"
```
var a = input("Gib eine Zahl ein!")
a = number(a)
a = a * 1000 + 1
output(a)
```

### Python
```
a = input("Gib eine Zahl ein!")
a = int(a) * 1000 + 1
print(a)
```

### C++
```
#include <iostream>
using namespace std;

int main() {
 int a;
 cout << "Gib eine Zahl ein!";
 cin >> a;
 a = a * 1000 + 1;
 cout << a;
 return 0;
```

## Verzweigung

![IF-Then-ELSE](/Bilder/Screenshot%202026-02-05%20060445.png)

## Schleifen

### Fußgesteuerte Schleife

![DO-WHILE](/Bilder/Screenshot%202026-02-02%20135938_Schleife.png)

!Bild(Schleifen)
