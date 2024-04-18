# Übungen

```{admonition} Übung 9.1
:class: miniexercise
Bestimmen Sie die Gleichung der Tangentialebene bzw. die Linearisierung für die Funktion

$$f:\mathbb{R}^2 \mapsto \mathbb{R}, \; f(x,y)=\frac{x^2+y^2}{1+x^2+y^2}$$

am Punkt $(1,2)$.
```
````{admonition} Lösung
:class: miniexercise, toggle

$$T_{f,1}(x,y)=\frac{5}{6}+\frac{1}{18}\cdot (x-1)+\frac{1}{9}\cdot (y-2)$$

```{dropdown} Lösungsweg
Das Taylorpolynom vom Grad 1 einer Funktion $f(x,y)$ bei $(x_0,y_0)$ hat die allgemeinen Form 

$$T_{f,1}(x,y)
 = f(x_0,y_0)+\frac{\partial f(x_0,y_0)}{\partial x}\cdot(x-x_0)+\frac{\partial f(x_0,y_0)}{\partial y}\cdot(y-y_0).$$

Der Funktionswert in Punkt $(1,2)$ ist $f(1,2) = \frac{5}{6}$. 
 
Die partiellen Ableitungen von $f$ lauten : 
 
\begin{align*}
\frac{\partial f(x,y)}{\partial x} &=
\frac{2x}{x^2+y^2+1} - \frac{2x \left(x^2+y^2\right)}{\left(x^2+y^2+1\right)^2} \\
\qquad \Rightarrow & \frac{\partial f(1,2)}{\partial x} = \frac{1}{18}\\
\frac{\partial f(x,y)}{\partial y} &=
\frac{2y}{x^2+y^2+1}-\frac{2y\left(x^2+y^2\right)}{\left(x^2+y^2+1\right)^2} \\
\qquad \Rightarrow & \frac{\partial f(1,2)}{\partial y} = \frac{1}{9}\\
\end{align*}

Damit erhält man das Taylorpolynom von $f$ bei $(x_0,y_0)=(1,2)$ als 

\begin{align*} 
T_{f,1}(x,y)
& = f(1,2)+\frac{\partial f}{\partial x}(1,2)\cdot(x-1)+\frac{\partial f}{\partial y}(1,2)\cdot(y-2)\\
& = \frac{5}{6}+\frac{1}{18}\cdot (x-1)+\frac{1}{9}\cdot (y-2)\ . 
\end{align*} 
```
````

```{admonition} Übung 9.2
:class: miniexercise
Bestimmen Sie die Gleichung der Tangentialebene bzw. die Linearisierung für die Funktion

$$f:\mathbb{R}^2 \mapsto \mathbb{R}, \; f(x,y)=\sqrt{x^2 + y^2}$$

am Punkt $(1,0)$.
```
````{admonition} Lösung
:class: miniexercise, toggle
$$T_{1,f}(x,y) = x$$
```{dropdown} Lösungsweg
Das Taylorpolynom vom Grad 1 einer Funktion $f(x,y)$ bei $(x_0,y_0)$ hat die allgemeinen Form 

$$T_{f,1}(x,y)
 = f(x_0,y_0)+\frac{\partial f(x_0,y_0)}{\partial x}\cdot(x-x_0)+\frac{\partial f(x_0,y_0)}{\partial y}\cdot(y-y_0).$$

Der Funktionswert im Punkt $(1,0)$ ist $f(1,0) = 1$. 
 
Die partiellen Ableitungen von $f$ lauten:

\begin{align*}
\frac{\partial f(x,y)}{\partial x} &= \frac{x}{\sqrt{x^2+y^2}}, \\
\frac{\partial f(x,y)}{\partial y} &= \frac{y}{\sqrt{x^2+y^2}}.
\end{align*}

Am Entwicklungspunkt $(x_0,y_0)=(1,0)$ sind die partiellen Ableitungen

\begin{align*}
\frac{\partial f(1,0)}{\partial x} &= 1, \\
\frac{\partial f(1,0)}{\partial y} &= 0.
\end{align*}

Damit ist das Taylorpolynom  1. Grades von $f$ am Entwicklungspunkt $(x_0,y_0)=(1,0)$ 

$$T_{f,1}(x,y) = 1 + 1\cdot(x-1) + 0\cdot (y-y_0) = x.$$
```
````

```{admonition} Übung 9.3 
:class: miniexercise
Bestimmen Sie alle Extremwerte der Funktion $f:\mathbb{R}^2 \rightarrow\mathbb{R}$ gegeben durch  

$$f(x,y)=x^3+y^3 - x - y$$

und untersuchen Sie, ob in diesen Punkten lokale Minima bzw. Maxima vorliegen. 
```
````{admonition} Lösung
:class: miniexercise, toggle
* $(\sqrt{\frac{1}{3}}, \sqrt{\frac{1}{3}})$ Minimum
* $(\sqrt{\frac{1}{3}}, - \sqrt{\frac{1}{3}})$ kein Extremum 
* $(-\sqrt{\frac{1}{3}}, \sqrt{\frac{1}{3}})$ kein Extremum
* $(-\sqrt{\frac{1}{3}}, -\sqrt{\frac{1}{3}})$ Maximum
```{dropdown} Lösungsweg
Die ersten partiellen Ableitungen lauten:
\begin{align*} 
\frac{\partial f(x,y)}{\partial x} &= 3 x^2-1, \\ 
\frac{\partial f(x,y)}{\partial y} & =3 y^2-1. \\
\end{align*}
 
Um die stationären Punkte, also die möglichen Kandidaten zu finden, ist das folgende Gleichungssystem zu lösen: 
 
$$
\begin{cases} 
\frac{\partial f(x,y)}{\partial x} = 3 x^2 - 1 = 0 \\ 
\frac{\partial f(x,y)}{\partial y} = 3 y^2 - 1 = 0. 
\end{cases} 
$$

Dieses Gleichungssystem hat 4 Lösungen, nämlich 

1. $(x_{1},y_{1})=(-\frac{\sqrt{3}}{3},-\frac{\sqrt{3}}{3})$, 
2. $(x_{2},y_{2})=(\frac{\sqrt{3}}{3},-\frac{\sqrt{3}}{3})$, 
3. $(x_{3},y_{3})=(-\frac{\sqrt{3}}{3},\frac{\sqrt{3}}{3})$ und 
4. $(x_{4},y_{4})=(\frac{\sqrt{3}}{3},\frac{\sqrt{3}}{3})$,  

die die stationären Punkte darstellen.
 
Um den Typ der stationären Punkte zu bestimmen, werden die zweiten partiellen Ableitungen berechnet:
\begin{align*}
\frac{\partial^2 f(x,y)}{\partial x \partial x} &= 6x, \\ 
\frac{\partial^2 f(x,y)}{\partial y \partial x} &= 0, \\
\frac{\partial^2 f(x,y)}{\partial y \partial y} &= 6y, \\ 
\frac{\partial^2 f(x,y)}{\partial x \partial y} &= 0.
\end{align*}

Die Hesse-Matrix besteht aus den zweiten partiellen Ableitungen

$$
\mathbf{H}(x,y)= 
\left( \begin{array}{cc} 
\frac{\partial^2 f(x,y)}{\partial x \partial x} & \frac{\partial^2 f(x,y)}{\partial x \partial y} \\ 
\frac{\partial^2 f(x,y)}{\partial y \partial x} & \frac{\partial^2 f(x,y)}{\partial y \partial y}
\end{array} \right) 
= \left( \begin{array}{cc} 
6x & 0 \\ 
0  & 6y
\end{array} \right). 
$$

Die Determinante der Hesse-Matrix ist

$$\det(\mathbf{H}(x,y)) = 6x \cdot 6y - 0 \cdot 0 = 36 xy.$$

Nun wird für jeden stationären Punkt überprüft, ob tatsächlich ein Extremum vorliegt.

1. $(x_{1},y_{1})=(-\frac{\sqrt{3}}{3},-\frac{\sqrt{3}}{3})$:

Die Determinante der Hesse-Matrix für diesen Punkt ist

$$\det\left(\mathbf{H}\left(-\frac{\sqrt{3}}{3},-\frac{\sqrt{3}}{3}\right)\right) = 
36\cdot \left(-\frac{\sqrt{3}}{3}\right) \cdot \left(-\frac{\sqrt{3}}{3}\right) = 12 > 0.$$

Damit ist der Punkt $(x_{1},y_{1})=(-\frac{\sqrt{3}}{3},-\frac{\sqrt{3}}{3})$ ein Extremum. Da das Vorzeichen von $\frac{\partial^2 f(-\frac{\sqrt{3}}{3},-\frac{\sqrt{3}}{3})}{\partial x \partial x}$ negativ ist, ist die Hesse-Matrix negativ definit und dieser Punkt ist ein Maximum (Hochpunkt).

2. $(x_{2},y_{2})=(\frac{\sqrt{3}}{3},-\frac{\sqrt{3}}{3})$

Die Determinante der Hesse-Matrix für diesen Punkt ist

$$\det\left(\mathbf{H}\left(\frac{\sqrt{3}}{3},-\frac{\sqrt{3}}{3}\right)\right) =
36 \cdot \frac{\sqrt{3}}{3} \cdot \left(-\frac{\sqrt{3}}{3}\right) = -12 < 0.$$

Damit ist die Hesse-Matrix für diesen Punkt indefinit und der Punkt $(x_{2},y_{2})$ ist kein Extremum.

3. $(x_{3},y_{3})=(-\frac{\sqrt{3}}{3},\frac{\sqrt{3}}{3})$ 

Die Determinante der Hesse-Matrix für diesen Punkt ist

$$\det\left(\mathbf{H}\left(-\frac{\sqrt{3}}{3},\frac{\sqrt{3}}{3}\right)\right) =
36 \cdot \left(-\frac{\sqrt{3}}{3}\right) \cdot \frac{\sqrt{3}}{3} = -12 < 0.$$

Damit ist die Hesse-Matrix für diesen Punkt indefinit und der Punkt $(x_{3},y_{3})$ ist kein Extremum.

4. $(x_{4},y_{4})=(\frac{\sqrt{3}}{3},\frac{\sqrt{3}}{3})$

Die Determinante der Hesse-Matrix für diesen Punkt ist

$$\det\left(\mathbf{H}\left(\frac{\sqrt{3}}{3},\frac{\sqrt{3}}{3}\right)\right) =
36 \cdot \frac{\sqrt{3}}{3} \cdot \frac{\sqrt{3}}{3} = 12 > 0.$$

Damit ist der Punkt $(x_{4},y_{4})=(\frac{\sqrt{3}}{3},\frac{\sqrt{3}}{3})$ ein Extremum. Da das Vorzeichen von $\frac{\partial^2 f(\frac{\sqrt{3}}{3},\frac{\sqrt{3}}{3})}{\partial x \partial x}$ positiv ist, ist die Hesse-Matrix positiv definit und dieser Punkt ist ein Minimum (Tiefpunkt).
```
````

```{admonition} Übung 9.4
:class: miniexercise
Bestimmen Sie alle Extremwerte der Funktion $f:\mathbb{R}^2 \rightarrow\mathbb{R}$ gegeben durch  

$$f(x,y) = -x^3-\frac{3x^2}{2}+6x-2y^3-9y^2+24y+3$$

und untersuchen Sie, ob in diesen Punkten lokale Minima bzw. Maxima vorliegen. 
```
````{admonition} Lösung
:class: miniexercise, toggle
* $(1,1)$ Maximum
* $(-2,1)$ kein Extremum 
* $(1,-4)$ kein Extremum 
* $(-2,-4)$ Minimum
```{dropdown} Lösungsweg
Die ersten partiellen Ableitungen lauten:
\begin{align*} 
\frac{\partial f(x,y)}{\partial x} &= -3 x^2 -3x + 6, \\ 
\frac{\partial f(x,y)}{\partial y} &= -6 y^2 - 18y + 24. 
\end{align*}

Um die stationären Punkte zu finden, ist das folgende Gleichungssystem zu lösen: 

$$ 
\begin{cases} 
\frac{\partial f(x,y)}{\partial x} = -3x^2-3x+6=0 \\ 
\frac{\partial f(x,y)}{\partial y} =-6y^2-18y+24=0. 
\end{cases} 
$$

Dieses Gleichungssystem hat 4 Lösungen, nämlich
 
1. $(x_{1},y_{1})=(1,1)$, 
2. $(x_{2},y_{2})=(-2,1)$, 
3. $(x_{3},y_{3})=(1,-4)$ und 
4. $(x_{4},y_{4})=(-2,-4)$,  

die die stationären Punkte darstellen.
 
Um den Typ der stationären Punkte zu bestimmen, werden die zweiten partiellen Ableitungen berechnet:

\begin{align*}
\frac{\partial^2 f(x,y)}{\partial x \partial x} &= -6x-3, \\ 
\frac{\partial^2 f(x,y)}{\partial y \partial x} &= 0, \\
\frac{\partial^2 f(x,y)}{\partial y \partial y} &= -12y-18, \\ 
\frac{\partial^2 f(x,y)}{\partial x \partial y} &= 0. 
\end{align*}
 
Die Hesse-Matrix besteht aus den zweiten Ableitungen
 
 $$
\mathbf{H}(x,y)= 
\left( \begin{array}{cc} 
\frac{\partial^2 f(x,y)}{\partial x \partial x} & \frac{\partial^2 f(x,y)}{\partial x \partial y} \\ 
\frac{\partial^2 f(x,y)}{\partial y \partial x} & \frac{\partial^2 f(x,y)}{\partial y \partial y}
\end{array} \right) 
= \left( \begin{array}{cc} 
-6x-3 & 0 \\ 
0     & -12y-18
\end{array} \right). 
$$

Die Determinante der Hesse-Matrix ist

$$\det(\mathbf{H}(x,y)) = (-6x-3) \cdot (-12y-18) - 0 \cdot 0 = 72xy + 108x +36y + 54.$$

Nun wird für jeden stationären Punkt überprüft, ob tatsächlich ein Extremum vorliegt.

1. $(x_{1},y_{1})=(1,1)$

Die Determinante der Hesse-Matrix für diesen Punkt ist

$$\det(\mathbf{H}(1,1)) = 270 > 0.$$

Damit ist der Punkt $(x_{1},y_{1})=(1,1)$ ein Extremum. Da das Vorzeichen von $\frac{\partial^2 f(1,1)}{\partial x \partial x} = -9$ negativ ist, ist die Hesse-Matrix negativ definit und dieser Punkt ist ein Maximum (Hochpunkt).

2. $(x_{2},y_{2})=(-2,1)$

Die Determinante der Hesse-Matrix für diesen Punkt ist

$$\det(\mathbf{H}(-2,1)) = -270 < 0.$$

Damit ist die Hesse-Matrix für diesen Punkt indefinit und der Punkt $(x_{2},y_{2})$ ist kein Extremum.

3. $(x_{3},y_{3})=(1,-4)$

Die Determinante der Hesse-Matrix für diesen Punkt ist

$$\det(\mathbf{H}(1,-4)) = -270 < 0.$$

Damit ist die Hesse-Matrix für diesen Punkt indefinit und der Punkt $(x_{3},y_{3})$ ist kein Extremum.

4. $(x_{4},y_{4})=(-2,-4)$

Die Determinante der Hesse-Matrix für diesen Punkt ist

$$\det(\mathbf{H}(-2,-4)) = 270 > 0.$$

Damit ist der Punkt $(x_{4},y_{4})=(-2,-4)$ ein Extremum. Da das Vorzeichen von $\frac{\partial^2 f(-2,-4)}{\partial x \partial x} = -6\cdot(-2)-3=9$ positiv ist, ist die Hesse-Matrix positiv definit und dieser Punkt ist ein Minimum (Tiefpunkt).
```
````

```{admonition} Übung 9.5
:class: miniexercise
Die Querschnittsfläche eines Tunnels kann als Rechteck beschrieben werden, auf
dem sich ein Halbkreis befindet. Wie müssen die geometrischen Abmessungen
gewählt werden, wenn der Umfang minimal sein soll und der Flächeninhalt 50 m²
betragen soll. 
```
````{admonition} Lösung
:class: miniexercise, toggle
Seitenlänge des Rechtecks: $x = 7.48 \text{m}$ (Boden) und $y = 3.75 \text{m}$ (Höhe des Rechtecks ohne Halbkreis)
```{dropdown} Lösungsweg
Der Umfang $U$ der Tunnel-Querschnittsfläche ist

$$U(x,y) = x + 2y + \frac{\pi}{2} x = (1 + \frac{\pi}{2})x + 2y.$$

Da der Umfang minimiert werden soll, ist dies unsere Zielfunktion, die von den beiden Seitenlängen des Rechtecks $x$ und $y$ abhängt. Dabei haben wir $x$ als Boden des Tunnels gewählt.

Die Nebenbedingung ist, dass die Querschnittsfläche 50 m² beträgt. Als Gleichung formuliert gilt dann

$$A = xy + \frac{\pi}{8}x^2 = 50.$$

Wir verwenden das Eliminationsverfahren und lösen die Nebenbedingung nach $y$ auf:

$$\Rightarrow y = \frac{50 - \frac{\pi}{8}x^2}{x}, \quad x\neq 0.$$

In die Zielfunktion eingesetzt erhalten wir

\begin{align*}
\tilde{U}(x) &= (1+\frac{\pi}{2})x + \frac{100}{x} - \frac{\pi}{4}x = \\
&= (1+\frac{\pi}{4})x + \frac{100}{x}.
\end{align*}

Die 1. Ableitung ist

$$\tilde{U}'(x) = (1+\frac{\pi}{2}) - \frac{100}{x^2}.$$

Wir setzen die 1. Ableitung gleich Null, um Kandidaten für Extrema zu bestimmen,

$$(1+\frac{\pi}{2}) - \frac{100}{x^2} = 0$$

und lösen die Gleichung. Das Ergebnis ist 

$$x_{1,2} = \pm \sqrt{\frac{100}{1+\frac{\pi}{4}}} \approx \pm 7.48.$$

Es kommt nur die positive Nullstelle infrage, da es keine negativen Längen gibt. Von diesem Kandidaten müssen wir aber erst noch zeigen, dass es sich um ein Extremum handelt. Wir bilden die 2. Ableitung

$$\tilde{U}''(x) = \frac{200}{x^3}.$$

Die mögliche Extremstelle $x_1 = 7.48$ eingesetzt ergibt 

$$\tilde{U}''\left(\sqrt{\frac{100}{1+\frac{\pi}{4}}}\right) \approx 0.48.$$

Da die 2. Ableitung ungleich Null ist, ist $x_1$ tatsächlich ein Extremum. Das Vorzeichen der 2. Ableitung ist positiv, damit ist $x_1$ ein Minimum (Tiefpunkt).

Der Tunnel hat also minimalen Umfang bei einer Querschnittsfläche von 50 m², wenn die Seitenlänge x = 7.48 m (Boden) und die Seitenlänge y = 3.75 m gewählt werden.
```
````


Tipp: weitere Übungsaufgaben zu Extremwertproblemen ohne Nebenbedingungen bietet
der MATEX-Aufgabengenerator

> [MATEX 05 Mehrdimensionale Analysis: Extremwertaufgaben (ohne
> Nebenbedingungen)](https://lx4.mint-kolleg.kit.edu/MATeX/generatorview.php?data=NGVJb2NoT3FLU0ZIOFkzOGxOVC91dz09)

Wählen Sie Stufe 3.