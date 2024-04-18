# 8.3 Jacobi-Matrix

Der Gradient einer skalarwertigen Funktion entspricht bei vektorwertigen Funktionen der Jacobi-Matrix.

## Lernziele

```{admonition} Lernziel
:class: goals
Sie wissen, wie die **Jacobi-Matrix** einer vektorwertigen Funktion berechnet wird.
```

## Jacobi-Matrix einer vektorwertigen Funktion

Die Jacobi-Matrix einer vektorwertigen Funktion von mehreren Variablen ist eine
Matrix, die genau wie der Gradient alle partiellen Ableitungen einsammelt. Da
aber die Funktionswerte der Matrix selbst Vektoren sind, entsteht eine Matrix.

Kochrezept zur Berechnung der Jacobi-Matrix:
* Interpretiere die vektorwertige Funktion zeilenweise als skalarwertige
  Funktion.
* Bilde den Gradienten für jede Zeile.
* Schreibe die Gradienten untereinander in eine Matrix. 

Die Jacobi-Matrix ist sozusagen die Erweiterung des Gradienten für
*vektor*wertige Funktion von mehreren Variablen.

```{dropdown} Video zu "Jacobi-Matrix" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/FqaCPP8OZWU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Beispiel einer Jacobi-Matrix

Wir schauen uns an dem folgenden Beispiel an, wie die Jacobi-Matrix der
vektorwertigen Funktion

$$f:\mathbb{R}^3\longrightarrow\mathbb{R}^2 \quad \text{mit} \quad
f(x,y,z)=\begin{pmatrix} x^2 + y^3 + \sin(z) \\ z^2\end{pmatrix}$$

berechnet wird.

Schritt 1: Die erste Zeile enthält die Funktion $f_1(x,y,z)=x^2 + y^3 + \sin(z)$ mit dem
Gradienten 

$$\nabla f_1(x,y,z) = \left(2x , 3y^2, \cos(z)\right).$$

Schritt 2: Die zweite Zeile enthält die Funktion $f_2(x,y,z)=z^2$ mit dem Gradienten

$$\nabla f_2(x,y,z) = \left(0, 0, 2z\right).$$

Schritt 3: Aus beiden Zeilen wird dann die Matrix zusammengesetzt, die Jacobi-Matrix
lautet also 

$$J(f)(x,y,z)=
\begin{pmatrix} 
2x & 3x^2 & \cos(z)\\ 
0 & 0 & 2z
\end{pmatrix}.
$$

Weitere Beispiele finden Sie in den folgenden Videos.

```{dropdown} Video zu "Jacobi-Matrix Beispiel 1" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/LiFyUo6snK8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Jacobi-Matrix aufstellen" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/kMizXsfSK2o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

