## Operatoren in der Programmierung

### Einführung

Programmiersprachen haben im Allgemeinen Operatoren. Das sind bestimmte Zeichen, die dem Computer eine Anweisung geben.
Das wohl einfachste Beispiel ist "-", das Minus-Zeichen. Das gibt dem Computer das Signal: hier wird gerechnet - und zwar Subtrahiert.

Warum ist "-" einfacher als "+"?
Weil "+" mehrfach belegt ist - es hat also, je nach Umstand, mehrere Bedeutungen.
Für Zahlen gilt: "+" bedeutet Addition! Es wird also gerechnet.
Sobald aber mindestens einer der Operanden, also der Werte, die links und rechts vom Operator stehen, keine Zahl ist - dann ändert sich die Bedeutung des "+".
Wenn man also mit Zeichenfolgen (auch: Strings, wie etwa "abc" oder "Hallo!") arbeitet, dann bedeutet das "+": Diese Zeichenfolgen werden aneinandergehängt!
Man nennt dieses "aneinanderhängen" auch "Konkatenation".

### Liste bisher behandelter Operatoren

| Operator | Bedeutung                                                                 |
|:--------:|---------------------------------------------------------------------------|
| **`+`**  | bei Zahlen: Addition. **Bei Zeichen: Konkatenation**                      |
| `-`      | Subtraktion                                                               |
| `*`      | Multiplikation                                                            |
| `/`      | Division                                                                  |
| **`%`**  | **Modulo: gibt den Rest einer Division.** (Bsp.: 5%2 ergibt 1)            |
| `=`      | Zuweisung: der Wert RECHTS vom Zeichen wird im Wert LINKS gespeichtert.   |
| `==`     | Vergleich: Gibt einen Wahrheitswert wieder, ob die Werte gleich sind.     |
| `<`      | Kleiner Als: Gibt Wahrheitswert                                           |
| `<=`     | Kleiner Gleich                                                            |
| `>`      | Größer Als                                                                |
| `>=`     | Größer Gleich                                                             |
| `&&`     | Logisches UND: Gibt TRUE wieder, wenn beide Werte TRUE sind               |
| `\|\|`   | Logisches ODER: Gibt TRUE wieder, wenn mindest. einer der Werte TRUE ist. |
