# 4.4 Rechnen mit Potenzreihen

In diesem Abschnitt befassen wir uns mit den Rechenregeln für Potenzreihen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können Potenzreihen mit demselben Entwicklungspunkt
  * addieren,
  * subtrahieren, 
  * multiplizieren und
  * dividieren.
* Sie können Potenzreihen ableiten und integrieren.
* Sie können mit Potenzreihen den Grenzwert einer Funktion bestimmen.
```

## Addition und Subtraktion

Zwei Potenzreihen können addiert oder subtrahiert werden, wenn sie denselben
Entwicklungspunkt $x_0$ haben. Um sie zu addieren oder zu subtrahieren, müssen
lediglich die Koeffizienten addiert bzw. subtrahiert werden.

Lauten die beiden Potenzreihen

$$\sum_{k=0}^{\infty}a_k (x-x_0)^k \text{ und } \sum_{k=0}^{\infty} b_k
(x-x_0)^k,$$

dann ist die Summe

$$\sum_{k=0}^{\infty} (a_k + b_k)\cdot (x-x_0)^k$$

und die Differenz

$$\sum_{k=0}^{\infty} (a_k - b_k)\cdot (x-x_0)^k.$$

Allerdings muss der Konvergenzradius neu überprüft werden. Wenn eine der
Potenzreihen einen kleineren Konvergenzradius als die andere hat, dann hat die
Summe/Differenz mindestens denselben kleineren Konvergenzradius. Möglicherweise
ist der Konvergenzradius jedoch größer.

## Ableiten und Integrieren

Potenzreihen lassen sich sehr einfach ableiten oder integrieren. Dazu wird jeder
einzelne Term der Reihe abgeleitet oder integriert. Der Konvergenzradius bleibt
dabei erhalten.

## Multiplikation und Division

Die Multiplikation und Division zweier Potenzreihen ist leider etwas komplizierter.

Um zwei Potenzreihen zu multiplizieren, verwenden wir die Cauchy-Produkt-Formel.
Damit die Formel nicht zu unübersichtlich wird, nehmen wir den Entwicklungspunkt
$x_0=0$, aber natürlich gilt die Formel auch für andere Entwicklungspunkte.

$$\left(\sum_{k=0}^{\infty} a_k x^k \right) \cdot \left(\sum_{k=0}^{\infty} b_k x^k \right)
= \left(\sum_{k=0}^{\infty} c_k x^k \right) $$

mit

$$c_k = \sum_{l=0}^{k} a_l b_{k-l}
= a_0 b_k + a_1 b_{k-1} + a_2 b_{k-2} + \ldots + a_k b_0.$$

Der Konvergenzradius muss neu überprüft werden.

Wenn die Potenzreihe $A(x)$ durch die Potenzreihe $B(x)$ geteilt werden soll,
dann muss eine neue Potenzreihe $C(x)$ gefunden werden, so dass

$$A(x) = B(x) \cdot C(x)$$

gilt. Für die Multiplikation $B(x) \cdot C(x)$ gilt jedoch

$$\left(\sum_{k=0}^{\infty} b_k x^k \right) \cdot \left(\sum_{k=0}^{\infty} c_k
x^k \right) = \left(\sum_{k=0}^{\infty} d_k x^k \right) $$

mit den Koeffizienten

$$d_k = \sum_{l=0}^{k} b_l c_{k-l} = b_0 c_k + b_1 c_{k-1} + b_2 c_{k-2} +
\ldots + b_k c_0.$$

Damit das Produkt $B(x) \cdot C(x)$ gleich der Potenzreihe $A(x)$ ist, muss
jeder Koeffizient $d_k$ mit $a_k$ übereinstimmen. Wir vergleichen also die
Koeffizienten

$a_k = d_k$

und berechnen daraus die gesuchten $c_k$. Das funktioniert allerdings nur, wenn
wir nicht ins Unendliche gehen, sondern die Potenzreihe abbrechen. Der
Konvergenzradius muss ebenfalls neu bestimmt werden.

```{dropdown} Video "Multiplikation zweier Potenzreihen" von Joachim Gaukel
<iframe width="560" height="315" src="https://www.youtube.com/embed/7hRJKp-QJw0?si=Xe-Q2HJHNfsHHCf2" title="YouTube video player" frameborder="0" allow="accelerometer;
autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

```{dropdown} Video "Division zweier Potenzreihen" von Joachim Gaukel
<iframe width="560" height="315" src="https://www.youtube.com/embed/7m26r05BjbE?si=NKu4dvyqaqLnJPeG" title="YouTube video player" frameborder="0" allow="accelerometer;
autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

## Bestimmung von Grenzwerten mit Potenzreihen

Potenzreihen bieten eine alternative Methode zur Berechnung von
Funktionsgrenzwerten im Vergleich zum Verfahren von Bernoulli-de l'Hospital.
Beim Verfahren von Bernoulli-de l'Hospital werden Zähler und Nenner getrennt
voneinander abgeleitet, bis der Funktionsgrenzwert bestimmt werden kann.
Gegebenenfalls ist es jedoch möglich, eine Funktion als Potenzreihe darzustellen,
dann die Division durchzuführen und daraus den Grenzwert direkt zu bilden. Am
einfachsten ist es, ein Beispiel zu betrachten.

Berechnen Sie den Grenzwert der Funktion $f(x) = \sin(x)/x$, wenn $x$ gegen 0
geht, also

$$\lim_{x \to 0}\frac{\sin(x)}{x}.$$

$x=0$ darf in die Funktion nicht eingesetzt werden, da ansonsten durch 0 geteilt
werden würde. Die Potenzreihe der Sinusfunktion lautet:

$$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \ldots$$

und damit ist

$$\frac{\sin(x)}{x} = 1 - \frac{x^2}{3!} + \frac{x^4}{5!} - \frac{x^6}{7!}+\ldots.$$

Für jeden einzelnen Term können wir jetzt aber den Grenzwert berechnen, also

$$
\lim_{x\to 0} \left(1 \right) = 1, \;
\lim_{x\to 0} \left(\frac{x^2}{3!} \right) = 0, \;
\lim_{x\to 0} \left(\frac{x^4}{5!} \right) = 0, \ldots $$

Nur der erste Term hat den Grenzwert 1, alle nachfolgenden Grenzwerte sind 0. Da
alle Grenzwerte endlich sind, dürfen wir die Grenzwerte addieren bzw. subtrahieren
und erhalten so den gesuchten Grenzwert

$$\lim_{x \to 0}\frac{\sin(x)}{x} = 1.$$
