# Aussagenlogik

Aussagenlogik ist etwas, was uns nicht nur in der Informatik und auch der Mathematik begegnet. Tatsächlich bildet auch eine wichtige Grundlage für unser tägliches Leben. 
Was man darunter versteht, ist die Verkettung von Aussagen, mit unterschiedlichem Wahrheitsgehalt.

Aussagen könnten zum Beispiel sein:

- Es regnet -> Aussage **A**
- Ich habe keinen Schirm -> Aussage **B**
- Ich werde nass -> Aussage **C**

Diese Drei Aussagen können unabhängig voneinander entweder Wahr oder Falsch sein. Spannend wird es nun, wenn wir anfangen, sie zu verknüpfen, zum Beispiel:

Wenn es regnet **UND** ich keinen Schirm habe, werde ich nass
`oder anders:`
Wenn A **UND**  B dann C 

Es gibt also Operatoren, mit denen wir Aussagen verbinden und sogar "rechnen" können. Die grundlegenden Operatoren sind:

- AND -> genau dann wenn sowohl A, **und** B Wahr sind, ist auch C wahr
- OR   -> wenn entweder A **oder** B, **oder beide** wahr sind, dann C
- XOR -> wenn entweder A **oder** B, aber **nicht beide** wahr sind, dann C 
- NOT -> nicht A

Nun ergibt es in der Informatik eher selten Sinn, darüber zu sprechen, ob man nass wird, wenn es regnet. Betrachtet man Computerkomponenten allerdings, sieht das anders aus. Es lässt sich Beispielsweise eine Schaltung bauen, die folgendes macht:

Eine Lampe (L) ist mit zwei Schaltern (A und B) verbunden und soll nur leuchten, wenn nur und genau einer der beiden betätigt wird.
Also, wenn **entweder** Schalter A **oder** Schalter B an sind, dann leuchtet die Lampe L
Oder: `L = A XOR B` 

Das klingt vielleicht abstrakt, aber genau das macht ein Lichtschalter über dem Bett, der die Deckenlampe aus macht, damit man nicht aufstehen und zur Tür laufen muss.

Für die Informatik ist das in sofern wichtig, dass jeder logische Operator, durch ein entsprechendes Bauteil realisiert ist. Man spricht hier von sogenannten **Gattern**.  Das funktioniert, weil unsere Digitaltechnik nach genau dem gleichen Prinzip funktioniert. Ein Signal ist entweder 1 bzw. Wahr, oder eben 0 bzw. Falsch.

![Beispiel Logik-Gatter](/Bilder/TexasInstruments_7400_chip%2C_view_and_element_placement.jpg)

## Zeichensatz:

- True / Wahr / 1
- False / Falsch / 0

## Logiktabellen:

|A	|B 	|AND	|OR		|XOR	|
|---|---|-------|-------|-------|
|0	|0	|0		|0		|0		|
|0	|1	|0		|1		|1		|
|1	|0	|0		|1		|1		|
|1	|1	|1		|1		|0		|

### `NOT` invertiert die EIngabe:
- `A = 0` 	->		`NOT(A) = 1`
- `A = 1`	->		`NOT(A) = 0`


