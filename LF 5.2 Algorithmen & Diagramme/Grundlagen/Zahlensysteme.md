[zurück](/README.md)
# Zahlensysteme

## Dezimalsystem

Wir alle wissen, wie Zahlen funktionieren, oder tun wir das? Kaum einer macht sich wirklich darüber Gedanken, wie unsere Dezimalzahlen eigentlich arbeiten.
Ein guter Vergleich sind römische Zahlen, die ein kompliziertes System von Zeichen und Rechenregeln beinhalten. Anders unser System.
Im Dezimalsystem arbeiten wir mit Stellen, die jeweils ein Vielfaches der entsprechenden 10er-Potenz darstellen.

>[!NOTE]
Zeichensatz: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`
Basis: `10`

Klingt kompliziert? Ist es eigentlich gar nicht. Folgende Tabelle wird es verdeutlichen:

Gegeben ist die Zahl: `123`

Jede Ziffer stellt einen Faktor dar, der mit der entsprechenden Potenz der Basis *(im Dezimalsystem `10`)* multipliziert wird.

| $10^2$ = 100 | $10^1$ = 10 | $10^0$ = 1 |
| :----------: | :---------: | :--------: |
|      1       |      2      |     3      |
| $1*100 =100$ |  $2*10=20$  |  $3*1=3$   |

$$
1 * 10^2 + 2* 10^1 + 3 * 10^0 = 1 * 100 + 2 * 10 + 3 * 1  = 100 + 20 + 3 = 123
$$
## Dualsystem

Nachdem wir das nun wissen, ist der Sprung zum Dualsystem gar nicht mehr schwer, das funktioniert nämlich genauso. Genau genommen gibt es nur zwei Unterschiede:

>[!NOTE]
 Zeichensatz: `0` und `1`
 Basis: `2`
 
Auch damit kann man wieder eine ähnliche Tabelle erstellen, wie im Dezimalsystem.

Gegeben ist die Zahl: `1011`


| $2^3$ = 8 | $2^2$ = 4 | $2^1$ = 2 | $2^0$ = 1 |
| --------- | --------- | --------- | --------- |
| 1         | 0         | 1         | 1         |
| $1*8 = 8$ | $0*4=0$   | $1*2=2$   | $1*1=1$   |

$$
1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0 = 1 * 8 + 0 * 4 + 1 * 2 + 1 * 1 = 11
$$

## Hexadezimal-System

Die dritte gerade auch in der IT verbreitete Darstellungsform von Zahlen, sind Hexadezimal-Zahlen. Insbesondere für **(Speicher-)Adressen**, **IPv6**, sowie **Farbwertcodierung**, kommen diese zum Einsatz.

>[!NOTE]
>Zeichensatz: `0`, `1` `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `A`, `B`, `C`, `D`, `E`, `F`
>Basis: `16`

Gegeben ist die Zahl: `x3B8`

| $16^2$ = 256 | $16^1$ = 16 | $16^0$ = 1 |
| ------------ | ----------- | ---------- |
| 3            | B (=11)     | 8          |
| $3*256=768$  | $11*16=176$ | $8*1=8$    |

$$
3 * 16^2 + 11 * 16^1 + 8 * 16^0 = 3 * 256 + 11 * 16 + 8 * 1 = 952
$$
