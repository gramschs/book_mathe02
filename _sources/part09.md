# Doppelintegral

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

Nachdem wir in den vorhergehenden Kapiteln Ableitungen von eindimensionalen Funktionen auf mehrdimensionale Funktionen verallgemeinert haben, werden wir in diesem Kapitel Integrale von Funktionen mit zwei Variablen betrachten.


## Lernziele

```{admonition} Lernziele
:class: tip
* Sie können erklären, was ein **Doppelintegral** $\iint_{A} f(x,y)\, dA$ ist.
* Sie können ein **Doppelintegral in kartesischen Koordinaten** berechnen, indem Sie zuerst die **innere Integration** und dann die **äußere Integration** durchführen.
* Sie können mit einem Doppelintegral den Flächeninhalt berechnen.
* Sie können mit dem Doppelintegral den Schwerpunkt $(x_S, y_S)$ einer homogenen ebenen Fläche mit den Formeln

$$x_S = \frac{1}{A}\iint_{A} x \, dA \quad \text{ und } \quad y_S = \frac{1}{A} \iint_{A} y\, dA$$

berechnen.
```


## Idee der Doppelintegrale

Bei eindimensionalen Funktionen entspricht das Integral $\int_{x_{min}}^{x_{max}} f(x)\, dx$ dem Flächeninhalt der Fläche $A$ (siehe Abbildung).


```{figure} pics/part09_integral1D.svg
---
width: 300px
name: fig_part09_integral1D
---
Integral entspricht dem Flächeninhalt

([Quelle:](https://commons.wikimedia.org/w/index.php?curid=1039841) "Wikimedia", Autor: 4C - Eigenes Werk, based on JPG version, Lizenz: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/))
```


Dementsprechend beschreibt das Doppelintegral einer Funktion von zwei Variablen das Volumen $V$, das zwischen der Fläche $B$ (B wie Boden oder Bereich) und der Fläche $f(x,y)$ entsteht, wobei die Punkte $(x,y)$ aus $B$ stammen.


```{figure} pics/part09_sketch_doubleintegral.svg
---
width: 600px
name: fig_part09_sketch_doubleintegral
---
Integral entspricht dem Volumen
```


Doppelintegrale haben vielfältige Anwendungen in den Ingenieurwissenschaften. Sie dienen u.a. zur Berechnung von 

* Flächeninhalt,
* Schwerpunkt einer Fläche und
* Flächenmoment.


## Definition Doppelintegral

Für die Berechnung des Volumens der Funktion $f(x,y)$ über einem Bereich $B$ gehen wir so vor, wie im eindimensionalen Fall bei der Berechnung des Flächeninhaltes einer eindimensionalen Funktion. Wir zerlegen den Bereich $B$ mit einem sogenannten **Gitter**, d.h. wir teilen den Bereich $B$ in viele kleine Teilbereiche ein, die wir mit $B_i$ durchnummerieren. Von jedem Teilbereich $B_i$ können wir die x- und y-Koordinate des Mittelpunkts bestimmen. Diese Koordinaten nennen wir $(x_i,y_i)$. 

Wenn die Teilbereiche rechteckig sind (das müssen sie nicht sein, wir könnten auch beispielsweise Kreise oder andere Muster nehmen), dann kann das Volumen der Säule $V_i$ (siehe Abbildung rote Säule) berechnet werden als

$$V_i = f(x_i,y_i) \cdot \Delta x \cdot \Delta y.$$


```{figure} pics/part09_sketch_volume.svg
---
width: 600px
name: fig_part09_sketch_volume
---
Volumen als Summe einzelner Säulen, hier mit rechteckigem Gitter
```


Jetzt müssen wir noch alle Säulen aufaddieren, um eine Annäherung für das Volumen zwischen Boden und Deckel $f(x,y)$ zu bekommen, also

$$V\approx f(x_1,y_1) \cdot \Delta y \cdot \Delta x + f(x_2,y_2) \cdot \Delta y \cdot \Delta x + \ldots f(x_N,y_N) \cdot \Delta y \cdot \Delta x.$$

Dabei haben wir jetzt angenommen, dass alle Teilbereiche $B_i$ die gleiche Form haben und als Rechtecke mit den Seitenlängen $\Delta x$ und $\Delta y$ beschrieben werden. Wir können das Summenzeichen verwenden:

$$V\approx \sum_{i=1}^{N} f(x_i,y_i) \cdot \Delta y \cdot \Delta x .$$

Wenn wir nun die Teilbereiche $B_i$ immer kleiner machen, so brauchen wir immer mehr Säulen, also $N\rightarrow\infty$. Falls der Grenzwert 

$$\lim_{N\rightarrow\infty} \sum_{i=1}^{N} f(x_i,y_i) \cdot \Delta y  \cdot \Delta x$$

existiert, nennen wir ihn Integral von $f(x,y)$ über $B$ und schreiben das als sogenanntes **Doppelintegral**

$$V = \iint_{B} f(x,y) \, dy \, dx.$$

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/7VjP3jEGW24
```

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/FtoHJaUR6T8
```

## Doppelintegral in kartesischen Koordinaten berechnen

Wie wird nun ein Doppelintegral konkret ausgerechnet? Glücklicherweise können wir die Berechnung des Doppelintegrals durch zwei "normale" Integrationen ersetzen. Die Voraussetzung dafür ist, dass wir ein [kartesisches Koordinatensystem](https://de.wikipedia.org/wiki/Kartesisches_Koordinatensystem) betrachten.

Zuerst brauchen wir eine Beschreibung der Fläche $B$, also des Bodens. Wenn man das Koordinatensystem von oben betrachtet, kann der Rand von $B$ durch zwei Funktionen beschrieben werden. Im einfachsten Fall besteht der obere und der untere Rand von $B$ nur aus Linien. Dann lautet die obere Funktion einfach nur $y=y_{\max}$ und die untere Funktion $y=y_{\min}$. Meist brauchen wir aber Funktionen zur Beschreibung des Randes.

**Schritt 1: Funktionen für den Rand von $B$ finden**

Wir nennen die obere Funktion $f_o(x)$ und die untere Funktion $f_u(x)$. Nun können wir das Doppelintegral $\iint_{B}f(x,y)\, dB$ durch zwei Integrale ersetzen:

$$\iint_{B}f(x,y)\, dB = \int_{x=a}^{x=b} \int_{y=f_u(x)}^{y=f_o(x)} f(x,y)\, dy \, dx.$$

**Schritt 2: innere Integration (nach y)**

Zuerst behandeln wir die Variable $x$ als eine Konstante. Dann wird die Funktion $f(x,y)$ nach $y$ integriert. In die Stammfunktion setzt man dann als obere Grenze die obere Funktion $f_o(x)$ ein und als untere Grenze die untere Funktion $f_u(x)$. Dadurch ist das Ergebnis der Integration wieder eine Funktion.

**Schritt 3: äußere Integration (nach x)**

Die in Schritt 2 entstandene Funktion wird wieder integriert, aber diesmal nach $x$. Diesmal setzen wir in die Stammfunktion die obere Grenze $b$ und die untere Grenze $a$ ein, so dass diesmal wirklich eine Zahl herauskommt.

In den folgenden Videos sehen Sie drei Beispiele: 

1. rechteckiger Bereich
2. allgemeine Vorgehensweise
3. Beispiel für nicht-rechteckige Bereiche

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/l_Fg_tDqx2E
```

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/ZesBkRCLLPY
```

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/gh5_lifDH48
```

## Anwendungen von Doppelintegralen

Der Flächeninhalt kann mit der Formel

$$A = \iint_{B} 1 \, dB = \int_{x=a}^{x=b} \int_{y=f_u(x)}^{y=f_o(x)} 1 \, dy \, dx.$$ 

berechnet werden, also $f(x,y)=1$.


Für den Schwerpunkt einer ebenen homogenen Fläche erhalten wir für die x-Koordinate die folgende Formel

$$x_S = \frac{1}{A} \int_{x=a}^{x=b} \int_{y=f_u(x)}^{y=f_o(x)} x \, dy \, dx$$ 

und für die y-Koordinate des Schwerpunkts

$$y_S = \frac{1}{A} \int_{x=a}^{x=b} \int_{y=f_u(x)}^{y=f_o(x)} y \, dy \, dx.$$ 
