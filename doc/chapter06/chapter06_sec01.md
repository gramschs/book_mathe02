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

# 6.1 Definition und Visualisierung

Bisher haben wir nur Funktionen kennengelernt, bei denen eine reelle Zahl in die
Funktionsvorschrift eingesetzt wurde und eine reelle Zahl herauskam. Die
mathematische Schreibweise dafür ist $f:\mathbb{R}\rightarrow\mathbb{R}$.

Allerdings ist die Welt nicht so eindimensional. Die folgende Abbildung zeigt
beispielsweise die durchschnittliche Solarstrahlung in Deutschland. Dies ist
mathematisch gesehen eine Funktion von mehreren Variablen, nämlich Längen- und
Breitengrad, also $f:\mathbb{R}^2\rightarrow\mathbb{R}$.

```{figure} pics/chapter06_fig01_solar_map.png
---
width: 50%
name: chapter06_fig01_solar_map
---
Solarstrahlung in Deutschland

([Quelle:](https://commons.wikimedia.org/wiki/File:SolarGIS-Solar-map-Germany-de.png) "Solar Radiation Map: Globalstrahlung Deutschland, SolarGIS 2011", Autor: SolarGIS Lizenz: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/))
```

In diesem Kapitel werden wir uns Funktionen von mehreren unabhängigen Variablen
genauer ansehen und insbesondere erarbeiten, wie solche Funktionen visualisiert
werden können. Diese Art von Funktionen begegnet Ingenieuren im Maschinenbau
täglich, zum Beispiel bei der Analyse von Temperaturverteilungen in Bauteilen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können erklären, was eine **Funktion von mehreren unabhängigen Variablen**
  ist. 
* Sie können eine Funktion von zwei unabhängigen Variablen als Fläche im Raum
  zeichnen.
* Sie können die **Höhenlinien** einer Funktion von zwei unabhängigen Variablen
  interpretieren und zeichnen.
```

## Wiederholung: Begrifflichkeiten bei Funktionen

Eine Funktion stellt eine Beziehung zwischen zwei Mengen her. Bei den bisher
eingeführten Funktionen wird ein Element aus der sogenannten Definitionsmenge
genommen und diesem genau ein Element aus der sogenannten Wertemenge zugeordnet.
Wenn es darum geht, nun die Regeln dieser Beziehung genauer zu beschreiben, wird
häufig eine Funktionsgleichung aufgestellt. Aber auch Tabellen oder grafische
Abbildungen können dazu benutzt werden, um die Beziehung präzise zu beschreiben.

Als Beispiel einer Funktion betrachten wir die Parabel. Als Definitionsmenge
wählen wir alle reelle Zahlen, also alle Zahlen $x\in\mathbb{R}$. Als
Funktionsvorschrift legen wir nun fest, dass jedem $x$ sein eigenes Quadrat
zugeordnet wird, also in mathematischer Schreibweise

$$x\mapsto x^2.$$

Üblicherweise wird die Funktionsvorschrift als $f(x)=x^2$ angegeben. Die
grafische Darstellung sieht folgendermaßen aus:

```{figure} pics/chapter06_plot_parabel.svg
---
width: 75%
name: chapter06_plot_parabel
---
Grafische Darstellung der Funktion $f(x)=x^2$
```

Anhand der grafischen Darstellung wird schnell deutlich, dass zwar die
Definitionsmenge alle reellen Zahlen umfasst, die Wertemenge jedoch nur die
nichtnegativen reellen Zahlen enthält.

## Funktionen von mehreren unabhängigen Variablen

Nun betrachten wir ein Beispiel einer Funktion mit mehreren Eingabegrößen. Auch
hier benötigen wir, um die Funktion zu beschreiben, eine Definitionsmenge, eine
Wertemenge und eine eindeutige Zuordnungsregel. Während wir bisher Funktionen
mit einer einzelnen Eingabegröße betrachtet haben, sollen nun mehrere Elemente
der Definitionsmenge gemeinsam einem Element der Wertemenge zugeordnet werden.
Die Elemente der Definitionsmenge werden auch **unabhängige Variablen** genannt,
das Element der Wertemenge wird **abhängige Variable** genannt.

Ein typisches Beispiel aus dem Maschinenbau ist die Temperaturverteilung in
einem Bauteil. Die Temperatur $T$ an einem bestimmten Punkt hängt von den
Raumkoordinaten $(x, y, z)$ ab, also $T = f(x, y, z)$. Dies ist eine Funktion
mit drei unabhängigen Variablen, die einem Punkt im Raum einen Temperaturwert
zuordnet.

Für den einfacheren Fall mit zwei unabhängigen Variablen nennen wir diese $x$
und $y$ und legen fest, dass beides reelle Zahlen sind. Wir definieren nun eine
Funktion, die jedem Wertepaar $(x,y)$ einen Funktionswert zuordnet.

```{admonition} Was ist ... eine multivariate Funktion?
:class: note
Eine multivariate Funktion $f: \mathbb{R}^n \rightarrow \mathbb{R}$ ist eine
Vorschrift, die jedem Punkt $(x_1, x_2, \ldots, x_n) \in \mathbb{R}^n$ aus der
Definitionsmenge genau einen Wert $f(x_1, x_2, \ldots, x_n) \in \mathbb{R}$ aus
der Wertemenge zuordnet.
```

Als konkretes Beispiel betrachten wir die Funktion, die jedem Punkt $(x,y)$ die
Summe der Quadrate zuordnet. Diese lässt sich in der mathematischen Notation auf
zwei äquivalente Arten darstellen:

1. als Abbildungsvorschrift: $(x,y) \mapsto x^2 + y^2$ oder
2. als Funktionsgleichung: $f(x,y) = x^2 + y^2$.

Die abhängige Variable $z = f(x,y)$ kann nur Werte größer oder gleich Null
annehmen, sodass die Wertemenge gleich $\mathbb{R}_{0}^{+} = \{z \in \mathbb{R}
\mid z \geq 0\}$ ist.

Das folgende Video erklärt multivariate Funktionen.

```{dropdown} Video "multivariate Funktionen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/gV5zjtVHIWE"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Darstellungen von Funktionen mit mehreren unabhängigen Variablen

Für die Darstellung von multivariaten Funktionen gibt es verschiedene
Möglichkeiten. Hier betrachten wir zwei Alternativen zur Darstellung von
Funktionen $f:\mathbb{R}^2 \rightarrow \mathbb{R}$, nämlich die 3D-Darstellung
als Fläche im Raum und Höhenlinien.

### 3D-Darstellung als Fläche im Raum

Um das obige Beispiel der Funktion $f(x,y) = x^2 + y^2$ zu visualisieren,
betrachten wir alle möglichen Kombinationen aus $x$ und $y$, d.h., die
unabhängigen Variablen kommen aus der $xy$-Ebene. Zur Darstellung der abhängigen
Variable $z = f(x,y)$ benötigen wir eine dritte Dimension, die Höhe.

Die Funktion $f(x,y) = x^2 + y^2$ beschreibt einen sogenannten Paraboloid, der
folgendermaßen aussieht (Hinweis: Die Grafik ist interaktiv und kann durch
Klicken und Ziehen gedreht werden):

```{code-cell}
:tags: [remove-input]
import numpy as np
import plotly.graph_objects as go

# generate grid
r = np.linspace(0, 5, 101)
phi = np.linspace(0, 2*np.pi, 101)
grid_r, grid_phi = np.meshgrid(r, phi) 
x = grid_r * np.cos(grid_phi)
y = grid_r * np.sin(grid_phi)

# evaluate function
z = 0.5 * (x**2 + y**2) 

# plot
fig = go.Figure()
fig.add_trace(go.Surface(z=z, x=x, y=y, colorscale='viridis'))
fig.update_layout(title='Paraboloid f(x,y)=x^2 + y^2', 
xaxis_title='x-Achse', yaxis_title='y-Achse')
```

Zusätzlich zur Höhe wurde die Paraboloid-Fläche gemäß der Funktionswerte
$f(x,y)$ eingefärbt. Die Farbskala rechts gibt an, welche Farbe welchem
Funktionswert entspricht. Die Visualisierung von Funktionen mit mehr als zwei
unabhängigen Variablen stellt eine Herausforderung dar, da wir nur drei
räumliche Dimensionen zur grafischen Darstellung nutzen können. Es gibt jedoch
alternative verschiedene Techniken, um multivariate Funktionen zu visualisieren,
wie wir gleich sehen werden.

```{dropdown} Video "Multivariate Funktionen: Graph" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/oJdN_Ics6qs"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

### Höhenlinien

Eine alternative Darstellung einer Funktion von zwei unabhängigen Variablen ist
der sogenannte **Contourplot** oder das **Konturliniendiagramm**. Konturlinien
sind auch aus dem Erdkundeunterricht bekannt, wo sie normalerweise
**Höhenlinien** genannt werden.

```{admonition} Was sind ... Höhenlinien?
:class: note
Höhenlinien sind Linien in einer zweidimensionalen Ebene, die diejenigen Punkte
$(x,y)$ verbinden, die den gleichen Funktionswert $f(x,y)=c$ haben, wobei $c$
eine Konstante ist.
```

Höhenlinien bieten eine zweidimensionale Darstellung einer dreidimensionalen
Fläche. Liegen Höhenlinien eng beieinander, so ist die Steigung der Fläche in
diesem Bereich steil; liegen sie weit auseinander, ist die Steigung flach.

Das folgende Beispiel zeigt die Höhenlinien der zuvor dargestellten Funktion
$f(x,y) = x^2 + y^2$:

```{code-cell}
:tags: [remove-input]
import numpy as np
import matplotlib.pyplot as plt

# Erzeuge x-y-Gitter
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Berechne Funktionswerte
Z = X**2 + Y**2

# Erstelle Contourplot
plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, Z, levels=np.linspace(0, 25, 11), cmap='viridis')
plt.colorbar(contour, label='f(x,y) = x² + y²')
plt.title('Höhenlinien der Funktion f(x,y) = x² + y²')
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.grid(True)
plt.axis('equal')
plt.show()
```

Die kreisförmigen Höhenlinien in dieser Darstellung zeigen, dass die Funktion
$f(x,y) = x^2 + y^2$ für alle Punkte $(x,y)$ mit gleichem Abstand vom Ursprung
denselben Wert annimmt. Dies entspricht dem rotationssymmetrischen Paraboloid,
das wir in der 3D-Darstellung gesehen haben.

Das folgende Video erklärt den Contourplot.

```{dropdown} Video "Contourplot" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/t4N7n_u8TYk"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir Funktionen mit mehreren unabhängigen Variablen
kennengelernt. Wir haben gesehen, wie sich solche Funktionen mathematisch
beschreiben lassen und wie sie visualisiert werden können, entweder als Fläche
im dreidimensionalen Raum oder mithilfe von Höhenlinien in der Ebene. Im
nächsten Kapitel werden wir uns mit der Stetigkeit von Funktionen mehrerer
Variablen beschäftigen.
