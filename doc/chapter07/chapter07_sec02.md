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

# 7.2 Vektorwertige Funktionen

## Lernziele

```{admonition} Lernziel
:class: goals
* Sie wissen, was eine **vektorwertige** Funktion bzw. ein **Vektorfeld** ist.
* Sie können vektorwertige Funktionen komponentenweise darstellen.
```

## Begrifflichkeiten

Bis jetzt haben wir Funktionen betrachtet, deren Funktionswert stets eine reelle
Zahl, also ein Skalar ist. Solche Funktionen nennen wir **skalarwertig**. So wie wir
beim Definitionsgebiet von einem eindimensionalen Definitionsgebiet $x\in
\mathbb{R}$ der reellen Zahlen zu Definitionsgebieten mit mehreren unabhängigen
Variablen, also Vektoren $\vec{x}\in\mathbb{R}^n$ mit $n \geq 2$ übergegangen
sind, können wir auch den Wertebereich von Funktionen erweitern. Wenn die
Funktionswerte einer Funktion Vektoren sind, so nennen wir die Funktion
**vektorwertig**.

```{admonition} Was ist ... eine vektorwertige Funktion?
:class: note
Eine vektorwertige Funktion ist eine Funktion, die Vektoren als Wertemenge bzw.
Funktionswerte hat. Jedem Punkt $\vec{x}\in\mathbb{R}^m$ wird eindeutig ein
Vektor $\mathbb{R}^n$ zugeordnet, in mathematischer Notation

$$f:\mathbb{R}^m \rightarrow \mathbb{R}^n.$$ 

Übrigens, in der Physik wird eine vektorwertige Funktion auch oft **Vektorfeld**
genannt.
```

Eine vektorwertige Funktion $\vec{f}: \mathbb{R}^m \rightarrow \mathbb{R}^n$
kann durch ihre Komponentenfunktionen dargestellt werden:

$$f(\vec{x}) =
\begin{pmatrix} f_1(\vec{x}) \\ f_2(\vec{x}) \\ \vdots \\ f_n(\vec{x}) \end{pmatrix}.$$

Jede Komponentenfunktion $f_i: \mathbb{R}^m \rightarrow \mathbb{R}$ ist dabei
eine skalarwertige Funktion.

```{dropdown} Video zu "Vektorwertige Funktionen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/KUSljbPOK78"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Beispiel einer vektorwertigen Funktion

Betrachten wir eine konkrete vektorwertige Funktion $f: \mathbb{R}^2
\rightarrow \mathbb{R}^3$, die jedem Punkt $(x,y)$ in der Ebene einen
dreidimensionalen Vektor zuordnet:

$$f(x,y) = \begin{pmatrix} x^2 - y \\ xy \\ x + y^2 \end{pmatrix}.$$

Diese Funktion hat drei Komponentenfunktionen:

* $f_1(x,y) = x^2 - y$
* $f_2(x,y) = xy$
* $f_3(x,y) = x + y^2$

Für den konkreten Punkt $(x,y) = (2,3)$ erhalten wir:

$$f(2,3) =
\begin{pmatrix} 2^2 - 3 \\ 2 \cdot 3 \\ 2 + 3^2 \end{pmatrix} =
\begin{pmatrix} 1 \\ 6 \\ 11 \end{pmatrix}.$$

Geometrisch interpretiert ordnet diese Funktion jedem Punkt der $xy$-Ebene einen Vektor im dreidimensionalen Raum zu.

In der folgenden Abbildung finden Sie eine Visualisierung der Funktion.
Allerdings können wir nicht zu jedem Punkt der $xy$-Ebene die Vektoren
darstellen, da wir dann nichts mehr erkennen würden. Wir beschränken uns für die
Visualisierung auf $x \in [-3,3]$ und $y \in [-3,3]$ und nehmen in beide
Richtungen Punkte mit einem Abstand von $\Delta x =\Delta y = 0.3$. Diese Punkte
sind durch kleine Kugeln gekennzeichnet. Die Richtung der Vektoren wird durch
Striche dargestellt, wobei die Länge der Striche nur 20 % der Länge der
Vektoren beträgt.

Zoomen Sie in die Grafik hinein und drehen Sie sie auch.

```{code-cell}
:tags: [remove-input]
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot

def vektorwertige_funktion(x, y):
    """Berechnet die vektorwertige Funktion f(x,y) = (x² - y, xy, x + y²)"""
    f1 = x**2 - y
    f2 = x * y
    f3 = x + y**2
    return np.array([f1, f2, f3])

"""Erstellt eine Visualisierung der vektorwertigen Funktion"""
# Definiere den Bereich
bereich = [-3, 3]
schrittweite = 0.3

# Erzeuge Gitter mit der gegebenen Schrittweite
x = np.arange(bereich[0], bereich[1] + 0.01, schrittweite)
y = np.arange(bereich[0], bereich[1] + 0.01, schrittweite)
X, Y = np.meshgrid(x, y)

# Arrays für Startpunkte
startX = X.flatten()
startY = Y.flatten()
startZ = np.zeros_like(startX)

# Arrays für die Vektoren
linien_x = []
linien_y = []
linien_z = []

# Arrays für Hover-Texte
hoverTexts = []

# Skalierungsfaktor für Vektorlängen
skalierungsfaktor = 0.2

# Berechne die Vektoren und erstelle Linien
for i in range(len(startX)):
    x_start = startX[i]
    y_start = startY[i]
    z_start = startZ[i]
    #
    # Berechne Vektor
    vektor = vektorwertige_funktion(x_start, y_start)
    vektor_betrag = np.linalg.norm(vektor)
    #
    # Hover-Text
    hoverTexts.append(f"Punkt: ({x_start:.1f}, {y_start:.1f})<br>f(x,y): ({vektor[0]:.1f}, {vektor[1]:.1f}, {vektor[2]:.1f})<br>|f(x,y)|: {vektor_betrag:.1f}")
    #
    # Normalisiere Vektor
    if vektor_betrag > 1e-10:
        richtung = vektor / vektor_betrag
    else:
        richtung = np.array([0, 0, 0])
    #
    # Skaliere Vektor
    pfeil_laenge = vektor_betrag * skalierungsfaktor
    #
    # Berechne Endpunkt
    x_end = x_start + richtung[0] * pfeil_laenge
    y_end = y_start + richtung[1] * pfeil_laenge
    z_end = z_start + richtung[2] * pfeil_laenge
    #
    # Füge Liniensegment hinzu
    linien_x.extend([x_start, x_end, None])
    linien_y.extend([y_start, y_end, None])
    linien_z.extend([z_start, z_end, None])

# Erstelle Figur
fig = go.Figure()

# Füge transparente xy-Ebene hinzu
fig.add_trace(
    go.Surface(
        x=np.array([-3.5, 3.5]),
        y=np.array([-3.5, 3.5]),
        z=np.zeros((2, 2)),
        opacity=0.25,
        showscale=False,
        colorscale=[[0, '#f3f4f4'], [1, '#f3f4f4']],
        name='xy-Ebene'
    )
)

# Füge Vektoren als Linien hinzu
fig.add_trace(
    go.Scatter3d(
        x=linien_x,
        y=linien_y,
        z=linien_z,
        mode='lines',
        line=dict(
            color='royalblue',
            width=2
        ),
        showlegend=False,
        hoverinfo='none'
    )
)

# Füge Startpunkte hinzu
fig.add_trace(
    go.Scatter3d(
        x=startX,
        y=startY,
        z=startZ,
        mode='markers',
        marker=dict(
            size=4,
            color='darkblue',
            opacity=0.8
        ),
        hoverinfo='text',
        hovertext=hoverTexts,
        showlegend=False
    )
)

# Layout-Anpassungen
fig.update_layout(
    title='Vektorwertige Funktion f(x,y) = (x² - y, xy, x + y²)',
    scene=dict(
        xaxis=dict(title='x', range=[-3.5, 3.5]),
        yaxis=dict(title='y', range=[-3.5, 3.5]),
        zaxis=dict(title='z', range=[-2.5, 3.5]),
        aspectmode='cube',
        camera=dict(
            eye=dict(x=1.6, y=1.6, z=0.9)
        )
    ),
    margin=dict(l=0, r=0, b=0, t=30),
    legend=dict(
        y=0.95,
        x=0.95
    )
)
```

Im Folgenden werden auch noch die drei skalarwertigen Komponentenfunktionen
einzeln dargestellt.

```{code-cell}
:tags: [remove-input]
import numpy as np
import plotly.graph_objects as go

def komponentenfunktion_1(x, y):
    """Erste Komponentenfunktion: f₁(x,y) = x² - y"""
    return x**2 - y

def komponentenfunktion_2(x, y):
    """Zweite Komponentenfunktion: f₂(x,y) = xy"""
    return x * y

def komponentenfunktion_3(x, y):
    """Dritte Komponentenfunktion: f₃(x,y) = x + y²"""
    return x + y**2

def erstelle_komponentenfigur(komponente_func, titel, bereich=[-3, 3], aufloesung=50, mit_farbskala=False):
    """
    Erstellt eine Visualisierung einer Komponentenfunktion
    Parameter:
    - komponente_func: Die Komponentenfunktion
    - titel: Titel für die Figur
    - bereich: Liste mit [min, max] für x und y
    - aufloesung: Anzahl der Punkte pro Dimension
    - mit_farbskala: Ob eine Farbskala angezeigt werden soll
    Rückgabe:
    - Plotly-Figur mit der Komponentenfunktion
    """
    # Erzeuge Gitter mit gegebener Auflösung
    x = np.linspace(bereich[0], bereich[1], aufloesung)
    y = np.linspace(bereich[0], bereich[1], aufloesung)
    X, Y = np.meshgrid(x, y)
    #
    # Berechne die Werte der Komponentenfunktion
    Z = komponente_func(X, Y)
    #
    # Erstelle eine neue Figur
    fig = go.Figure()
    #
    # Farbskala
    colorscale = 'Viridis'
    #
    # Surface-Plot für die Komponentenfunktion
    fig.add_trace(
        go.Surface(
            x=X,
            y=Y,
            z=Z,
            colorscale=colorscale,
            showscale=mit_farbskala,
            opacity=0.95,
            contours={
                "z": {"show": True, "start": np.min(Z), "end": np.max(Z), "size": (np.max(Z) - np.min(Z))/10}
            }
        )
    )
    #
    # Layout-Anpassungen
    camera = dict(
        eye=dict(x=1.6, y=-1.6, z=1.2),
        up=dict(x=0, y=0, z=1)
    )
    #
    # Achsenbeschriftungen extrahieren
    funktionsname = titel.split('=')[0].strip()
    #
    # Layout konfigurieren
    fig.update_layout(
        scene=dict(
            xaxis_title='x',
            yaxis_title='y',
            zaxis_title=funktionsname,
            aspectratio=dict(x=1, y=1, z=1),
            camera=camera
        ),
        margin=dict(l=0, r=0, b=0, t=50)
    )
    #
    return fig

def erstelle_drei_komponentenfiguren(bereich=[-3, 3], aufloesung=50):
    """
    Erstellt drei separate Figuren für die Komponentenfunktionen
    Parameter:
    - bereich: Liste mit [min, max] für x und y
    - aufloesung: Anzahl der Punkte pro Dimension
    Rückgabe:
    - Liste mit drei Plotly-Figuren
    """
    # Titel für die drei Figuren
    titel1 = 'f₁(x,y) = x² - y'
    titel2 = 'f₂(x,y) = xy'
    titel3 = 'f₃(x,y) = x + y²'
    #
    # Erstelle die drei separaten Figuren
    fig1 = erstelle_komponentenfigur(komponentenfunktion_1, titel1, bereich, aufloesung, True)
    fig2 = erstelle_komponentenfigur(komponentenfunktion_2, titel2, bereich, aufloesung, True)
    fig3 = erstelle_komponentenfigur(komponentenfunktion_3, titel3, bereich, aufloesung, True)  # Dritte Figur mit Farbskala
    #
    return fig1, fig2, fig3

# Ausführung in Jupyter Notebook
# Erstellt drei separate Figuren für die Komponentenfunktionen
fig1, fig2, fig3 = erstelle_drei_komponentenfiguren()
```

**1\. Komponentenfunktion:** $f_1(x,y) = x^2 - y$

```{code-cell}
:tags: [remove-input]
fig1.show()
```

**2\. Komponentenfunktion:** $f_2(x,y) = xy$

```{code-cell}
:tags: [remove-input]
fig2.show()
```

**3\. Komponentenfunktion:** $f_3(x,y) = x + y^2$

```{code-cell}
:tags: [remove-input]
fig3.show()
```

## Eigenschaften vektorwertiger Funktionen

Vektorwertige Funktionen besitzen ähnliche grundlegende Eigenschaften wie
skalarwertige Funktionen, insbesondere in Bezug auf Stetigkeit und
Differenzierbarkeit. Eine vektorwertige Funktion $f:\mathbb{R}^m \rightarrow
\mathbb{R}^n$ ist genau dann stetig in einem Punkt $\vec{x}_{0}$, wenn alle ihre
Komponentenfunktionen in diesem Punkt stetig sind. Analog ist eine vektorwertige
Funktion differenzierbar, wenn alle ihre Komponentenfunktionen differenzierbar
sind. Die Ableitungen werden dabei in der sogenannten Jacobi-Matrix
zusammengefasst, die wir im nächsten Kapitel behandeln werden.

## Zusammenfassung und Ausblick

Nachdem wir uns in diesem Kapitel prinzipiell mit vektorwertigen Funktionen
beschäftigt haben, werden wir uns im nächsten Kapitel mit der Ableitung einer
vektorwertigen Funktion beschäftigen.
