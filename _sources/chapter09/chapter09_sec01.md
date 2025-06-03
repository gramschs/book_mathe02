# 9.1 Idee von Doppelintegralen

Nachdem wir in den vorhergehenden Kapiteln Ableitungen von eindimensionalen
Funktionen auf mehrdimensionale Funktionen verallgemeinert haben, werden wir in
diesem Kapitel Integrale von Funktionen mit zwei Variablen betrachten, also von
Funktionen $f:\mathbb{R}^2\to\mathbb{R}$. Dieses sogenannte Doppelintegral hat
in der Technischen Mechanik viele Anwendungen und wird insbesondere bei
Schwerpunktsberechnungen gebraucht.

## Lernziele

```{admonition} Lernziele
:class: goals
Sie können erklären, was ein **Doppelintegral** $\iint_{A} f(x,y)\, dA$ ist und unter welchen Voraussetzungen es existiert.
```

## Grundkonzept

Bei eindimensionalen Funktionen entspricht das Integral $\int_{a}^{b} f(x)\, dx$
dem Flächeninhalt der Fläche $A$ (siehe Abbildung).

```{figure} pics/part10_integral1D.svg
---
width: 300px
name: fig_part10_integral1D
---
Integral entspricht dem Flächeninhalt

([Quelle:](https://commons.wikimedia.org/w/index.php?curid=1039841) "Wikimedia", Autor: 4C - Eigenes Werk, based on JPG version, Lizenz: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/))
```

Dementsprechend beschreibt das Doppelintegral einer Funktion von zwei Variablen
das Volumen $V$, das zwischen dem Integrationsbereich $A$ (dem „Boden") und dem
Funktionsgraphen von $f(x,y)$ (der „Decke") entsteht. Dabei stammen die Punkte
$(x,y)$ aus dem Bereich $A$.

In der folgenden interaktiven Demonstration wird das Rechteck $A = [-2,2] \times
[-4,4]$ als Definitionsgebiet bzw. Integrationsbereich verwendet. Sie können
zwischen vier verschiedenen Funktionen wählen. Das Volumen zwischen der Fläche,
die durch $f(x,y)$ und der xy-Ebene erzeugt wird, ist hellblau eingefärbt.

<iframe src="https://gramschs.github.io/book_mathe02/_static/assets/doppelintegral_volumen.html"
width=100% height="600" frameborder="0" scrolling="yes"></iframe>

Doppelintegrale haben aber nicht nur die geometrische Anwendungen der
Volumenberechnung, sondern mit Doppelintegralen werden u.a. auch

* Flächeninhalte,
* Schwerpunkte einer Fläche und
* Flächenmomente

berechnet.

## Definition Doppelintegral

Für die Berechnung des Volumens der Funktion $f(x,y)$ über einem Bereich $A$
gehen wir so vor, wie im eindimensionalen Fall bei der Berechnung des
Flächeninhaltes einer eindimensionalen Funktion. Wir zerlegen den Bereich $A$
mit einem sogenannten **Gitter**, d.h. wir teilen den Bereich $A$ in viele
kleine Teilbereiche ein, die wir mit $A_i$ durchnummerieren. Von jedem
Teilbereich $A_i$ können wir die x- und y-Koordinate des Mittelpunkts bestimmen.
Diese Koordinaten nennen wir $(x_i,y_i)$.

Wenn die Teilbereiche rechteckig sind (das müssen sie nicht sein, wir könnten
auch beispielsweise andere geometrische Formen verwenden), dann kann das Volumen der
Säule $V_i$ (siehe Abbildung rote Säule) berechnet werden als

$$V_i = f(x_i,y_i) \cdot \Delta x \cdot \Delta y.$$

```{figure} pics/part10_sketch_volume.svg
---
width: 600px
name: fig_part10_sketch_volume
---
Volumen als Summe einzelner Säulen, hier mit rechteckigem Gitter
```

Jetzt müssen wir noch alle Säulen aufaddieren, um eine Annäherung für das
Volumen zwischen dem Integrationsbereich und dem Funktionsgraphen $f(x,y)$ zu
bekommen, also

$$V\approx f(x_1,y_1) \cdot \Delta x \cdot \Delta y + f(x_2,y_2) \cdot \Delta x
\cdot \Delta y + \ldots + f(x_N,y_N) \cdot \Delta x \cdot \Delta y.$$

Dabei haben wir jetzt angenommen, dass alle Teilbereiche $A_i$ die gleiche Form
haben und als Rechtecke mit den Seitenlängen $\Delta x$ und $\Delta y$
beschrieben werden. Wir können das Summenzeichen verwenden:

$$V\approx \sum_{i=1}^{N} f(x_i,y_i) \cdot \Delta x \cdot \Delta y .$$

Wenn wir nun die Teilbereiche $A_i$ immer kleiner machen, so brauchen wir immer
mehr Säulen, also $N\rightarrow\infty$. Falls der Grenzwert

$$\lim_{N\rightarrow\infty} \sum_{i=1}^{N} f(x_i,y_i) \cdot \Delta x  \cdot
\Delta y$$

existiert, nennen wir ihn Integral von $f(x,y)$ über $A$ und schreiben das als
sogenanntes **Doppelintegral**

$$V = \iint_{A} f(x,y) \, dx \, dy.$$

Bei den obigen Überlegungen sind wir davon ausgegangen, dass der Bereich $A$ in
rechteckige Teilbereiche $A_i$ aufgeteilt wird. Das muss nicht so sein, wir
hätten auch andere Aufteilungen wählen können. Daher ist die allgemein
formulierte Definition eines Doppelintegrals wie folgt:

```{admonition} Was ist ... ein Doppelintegral?
:class: note
Doppelintegrale sind Integrale für zweidimensionale Funktionen
$f:\mathbb{R}^2\to\mathbb{R}$ mit einer Definitionsmenge $A \subset
\mathbb{R}^2$. Die Definitionsmenge $A$ wird in $N$ Teilgebiete zerlegt, die
$A_i$ genannt werden. Der Flächeninhalt dieser Teilgebiete wird mit $\Delta A_i$
bezeichnet. Wenn der Grenzwert

$$\lim_{N\rightarrow\infty} \sum_{i=1}^{N} f(x_i,y_i) \cdot \Delta A_i$$

existiert, wird er als Doppelintegral von $f$ über $A$ bezeichnet und mit

$$\iint_{A} f(x,y)\, dA$$

abgekürzt.
```

Das Doppelintegral existiert insbesondere dann, wenn die Funktion $f(x,y)$ über
dem Bereich $A$ stetig ist und $A$ ein messbarer Bereich ist (z.B. ein Rechteck,
Kreis oder allgemein ein Bereich mit stückweise glatter Berandung).

Im folgenden Video wird das Grundkonzept des Doppelintegrals erklärt. Im
nachfolgenden Video wird die geometrische Interpretation des Doppelintegrals zur
Berechnung eines Volumens präsentiert.

```{dropdown} Video zu "Doppelintegral - Definition" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/7VjP3jEGW24"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Doppelintegral - Volumeninterpretation" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/FtoHJaUR6T8"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
