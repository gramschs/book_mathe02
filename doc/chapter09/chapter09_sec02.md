# 9.2 Berechnung von Doppelintegralen in kartesischen Koordinaten

Die Grenzwertbildung zur Berechnung eines Integrals ist mühsam. In vielen Fällen
kann die Berechnung des Doppelintegrals durch eine Berechnung von zwei einzelnen
Integralen ersetzt werden. Dabei kommt es darauf an, welches Koordinatensystem
verwendet wird. In diesem Kapitel geht es um die Berechnung des Doppelintegrals
in kartesischen Koordinaten.

## Lernziele

```{admonition} Lernziele
:class: goals
Sie können ein **Doppelintegral in kartesischen Koordinaten** berechnen, indem Sie zuerst die **innere Integration** und dann die **äußere Integration** durchführen:

$$\iint_{A}f(x,y)\, dA = \int_{x=a}^{x=b} \left( \int_{y=f_u(x)}^{y=f_o(x)} f(x,y)\, dy\right)dx.$$

```

## Doppelintegral in kartesischen Koordinaten berechnen

Wie wird nun ein Doppelintegral konkret ausgerechnet? Glücklicherweise können
wir die Berechnung des Doppelintegrals durch zwei "normale" Integrationen
ersetzen. Die Voraussetzung dafür ist, dass wir ein [kartesisches
Koordinatensystem](https://de.wikipedia.org/wiki/Kartesisches_Koordinatensystem)
betrachten.

Zuerst brauchen wir eine Beschreibung der Fläche $A$, also des Bodens. Wenn man
das Koordinatensystem von oben betrachtet, kann der Rand von $A$ durch zwei
Funktionen beschrieben werden. Im einfachsten Fall besteht der obere und der
untere Rand von $A$ nur aus Linien. Dann lautet die obere Funktion einfach nur
$y=y_{\max}$ und die untere Funktion $y=y_{\min}$. Meist brauchen wir aber
Funktionen zur Beschreibung des Randes.

**Schritt 1: Funktionen für den Rand von $A$ finden**

Wir nennen die obere Funktion $f_o(x)$ und die untere Funktion $f_u(x)$. Nun
können wir das Doppelintegral $\iint_{A}f(x,y)\, dA$ durch zwei Integrale
ersetzen:

$$\iint_{A}f(x,y)\, dA = \int_{x=a}^{x=b} \int_{y=f_u(x)}^{y=f_o(x)} f(x,y)\, dy
\, dx.$$

**Schritt 2: innere Integration (nach y)**

Zuerst behandeln wir die Variable $x$ als eine Konstante. Dann wird die Funktion
$f(x,y)$ nach $y$ integriert. In die Stammfunktion setzt man dann als obere
Grenze die obere Funktion $f_o(x)$ ein und als untere Grenze die untere Funktion
$f_u(x)$. Dadurch ist das Ergebnis der Integration wieder eine Funktion.

**Schritt 3: äußere Integration (nach x)**

Die in Schritt 2 entstandene Funktion wird wieder integriert, aber diesmal nach
$x$. Diesmal setzen wir in die Stammfunktion die obere Grenze $b$ und die untere
Grenze $a$ ein, so dass diesmal wirklich eine Zahl herauskommt.

```{dropdown} Video zu "Doppenintegral, kein Rechteck" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/ZesBkRCLLPY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Beispiel: A ist ein Rechteck

Als erstes Beispiel berechnen wir das Doppelintegral der Funktion $f(x,y) = xy$
über dem Rechteck $A = [0, 1] \times [1, 2]$. Die Grenzen der Integration für $x$
sind $0$ und $1$.

**Schritt 1: obere und untere Funktion finden**

Das Rechteck wird oben durch die Konstante 2 berandet und unten durch die
Konstante 1. Also sind die obere und die untere Funktion

\begin{align*}
f_o(x) &= 2 \\
f_u(x) &= 1 \\
\end{align*}

```{figure} pics/part10_plot_example01.svg
---
width: 75%
name: part10_plot_example01
---
Draufsicht auf das Integrationsgebiet $A =  [0, 1] \times [1, 2]$
```

Das Doppelintegral lautet also:

$$\iint_{A}f(x,y)\, dA = \int_{x=0}^{x=1} \left( \int_{y=1}^{y=2} xy \, dy
\right) \, dx.$$

**Schritt 2: innere Integration (nach y)**

Das innere Integral $I(x)$ wird berechnet, indem nach $y$ integriert wird:

\begin{align*}
I(x) &= \int_{y=1}^{y=2} xy \, dy = \\
     &= \left[ x \cdot \frac{1}{2}y^2 \right]_{y=1}^{y=2} = \\
     &= x\cdot \frac{1}{2}2^2 - x\cdot \frac{1}{2}1^2 = \\
     &= \frac{3}{2}x.\\
\end{align*}

**Schritt 3: äußere Integration (nach x)**

Das innere Integral $I(x) = \frac{3}{2}x$ wird nun in das äußere Integral
eingesetzt und nach $x$ integriert:

$$\int_{x=0}^{x=1} \frac{3}{2}x \, dx = \left[ \frac{3}{4}x^2\right] =
\frac{3}{4}.$$

Damit lautet das Doppelintegral von $f$ über $A$ mit $f(x,y)=xy$ und $A= [0, 1]
\times [1, 2]$

$$\iint_{A}f(x,y) \, dA = \frac{3}{4}.$$

In den folgenden beiden Videos finden Sie zwei weitere Beispiele für
Doppelintegrale auf einem Rechteckgebiet.

```{dropdown} Video zu "Beispiel Doppelintegral" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/l_Fg_tDqx2E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Beispiel Doppelintegral" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/7HRXCYZSYnI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Mehrdimensionale INTEGRATION – Doppelintegral mit Grenzen" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/n8NDyxOMVEw?si=EcYFuvJyetiVSJNt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Beispiel: A ist kein Rechteck

Als nächstes betrachten wir ein Beispiel, bei dem das Integrationsgebiet kein
Rechteck ist. Die Funktion $f(x,y) = x^2\cdot(y+1)$ soll auf dem
Definitionsgebiet $A$ integriert werden, dass durch die Gerade $y=-x+1$ und die
Parabel $y=x^2-5$ begrenzt wird.

**Schritt 1: obere und untere Funktion finden**

Als erstes wird eine Skizze der beiden Funktionen $y=-x+1$ und $y=x^2-5$
angefertigt. Die Skizze zeigt, dass die obere Funktion

$$f_o(x) = -x + 1$$

ist und die untere Funktion

$$f_u(x) = x^2 - 5$$

ist. Allerdings muss noch das Intervall auf der x-Achse gefunden werden. Dazu
wird der Lösungsansatz

$$f_o(x) = f_u(x)$$

angesetzt und die entstehende Gleichung $-x + 1 = x^2 -5$ gelöst. Das Ergebnis
sind die beiden Stellen $x_1 = -3$ und $x_2 = 2$.

```{figure} pics/part10_plot_example02.svg
---
width: 75%
name: part10_plot_example02
---
Draufsicht auf das Integrationsgebiet $A$, das durch die Gerade $f_o(x)=-x+1$ und die Parabel $f_u(x)=x^2-5$ umrandet wird.
```

Damit kann das Doppelintegral in zwei Integrale umgeschrieben werden:

$$\iint_{A}f(x,y)\, dA = \int_{x=-3}^{x=2} \left(\int_{y=x^2-5}^{y=-x+1}
x^2\cdot(y+1) \; dy\right)dx.$$

**Schritt 2: innere Integration (nach y)**

Das innere Integral $I(x)$ wird berechnet, indem nach $y$ integriert wird:

\begin{align*}
I(x) &= \int_{y=x^2-5}^{y=-x+1} x^2\cdot(y+1) \, dy = \\
     &= \left[ x^2 \cdot \left(\frac{1}{2}y^2 +y\right)\right]_{y=x^2-5}^{y=-x+1} = \\
     &= x^2 \left(\frac{1}{2}(-x+1)^2+(-x+1) - \frac{1}{2}(x^2-5)^2-(x^2-5) \right) = \\
     &= -\frac{1}{2}x^6 + \frac{9}{2}x^4-2x^3-6x^2.
\end{align*}

**Schritt 3: äußere Integration (nach x)**

Das innere Integral $I(x) = -\frac{1}{2}x^6 + \frac{9}{2}x^4-2x^3-6x^2$ wird nun
in das äußere Integral eingesetzt und nach $x$ integriert:

\begin{align*}
\int_{x=-3}^{x=2} I(x)\, dx &= \int_{x=-3}^{x=2} -\frac{1}{2}x^6 + \frac{9}{2}x^4-2x^3-6x^2 =\\
&= \left[-\frac{1}{14}x^7 + \frac{9}{10}x^5 - \frac{1}{2}x^4 - 2x^3\right]_{x=-3}^{x=2} = \\
&= \frac{625}{14} \approx 44.643
\end{align*}

Damit gilt insgesamt

$$\iint_{A}f(x,y)\, dA = \int_{x=-3}^{x=2} \left(\int_{y=x^2-5}^{y=-x+1}
x^2\cdot(y+1) \; dy\right)dx = \frac{625}{14} \approx 44.643.$$

Das folgende Video zeigt ein weiteres Beispiel.

```{dropdown} Video zu "Beispiel Doppelintegral, kein Rechteck" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/7HRXCYZSYnI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
