>[!NOTE]
Jedes Programm, das mit Goto-Anweisungen geschrieben werden kann, kann mit einer Kombination aus Sequenzen, Verzweigungen und Schleifen realisiert werden. 
Satz von Böhm und Jacopini

Das heißt: Man braucht zunächst nur drei verschiedene Bausteine zum Programmieren. Deshalb: Schauen wir uns diese Bausteine an:
- Sequenz
- Verzweigung
- Schleife

## Sequenz

>[!NOTE]
>Programmbefehle, werden hintereinander weg (von oben nach unten) abgearbeitet

![EVA](/Bilder/Screenshot%202026-02-02%20121924_EVA.png)

Beispiel:


| Pseudocode                                               | "Minipseudo Programmierer"<br>(Herr Grätzer)                                                  | Python                                                                     | C++                                                                                                                                                                                                            |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Eingabe: Zahl<br>Zahl = Zahl * 1000 + 1<br>Ausgabe: Zahl | `var a = input("Gib eine Zahl ein!")`<br>`a = number(a)`<br>`a = a * 1000 + 1`<br>`output(a)` | `a = input("Gib eine Zahl ein!")`<br>`a = int(a) * 1000 + 1`<br>`print(a)` | ```#include <iostream><br>using namespace std;<br><br>int main() {<br>int a;<br>    cout << "Gib eine Zahl ein!";<br>    cin >> a;<br>    a = a * 1000 + 1;<br>    cout << a;<br>    return 0;<br>}<br><br>``` |
|                                                          |                                                                                               |                                                                            |                                                                                                                                                                                                                |

## Verzweigung

![IF-Then-ELSE](/Bilder/Screenshot%202026-02-05%20060445.png)

## Schleifen

### Fußgesteuerte Schleife

![DO-WHILE](/Bilder/Screenshot%202026-02-02%20135938_Schleife.png)

!Bild(Schleifen)
