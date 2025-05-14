# 7.1 Gradient und Richtungsableitung

Die partiellen Ableitungen sind die Ableitungen in Richtung der
Koordinatenachsen. Bisher haben wir uns noch nicht damit beschäftigt, wie die
Ableitung in eine beliebige Richtung berechnet wird. Das wird in diesem Kapitel
nachgeholt.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was die **Richtungsableitung** einer Funktion von mehreren
  Variablen ist.
* Sie wissen, wann Sie die Richtungsableitung auch mit Hilfe des Gradienten
  berechnen dürfen und kennen für diesen Fall auch die Berechnungsformel.
* Sie kennen die **Rechenregeln für Gradienten**.
```

## Richtungsableitung

Die Ableitung einer Funktion von mehreren unabhängigen Variablen in eine
Richtung wird wie bei eindimensionalen Funktionen über den Grenzwert des
Differenzenquotienten eingeführt. Aber fangen wir langsam an. Die Funktion $f$
soll also von mehreren Variablen abhängen. Wir nehmen an, dass es $n$ Variablen
sind und schreiben diese als $x_1$, $x_2$, $\ldots$, $x_n$. Jetzt betrachten wir
einen festen Punkt $\vec{x} = (x_1, x_2, \ldots, x_n)$ aus der Definitionsmenge,
für den wir die Richtungsableitung bilden wollen. Die Richtung bezeichnen wir
als $\vec{v}$. Wie bei Richtungen üblich, soll die Richtung schon normiert
angegeben werden. Damit ist gemeint, dass der Vektor $\vec{v}$ die Länge 1 hat.

Als nächstes gehen wir von dem Punkt $\vec{x}$ ein kleines Stück in Richtung
$\vec{v}$. Da die Richtung die Länge 1 hat, führen wir die reelle Zahl $h$ ein
und multiplizieren sie mit der Richtung. Das kurze Stück von $\vec{x}$ in
Richtung $\vec{v}$ wird also durch

$$\vec{x} + h\cdot \vec{v}$$

beschrieben und hat automatisch die Länge $h$.

Nun wird der Differenzenquotient gebildet. Im Zähler steht die Differenz
zwischen dem Funktionswert an der Stelle $\vec{x} + h\cdot \vec{v}$ und dem
Funktionswert am Punkt $\vec{x}$. Im Nenner steht der Abstand zwischen den
beiden Punkten, was der Länge $h$ entspricht. Damit lautet der
Differenzenquotient

$$\frac{f(\vec{x}+h\vec{v}) - f(\vec{x})}{h}.$$

Der Grenzwert für $h \to 0$ ist die Richtungsableitung der Funktion $f$ in
Richtung $\vec{v}$. Wir verwenden für die Richtungsableitung das Symbol
$D_{\vec{v}}f$.

```{admonition} Was ist ... die Richtungsableitung?
:class: note
Die Richtungsableitung der Funktion $f$, die von mehreren Variablen abhängt, in
die Richtung $v$ ist der Grenzwert

$$D_{\vec{v}}f = \lim_{h\to 0} \frac{f(\vec{x}+h\cdot \vec{v}) - f(\vec{x})}{h}.$$

Das gilt allerdings nur dann, wenn die Richtungsableitung überhaupt existiert.
```

Wenn wir als Richtung $\vec{v}$ einen der Einheitsvektoren entlang der
Koordinatenachsen wählen, erhalten wir genau die partiellen Ableitungen.
Betrachten wir beispielsweise in einem zweidimensionalen Raum den Einheitsvektor
in x-Richtung $\vec{e}_1 = (1,0)$, dann gilt:

$$D_{\vec{e}_1}f(x,y) = \lim_{h\to 0} \frac{f(x+h,y) - f(x,y)}{h} =
\frac{\partial f}{\partial x}(x,y).$$

Entsprechend erhalten wir für den Einheitsvektor in y-Richtung $\vec{e}_2 =
(0,1)$:

$$D_{\vec{e}_2}f(x,y) = \lim_{h\to 0} \frac{f(x,y+h) - f(x,y)}{h} =
\frac{\partial f}{\partial y}(x,y).$$

Allgemein gilt im $n$-dimensionalen Raum für den $i$-ten Einheitsvektor
$\vec{e}_i$:

$$D_{\vec{e}_i}f(\vec{x}) = \frac{\partial f}{\partial x_i}(\vec{x}).$$

Dieser Zusammenhang verdeutlicht, dass die partiellen Ableitungen tatsächlich
Richtungsableitungen in Richtung der Koordinatenachsen sind. Die
Richtungsableitung erweitert dieses Konzept auf beliebige Richtungen und ist
somit eine Verallgemeinerung der partiellen Ableitung.

## Manchmal kann die Richtungsableitung auch mit dem Gradienten berechnet werden

Die Grenzwertbildung ist aufwendig. Schön wäre es, eine Formel für die
Berechnung der Richtungsableitung zu haben. Die gibt es auch, aber nur, wenn die
Funktion total differenzierbar ist. Diese Art der Differenzierbarkeit ist neu
und tatsächlich werden wir die korrekte mathematische Definition der totalen
Differenzierbarkeit in dieser Vorlesung nicht einführen. Bei Interesse kann die
Definition der totalen Differenzierbarkeit bei [Wikipedia → totale
Differenzierbarkeit](https://de.wikipedia.org/wiki/Totale_Differenzierbarkeit)
nachgelesen werden.

Glücklicherweise gehören Funktionen, deren partiellen Ableitungen alle stetig
sind, zu den total differenzierbaren Funktionen. Daher beschränken wir uns auf
diese Funktionen und halten fest:

```{admonition} Wie wird die Richtungsableitung berechnet?
:class: note
Wenn alle partiellen Ableitungen der Funktion $f$ stetig sind, kann die
Richtungsableitung in  Richtung $\vec{v}$ auch mit dem Gradienten $\nabla f$
berechnet werden. Dann gilt:

$$D_{\vec{v}}f(\vec{x}) = \nabla f(\vec{x}) \cdot \vec{v}.$$
```

Im folgendem Video wird ausführlich ein Beispiel vorgerechnet.

```{dropdown} Video zu "Richtungsableitung berechnen" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/95KyHXzhRII"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Rechenregeln für Gradienten

Wie Sie sehen, hat der Gradient eine große Bedeutung für das Ableiten
mehrdimensionaler Funktionen. Es wäre auch hier gut, die Berechnung des
Gradienten zu vereinfachen und ggf. neue Gradienten aus schon bekannten
Gradienten zusammenzubauen. Im Folgenden sind die Rechenregeln für Gradienten
angegeben.

* Ist $c$ eine konstante reelle Zahl, so ist der Gradient davon der Nullvektor, also

$$\nabla c = 0.$$

* Es gilt die Faktorregel:
  
$$\nabla (c\cdot f(\vec{x})) = c \cdot \nabla f(\vec{x}).$$

* Es gilt die Summenregel:

$$\nabla \left(f(\vec{x}) + g(\vec{x})\right) = \nabla f(\vec{x}) + \nabla
g(\vec{x}).$$

* Es gilt die Produktregel:
  
  $$\nabla \left(f(\vec{x})\cdot g(\vec{x})\right) = \nabla f(\vec{x}) \cdot
  g(\vec{x}) + f(\vec{x})\cdot \nabla g(\vec{x}).$$

* Und die Quotientenregel lautet:

$$\nabla \left(\frac{f(\vec{x})}{g(\vec{x})}\right) = \frac{\nabla
f(\vec{x})\cdot g(\vec{x}) - f(\vec{x})\cdot \nabla g(\vec{x})}{g^2(\vec{x})}.
$$

Auch eine Kettenregel gibt es, doch dafür müssen wir erst einmal vektorwertige
Funktionen betrachten.

Oft ist es in der Praxis einfacher, nicht die obigen Rechenregeln für Gradienten
anzuwenden, sondern direkt die Addition/Subtraktion/Multiplikation/Division
auszuführen und danach den Gradienten auszurechnen. Im folgenden Beispiel werden
beide Varianten am **Beispiel der Produktregel** vorgeführt.

Betrachten wir die Funktionen $f(x,y) = x^2 + y^2$ und $g(x,y) = xy$.

Die Gradienten dieser Funktionen sind:

\begin{align*}
\nabla f(x,y) &= (2x, 2y)\\
\nabla g(x,y) &= (y, x).
\end{align*}

Für das Produkt $h(x,y) = f(x,y) \cdot g(x,y) = (x^2 + y^2) \cdot xy$ erhalten
wir nach der Produktregel:

\begin{align*}
\nabla h(x,y) &= g(x,y) \cdot \nabla f(x,y) + f(x,y) \cdot \nabla g(x,y)\\
&= xy \cdot (2x, 2y) + (x^2 + y^2) \cdot (y, x)\\
&= (2x^2y, 2xy^2) + ((x^2 + y^2)y, (x^2 + y^2)x)\\
&= (2x^2y + (x^2 + y^2)y, 2xy^2 + (x^2 + y^2)x)\\
&= (2x^2y + x^2y + y^3, 2xy^2 + x^3 + xy^2)\\
&= (x^2y(2 + 1) + y^3, xy^2(2 + 1) + x^3)\\
&= (3x^2y + y^3, 3xy^2 + x^3).\\
\end{align*}

Zur Überprüfung können wir $h(x,y)$ direkt ausmultiplizieren

$$h(x,y) = (x^2 + y^2) \cdot xy = x^3y + xy^3$$

und dann partiell differenzieren

\begin{align*}
&\frac{\partial h}{\partial x} = 3x^2y + y^3, \\
&\frac{\partial h}{\partial y} = x^3 + 3xy^2. \\
\end{align*}

Dies ergibt den Gradienten $\nabla h(x,y) = (3x^2y + y^3, x^3 + 3xy^2)$, was mit
dem ersten Ergebnis übereinstimmt.

In den folgenden Videos können Sie sich die Rechenregeln für Gradienten ansehen.

```{dropdown} Video zu "Summenregel Gradient" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/OoO47lj7-BM"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Faktorregel Gradient" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/DiCAQfMMDk0"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Produktregel Gradient" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/dUyMIwbYuy8"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Quotientenregel Gradient" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/GlFNR8QTa10"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir die Richtungsableitung gelernt. Für Funktionen,
deren partielle Ableitungen stetig sind, kann die Richtungsableitung mit Hilfe
des Gradienten berechnet werden. Abgerundet wurde dieses Kapitel durch
Rechenregeln für Gradienten. Offensichtlich fehlt eine Kettenregel. Dazu
benötigen wir vektorwertige Funktionen, die wir im nächsten Kapitel lernen.
