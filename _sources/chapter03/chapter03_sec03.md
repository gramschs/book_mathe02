# 3.3 Potenzreihen

Polynome haben schöne Eigenschaften, vor allem sind sie einfach abzuleiten oder
zu integrieren. In der Praxis ist es daher oft sinnvoll, "schwierige" Funktionen
durch Polynome zu ersetzen, auch wenn man dafür Fehler macht.

Diese Vorgehensweise wird **Approximation** genannt, zu deutsch Annäherung. Für
Zahlen haben Sie dies schon kennengelernt. Wenn Sie beispielsweise den
Flächeninhalt $A$ eines Kreises mit Radius $r = 3 \,\text{m}$ berechnen wollen,
so gilt $A = \pi \cdot r^2 = 9\pi$. Da aber $\pi$ unendlich viele
Nachkommastellen hat, legen Sie fest, wie genau die Annäherung an den wahren
Flächeninhalt sein soll, indem Sie die Anzahl der Nachkommastellen festlegen.
Reichen Ihnen beispielsweise zwei Nachkommastellen, also $\pi \approx 3.14$, so
erhalten Sie $A = 28.27 \,\text{m}^2$.

In diesem Kapitel geht es um Potenzreihen und die Approximation von Funktionen durch Potenzreihen. 

## Lernziele

```{admonition} Lernziele
:class: important
* Sie können erklären, was eine **Potenzreihe** (im Gegensatz zu einer Reihe) ist.
* Sie können die **spezielle Darstellungsform einer Potenzreihe** auswendig aufschreiben:

$$p(x)=\sum_{k=0}^{\infty} a_k x^k$$

* Sie können die **allgemeine Darstellungsform einer Potenzreihe** 

$$p(x)=\sum_{k=0}^{\infty} a_k (x-x_0)^k$$
auswendig aufschreiben und erklären, was ein **Entwicklungspunkt** $x_0$ ist.
```

## Potenzreihen sind auch nur Reihen, aber Reihen von Potenzfunktionen

Bisher haben wir Zahlenfolgen aufsummiert und die Folge der Partialsummen als
Reihe bezeichnet. Nun summieren wir Potenzfunktionen auf. Zur Erinnerung,
Potenzfunktionen (manchmal auch kurz als Potenz bezeichnet) sind die Funktionen

$$1, x^1, x^2, x^3, \ldots.$$

Eine **Potenzreihe** ist eine Reihe vom Typ

$$p(x)=a_0 + a_1x + a_2x^2 + a_3 x^3 + \ldots = \sum_{k=0}^{\infty}a_k x^k.$$

Die reellen Zahlen $a_0, a_1, a_2, \ldots$ nennt man **Koeffizienten** der Potenzreihe.


Die Potenzfunktionen $x, x^2, x^3, \ldots$ gehen alle durch den Punkt $(0,0)$
den Koordinatenursprung. Damit verbunden sind auch spezielle
Symmetrieeigenschaften. Beispielsweise sind die Potenzfunktionen $x, x^3, x^5,
x^7, \ldots$ punktsymmetrisch zu $(0,0)$. Und die Potenzfunktionen mit geraden
Exponenten $x^2, x^4, x^6, \ldots$ sind symmetrisch zur y-Achse. Wenn nicht den
Koordinatenursprung so im Mittelpunkt stehen soll, sondern beispielsweise der
Punkt $(x_0,y_0)$, müssen wir die Potenzfunktionen leicht modifizieren. Durch
Additionn von y_0 werden die Potenzfunktionen nach oben (wenn $y_0 > 0$) oder
unten (wenn $y_0 < 0$) verschoben. In der Potenzreihe gibt es schon so einen
Summanden, nämlich $a_0$. Also brauchen wir nur $a_0=y_0$ setzen, damit nun die
Symmetrie/Punktsymmetrie sich auf den Punkt $(0, y_0)$ bezieht.

Als nächstes möchten wir aber die Potenzfunktionen noch so modifizieren, dass
die Punktsymmetrie bzw. Symmetrie der Potenzfunktionen sich auf die x-Koordinate
$x_0$ bezieht. Dazu müssen wir von jedem $x$ den Wert $x_0$ abziehen und dann
die Potenz bilden, also $(x-x_0)^k$ verwenden.

```{admonition} Was ist ... eine Potenzreihe?
:class: note
Eine **Potenzreihe** ist eine Reihe vom Typ

\begin{align*}
p(x) &= a_0 + a_1\cdot(x-x_0) + a_2\cdot(x-x_0)^2 + a_3\cdot(x-x_0)^3 + \ldots = \\
     &= \sum_{k=0}^{\infty} a_k \cdot (x-x_0)^k.
\end{align*}

Die reellen Zahlen $a_0, a_1, a_2, \ldots$ nennt man **Koeffizienten** der Potenzreihe. Der Punkt $x_0$ wird **Entwicklungspunkt** genannt.
```

Dabei wird der spezielle Punkt $x_0$ in der Industrie **Arbeitspunkt** genannt,
in der Mathematik sagen wir aber Entwicklungspunkt oder Entwicklungsstelle. Der
Wert $y_0 =  a_0$ hat keinen besonderen Namen.

Übrigens: Nur weil die Potenzfunktionen symmetrisch oder punktsymmetrisch zum
Entwicklungspunkt sind, heißt das nicht, dass die Summe der Potenzfunktionen
irgendeine Symmetrieeigenschaft besitzt.