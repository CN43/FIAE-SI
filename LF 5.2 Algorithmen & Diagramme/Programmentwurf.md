>[!NOTE]
Jedes Programm*, das mit Goto-Anweisungen geschrieben werden kann,* kann mit einer **Kombination aus Sequenzen, Verzweigungen und Schleifen** realisiert werden. 
Satz von Böhm und Jacopini

Programme bestehen damit aus Anweisungen, die in einer Kombination von Sequenzen, Verzweigungen und Schleifen angeordnet sind.

Das heißt: Man braucht zunächst nur drei verschiedene Bausteine zum Programmieren. 
Schauen wir uns diese Bausteine an:
- [Sequenz](#Sequenz)
- [Verzweigung](#Verzweigung)
- [Schleife](#Schleife)

## Sequenz

>[!NOTE]
>Programmbefehle, werden hintereinander (von oben nach unten) abgearbeitet

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

>[!NOTE]
>Programmbefehle oder Befehlsblöcke, werden nur ausgeführt, wenn eine definierte Bedingung erfüllt wird.

![IF-Then-ELSE](/Bilder/Screenshot%202026-02-05%20060445.png)

>[!NOTE]
>Beispiel: Ich brauche meinen Schirm nur, wenn es regnet. Regnet es nicht, brauche ich auch keinen Schirm.

### Pseudocode
```
Eingabe: Regnet es?
Wenn ja:
Ausgabe: Du brauchst einen Schirm
Ansonsten:
Ausgabe: Du brauchst keinen Schirm
```

### "Minipseudo Programmierer"
```
var regen = input("Regnet es?")
if(regen == "ja"){
	output("Du brauchst einen Schrim")
} else if(regen="nein"){
	output("Du brauchst keinen Schirm")
}
```

### Python
```
regen = input("Regnet es?")
if (regen == "ja"):
	print("Du brauchst einen Schirm")
else:
	Print("Du brauchst keinen Schirm")
```

### C++
```
#include <iostream>
#include <string>

int main() {
    string regen;

    cout << "Regnet es? ";
    cin >> regen;

    if (regen == "ja") {
        cout << "Du brauchst einen Schirm" << std::endl;
    } else {
        cout << "Du brauchst keinen Schirm" << std::endl;
    }

    return 0;
}

```

## Schleifen

### Fußgesteuerte Schleife

![DO-WHILE](/Bilder/Screenshot%202026-02-02%20135938_Schleife.png)


