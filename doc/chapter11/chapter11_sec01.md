# 11.1 Polarkoordinaten

Polarkoordinaten bieten eine alternative Möglichkeit, die Position von Punkten
in der Ebene zu beschreiben. Die häufigste Beschreibung der Position von Punkten
sind kartesische Koordinaten. Insbesondere bei technischen Systemen, bei denen
Symmetrie oder Rotation wichtig sind, sind Polarkoordinaten jedoch eine bessere
Möglichkeit, die Position der Punkte anzugeben.


## Lernziele

```{admonition} Lernziele
:class: important
* Sie wissen, was **Polarkoordinaten** sind.
* Sie können kartesische Koordinaten in Polarkoordinaten umrechnen.
* Sie können Polarkoordinaten in kartesische Koordinaten umrechnen.
```

## Kartesische Koordinaten

Das am häufigsten verwendete Koordinatensystem ist das **kartesische
koordinatensystem**. Es ist nach dem Methematiker [René
Descartes](https://de.wikipedia.org/wiki/René_Descartes) benannt, obwohl
Descartes ein solches Koordinatensystem nie beschrieben hat. Das Hauptmerkmal
von kartesischen Koordinatensytemen ist, dass die Koordinatenachsen senkrecht
aufeinander stehen. Die folgende Abbildung zeigt ein zweidimensionales
kartesisches Koordinatensystem mit dem Koordinatenursprung $(0,0)$ und einem
Punkt an der Position $P(2\sqrt{3},2)$.

```{figure} pics/fig11_01.svg
---
width: 75%
name: fig11_01
---
Kartesisches zweidimensionales Koordinatensystem
```

## Polarkoordinaten

Eine alternative Beschreibung ist, die Entfernung und den Winkel zum Punkt
anzugeben. Die Entfernung des Punktes wird bezogen auf den Koordinatenursprung
angegeben. Der Winkel wird gegen den Uhrzeigersinn von der positiven x-Achse aus
gemessen.  Üblicherweise wird zuerst die Entfernung $r$ notiert und dann der
Winkel $\varphi$, also

$$(r, \varphi).$$

Diese Art von Koordinaten wird als **Polarkoordinaten** bezeichnet. 

In dem Beispiel wird so aus dem Punkt $(2\sqrt{3},2)$ in kartesischen
Koordinaten der Punkt $(4, 30^{\circ})$, wie wir gleich sehen, wenn wir die
Umrechnung von kartesischen zu Polarkoordinaten behandeln.

```{figure} pics/fig11_02.svg
---
width: 75%
name: fig11_02
---
Zweidimensionales Polarkoordinatensystem
```

## Umrechnung von Polarkoordinaten in kartesische Koordinaten

Die Umrechnung von Polarkoordinaten in kartesische Koordinaten erfolgt mit den
Formeln:

\begin{align*}
x &= r\cdot \cos(\varphi) \\ 
y &= r\cdot \sin(\varphi)
\end{align*}

Bei dem obigen Beispiel ist $r=4$ und $\varphi=30^{\circ}$. Mit den beiden
Formeln zur Berechnung der kartesischen Koordinaten $x$ und $y$ erhalten wir

\begin{align*}
x &= 4 \cdot \cos(30^{\circ}) = 2\sqrt{3}, \\ 
y &= 4 \cdot \sin(30^{\circ}) = 2.
\end{align*}

Zur Erinnerung folgt hier eine Einführung in Polarkoordinaten:

```{dropdown} Video "Ebene Polarkoordinaten" von Daniel Jung
<iframe width="560" height="315" src="https://www.youtube.com/embed/l8ZF4m0fPxM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Umrechnung von kartesischen Koordinaten in Polarkoordinaten

Die umgekehrte Berechnung von kartesischen Koordinaten in Polarkoordinaten ist
etwas schwieriger. Die Berechnung des Radius $r$ ist noch einfach, da ein
rechtwinkliges Dreieck vorliegt und wir den Satz des Pythagoras anwenden können:

$$r = \sqrt{x^2 + y^2}.$$

Danach können wir entweder die Ankathete $x$ oder die Gegenkathete $y$ ausnutzen, um den Winkel $\varphi$ zu bestimmen. Im rechtwinkligen Dreieck gelten

$$\cos(\varphi) =
\frac{x}{r} \quad \text{ oder } \quad \sin(\varphi) = \frac{y}{r}.$$

```{figure} pics/fig11_03.svg
---
width: 75%
name: fig11_03
---
Die Umrechnung kartesische Koordinaten in Polarkoordinaten nutzt das rechtwinklige Dreieck aus.
```

Mit den Umkehrfunktionen der Sinus- und der Kosinusfunktion erhalten wir

$$\varphi = \arccos\left(\frac{x}{r}\right) \quad \text{ oder } \quad \varphi =
\arcsin\left( \frac{y}{r}\right).$$

Wo ist jetzt das Problem? Lösen wir die Gleichung

$$\sin(\varphi) = \frac{1}{2},$$

so hat diese Gleichung innerhalb des Intervalls $[0, 360^{\circ}]$ zwei
Lösungen, nämlich $30^{\circ}$ und $150^{\circ}$. Aber welcher Winkel ist der
richtige Winkel? Da die x-Koordinate positiv ist und der Punkt $P(2\sqrt{2},2)$
im 1. Quadranten liegt, ist der richtige Winkel $\varphi = 30^{\circ}$.
Überprüfen Sie daher immer durch eine Zeichnung, welches der richtige Winkel ist.

In dem folgenden Video wird gezeigt, wie eine Funktion mit Variablen in
kartesischen Koordinaten in eine Funktion mit Variablen in Polarkoordinaten
umgerechnet werden kann:

```{dropdown} Video zu "Polarkoordinaten" von Prof. Hoever
<iframe width="560" height="315" src="https://www.youtube.com/embed/MCRDcJKeR20" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{admonition} Weiteres Lernmaterial
:class: seealso
https://de.serlo.org/mathe/45643/polarkoordinaten
https://studyflix.de/mathematik/polarkoordinaten-1476
```