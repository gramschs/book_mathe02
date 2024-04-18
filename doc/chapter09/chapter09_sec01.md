# 9.1 Tangentenfunktionen

Für eindimensionale Funktionen haben wir die Linearisierung und die Annährung
einer Funktion durch eine Tangente bereits kennengelernt. Am einfachsten lässt
sich die Tangente einer eindimensionalen Funktion berechnen, indem wir das 1.
Taylorpolynom im Entwicklungspunkt $x_0$ berechnen:

$$f(x) \approx f(x_0) + f'(x_0)\cdot (x-x_0).$$

Aus der Tangente wird für eine Funktion $f: \mathbb{R}^2 \rightarrow \mathbb{R}$
eine **Tangentialebene**. Für Funktionen $f: \mathbb{R}^n \rightarrow
\mathbb{R}$ mit $n \geq 3$ wird die Verallgemeinerung der Tangente dann
**Tangentialhyperebene** genannt.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können die Tangentenfunktion einer Funktion $f: \mathbb{R}^n \rightarrow
\mathbb{R}$ aufstellen und damit die Funktion $f$ linearisieren:

$$T_{1,f}(\vec{x}) = f(\vec{x}_0) + \nabla f(\vec{x}_0) \cdot (\vec{x}-\vec{x}_0).$$
* Sie wissen, dass für $n=2$ die Tangentenfunktion auch **Tangentialebene**
  genannt wird. 
* Sie wissen, dass für $n \geq 3$ die Tangentenfunktion auch
  **Tangentialhyperebene** genannt wird.
```


## Was ist eine Tangentenfunktion?

```{admonition} Was ist ... eine Tangentenfunktion?
Um eine Tangentenfunktion zu bilden, brauchen wir erst einmal eine skalarwertige
Funktion, also $f:\mathbb{R}^n \to \mathbb{R}$. Außerdem brauchen wir einen
Entwicklungspunkt $\vec{x}_0$. Dann wird die folgende Funktion Tangentenfunktion
zu $f$ genannt:

$$T_{1,f}(\vec{x}) = f(\vec{x}_0) + \nabla f(\vec{x}_0) \cdot
(\vec{x}-\vec{x}_0).$$
```

Wenn wir jetzt eine Funktion betrachten, die nur von zwei Variablen abhängt,
dann können wir die Tangentenfunktion auch folgendermaßen darstellen:

\begin{align*}
T_{1,f}(x,y) 
&= f(x_0,y_0) + \nabla f(x_0,y_0) \cdot
    \begin{pmatrix} x - x_0 \\ y - y_0 \end{pmatrix} = \\
&= f(x_0,y_0) + \left( \frac{\partial f(x_0,y_0)}{\partial x}, 
    \frac{\partial f(x_0,y_0)}{\partial y} \right) \cdot \begin{pmatrix} x - x_0 \\ y - y_0 \end{pmatrix} = \\
&= f(x_0,y_0) + \frac{\partial f(x_0,y_0)}{\partial x}(x-x_0) + 
    \frac{\partial f(x_0,y_0)}{\partial y}(y-y_0).
\end{align*}

Damit haben wir die Beschreibung einer Ebene. Daher wird die Tangentenfunktion
für $n=2$ auch Tangentialebene genannt. Dieselbe Rechnung können wir auch für
$n=3$ oder größer durchführen. Darauf verzichten wir aber hier.

Das folgende Video fasst Tangentenfunktion noch einmal zusammen.

```{dropdown} Video zu "Tangentenfunktion" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/RFbjuIDKHG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Beispiel zu Tangentialebene

In dem folgenden Video wird ein Beispiel zur Berechnung der Tangentialebene
vorgeführt. Dabei wird die Funktion $f:\mathbb{R}^2\to\mathbb{R}$ definiert als

$$f(x,y) = -x^2 - y^2.$$

Als Entwicklungspunkt wird der Punkt $(-1,-1)$ gewählt. Das Ergebnis ist die
Tangentialebene

$$T_{1,f} = 2 + 2x + 2y.$$ 

Hier wird auf die detaillierte Berechnung der Tangentialebene verzichtet. Bitte
schauen Sie sich stattdessen das Video an.

```{dropdown} Video zu "Beispiel Tangentenfunktion" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/Cms3lsrG0cM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
