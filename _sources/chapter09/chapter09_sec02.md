# 9.2 Totales Differential

## Lernziel

```{admonition} Lernziel
:class: important
Sie können das **totale Differential** einer Funktion von mehreren Variablen
berechnen.
```

## Was ist das Differential?

Bei eindimensionalen Funktionen gilt näherungsweise das 1.
Taylorpolynom im Entwicklungspunkt $x_0$:

$$f(x) \approx f(x_0) + f'(x_0)\cdot (x-x_0).$$

Wenn wir jetzt wissen wollen, um wieviel sich der Funktionswert $f(x_0)$ ändert,
wenn wir $x_0$ um $\Delta x$ auf $x_0 + \Delta x$ erhöhen, können wir diese Approximation nutzen. 

$$f(x_0 +\Delta x) \approx f(x_0) + f'(x_0) \cdot \left( (x_0+\Delta x) - x_0\right).$$

Die Änderung von $f(x_0)$ auf $f(x_0 + \Delta x)$ ist die Differenz, also

$$f(x_0 +\Delta x) - f(x_0) = f(x_0) + f'(x_0) \cdot \left( (x_0+\Delta x) - x_0\right) - f(x_0).$$

Damit bleibt nur noch übrig:

$$f(x_0 +\Delta x) - f(x_0) = f'(x_0) \cdot  \Delta x.$$

Dieser Ausdruck wird Differential genannt.

```{admonition} Was ist ... das Differential?
:class: note
Ist eine Funktion $f$ differenzierbar, so wird der Term

$$f'(x)\cdot \Delta x$$

Differential genannt. Das Differential beschreibt den linearen Anteil der
Änderung der Funktion $f$.
```

## Was ist das totale Differential?

Da sich die Tangentenfunktion von eindimensionalen Funktionen aud mehrdimensionale Funktionen übertragen lässt, kann auch das Differential auf mehrdimensionale Funktionen übertragen werden. Es wird dann totales Differential genannt.

```{admonition} Was ist ... das totale Differential?
:class: note
Existiert zu einer Funktion $f:\mathbb{R}^n\to\mathbb{R}$ die Tangentenfunktion,
so wird 

$$\sum_{i=1}^n \frac{\partial f(\vec{x})}{x_i} \cdot \Delta x_i$$

totales Differential genannt. Es beschreibt den linearen Anteil wie sich die
Funktionswerte $f(\vec{x}$ ändern, wenn sich die Variablen $x_1, x_2, \ldots,
x_n$ entlang der Koordinatenachsen sum $\Delta x_1, \Delta x_2, \ldots, \Delta
x_n$ ändern.
```


```{dropdown} Video zu "Totales Differential" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/qDgsHyg928Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

