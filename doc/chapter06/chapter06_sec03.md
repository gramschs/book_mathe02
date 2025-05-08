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

# 6.3 Partielle Ableitungen und Gradient

In den vorherigen Kapiteln haben wir Funktionen mehrerer Variablen kennengelernt
und den Begriff der Stetigkeit auf solche Funktionen erweitert. Nun befassen wir
uns mit der Frage, wie das Konzept der Ableitung auf Funktionen mehrerer
Variablen übertragen werden kann. Bei Funktionen einer Variablen gibt die
Ableitung die Änderungsrate oder Steigung an einer bestimmten Stelle an. Bei
Funktionen mehrerer Variablen müssen wir berücksichtigen, dass die Änderungsrate
von der Richtung abhängt, in der wir uns bewegen. Hier kommt der Begriff der
partiellen Ableitung ins Spiel.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können den Begriff der **partiellen Ableitung** einer Funktion mehrerer
  Variablen erklären und verstehen seine geometrische Bedeutung.
* Sie können partielle Ableitungen von Funktionen mehrerer Variablen berechnen.
* Sie verstehen die Bedeutung des **Gradienten** als Richtung des steilsten
  Anstiegs.
* Sie können den Gradienten einer Funktion mehrerer Variablen berechnen und
  interpretieren.
```

## Partielle Ableitungen

Stellen Sie sich vor, wir betrachten eine hügelige Landschaft, die durch eine
Funktion $f: \mathbb{R}^2 \rightarrow \mathbb{R}$ repräsentiert wird, wobei $x$
und $y$ die Koordinaten auf der horizontalen Ebene sind und $f(x,y)$ die Höhe an
der Position $(x,y)$ angibt. Nun möchten wir wissen, wie sich die Höhe ändert,
wenn wir uns in Richtung der x-Achse bewegen, während wir die y-Koordinate
konstant halten.

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
<iframe width="560" height="315" src="https://www.youtube.com/embed/4ppZE30P2Yw"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video "Partielle Ableitung Definition" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/KqpLPQvboPY"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
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

$$h(y) = c^3 + y^3 - c^2 + 2y^2 - 5c + y + 3.$$

Diese Funktion nach $y$ abgeleitet ergibt

$$h'(y) = 0 + 3y^2 - 0 + 4y - 0 + 1 + 0.$$

Somit ist die 1. partielle Ableitung der Funktion $f$ nach $y$

$$\frac{\partial f(x,y)}{\partial y} = 3y^2 + 4y + 1.$$

```{dropdown} Video "Partielle Ableitung einfach erklärt" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/N0Y9E0wdLKk"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Gradient

Die partiellen Ableitungen sind unabhängig voneinander. Kehren wir zu dem
Beispiel mit der Hügellandschaft zurück. Mit Hilfe der partiellen Ableitung nach
$x$ kann die Steigung in x-Richtung bestimmt werden, mit der partiellen
Ableitung nach $y$ die Steigung in die $y$-Richtung. Fassen wir beide Steigungen
in einem Vektor zusammen, zeigt der Vektor in die Richtung des steilsten
Anstiegs und seine Länge entspricht dem Betrag der Steigung in diese Richtung.

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

Für die Funktion $f(x,y) = x^3 + y^3 - x^2 + 2y^2 - 5x + y + 3$ haben wir die
partiellen Ableitungen bereits berechnet.

$$\frac{\partial f}{\partial x}(x,y) = 3x^2 - 2x - 5$$
$$\frac{\partial f}{\partial y}(x,y) = 3y^2 + 4y + 1$$

Wir müssen die partiellen Ableitungen nur noch als Zeilenvektor aufschreiben, um
den Gradienten der Funktion zu bestimmen:

$$\nabla f(x,y) = \left(3x^2 - 2x - 5, 3y^2 + 4y + 1\right).$$

Zur Veranschaulichung berechnen wir den Gradienten an einigen spezifischen Punkten:

1. Am Punkt $(0,0)$:

  $$\nabla f(0,0) = (3 \cdot 0^2 - 2 \cdot 0 - 5,  3 \cdot 0^2 + 4 \cdot 0 + 1) = (-5, 1)$$
  
2. Am Punkt $(1,1)$:

  $$\nabla f(1,1) = (3 \cdot 1^2 - 2 \cdot 1 - 5, 3 \cdot 1^2 + 4 \cdot 1 + 1) =  (-4, 8)$$
  
3. Am Punkt $(2,-1)$:

  $$\nabla f(2,-1) = (3 \cdot 2^2 - 2 \cdot 2 - 5, 3 \cdot (-1)^2 + 4 \cdot (-1) + 1) = (3,0)$$

Der Gradient an einem bestimmten Punkt zeigt stets in die Richtung des steilsten
Anstiegs der Funktion an diesem Punkt. Der Betrag des Gradienten gibt die Stärke
(Steigung) dieses Anstiegs an. So ist beispielsweise am Punkt $(1,1)$ die
Steigung in Richtung des Gradienten

$$\|\nabla f(1,1)\| = \sqrt{(-4)^2 + 8^2} = \sqrt{16 + 64} = \sqrt{80} \approx
8.94.$$

```{code-cell}
:tags: [remove-input]
import numpy as np
import plotly.graph_objects as go

# Definiere die Funktion und ihre partiellen Ableitungen
def f(x, y):
    return x**3 + y**3 - x**2 + 2*y**2 - 5*x + y + 3

def df_dx(x, y):
    return 3*x**2 - 2*x - 5

def df_dy(x, y):
    return 3*y**2 + 4*y + 1

# Erstelle die Gitter für die Visualisierung
x = np.linspace(-2, 2, 40)
y = np.linspace(-2, 2, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Berechne den Gradienten an jedem Punkt
DX = df_dx(X, Y)
DY = df_dy(X, Y)

# Berechne den Betrag des Gradienten für die Farbkodierung
magnitude = np.sqrt(DX**2 + DY**2)

# Normalisiere die Gradientenvektoren für eine bessere Darstellung
# Verwende einen Skalierungsfaktor für die Pfeillänge
scale_factor = 0.2
norm = np.sqrt(DX**2 + DY**2)
norm[norm == 0] = 1  # Vermeide Division durch Null
DX_norm = DX / norm * scale_factor
DY_norm = DY / norm * scale_factor

# Dünne die Gitterpunkte aus, um die Darstellung übersichtlicher zu gestalten
skip = 2
X_sparse = X[::skip, ::skip]
Y_sparse = Y[::skip, ::skip]
DX_sparse = DX_norm[::skip, ::skip]
DY_sparse = DY_norm[::skip, ::skip]
magnitude_sparse = magnitude[::skip, ::skip]

# Erstelle die Figur mit einem einzelnen Plot
fig = go.Figure()

# Füge den Konturplot hinzu
fig.add_trace(
    go.Contour(
        z=Z,
        x=x,
        y=y,
        colorscale='viridis',
        showscale=True,
        contours=dict(
            start=-10,
            end=10,
            size=1,
            showlabels=True,
            labelfont=dict(
                size=10,
                color='white'
            )
        ),
        colorbar=dict(
            title='f(x,y)',
            titleside='right'
        )
    )
)

# Füge unsichtbare Marker für die Punkte hinzu, an denen die Gradientenvektoren gezeichnet werden
fig.add_trace(
    go.Scatter(
        x=X_sparse.flatten(),
        y=Y_sparse.flatten(),
        mode='markers',
        marker=dict(
            size=1,
            color='rgba(0,0,0,0)'
        ),
        showlegend=False
    )
)

# Füge Pfeile als Anmerkungen hinzu, um den Gradienten zu visualisieren
annotations = []
for i in range(X_sparse.shape[0]):
    for j in range(X_sparse.shape[1]):
        x_pos = X_sparse[i, j]
        y_pos = Y_sparse[i, j]
        dx = DX_sparse[i, j]
        dy = DY_sparse[i, j]
        #
        # Berechne die Farbe basierend auf dem Betrag des Gradienten
        # Wir verwenden eine Farbskala von Gelb bis Rot
        mag = magnitude_sparse[i, j]
        max_mag = 20  # Maximale erwartete Größe für die Farbskalierung
        #
        # Je stärker der Gradient, desto intensiver die Farbe
        intensity = min(mag / max_mag, 1.0)
        arrow_color = f'rgba(255, {int(255*(1-intensity))}, 0, 0.8)'
        #
        # Erstelle den Pfeil
        annotations.append(dict(
            x=x_pos,
            y=y_pos,
            ax=x_pos + dx,
            ay=y_pos + dy,
            xref="x",
            yref="y",
            axref="x",
            ayref="y",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=1.5,
            arrowcolor=arrow_color
        ))

# Füge die Pfeile zur Figur hinzu
fig.update_layout(annotations=annotations)

# Gestalte das Layout
fig.update_layout(
    title=dict(
        text='Visualisierung des Gradienten\nf(x,y) = x³ + y³ - x² + 2y² - 5x + y + 3',
        x=0.5,
        xanchor='center'
    ),
    xaxis=dict(
        title='x-Achse',
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor='black',
        showgrid=True,
        gridwidth=0.5,
        gridcolor='lightgray',
        range=[-2, 2]
    ),
    yaxis=dict(
        title='y-Achse',
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor='black',
        showgrid=True,
        gridwidth=0.5,
        gridcolor='lightgray',
        scaleanchor="x",  # Sorgt für gleiches Seitenverhältnis
        scaleratio=1,
        range=[-2, 2]
    ),
    height=600,
    width=600,
    plot_bgcolor='rgba(240, 240, 240, 0.5)',
    margin=dict(l=50, r=50, t=100, b=50),
    hovermode='closest'
)

# Füge eine Legende für die Stärke des Gradienten hinzu
legend_annotations = [
    dict(
        x=0.85,
        y=0.95,
        xref="paper",
        yref="paper",
        text="<b>Gradientenstärke:</b>",
        showarrow=False,
        font=dict(size=12)
    ),
    dict(
        x=0.85,
        y=0.90,
        xref="paper",
        yref="paper",
        text="Stark",
        showarrow=False,
        font=dict(color="rgb(255, 0, 0)", size=12)
    ),
    dict(
        x=0.85,
        y=0.85,
        xref="paper",
        yref="paper",
        text="Mittel",
        showarrow=False,
        font=dict(color="rgb(255, 128, 0)", size=12)
    ),
    dict(
        x=0.85,
        y=0.80,
        xref="paper",
        yref="paper",
        text="Schwach",
        showarrow=False,
        font=dict(color="rgb(255, 255, 0)", size=12)
    )
]

# Füge die Legende-Anmerkungen hinzu
for annotation in legend_annotations:
    fig.add_annotation(annotation)

# Zeige die Figur an
fig.show()
```

Der Gradient sowie ein weiteres Beispiel werden in den folgenden Videos
präsentiert.

```{dropdown} Video "Gradient" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/BbOUhSRh57I?si=750hDMUywwy1p2YZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video "Gradient" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/627f_DgQJpY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir das Konzept der partiellen Ableitung eingeführt, das
die Änderungsrate einer Funktion mehrerer Variablen in Richtung der
Koordinatenachsen beschreibt. Durch Zusammenfassung der partiellen Ableitungen
erhalten wir den Gradienten, der in Richtung des steilsten Anstiegs zeigt und
senkrecht auf den Höhenlinien steht. Im nächsten Kapitel wereden wir höhere
partielle Ableitungen behandeln.
