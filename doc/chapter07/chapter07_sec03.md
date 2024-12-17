---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  main_language: python
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
---

# 7.3 Partielle Ableitungen und Gradient

Ableitungen kennen Sie schon, was genau meint jetzt wiederum der Fachbegriff
partiell? Partiell heißt ja auf deutsch teilweise, vielleicht ist Ihnen der
Begriff von einer partiellen Sonnenfinsternis geläufig. Bei Funktionen von
mehreren unabhängigen Variablen ist der Ableitungsbegriff komplizierter als bei
Funktionen von nur einer Variable. Auf die Ableitung einer Funktion von mehreren
Variablen werden wir in einem späteren Kapitel zurückkommen. Zuerst beschäftigen
wir uns mit partiellen Ableitungen 1. Ordnung.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was eine **partielle Ableitung** einer Funktion von mehreren
Variablen ist und können sie auch berechnen.
* Sie wissen, wie der **Gradient** einer Funktion von mehreren Variablen
  berechnet wird.
```

## Partielle Ableitungen

Um den Begriff der partiellen Ableitung einzuführen, betrachten wir erstmal nur
"2:1"-Funktionen, also Funktionen $f:\mathbb{R}^2 \rightarrow \mathbb{R}$.
Stellen Sie sich vor, wir betrachten eine hügelige Landschaft, die durch eine
Funktion $f(x, y)$ repräsentiert wird, wobei $x$ und $y$ die Koordinaten auf der
horizontalen Ebene sind und $f(x,y)$ die Höhe an der Position $(x,y)$ angibt.
Nun möchten wir wissen, wie sich die Höhe ändert, wenn wir uns in Richtung der
x-Achse bewegen, während wir die y-Koordinate konstant halten.

Die partielle Ableitung von $f$ nach $x$ gibt uns genau diese Information. Sie
zeigt uns die Steigung der Funktion in x-Richtung an jedem Punkt $(x,y)$ auf der
Landschaft. Wenn die partielle Ableitung positiv ist, bedeutet dies, dass die
Höhe zunimmt, wenn wir uns in positiver x-Richtung bewegen. Die Höhe nimmt ab,
wenn die partielle Ableitung negativ ist. Und wir bleiben uns auf konstanter
Höhe entlang der x-Achse, wenn die partielle Ableitung Null ist.

Analog dazu gibt uns die partielle Ableitung von $f$ nach $y$, die Steigung der
Funktion in y-Richtung an jedem Punkt $(x, y)$ auf der Landschaft. Partielle
Ableitungen helfen aber nicht die Steigung des Geländes zu verstehen, wenn wir
querfeldein gehen, d.h. nicht entlang der x- oder y-Achse.

Insgesamt helfen uns partielle Ableitungen, die Steigungen einer Funktion mit
mehreren Variablen zu verstehen, indem sie uns zeigen, wie sich die Funktion in
Bezug auf jede ihrer Variablen ändert, während die anderen konstant gehalten
werden.

Um die 1. partielle Ableitung einer Funktion mathematisch zu notieren, können
wir aber nicht mehr einfach nur einen Strich nehmen $f'(x,y)$, da ja dann die
Information fehlen würde, entlang welcher Koordinatenachse wir uns bewegen.
Daher wird die Notation des sogenannten Differentialquotienten $df/dx$
modifiziert. Aus dem $d$ wird ein $\partial$.

Die 1. partielle Ableitung der Funktion $f$ nach $x$ wird als

$$\frac{\partial f}{\partial x}$$

notiert und die 1. partielle Ableitung der Funktion $f$ nach $y$ als

$$\frac{\partial f}{\partial y}.$$

Partielle Ableitungen können nicht nur für Funktionen von zwei unabhängigen
Variablen gebildet werden. Ist die Funktion $f$ beispielsweise von den drei
unabhängigen Variablen $x_1, x_2$ und $x_3$ abhängig, so würden die 1.
partiellen Ableitungen als

$$\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2},
\frac{\partial f}{\partial x_3}$$

notiert werden.

```{admonition} Was ist ... die partielle Ableitung?
:class: note
Gegeben ist eine Funktion $f$ von mehreren unabhängigen Variablen $x_1, x_2,
\ldots, x_n$. Die partielle Ableitung von $f$ nach der Variablen $x_i$ ist die
"normale" Ableitung der Funktion $f$ nach $x_i$, wobei aber alle anderen
Variablen konstant gehalten werden.
```

Die partielle Ableitung wird also gebildet, indem nur eine der mehreren
Variablen als echte Variable angesehen wird und die übrigen Variablen als
Konstanten aufgefasst werden. Formal ergibt sich die partielle Ableitung wie
auch schon die "normale" Ableitung als Grenzwert des Differentialquotienten in
Richtung der Koordinatenachsen.

```{dropdown} Video "Motivation partielle Ableitung" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/4ppZE30P2Yw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video "Partielle Ableitung Definition" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/KqpLPQvboPY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Beispiel für das partielle Ableiten

Im Folgenden wird ein Beispiel für das partielle Ableiten gezeigt, das ich von
Mathematrick übernommen habe (siehe nachfolgend verlinktes Video). Wir
betrachten eine Funktion, die von zwei unabhängigen Variablen abhängt, nämlich

$$f(x,y) = x^3 + y^3 - x^2 + 2y^2 - 5x + y + 3.$$

```{code-cell} ipython3
:tags: [remove-input]
import numpy as np
import plotly.graph_objects as go

# generate grid
x = np.linspace(-2, 2, 101)
y = np.linspace(-2, 2, 101)
X, Y = np.meshgrid(x, y)

# evaluate function
Z = X**3 + Y**3 - X**2 + 2*Y**2 - 5*X + Y + 3

# plot
fig = go.Figure()
fig.add_trace(go.Surface(z=Z, x=x, y=y, colorscale='viridis'))
fig.update_layout(title='f(x,y)=x^3 + y^3 - x^2 + 2y^2 - 5x + y + 3',
xaxis_title='x-Achse', yaxis_title='y-Achse')
```

Als erstes bilden wir die 1. partielle Ableitung nach $x$. Wir bewegen uns also
entlang der x-Achse und betrachten $y$ nicht als eine Variable, sondern als eine
Konstante. Diese Konstante nennen wir $c$. Um das Ableiten übersichtlicher zu
gestalten, setzen wir jetzt tatsächlich die Konstante $c$ für die Variable $y$
ein. Was übrig bleibt, ist eine Funktion, die nur noch der Variablen $x$
abhängt. Diese Funktion nennen wir $g$:

$$g(x) = x^3 + c^3 - x^2 + 2c^2 - 5x + c + 3.$$

Diese Funktion wird nun nach $x$ abgeleitet:

$$g'(x) = 3x^2 + 0 - 2x + 0 - 5 + 0 + 0.$$

Also ist die 1. partielle Ableitung von $f$ nach $x$

$$\frac{\partial f(x,y)}{\partial x} = 3x^2 - 2x - 5.$$

Jetzt betrachten wir die partielle Ableitung nach $y$ und setzen dafür anstatt
der Variablen $x$ die Konstante $c$ ein. Diese Funktion nennen wir $h$:

$$h(x) = c^3 + y^3 - c^2 + 2y^2 - 5c + y + 3.$$

Diese Funktion nach $y$ abgeleitet ergibt

$$h'(x) = 0 + 3y^2 - 0 + 4y - 0 + 1 + 0.$$

Somit ist die 1. partielle Ableitung der Funktion $f$ nach $y$

$$\frac{\partial f(x,y)}{\partial y} = 3y^2 + 4y + 1.$$

```{dropdown} Video zu "Partielle Ableitung einfach erklärt" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/N0Y9E0wdLKk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Gradient

Die partiellen Ableitungen sind unabhängig voneinander. Kehren wir zu dem
Beispiel mit der Hügellandschaft zurück. Mit Hilfe der partiellen Ableitung nach
$x$ kann die Steigung in x-Richtung bestimmt werden, mit der partiellen
Ableitung nach $y$ die Steigung in die $y$-Richtung. Fassen wir beide Steigungen
in einem Vektor zusammen, zeigt der Vektor in die Richtung des steilsten
Anstiegs und seine Länge entspricht der Steigung in diese Richtung.

Bei Funktionen von mehreren unabhängigen Variablen $x_1$, $x_2$ bis $x_n$ gilt
diese Erkenntnis ebenfalls. Der Vektor, der aus den partiellen Ableitungen nach
allen $x_i$, also allen Koordinatenachsen, gebildet wird, zeigt in die Richtung
des steilsten Anstiegs. Diese Information über eine Funktion von mehreren
Variablen ist so wichtig, dass der Vektor einen eigenen Namen hat: **Gradient**.

```{admonition} Was ist ... der Gradient?
:class: note
Wir betrachten eine Funktion $f$ von mehreren Variablen $x_1, x_2, \ldots, x_n$.
Der Zeilenvektor mit allen 1. partiellen Ableitungen wird Gradient genannt. Es
gibt sogar ein eigenes Formelzeichen für den Gradienten, das
"Nabla"ausgesproichen wird und so aussieht: $\nabla$.

Es gilt also

$$\nabla f(x_1, x_2, \ldots, x_n) = \left(\frac{\partial f(x_1,
\ldots,x_n)}{\partial x_1}, \frac{\partial f(x_1, \ldots,x_n)}{\partial x_2},
\ldots, \frac{\partial f(x_1, \ldots,x_n)}{\partial x_n},\right).$$
```

Für die Funktion $f(x,y) = x^3 + y^3 - x^2 + 2y^2 - 5x + y + 3$ haben wir die 1.
partiellen Ableitungen ja bereits bestimmt. Wir müssen die partiellen
Ableitungen nur noch als Zeilenvektor aufschreiben, um den Gradienten der
Funktion zu bestimmen:

$$\nabla f(x,y) = \left(3x^2 - 2x - 5, 3y^2 + 4y + 1\right).$$

Der Gradient sowie ein weiteres Beispiel werden in den folgenden Videos
präsentiert.

```{dropdown} Video zu "Gradient" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/BbOUhSRh57I?si=750hDMUywwy1p2YZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Gradient" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/627f_DgQJpY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
