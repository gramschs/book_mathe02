# Gradient und Jacobi-Matrix

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

Mit den partiellen Ableitungen haben wir Ableitungen kennengelernt, die in Richtung des Achsen des Koordinatensystems gehen. In diesem Kapitel beschäftigen wir uns mit dem **Gradienten**, der die partiellen Ableitungen als Vektor zusammenfasst und sozusagen den Ersatz für die erste Ableitung bei Funktionen mit mehreren Variablen bildet.
Als zweites Thema werden uns vektorwertige Funktionen beschäftigen. Das Analogon zur ersten Ableitung von vektorwertigen Funktionen ist die **Jacobi-Matrix**. Mit Hilfe von Jacobi-Matrizen kann die **mehrdimensionale Kettenregel** formuliert werden.



## Lernziele 

```{admonition} Lernziele
:class: tip
* Sie können den Unterschied zwischen einer **skalarwertigen Funktion** und einer **vektorwertigen Funktion** erklären.
* Sie können den **Gradienten** einer skalarwertigen Funktion berechnen und wissen, dass man den Gradienten meist mit dem Zeichen **Nabla** $\nabla$ abkürzt. 
* Sie können die **Jacobi-Matrix** einer vektorwertigen Funktion berechnen.
* Sie kennen die **mehrdimensionale Kettenregel** und können sie anwenden.
```


## Skalarwertige und vektorwertige Funktionen

In dem letzten Kapitel haben wir eindimensionale Funktionen $f:\mathbb{r}\rightarrow \mathbb{R}$ auf mehrdimensionale Funktionen erweitert $f:\mathbb{R}^n\rightarrow\mathbb{R}$ erweitert. Ein Beispiel aus dem Alltag ist die Wetterkarte mit den prognostizierten Durchschnittstemperaturen für den morgigen Tag. Zu jeder Position spezifiziert durch den Breiten- und den Längengrad gibt es eine Temperatur. Die Temperatur ist eine sogenannte **skalare Größe**, denn sie wird durch eine einzelne Zahl dargestellt. Gerade bei Unwetterwarnungen sind jedoch auch Darstellungen des Windfeldes üblich. Zu jeder Position mit Längen- und Breitengrad wird eine Windrichtung angegeben, also eine **vektorielle Größe**. In den Wetterkarten wird dazu häufig ein Pfeil eingezeichnet ähnlich zu folgenden Abbildung.


```{figure} pics/part07_vektorfeld.svg
---
width: 300px
name: fig_part07_vektorfeld
---
Visualisierung eines Vektorfeldes ([Quelle:](https://commons.wikimedia.org/wiki/File:VectorField.svg) "A portion of the vector field (sin y, sin x)" von Jim.belk. Lizenz: gemeinfrei)
```


Wir unterscheiden Funktionen also nicht nur nach der Anzahl ihrer Variablen, sondern auch danach, ob die Funktionswerte ein- oder mehrdimensional sind. Wir verwenden zur Unterschiedung der beiden Kategorien die folgenden Fachbegriffe.


````{prf:definition} Was ist ... eine skalarwertige Funktion?
:label: def:07:01
Eine skalarwertige Funktion ist eine Funktion, deren Funktionswerte reelle Zahlen sind. 

Die mathematische Notation dafür ist $f:\mathbb{R}^m \rightarrow \mathbb{R}$, wobei $m$ sowohl 1 (eindimensional) als auch $\geq 2$ (mehrdimensional) sein kann.
````


````{prf:definition} Was ist ... eine vektorwertige Funktion?
:label: def:07:02
Eine vektorwertige Funktion ist eine Funktion, deren Funktionswerte Vektoren sind. 

Die mathematische Notation dafür ist $f:\mathbb{R}^m \rightarrow \mathbb{R}^n$, wobei $m$ sowohl 1 (eindimensional) als auch $\geq 2$ (mehrdimensional) sein kann. Aber $n$ muss mindestens 2 sein, sonst wäre es ja eine skalarwertige Funktion.
````


## Der Gradient

Der Gradient einer skalarwertigen Funktion von mehreren Variablen ist der Zeilenvektor, in dem alle partiellen Ableitungen gesammelt werden. Als Abkürzung für den Gradienten vwerwenden wir das Symbol Nabla:

$$\nabla f(x,y,z) = \left(\frac{\partial f(x,y,z)}{\partial x}, \frac{\partial f(x,y,z)}{\partial y}, \frac{\partial f(x,y,z)}{\partial z} \right).$$

Manchmal wird auch die Schreibweise $\text{grad}f(x,y,z)$ verwendet. Der Gradient ist sozusagen die 1. Ableitung einer *skalar*wertigen Funktion von mehreren Variablen.

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/627f_DgQJpY
```

## Jacobi-Matrix einer vektorwertigen Funktion

Die Jacobi-Matrix einer vektorwertigen Funktion von mehreren Variablen ist eine Matrix, die genau wie der Gradient alle partiellen Ableitungen einsammelt. Da aber die Funktionswerte der Matrix selbst Vektoren sind, entsteht eine Matrix.

Kochrezept zur Berechnung der Jacobi-Matrix:
* Interpretiere die vektorwertige Funktion zeilenweise als skalarwertige Funktion.
* Bilde den Gradienten für jede Zeile.
* Schreibe die Gradienten untereinander in eine Matrix. 

Die Jacobi-Matrix ist sozusagen die 1. Ableitung einer *vektor*wertigen Funktion von mehreren Variablen.

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/FqaCPP8OZWU
```

## Beispiel einer Jacobi-Matrix

Wir schauen uns an dem folgenden Beispiel an, wie die Jacobi-Matrix der vektorwertigen Funktion

$$f:\mathbb{R}^3\longrightarrow\mathbb{R}^2 \quad \text{mit} \quad f(x,y,z)=\begin{pmatrix} x^2 + y^3 + \sin(z) \\ z^2\end{pmatrix}$$

berechnet wird.

1. Die erste Zeile enthält die Funktion $f_1(x,y,z)=x^2 + y^3 + \sin(z)$ mit dem Gradienten
$\left(2x , 3y^2, \cos(z)\right).$
2. Die zweite Zeile enthält die Funktion $f_2(x,y,z)=z^2$ mit dem Gradienten
$\left(0, 0, 2z\right).$
3. Aus beiden Zeilen wird dann die Matrix zusammengesetzt, die Jacobi-Matrix lautet also
$$J(f)(x,y,z)=\begin{pmatrix} 2x & 3x^2 & \cos(z)\\ 0 & 0 & 2z \end{pmatrix}.$$

Weitere Beispiele finden Sie in den folgenden Videos.

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/LiFyUo6snK8
```

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/kMizXsfSK2o
```

## Mehrdimensionale Kettenregel

Zur Erinnerung, die eindimensionale Kettenregel lautet wie folgt:
Die Ableitung der verketten Funktion $f(g(x))$ ist äußere Ableitung mal innere Ableitung, d.h.

$$f(g(x))' = f'(g(x))\cdot g'(x).$$

Mit den Jacobi-Matrizen können wir die mehrdimensionale Kettenregel nun wie folgt formulieren:

Die Jacobi-Matrix der verketten Funktionen $f(g(x,y,z))$ ist Jacobi-Matrix der äußeren Funktion mal Jacobi-Matrix der inneren Funktion, d.h.

$$J(f(g(x,y,z)) = J(f) \cdot J(g).$$

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/LkWAGcGGDD8
```
