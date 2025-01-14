# Übungen

Die folgenden Übungsaufgaben wurden teilweise mit dem Aufgabengenerator MATEX
[Generator 07 DGL "Lineare nichthomogene DGL mit konstanten
Koeffizienten](https://lx4.mint-kolleg.kit.edu/MATeX/generatorview.php?data=eXZyZm14SldjcWRFc092RVZ5dkF6Zz09)
erzeugt. Dort können Sie sich auch selbst weitere Aufgaben mit Lösung erzeugen.
Wählen Sie dazu Stufe 1b.

```{admonition} Übung 13.1
:class: miniexercise
Lösen Sie das Anfangswertproblem

$$y'= -5y$$

für $y(0)=5$.
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung:

$$y(x)=C\, e^{-5x}, \quad C\in\mathbb{R}$$

Spezielle Lösung für $y(0)=5$:

$$y(x) = 5 \, e^{-5x}.$$
```{dropdown} Lösungsweg
Die DGL ist eine lineare DGL mit $a_1(x)=1$ und $a_0(x)=5$. Daher lautet die allgemeine Lösung

$$y(x)=C \, e^{-\int \frac{a_0(x)}{a_1(x)}\, dx} 
= C \, e^{-\int 5 \, dx} = C \, e^{-5x}. $$

Für die spezielle Lösung soll

$$y(0)= C \, e^{-5x} \overset{!}{=} 5$$

gelten. Die Gleichung wird nach $C$ aufgelöst und wir erhalten $C=5$. Also lautet die spezielle Lösung des Anfangwertproblems

$$y(x) = 5 \, e^{-5x}.$$

Hinweis: Direkt integrieren hätte auch funktioniert.
```
````

```{admonition} Übung 13.2
:class: miniexercise
Lösen Sie das Anfangswertproblem

$$\dot{x} + 5x = -5t$$

für $x(0)=5$.
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung:

$$x(t) = -t + \frac{1}{5} + C\cdot e^{-5t}, \quad C\in\mathbb{R}$$

Spezielle Lösung für $x(0)=5$:

$$x(t) = -t + \frac{1}{5} + \frac{24}{5} e^{-5t}$$
```{dropdown} Lösungsweg
Die DGL ist eine lineare inhomogene DGL mit $a_1(t)=1$ und $a_0(t)=5$. Daher bestimmen wir zuerst die allgemeine Lösung der homogenen DGL

$$\dot{x} + 5x = 0.$$

Das ist die Differentialgleichung aus Aufgabe 12.1 und die allgemeine homogene Lösung lautet

$$x_h(t) = C \cdot e^{-5t}.$$

Wir variieren die Konstante und nehmen den Lösungsansatz

$$x(t) = C(t) \cdot e^{-5t}.$$

Die erste Ableitung ist

$$\dot{x}(t) = \dot{C}(t) e^{-5t} - 5 C(t) \cdot e^{-5t}.$$

Jetzt werden die Lösungsansatzfunktion $x$ und deren Ableitung $\dot{x}$ in die inhomogene DGL eingesetzt:

$$\dot{C}(t) e^{-5t} - 5C(t) e^{-5t} + 5 C(t) e^{-5t} = -5t.$$

Werden die Terme vereinfacht, so wird diese Gleichung zu

$$\dot{C}(t) = -5t e^{5t}.$$

Wir integrieren partiell nach $t$ und erhalten

$$C(t) = -t e^{5t} + \frac{1}{5} e^{5t} + C.$$

Somit lautet die allgemeine Lösung der inhomogenen DGL

$$x(t) = -t + \frac{1}{5} + C\cdot e^{-5t}, \quad C\in\mathbb{R}$$

Für die spezielle Lösung soll

$$x(0)= -0 + \frac{1}{5} + C \cdot e^{-5\cdot 0} \overset{!}{=} 5$$

gelten. Die Gleichung wird nach $C$ aufgelöst und wir erhalten $C=\frac{24}{5}$. Also lautet die spezielle Lösung des Anfangwertproblems

$$x(t) = -t + \frac{1}{5} + \frac{24}{5} e^{-5t}$$
```
````

```{admonition} Übung 13.3
:class: miniexercise
Lösen Sie das Anfangswertproblem

$$y'-5y = \sin(-5x)$$

für $y(0)=-1$.
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung:

$$y(x) = \frac{1}{10} \left(\sin(5x) + \cos(x)\right) + C\cdot e^{5x}$$

Spezielle Lösung zum Anfangswert $y(0)=-1$

$$y(x) = \frac{1}{10} \cdot \left( \sin(5x) + \cos(5x)\right) - \frac{11}{10}\cdot e^{5x}.$$
```{dropdown} Lösungsweg
Die DGL ist eine lineare inhomogene DGL mit $a_1(x)=1$ und $a_0(x)=-5$. Daher bestimmen wir zuerst die allgemeine Lösung der homogenen DGL

$$y' - 5y = 0.$$

Die allgemeine Lösung der homogenen DGL lautet

$$y_h(x) = C \cdot e^{5x}.$$

Wir variieren die Konstante und nehmen den Lösungsansatz

$$y(x) = C(x) \cdot e^{5x}.$$

Die erste Ableitung ist

$$y'(x) = C'(x) \cdot e^{5x} + C(x) \cdot 5e^{5x}.$$

Jetzt werden die Lösungsansatzfunktion $y$ und deren Ableitung $y'$ in die inhomogene DGL eingesetzt:

$$C'(x) \cdot e^{5x} + C(x) \cdot 5e^{5x} - 5 \cdot C(x) \cdot e^{5x} = \sin(-5x).$$

Werden die Terme vereinfacht, so wird diese Gleichung zu

$$C'(x) = \sin(-5x) \cdot e^{-5x}.$$

Wir integrieren partiell nach $x$ und erhalten

$$C(x) = \frac{1}{10} e^{-5x}\cdot \left( \sin(5x) + \cos(5x)\right) + C.$$

Somit lautet die allgemeine Lösung der inhomogenen DGL

$$y(x) = \frac{1}{10} \cdot \left( \sin(5x) + \cos(5x)\right) + C\cdot e^{5x}.$$

Für die spezielle Lösung soll

$$y(0) = \frac{1}{10} \cdot \left( \sin(0) + \cos(0)\right) + C\cdot e^{0} \overset{!}{=} -1$$

gelten. Die Gleichung wird nach $C$ aufgelöst und wir erhalten $C=-\frac{11}{10}$. Also lautet die spezielle Lösung des Anfangwertproblems

$$y(x) = \frac{1}{10} \cdot \left( \sin(5x) + \cos(5x)\right) - \frac{11}{10}\cdot e^{5x}.$$
```
````

```{admonition} Übung 13.4
:class: miniexercise
Lösen Sie das Anfangswertproblem

$$2\dot{x} - 4x =e^{-t}$$

für $x(0)=0$.
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung

$$x(t) = -\frac{1}{6} e^{-t} + C\cdot e^{2t}.$$

Spezielle Lösung für $x(0)=0$

$$x(t) = -\frac{1}{6} e^{-t} + \frac{1}{6}\cdot e^{2t}.$$
```{dropdown} Lösungsweg
Die DGL ist eine lineare inhomogene DGL mit $a_1(t)=2$ und $a_0(t)=-4$. Daher bestimmen wir zuerst die allgemeine Lösung der homogenen DGL

$$2\dot{x} - 4x = 0.$$

Die allgemeine Lösung der homogenen DGL lautet

$$x_h(t) = C\cdot e^{2t}.$$

Wir variieren die Konstante und nehmen den Lösungsansatz

$$x(t) = C(t)\cdot e^{2t}.$$

Die erste Ableitung ist

$$\dot(x)(t) = \dot{C}(t) e^{2t} + 2 C(t) e^{2t}.$$

Jetzt werden die Lösungsansatzfunktion $x$ und deren Ableitung $\dot{x}$ in die inhomogene DGL eingesetzt:

$$2\cdot\dot{C}(t) e^{2t} + 4 C(t) e^{2t} - 4 C(t) e^{2t} = e^{-t}.$$

Werden die Terme vereinfacht, so wird diese Gleichung zu

$$\dot{C}(t) = \frac{1}{2} e^{-3t}.$$

Wir integrieren partiell nach $t$ und erhalten

$$C(t) = -\frac{1}{6} e^{-3t} + C.$$

Somit lautet die allgemeine Lösung der inhomogenen DGL

$$x(t) = \left(-\frac{1}{6}e^{-3t} + C \right) \cdot e^{2t} = -\frac{1}{6} e^{-t} + C\cdot e^{2t}.$$

Für die spezielle Lösung soll

$$x(0) = -\frac{1}{6} e^{0} + C\cdot e^{0} \overset{!}{=} 0$$

gelten. Die Gleichung wird nach $C$ aufgelöst und wir erhalten $C=\frac{1}{6}$. Also lautet die spezielle Lösung des Anfangwertproblems

$$x(t) = -\frac{1}{6} e^{-t} + \frac{1}{6}\cdot e^{2t}.$$
```
````

```{admonition} Übung 13.5
:class: miniexercise
Lösen Sie das Anfangswertproblem

$$y'-3y = x^2+2x+1$$

für $y(0)=3$.
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung:

$$y(x) = -\frac{1}{3}x^2 - \frac{8}{9}x - \frac{17}{27} + C\cdot e^{3x} , \quad C\in\mathbb{R}$$

Spezielle Lösung für $y(0)=3$:

$$y(x) = -\frac{1}{3}x^2 - \frac{8}{9}x - \frac{17}{27} + \frac{98}{27} e^{3x}$$
```{dropdown} Lösungsweg
Die DGL ist eine lineare inhomogene DGL mit $a_1(x)=1$ und $a_0(x)=-3$. Daher bestimmen wir zuerst die allgemeine Lösung der homogenen DGL

$$y' - 3y = 0.$$

Die allgemeine Lösung der homogenen DGL lautet

$$y_h(x) = C \cdot e^{3x}.$$

Wir variieren die Konstante und nehmen den Lösungsansatz

$$y(x) = C(x) \cdot e^{3x}.$$

Die erste Ableitung ist

$$y'(x) = C'(x) \cdot e^{3x} + C(x) \cdot 3 e^{3x}.$$

Jetzt werden die Lösungsansatzfunktion $y$ und deren Ableitung $y'$ in die inhomogene DGL eingesetzt:

$$C'(x) \cdot e^{3x} + C(x) \cdot 3e^{3x} - 3 \cdot C(x) \cdot e^{3x} = x^2 + 2x + 1.$$

Werden die Terme vereinfacht, so wird diese Gleichung zu

$$C'(x) = \left(x^2 + 2x +1\right) \cdot e^{-3x}.$$

Wir integrieren partiell nach $x$ und erhalten

$$C(x) = (-\frac{1}{3}x^2-\frac{8}{9}x - \frac{17}{27}) \cdot e^{-3x} + C.$$

Somit lautet die allgemeine Lösung der inhomogenen DGL

$$y(x) = \left(-\frac{1}{3}x^2 - \frac{8}{9}x - \frac{17}{27} \right) + C\cdot e^{3x}.$$

Für die spezielle Lösung soll

$$y(0) = \left(-\frac{1}{3}\cdot 0^2 - \frac{8}{9}\cdot 0 - \frac{17}{27} \right) + C\cdot e^{0} \overset{!}{=} 3$$

gelten. Die Gleichung wird nach $C$ aufgelöst und wir erhalten $C=\frac{98}{27}$. Also lautet die spezielle Lösung des Anfangwertproblems

$$y(x) = \left(-\frac{1}{3}x^2 - \frac{8}{9}x - \frac{17}{27} \right) + \frac{98}{27}\cdot e^{3x}$$
```
````

```{admonition} Übung 13.6
:class: miniexercise
Lösen Sie das Anfangswertproblem

$$\dot{x} + 4x = \sin(-2t)$$

für $x(0)=-1$.
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung:

$$x(t) = \frac{1}{10} \left(\cos(2t) - 2\sin(2t)\right) + C\cdot e^{-4t}, \quad C\in\mathbb{R}$$

Spezielle Lösung für $x(0)=-1$

$$x(t) = \frac{1}{10} \left(\cos(2t) - 2\sin(2t)\right) - \frac{11}{10}\cdot e^{-4t}$$
```{dropdown} Lösungsweg
Die DGL ist eine lineare inhomogene DGL mit $a_1(t)=1$ und $a_0(t)=4$. Daher bestimmen wir zuerst die allgemeine Lösung der homogenen DGL

$$\dot{x} + 4x = 0.$$

Die allgemeine Lösung der homogenen DGL lautet

$$x_h(t) = C\cdot e^{-4t}.$$

Wir variieren die Konstante und nehmen den Lösungsansatz

$$x(t) = C(t)\cdot e^{-4t}.$$

Die erste Ableitung ist

$$\dot{x}(t) = \dot{C}(t) e^{-4t} - 4 C(t) e^{-4t}.$$

Jetzt werden die Lösungsansatzfunktion $x$ und deren Ableitung $\dot{x}$ in die inhomogene DGL eingesetzt:

$$\dot{C}(t) e^{-4t} - 4 C(t) e^{-4t} + 4 C(t) e^{-4t} = \sin(-2t).$$

Werden die Terme vereinfacht, so wird diese Gleichung zu

$$\dot{C}(t) = \sin(-2t)\cdot e^{4t}.$$

Wir integrieren partiell nach $t$ und erhalten

$$C(t) = \frac{1}{10}e^{4t}\left(\cos(2t) - 2\sin(2t)\right) + C.$$

Somit lautet die allgemeine Lösung der inhomogenen DGL

$$x(t) = \frac{1}{10} \left(\cos(2t) - 2\sin(2t)\right) + C\cdot e^{-4t}.$$

Für die spezielle Lösung soll

$$x(0) = \frac{1}{10} \left(\cos(0) - 2\sin(0)\right) + C\cdot e^{0} \overset{!}{=} -1$$

gelten. Die Gleichung wird nach $C$ aufgelöst und wir erhalten $C=-\frac{11}{10}$. Also lautet die spezielle Lösung des Anfangwertproblems

$$x(t) = \frac{1}{10} \left(\cos(2t) - 2\sin(2t)\right) - \frac{11}{10}\cdot e^{-4t}.$$
```
````

```{admonition} Übung 13.7
:class: miniexercise
Lösen Sie das Anfangswertproblem

$$y'-3y = -e^{2x}$$

für $y(0)=1$.
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung:

$$y(x)= C\, e^{3x} + e^{2x}, \quad C\in\mathbb{R}$$

Spezielle Lösung für $y(0)=1$:

$$y(x)= e^{2x}$$
```{dropdown} Lösungsweg
Die DGL ist eine lineare inhomogene DGL mit $a_1(x)=1$ und $a_0(x)=-3$. Daher bestimmen wir zuerst die allgemeine Lösung der homogenen DGL

$$y' - 3y = 0.$$

Die allgemeine Lösung der homogenen DGL lautet

$$y_h(x) = C \cdot e^{3x}.$$

Wir variieren die Konstante und nehmen den Lösungsansatz

$$y(x) = C(x) \cdot e^{3x}.$$

Die erste Ableitung ist

$$y'(x) = C'(x) \cdot e^{3x} + C(x) \cdot 3e^{3x}.$$

Jetzt werden die Lösungsansatzfunktion $y$ und deren Ableitung $y'$ in die inhomogene DGL eingesetzt:

$$C'(x) \cdot e^{3x} + C(x) \cdot 3e^{3x} - 3 \cdot C(x) \cdot e^{3x} = -e^{2x}.$$

Werden die Terme vereinfacht, so wird diese Gleichung zu

$$C'(x) = -e^{2x} \cdot e^{-3x} = -e^{-x}.$$

Wir integrieren nach $x$ und erhalten

$$C(x) = e^{-x} + C.$$

Somit lautet die allgemeine Lösung der inhomogenen DGL

$$y(x) = e^{2x} + C\cdot e^{3x}.$$

Für die spezielle Lösung soll

$$y(0) = e^{0} + C\cdot e^{0} \overset{!}{=} 1$$

gelten. Die Gleichung wird nach $C$ aufgelöst und wir erhalten $C=0$. Also lautet die spezielle Lösung des Anfangwertproblems

$$y(x) = e^{2x}.$$
```
````

```{admonition} Übung 13.8
:class: miniexercise
Lösen Sie das Anfangswertproblem

$$\dot{x} - 2x = (3t+1) \, e^{-3t}$$

für $x(0)=-5$.
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung:

$$x(t) = -\frac{1}{25}e^{-3t}\cdot (15t+8) + C\cdot e^{2t}, \quad C\in\mathbb{R}$$

Spezielle Lösung für $x(0)=-5$:

$$x(t) = -\frac{1}{25}e^{-3t}\cdot (15t+8) + \frac{17}{25}\cdot e^{2t}$$
```{dropdown} Lösungsweg
Die DGL ist eine lineare inhomogene DGL mit $a_1(t)=1$ und $a_0(t)=-2$. Daher bestimmen wir zuerst die allgemeine Lösung der homogenen DGL

$$\dot{x} - 2x = 0.$$

Die allgemeine Lösung der homogenen DGL lautet

$$x_h(t) = C\cdot e^{2t}.$$

Wir variieren die Konstante und nehmen den Lösungsansatz

$$x(t) = C(t)\cdot e^{2t}.$$

Die erste Ableitung ist

$$\dot{x}(t) = \dot{C}(t) e^{2t} + 2 C(t) e^{2t}.$$

Jetzt werden die Lösungsansatzfunktion $x$ und deren Ableitung $\dot{x}$ in die inhomogene DGL eingesetzt:

$$\dot{C}(t) e^{2t} + 2 C(t) e^{2t} - 2 C(t) e^{2t} = (3t+1)\cdot e^{-3t}.$$

Werden die Terme vereinfacht, so wird diese Gleichung zu

$$\dot{C}(t) = (3t+1) e^{-5t}.$$

Wir integrieren nach $t$ und erhalten

$$C(t) = -\frac{1}{25}e^{-5t}\cdot (15t+8) + C.$$

Somit lautet die allgemeine Lösung der inhomogenen DGL

$$x(t) = -\frac{1}{25}e^{-3t}\cdot (15t+8) + C\cdot e^{2t}.$$

Für die spezielle Lösung soll

$$x(0) = -\frac{1}{25}e^{0}\cdot (15\cdot 0+8) + C\cdot e^{0} \overset{!}{=} -5$$

gelten. Die Gleichung wird nach $C$ aufgelöst und wir erhalten $C=\frac{17}{25}$. Also lautet die spezielle Lösung des Anfangwertproblems

$$x(t) = -\frac{1}{25}e^{-3t}\cdot (15t+8) + \frac{17}{25}\cdot e^{2t}.$$
```
````

```{admonition} Übung 13.9
:class: miniexercise
Berechnen Sie die Lösungen des folgenden homogenen Systems von linearen Differentialgleichungen 1. Ordnung:

\begin{align*}
y_1' &= y_1 + y_2 &\\
y_2' &= 4 y_1 - 2y_2 & 
\end{align*} 
```

````{admonition} Lösung
:class: miniexercise, toggle
\begin{align*}
y_1(x) &= C_1 e^{-3x} + C_2 e^{2x} \\
y_2(x) &= -4 C_1 e^{-3x}  + C_2 e^{2x}
\end{align*}
```{dropdown} Lösungsweg
Das System von Differentialgleichungen lautet in Matrix-Vektor-Schreibweise

$$\begin{pmatrix} y_1'\\ y_2'\end{pmatrix} = 
\begin{pmatrix} 1 & 1 \\ 4 & -2 \end{pmatrix} \cdot 
\begin{pmatrix} y_1 \\ y_2 \end{pmatrix}.$$

Das charakteristische Polynom ist

\begin{align*}
\det (A-\lambda E) &= \det \begin{pmatrix} 1 - \lambda & 1 \\ 4 & -2-\lambda \end{pmatrix} = \\
&= (1-\lambda)(-2-\lambda)-4 = \\
&= \lambda^2 + \lambda - 6 =\\
&= (\lambda+3)(\lambda-2)
\end{align*}

Aus der charakteristischen Gleichung 

$$\det (A-\lambda E) \overset{!}{=} 0 \Rightarrow (\lambda+3)(\lambda-2) = 0$$

folgen die Eigenwerte $\lambda_1 = -3$ und $\lambda_2 = 2$. Beide Eigenwerte sind reell und verschieden. Also ist die erste Lösungsfunktion

$$y_1(x) = C_1 e^{-3x} + C_2 e^{2x}.$$

Deren erste Ableitung ist

$$y_1'(x)= -3C_1 e^{-3x} + 2 C_2 e^{2x}.$$

Beides wird in die erste Differentialgleichung $y_1' = y_1 + y_2$ eingesetzt und durch Umformen erhalten wir

$$y_2(x) = -4C_1 e^{-3x} + C_2 e^{2x}.$$
```
````

```{admonition} Übung 13.10
:class: miniexercise
Berechnen Sie die Lösungen des folgenden homogenen Systems von linearen Differentialgleichungen 1. Ordnung:

\begin{align*}
y_1' &= y_1  +y_2&\\
y_2' &= 4y_1 +y_2 &
\end{align*} 
```

````{admonition} Lösung
:class: miniexercise, toggle
\begin{align*}
y_1(x) &= C_1 e^{-x} + C_2 e^{3x} \\
y_2(x) &= -2C_1 e^{-x} + 2 C_2 e^{3x}
\end{align*}
```{dropdown} Lösungsweg
Das System von Differentialgleichungen lautet in Matrix-Vektor-Schreibweise

$$\begin{pmatrix} y_1'\\ y_2'\end{pmatrix} = 
\begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix} \cdot 
\begin{pmatrix} y_1 \\ y_2 \end{pmatrix}.$$

Das charakteristische Polynom ist

\begin{align*}
\det (A-\lambda E) &= \det \begin{pmatrix} 1 - \lambda & 1 \\ 4 & 1-\lambda \end{pmatrix} = \\
&= (1-\lambda)^2 -4 = \\
&= \lambda^2 -2\lambda - 3 =\\
&= (\lambda-3)(\lambda+1)
\end{align*}

Aus der charakteristischen Gleichung 

$$\det (A-\lambda E) \overset{!}{=} 0 \Rightarrow (\lambda-3)(\lambda+1) = 0$$

folgen die Eigenwerte $\lambda_1 = -1$ und $\lambda_2 = 3$. Beide Eigenwerte sind reell und verschieden. Also ist die erste Lösungsfunktion

$$y_1(x) = C_1 e^{-x} + C_2 e^{3x}.$$

Deren erste Ableitung ist

$$y_1'(x)= -C_1 e^{-x} + 3 C_2 e^{3x}.$$

Beides wird in die erste Differentialgleichung $y_1(x) = y_1  +y_2$ eingesetzt und durch Umformen erhalten wir

$$y_2(x) = -2C_1 e^{-x} + 2C_2 e^{3x}.$$
```
````
