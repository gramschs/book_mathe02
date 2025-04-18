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
mathematisch gesehen eine Funktion von mehereren Variablen, nämlich Längen- und
Breitengrad, also $f:\mathbb{R}^2\rightarrow\mathbb{R}$.

```{figure} pics/chapter07_fig01_solar_map.png
---
width: 50%
name: chapter07_fig01_solar_map
---
Solarstrahlung in Deutschland

([Quelle:](https://commons.wikimedia.org/wiki/File:SolarGIS-Solar-map-Germany-de.png) "Solar Radiation Map: Globalstrahlung Deutschland, SolarGIS 2011", Autor: SolarGIS Lizenz: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/))
```

In diesem Kapitel werden wir uns Funktionen von mehreren unabhängigen Variablen
genauer ansehen und insbesondere erarbeiten, wie solche Funktionen visualisiert
werden können.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können erklären, was eine **Funktion von mehreren unabhängigen Variablen** ist. 
* Sie können eine Funktion von zwei unabhängigen Variablen als Fläche im Raum zeichnen.
* Sie können die **Höhenlinien** einer Funktion von zwei unabhängigen Variablen interpretieren und zeichnen.
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

```{figure} pics/chapter07_plot_parabel.svg
---
width: 75%
name: chapter07_plot_parabel
---
Grafische Darstellung der Funktion $f(x)=x^2$
```

Anhand der grafischen Darstellung wird schnell deutlich, dass zwar die
Definitionsmenge alle reellen Zahlen umfasst, die Wertemenge jedoch nur die
nichtnegativen reellen Zahlen enthält.

## Funktionen von mehreren unabhängigen Variablen

Nun betrachten wir ein Beispiel einer "2:1-Beziehung". Auch hier benötigen wir,
um die Funktion zu beschreiben, eine Definitionsmenge, eine Wertemenge und eine
eindeutige Zuordnungsregel. Der flapsige Ausdruck "2:1-Beziehung" bedeutet, dass
zwei Elementen der Definitionsmenge ein Element der Wertemenge zugeordnet werden
soll. Die Elemente der Definitionsmenge werden auch **unabhängige Variablen**
genannt, das Element der Wertemenge wird **abhängige Variable** genannt.

Wir nennen die beiden unabhängigen Variablen $x$ und $y$ und legen fest, dass
beides reelle Zahlen sind. Diesmal sollen beide Zahlen quadriert werden und aus
den Quadraten dann die Summe gebildet werden. Mathematisch könnte das als

$$(x,y)\mapsto x^2 + y^2$$

oder als

$$f(x,y) = x^2 + y^2$$

notiert werden. Die abhängige Variable $z = f(x,y)$ ist 0 oder positiv, so dass
die Wertemenge gleich $\mathbb{R}^{+}$ ist.

Wenn die Funktion mehrere unabhängige Variablen hat, nennt man die Funktion auch
**multivariate Funktion**.

```{dropdown} Video zu "multivariate Funktionen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/gV5zjtVHIWE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

Fassen wir zusammen.

```{admonition} Was ist ... eine Funktion mit mehreren unabhängigen Variablen?
:class: note
Eine Funktion ist eine eindeutige Regel, die jedem Vektor aus mehreren
unabhängigen Variablen (aus der Definitionsmenge) genau eine reelle Zahl (aus
der Wertemenge) zuordnet.
```

## Darstellungen von Funktionen mit mehreren unabhängigen Variablen

Um das obige Beispiel Funktion zu visualisieren, werden jetzt alle mögliche
Kombinationen aus $x$ und $y$ gebildet, d.h. die unabhängigen Variablen kommen
aus der xy-Ebene. Zur Darstellung der abhängigen Variable brauchen wir also noch
eine dritte Dimension, die Höhe. Die Funktion $f(x,y) =  x^2 + y^2$, ein
sogenannter Paraboloid, sieht dann folgendermaßen aus (Hinweis: die Grafik ist interaktiv!):

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

Zusätzlich zur Höhe wurde die Paraboloid-Fläche noch gemäß der Funktionswerte
$f(x,y)$ eingefärbt. Leider ist es gar nicht so einfach, Funktionen von mehreren
Variablen zu zeichnen. Eine Funktion von zwei Variablen kann man noch ganz gut
zeichnen, bei drei und gar mehr unabhängigen Variablen klappt es mit Zeichnungen
nicht mehr.

```{dropdown} Video "Multivariate Funktionen: Graph" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/oJdN_Ics6qs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Höhenlinien

Eine reduzierte Darstellung einer Funktion von zwei unabhängigen Variablen ist
der sogenannte **Contourplot**, der **Konturlinien** visualisiert. Konturlinien
sind auch aus dem Erdkundeunterricht bekannt, wo sie normalerweise
**Höhenlinien** genannt werden.

```{admonition} Was sind ... Höhenlinien?
:class: note
Höhenlinien sind Linien in einer zweidimensionalen Ebene, die diejenigen Punkte $(x,y)$
verbinden, die den gleichen Funktionswert $f(x,y)=c$ haben.  
```

Das folgende Video erklärt den Contourplot.

```{dropdown} Video "Contourplot" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/t4N7n_u8TYk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
