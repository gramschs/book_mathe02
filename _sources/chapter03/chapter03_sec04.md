# 3.4 Konvergenz von Potenzreihen

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können erklären, was der **Konvergenzbereich** einer Potenzreihe ist.
* Sie können den Konvergenzbereich einer Potenzreihe geometrisch interpretieren und anhand des **Konvergenzradius** entscheiden, ob eine Potenzreihe konvergiert oder divergiert oder berechnen, was in den **Randpunkten** passiert.
* Sie kennen zwei Formeln auswendig, um den Konvergenzradius $r$ einer Potenzreihe zu berechnen, nämlich

$$r = \lim_{k\to\infty}\left| \frac{a_k}{a_{k+1}}\right| \quad \text{ und } \quad r = \lim_{k\to\infty}\frac{1}{\sqrt[k]{|a_k|}},$$

und können diese auch anwenden. 
```

## Manchmal kann man eine Funktion mit einer Potenzreihe approximieren, manchmal nicht

Experiment:

1. Gehen Sie mit Ihrem Mauszeiger auf das GeoGebra-Applet [Taylor polynomial
   graphs](https://www.geogebra.org/m/s9SkCsvC) und klicken Sie darauf (ggf. auf
   den Pfeil klicken), um es zu aktivieren.
2. Schauen Sie sich zunächst die Approximation der Kosinusfunktion an. Schieben
   Sie den Slider für n von 1 bis 30 und beobachten Sie? Ab wann ist Ihrer
   Meinung nach die Potenzreihe eine gute Approximation der Kosinusfunktion?
3. Ändern Sie jetzt die Funktion und geben Sie `f(x) = ln(x)` ein. Schieben Sie
   den Schieberegler wieder von 1 bis 30. Was beobachten Sie diesmal?

Für jedes x wird die Summe $\sum_{k=0}^{\infty} a_k (x-x_0)^k$ einen anderen
Grenzwert annehmen, sofern der Grenzwert überhaupt existiert. Diejenigen x, für
die die Folge der Partialsummen konvergiert, nennen wir Konvergenzbereich.

```{admonition} Was ist ... der Konvergenzbereich einer Potenzreihe?
:class: note
Die Menge aller Zahlen $x$, für die die spezielle Potenzreihe

$$p(x) = \sum_{k=0}^{\infty} a_k x^k$$

konvergiert, wird **Konvergenzbereich** genannt.
```

## Konvergenzradius

Wenn man den Konvergenzbereich von Potenzfunktionen näher untersucht, stellt man
fest, dass der Konvergenzbereich ein Intervall ist, in dessen Mitte die 0 liegt.
Das Intervall ist symmetrisch zur Null, kann also als $(-r, +r)$ dargestellt
werden. Die Zahl $r$ wird als **Konvergenzradius** bezeichnet.

Wenn $x < -r$ ist oder $r < x$ ist, dann divergiert die Potenzreihe. Was
passiert, wenn $x = -r$ ist oder $x = +r$ gilt, ist nicht klar. Diese
sogenannten Randpunkte des Konvergenzbereichs müssen gesondert untersucht
werden.

Betrachten wir nicht eine spezielle Potenzreihe sondern eine allgemeine
Potenzreihe

$$p(x) = \sum_{k=0}^{\infty} a_k (x - x_0)^k,$$

dann ist nicht die 0 in der Mitte des Konvergenzbereichs, sondern $x_0$. Der
Konvergenzbereich ist dann $(-r + x_0, +r + x_0)$.

```{dropdown} Video "Konvergenzradius" von Prof. Hoever
<iframe width="560" height="315" src="https://www.youtube.com/embed/69PgueE9CI0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Formeln zur Berechnung des Konvergenzradius

Die beiden folgenden Videos zeigen, wie die beiden Formeln

* Wurzelkriterium
* Quotientenkriterium
  
zur Berechnung des Konvergenzradius funktionieren.

```{dropdown} Video "Wurzel-Formel bei Konvergenzradius" von Prof. Hoever
<iframe width="560" height="315" src="https://www.youtube.com/embed/yO2mP5aToMU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video "Quotienten-Formel bei Konvergenzradius" von Prof. Hoever
<iframe width="560" height="315" src="https://www.youtube.com/embed/ConZiKDKA9Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
