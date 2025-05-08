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

# 6.2 Stetigkeit von Funktionen mehrerer Variablen

Im vorherigen Kapitel haben wir Funktionen mit mehreren unabhängigen Variablen
kennengelernt und deren grafische Darstellung betrachtet. Für eine tiefergehende
mathematische Analyse solcher Funktionen ist das Konzept der Stetigkeit
fundamental. Die Stetigkeit ist eine wichtige Eigenschaft, die uns Auskunft
darüber gibt, ob eine Funktion an bestimmten Stellen "Sprünge" aufweist oder
sich "glatt" verhält.

Im Maschinenbau ist die Stetigkeit von Funktionen mehrerer Variablen von großer
praktischer Bedeutung. Bei der Modellierung von physikalischen Prozessen, wie
etwa der Wärmeleitung in Bauteilen oder der Spannungsverteilung in belasteten
Strukturen, erwarten wir in der Regel stetige Funktionen. Unstetigkeiten können
auf physikalische Phasenübergänge, Materialübergänge oder mathematische
Idealisierungen hindeuten.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können **Stetigkeit** für Funktionen mehrerer Variablen mathematisch
  definieren.
* Sie können die  von Funktionen mehrerer Variablen anschaulich interpretieren.
```

## Wiederholung: Stetigkeit von Funktionen einer Variablen

Bevor wir die Stetigkeit für Funktionen mehrerer Variablen betrachten, erinnern
wir uns kurz an die Definition für Funktionen einer Variablen. Eine Funktion $f:
\mathbb{R} \rightarrow \mathbb{R}$ ist stetig an der Stelle $x_0$, wenn gilt:

$$\lim_{x \to x_0} f(x) = f(x_0)$$

Das bedeutet anschaulich:

1. Der Grenzwert $\lim_{x \to x_0} f(x)$ existiert.
2. Der Funktionswert $f(x_0)$ existiert.
3. Beide Werte stimmen überein.

Eine alternative, oft anschaulichere Formulierung ist die
$\varepsilon$-$\delta$-Definition:

Eine Funktion $f: \mathbb{R} \rightarrow \mathbb{R}$ ist stetig an der Stelle
$x$, wenn für jedes $\varepsilon > 0$ ein $\delta > 0$ existiert, sodass für
alle $x$ mit $|x - x_0| < \delta$ gilt: $|f(x) - f(x_0)| < \varepsilon$.

Intuitiv bedeutet dies: Wenn wir Punkte betrachten, die nahe genug an $x_0$
liegen (Abstand kleiner als $\delta$), dann liegen die zugehörigen
Funktionswerte beliebig nahe an $f(x_0)$ (Abstand kleiner als $\varepsilon$).

## Stetigkeit von Funktionen mehrerer Variablen

Bei Funktionen mehrerer Variablen müssen wir das Konzept der Stetigkeit
erweitern. Wir fassen die unabhängigen Variablen $(x_1, x_2, \ldots, x_n)$  in
Vektorschreibweise zusammen als

$$\vec{x} = (x_1, x_2, \ldots, x_n).$$

Für eine Funktion $f: \mathbb{R}^n \rightarrow \mathbb{R}$ mit den unabhängigen
Variablen $\vec{x} = (x_1, x_2, \ldots, x_n)$ definieren wir Stetigkeit wie
folgt.

```{admonition} Definition: Stetigkeit einer Funktion mehrerer Variablen
:class: note
Eine Funktion $f: \mathbb{R}^n \rightarrow \mathbb{R}$ ist stetig an der Stelle
$\vec{x_0} = (x_{01}, x_{02}, \ldots, x_{0n})$, wenn gilt:

$$\lim_{\vec{x} \to \vec{x_0}} f(\vec{x}) = f(\vec{x_0})$$

In der $\varepsilon$-$\delta$-Form: Für jedes $\varepsilon > 0$ existiert ein
$\delta > 0$, sodass für alle $\vec{x}$ mit $\|\vec{x} - \vec{x_0}\| < \delta$
gilt: 

$$|f(\vec{x}) - f(\vec{x_0})| < \varepsilon.$$

Dabei bezeichnet $\|\vec{x} - \vec{x_0}\|$ den euklidischen Abstand im
$\mathbb{R}^n$.
```

Der wichtigste Unterschied zur Stetigkeit von Funktionen einer Variablen besteht
darin, dass wir jetzt den Abstand von Punkten im mehrdimensionalen Raum
betrachten. Die euklidische Norm $\|\vec{x} - \vec{x_0}\|$ gibt den Abstand
zwischen den Punkten $\vec{x}$ und $\vec{x_0}$ im $\mathbb{R}^n$ an und wird
definiert als:

$$\|\vec{x} - \vec{x_0}\| = \sqrt{(x_1 - x_{01})^2 + (x_2 - x_{02})^2 + \ldots +
(x_n - x_{0n})^2}.$$

Das folgende Video erklärt die Stetigkeit von mehrdimensionalen Funktionen.

```{dropdown} Video "Stetigkeit" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/0FoFSpOt5UY"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Anschauliche Interpretation der Stetigkeit

Bei Funktionen von zwei Variablen $f(x,y)$ können wir die Stetigkeit anschaulich
interpretieren:

Eine Funktion $f: \mathbb{R}^2 \rightarrow \mathbb{R}$ ist stetig an der Stelle
$(x_0, y_0)$, wenn sich der Funktionswert $f(x,y)$ beliebig wenig von $f(x_0,
y_0)$ unterscheidet, sobald sich der Punkt $(x,y)$ in einer hinreichend kleinen
Umgebung des Punktes $(x_0, y_0)$ befindet.

In der grafischen Darstellung als Fläche im dreidimensionalen Raum bedeutet
dies, dass die Fläche keine "Löcher" oder "Sprünge" aufweist.

Betrachten wir die Funktion

$$f(x,y) =
\begin{cases}
\frac{xy}{x^2 + y^2}, & \text{falls } (x,y) \neq (0,0) \\
0, & \text{falls } (x,y) = (0,0)
\end{cases}$$

Diese Funktion ist an der Stelle $(0,0)$ nicht stetig. Um dies zu zeigen,
betrachten wir Annäherungen an den Ursprung entlang verschiedener Wege:

1. Entlang der $x$-Achse ($y = 0$): $\lim_{x \to 0} f(x,0) = \lim_{x \to 0}
   \frac{x \cdot 0}{x^2 + 0^2} = 0$
2. Entlang der $y$-Achse ($x = 0$): $\lim_{y \to 0} f(0,y) = \lim_{y \to 0}
   \frac{0 \cdot y}{0^2 + y^2} = 0$
3. Entlang der Geraden $y = x$: $\lim_{x \to 0} f(x,x) = \lim_{x \to 0} \frac{x
   \cdot x}{x^2 + x^2} = \lim_{x \to 0} \frac{x^2}{2x^2} = \frac{1}{2}$

Da die Grenzwerte je nach Annäherungsweg unterschiedlich sind, existiert kein
eindeutiger Grenzwert für $(x,y) \to (0,0)$. Daher ist die Funktion an der
Stelle $(0,0)$ nicht stetig.

```{code-cell}
:tags: [remove-input]
import numpy as np
import plotly.graph_objects as go

def f(x, y):
    """
    Die unstetige Funktion f(x,y) = xy/(x^2 + y^2) für (x,y) ≠ (0,0) und f(0,0) = 0
    """
    # Erstelle eine Kopie des Ergebnisses, um die ursprünglichen Arrays nicht zu verändern
    result = np.zeros_like(x, dtype=float)
    # Berechne die Funktion für alle Punkte außer (0,0)
    # Verwende eine Maske, um Punkte zu identifizieren, die nicht (0,0) sind
    mask = (x != 0) | (y != 0)
    result[mask] = (x[mask] * y[mask]) / (x[mask]**2 + y[mask]**2)
    # Der Wert an (0,0) ist definiert als 0
    # Da result bereits mit Nullen initialisiert wurde, müssen wir nichts mehr tun
    return result

# Gitterparameter
n = 100  # Anzahl der Punkte in jeder Dimension
x_min, x_max = -1.0, 1.0
y_min, y_max = -1.0, 1.0

# Erstelle das Gitter
x = np.linspace(x_min, x_max, n)
y = np.linspace(y_min, y_max, n)
X, Y = np.meshgrid(x, y)

# Berechne die Funktionswerte
Z = f(X, Y)

# Begrenze die Werte für eine bessere Visualisierung
# Die Funktion kann extreme Werte nahe der Singularität annehmen
Z = np.clip(Z, -1, 1)

# Erstelle eine interaktive 3D-Darstellung mit Plotly
fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='viridis')])

# Passe das Layout an
fig.update_layout(
    title='3D-Darstellung der unstetigen Funktion f(x,y) = xy/(x² + y²)',
    scene=dict(
        xaxis_title='x-Achse',
        yaxis_title='y-Achse',
        zaxis_title='f(x,y)',
        zaxis=dict(range=[-1, 1]),  # Begrenze die z-Achse
        aspectratio=dict(x=1, y=1, z=0.8),
        camera=dict(
            eye=dict(x=1.5, y=1.5, z=1.2)  # Anpassung der Kameraposition
        )
    ),
    width=800,
    height=800,
    margin=dict(l=65, r=50, b=65, t=90)
)

# Zeige die Figur an
fig.show()
```

Bei Funktionen mehrerer Variablen gilt wie bei Funktionen einer Variablen: Jede
differenzierbare Funktion ist auch stetig. Umgekehrt ist jedoch eine stetige
Funktion nicht notwendigerweise differenzierbar.

Im nächsten Kapitel werden wir uns mit der Differenzierbarkeit von Funktionen
mehrerer Variablen befassen. Die Stetigkeit ist hierfür eine notwendige
Voraussetzung.

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir das Konzept der Stetigkeit für Funktionen mehrerer
Variablen eingeführt. Eine Funktion ist stetig an einer Stelle, wenn der
Grenzwert der Funktion für alle Annäherungswege an diese Stelle existiert und
mit dem Funktionswert an dieser Stelle übereinstimmt. Im nächsten Kapitel werden
wir auf dem Konzept der Stetigkeit aufbauen und die Differenzierbarkeit von
Funktionen mehrerer Variablen untersuchen, die für die Berechnung von
Änderungsraten und die Optimierung technischer Systeme von zentraler Bedeutung
ist.
