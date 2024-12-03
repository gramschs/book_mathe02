# 8.1 Gradient und Richtungsableitung

Die partiellen Ableitungen sind die Ableitungen in Richtung der
Koordinatenachsen. Bisher haben wir uns noch nicht damit beschäftigt, wie die
Ableitung in eine beliebige Richtung berechnet wird. Das wird in diesem Kapitel
nachgeholt.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was die **Richtungsableitung** einer Funktion von mehreren
  Variablen ist.
* Sie wissen, wann sie die Richtungsableitung auch mit Hilfe des Gradienten
  berechnen dürfen und kennen für diesen Fall auch die Berechnungsformel.
* Sie kennen die Rechenregeln für Gradienten.
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

Als nächstes gehen wir von dem Punkt $\vec{x}$ ein kurzes Stückchen in Richtung
$\vec{v}$. Da die Richtung die Länge 1 hat, führen wir die reelle Zahl $h$ ein
und multiplizieren sie mit der Richtung. Das kurze Stückchen von $\vec{x}$ in
Richtung $\vec{v}$ wird also durch

$$\vec{x} + h\cdot \vec{v}$$

beschrieben und hat automatisch die Länge $h$.

Nun wird der Differenzenquotient gebildet. Im Zähler steht die Differenz
zwischem dem Funktionswert an der Stelle $\vec{x} + h\cdot \vec{v}$ und dem
Funktionswert am Punkt $\vec{x}$. Im Nenner die Differenz zwischen den beiden
Punkten selbst, also $\vec{x} - \left(\vec{x}+h\vec{v} \right)$. Damit lautet
der Differenzenquotient

$$\frac{f(\vec{x}+h\vec{v}) - f(\vec{x})}{h}.$$

Der Grenzwert für $h \to 0$ ist die Richtungsableitung der Funktion $f$ in
Richtung $v$. Wir verwenden für die Richtungsableitung das Symbol $D_{v}f$.

```{admonition} Was ist ... die Richtungsableitung?
:class: note
Die Richtungsableitung der Funktion $f$, die von mehreren Variablen abhängt, in
die Richtung $v$ ist der Grenzwert

$$D_{v}f = \lim_{h\to 0} \frac{f(\vec{x}+h\cdot \vec{v}) - f(\vec{x})}{h}.$$

Das gilt allerdings nur dann, wenn die Richtungsableitung überhaupt existiert.
```

Wenn wir als Richtung die Koordinatenachsen wählen, landen wir wieder bei den
partiellen Ableitungen.

## Manchmal kann die Richtungsableitung auch mit dem Gradienten berechnet werden

Die Grenzwertbildung ist aufwendig. Schön wäre es, ein Formel für die Berechnung
der Richtungsableitung zu haben. Die gibt es auch, aber nur, wenn die Funktion
total differenzierbar ist. Diese Art der Differenzierbarkeit ist neu und
tatsächlich werden wir die korrekte mathematische Definition der totalen
Differenzierbarkeit hier weglassen. Glücklicherweise gehören Funktionen, deren
partiellen Ableitungen alle stetig sind, zu den total differenzierbaren
Funktionen. Daher beschränken wir uns auf diese Funktionen und halten fest:

```{admonition} Wie wird die Richtungsableitung berechnet?
:class: note
Wenn alle partiellen Ableitung der Funktion $f$ stetig sind, kann die
Richtungsableitung in  Richtung $v$ auch mit dem Gradienten $\nabla f$ berechnet
werden. Dann gilt:

$$D_{v}f(\vec{x}) = \nabla f(\vec{x}) \cdot \vec{v}.$$
```

Im folgenden Video wird ausführlich ein Beispiel vorgerechnet.

```{dropdown} Video zu "Richtungsableitung berechnen" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/95KyHXzhRII" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Rechenregeln für Gradienten

Wie Sie sehen, hat der Gradient eine große Bedeutung für das Ableiten
mehrdimensionaler Funktionen. Es wäre auch hier gut, sich das Berechnen des
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

Zunächst folgen aber noch Videos, die die obigen Regeln erklären.

```{dropdown} Video zu "Summenregel Gradient" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/OoO47lj7-BM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Faktorregel Gradient" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/DiCAQfMMDk0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Produktregel Gradient" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/dUyMIwbYuy8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Quotientenregel Gradient" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/GlFNR8QTa10" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
