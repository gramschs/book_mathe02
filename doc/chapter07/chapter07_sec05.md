# Übungen

```{admonition} Übung 7.1
:class: miniexercise
Berechnen Sie den Gradient $\nabla f$ der folgenden Funktionen:

a) $f(x,y) = e^{-(x^2+y^2)}$

b) $f(x,y,z) = \frac{1+x+y+z}{1+x^2+y^2+z^2}$ 

c) $f(x_1,x_2) = x_1^4 -5x_2^2 - 10x_1x_2$

d) $f(x_1,x_2,x_3) = 2x_1^2 -4x_1x_2 + x_2^3\cdot \sin(x_3)$  
```
````{admonition} Lösung
:class: minisolution, toggle
a)
\begin{align*} 
f(x,y) &= e^{-(x^2+y^2)} \\
\Rightarrow \quad \nabla f(x,y) &= \left(-2xe^{-x^2-y^2}, -2y e^{-x^2-y^2} \right)
\end{align*}

b)
\begin{align*}
f(x,y,z) &= \frac{1+x+y+z}{1+x^2+y^2+z^2} \\
\Rightarrow \quad \nabla f(x,y,z) &= \Big( \frac{-x^2-2x(y+z+1)+y^2+z^2+1}{(x^2+y^2+z^2+1)^2}, \\
& \quad \quad \frac{x^2-2y(x+y+z+1)+y^2+z^2+1}{(x^2+y^2+z^2+1)^2}, \\
& \quad \quad \frac{x^2-2z(x+y+z+1)+y^2+z^2+1}{(x^2+y^2+z^2+1)^2}\Big) 
\end{align*} 

c)
\begin{align*}
f(x_1,x_2) &= x_1^4 -5x_2^2 - 10x_1x_2 \\
\Rightarrow \quad \nabla f(x_1,x_2) &= \left( 4x_1^3-10x_2, -10(x_1+x_2) \right) 
\end{align*}

d)
\begin{align*}
f(x_1,x_2,x_3) &= 2x_1^2 -4x_1x_2 + x_2^3\cdot \sin(x_3) \\
\Rightarrow \quad \nabla f(x_1,x_2,x_3) &= \left(4(x_1-x_2), 3x_2^2\sin(x_3)-4x_1, x_2^3\cos(x_3)\right)
\end{align*}
```{dropdown} Lösungsweg
a) $f(x,y) = e^{-(x^2+y^2)}$ <br>
Wir berechnen zunächst die partiellen Ableitungen:
\begin{align*}
\frac{\partial f}{\partial x} &= -2xe^{-x^2-y^2} \\
\frac{\partial f}{\partial y} &= -2y e^{-x^2-y^2}  
\end{align*}
Damit ist der Gradient von f:

$$\nabla f(x,y) = \left(-2xe^{-x^2-y^2}, -2y e^{-x^2-y^2} \right)$$

b) $f(x,y,z) = \frac{1+x+y+z}{1+x^2+y^2+z^2}$ <br>
Wir berechnen zunächst die partiellen Ableitungen: 
\begin{align*}
\frac{\partial f}{\partial x} &=  \frac{-x^2-2x(y+z+1)+y^2+z^2+1}{(x^2+y^2+z^2+1)^2}\\
\frac{\partial f}{\partial y} &=  \frac{x^2-2y(x+y+z+1)+y^2+z^2+1}{(x^2+y^2+z^2+1)^2} \\  
\frac{\partial f}{\partial z} &=  \frac{x^2-2z(x+y+z+1)+y^2+z^2+1}{(x^2+y^2+z^2+1)^2}\\  
\end{align*}
Damit ist der Gradient von f:
\begin{multline*}\nabla f(x,y,z) = \Big( \frac{-x^2-2x(y+z+1)+y^2+z^2+1}{(x^2+y^2+z^2+1)^2}, ...\\
\frac{x^2-2y(x+y+z+1)+y^2+z^2+1}{(x^2+y^2+z^2+1)^2},  \frac{x^2-2z(x+y+z+1)+y^2+z^2+1}{(x^2+y^2+z^2+1)^2}\Big)
\end{multline*}
c) $f(x_1,x_2) = x_1^4 -5x_2^2 - 10x_1x_2$ <br>
Wir berechnen zunächst die partiellen Ableitungen:
\begin{align*}
\frac{\partial f}{\partial x_1} &= 4x_1^3-10x_2 \\
\frac{\partial f}{\partial x_2} &= -10(x_1+x_2)  
\end{align*}
Damit ist der Gradient von f:

$$\nabla f(x_1,x_2) = \left( 4x_1^3-10x_2, -10(x_1+x_2) \right)$$

d) $f(x_1,x_2,x_3) = 2x_1^2 -4x_1x_2 + x_2^3\cdot \sin(x_3)$ <br>
Wir berechnen zunächst die partiellen Ableitungen: 
\begin{align*}
\frac{\partial f}{\partial x} &= 4(x_1-x_2) \\
\frac{\partial f}{\partial y} &= 3x_2^2\sin(x_3)-4x_1 \\  
\frac{\partial f}{\partial z} &= x_2^3\cos(x_3) \\  
\end{align*}
Damit ist der Gradient von f:

$$\nabla f(x_1,x_2,x_3) = \left(4(x_1-x_2), 3x_2^2\sin(x_3)-4x_1, x_2^3\cos(x_3)\right)$$
```
````

```{admonition} Übung 7.2
:class: miniexercise
Berechnen Sie die Jacobi-Matrix $J(f)$ zu folgenden Funktionen.

a) 

$$f(x,y) = \begin{pmatrix} x^2 + y^2 \\ x^2 - y^2 \end{pmatrix}$$

b)

$$f(x,y) = \begin{pmatrix} 3x^3y^2 \\ \sin(x) \end{pmatrix}$$
```
````{admonition} Lösung
:class: minisolution, toggle
a)

$$J(f) = \begin{pmatrix} 2x & 2y \\ 2x & -2y \end{pmatrix}$$

b)

$$J(f) = \begin{pmatrix}9x^2y^2 & 6x^3y \\ \cos(x) & 0 \end{pmatrix}$$
```{dropdown} Lösungsweg
a)

$$f(x,y) = \begin{pmatrix} x^2 + y^2 \\ x^2 - y^2 \end{pmatrix}$$

\begin{align*}
\frac{\partial f_1}{\partial x} &= 2x\\
\frac{\partial f_1}{\partial y} &= 2y\\
\frac{\partial f_2}{\partial x} &= 2x\\
\frac{\partial f_2}{\partial y} &= -2y 
\end{align*}
Damit lautet die Jacobi-Matrix

$$J(f) = \begin{pmatrix} 2x & 2y \\ 2x & -2y \end{pmatrix}$$

b) 

$$f(x,y) = \begin{pmatrix} 3x^3y^2 \\ \sin(x) \end{pmatrix}$$

\begin{align*}
\frac{\partial f_1}{\partial x} &= 9x^2y^2\\
\frac{\partial f_1}{\partial y} &= 6x^3y\\
\frac{\partial f_2}{\partial x} &= \cos(x)\\
\frac{\partial f_2}{\partial y} &= 0 
\end{align*}

Damit lautet die Jacobi-Matrix

$$J(f) = \begin{pmatrix}9x^2y^2 & 6x^3y \\ \cos(x) & 0 \end{pmatrix}$$
```
````

```{admonition} Übung 7.3
:class: miniexercise
Bestimmen Sie die Jacobi-Matrix der verketteten Funktion $h = f \circ g$ mit der mehrdimensionalen Kettenregel:

a) $h:\mathbb{R}^2\mapsto\mathbb{R}$ mit $h(x_1,x_2) = f(g(x_1,x_2))$, wobei
\begin{align*}
f:\mathbb{R}^3\mapsto\mathbb{R},   \quad & f(x_1,x_2,x_3) = x_1^2 x_2^2 x_3^2,\\
g:\mathbb{R}^2\mapsto\mathbb{R}^3, \quad & g(x_1,x_2) = \begin{pmatrix} x_1 \\ x_2 \\ x_1 x_2 \end{pmatrix} 
\end{align*}

b) $h:\mathbb{R}^3\mapsto\mathbb{R}^3$ mit $h(x_1,x_2,x_3)=f(g(x_1,x_2,x_3))$, wobei
\begin{align*}
f:\mathbb{R}^3\mapsto\mathbb{R}^3, \quad & f(x_1,x_2,x_3) = \begin{pmatrix} -x_2 \\ -x_3 \\ -x_1 \end{pmatrix}\\
g:\mathbb{R}^3\mapsto\mathbb{R}^3, \quad & g(x_1,x_2,x_3) = \begin{pmatrix} x_1 x_2 \\ x_2 x_3 \\ x_3 x_1 \end{pmatrix}
\end{align*}
```
````{admonition} Lösung
:class: minisolution, toggle
a)

$$J(h)(x_1,x_2) = \left(2x_1^3 x_2^4 + 2x_1^3x_2^4, \; 2x_1^4 x_2^3 + 2x_1^4 x_2^3\right) = 
\left(4x_1^3x_2^4, \; 4x_1^4x_2^3 \right)$$

b)

$$J(h)(x_1,x_2,x_3) = \begin{pmatrix} 0 & -x_3 & -x_2 \\ -x_3 & 0 & -x_1 \\ -x_2 & -x_1 & 0 \end{pmatrix}$$

```{dropdown} Lösungsweg
a) $h:\mathbb{R}^2\mapsto\mathbb{R}$ mit $h(x_1,x_2) = f(g(x_1,x_2))$, wobei
\begin{align*}
f:\mathbb{R}^3\mapsto\mathbb{R},   \quad & f(x_1,x_2,x_3) = x_1^2 x_2^2 x_3^2,\\
g:\mathbb{R}^2\mapsto\mathbb{R}^3, \quad & g(x_1,x_2) = \begin{pmatrix} x_1 \\ x_2 \\ x_1 x_2 \end{pmatrix} 
\end{align*}
Wir berechnen zuerst die Jacobi-Matrix von $f$ und $g$:

$$J(f) = \left(2x_1 x_2^2 x_3^2,\; 2x_1^2 x_2 x_3^2,\; 2x_1 x_2^2 x_3\right) 
\quad \text{ und } \quad
J(g) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ x_2 & x_1\end{pmatrix}$$

Mit der mehrdimensionalen Kettenregel erhalten wir
\begin{multline*}
J(h) = J(f) \cdot J(g) = \left(2x_1 x_2^2 x_3^2, \; 2x_1^2 x_2 x_3^2,\; 2x_1 x_2^2 x_3\right) \cdot 
\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ x_2 & x_1\end{pmatrix} = \\
\left(2x_1 x_2^2 x_3^2 + 2x_1^2 x_2^3 x_3, \; 2x_1^2 x_2 x_3^2 + 2x_1^3 x_2^2 x_3 \right) 
\end{multline*} 
Als nächstes ersetzen wir noch $x_3$ durch $x_1 x_2$ (siehe Definition von $h$) und erhalten

$$J(h)(x_1,x_2) = \left(2x_1^3 x_2^4 + 2x_1^3x_2^4, \; 2x_1^4 x_2^3 + 2x_1^4 x_2^3\right) = 
\left(4x_1^3x_2^4, \; 4x_1^4x_2^3 \right).$$

b) $h:\mathbb{R}^3\mapsto\mathbb{R}^3$ mit $h(x_1,x_2,x_3)=f(g(x_1,x_2,x_3))$, wobei
\begin{align*}
f:\mathbb{R}^3\mapsto\mathbb{R}^3, \quad & f(x_1,x_2,x_3) = \begin{pmatrix} -x_2 \\ -x_3 \\ -x_1 \end{pmatrix}\\
g:\mathbb{R}^3\mapsto\mathbb{R}^3, \quad & g(x_1,x_2,x_3) = \begin{pmatrix} x_1 x_2 \\ x_2 x_3 \\ x_3 x_1 \end{pmatrix}
\end{align*}
Wir berechnen zuerst die Jacobi-Matrix von $f$ und $g$:

$$J(f) = \begin{pmatrix} 0 & -1 & 0 \\ 0 & 0 & -1 \\ -1 & 0 & 0 \end{pmatrix} 
\quad \text{ und } \quad
J(g) = \begin{pmatrix} x_2 & x_1 & 0 \\ 0 & x_3 & x_2 \\ x_3 & 0 & x_1 \end{pmatrix}$$

Mit der mehrdimensionalen Kettenregel erhalten wir

$$J(h)(x_1,x_2,x_3) = J(f)\cdot J(g) = 
\begin{pmatrix} 0 & -1 & 0 \\ 0 & 0 & -1 \\ -1 & 0 & 0 \end{pmatrix} \cdot \begin{pmatrix} x_2 & x_1 & 0 \\ 0 & x_3 & x_2 \\ x_3 & 0 & x_1 \end{pmatrix} =
\begin{pmatrix} 0 & -x_3 & -x_2 \\ -x_3 & 0 & -x_1 \\ -x_2 & -x_1 & 0 \end{pmatrix}$$
```
````