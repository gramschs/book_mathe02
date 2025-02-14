# Übungen

```{admonition} Übung 11.1
:class: miniexercise
Bestimmen Sie die Lösung des Anfangwertproblems

$$y \, y'- e^{5x} = 0, \qquad \text{für} \quad y(0)=1.$$
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung:

$$y(x) = \pm \sqrt{\frac{2}{5}e^{5x}+2c}$$


Spezielle Lösung des Anfangwertproblems:

$$y(x) = \sqrt{\frac{2}{5}e^{5x}+\frac{3}{5}}$$

```{dropdown} Lösungsweg
Trennung der Variablen:

$$y\frac{dy}{dx} = e^{5x} \quad \Rightarrow y \, dy = e^{5x} \, dx$$

Unbestimmte Integration der beiden Seiten:

$$\int y \, dy = \int e^{5x} \, dx \quad \Rightarrow \frac{1}{2}y^2 + c_1 = \frac{1}{5}e^{5x} + c_2$$

Setze $c=c_2-c_1$ und löse nach $y$ auf:

$$y(x) = \pm \sqrt{\frac{2}{5}e^{5x}+2c}.$$

Für den Anfangswert $y(0)=1$ lösen wir die Gleichung

$$1 = \pm \sqrt{\frac{2}{5}e^{0}+2c}$$

nach $c$ auf und erhalten $c=3/10$. Damit ist die spezielle Lösung für $y(0)=1$

$$y(x) = \sqrt{\frac{2}{5}e^{5x}+\frac{3}{5}}.$$

```
````

```{admonition} Übung 11.2
:class: miniexercise
Bestimmen Sie die Lösung des Anfangwertproblems

$$y'- 6yx^2 = 0, \quad \text{für} \quad y(0)=5.$$
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung: 

$$y(x) = c e^{2x^3}$$

Spezielle Lösung für $y(0)=5$:

$$y(x) = 5 e^{2x^3}.$$
```{dropdown} Lösungsweg
Trennung der Variablen:

$$\frac{1}{y}\frac{dy}{dx} = 6 x^2 \quad \Rightarrow \frac{1}{y} \, dy = 6 x^2 \, dx$$

Unbestimmte Integration der beiden Seiten:

$$\int \frac{1}{y} \, dy = \int 6x^2 \, dx \quad \Rightarrow 
\ln |y| + c_1 = 2x^3 + c_2$$

Setze $\tilde{C}=c_2-c_1$ und löse nach $y$ auf:

$$|y| = e^{2x^3 + \tilde{c}} \quad \Rightarrow y(x) = C \cdot e^{2x^3}$$

Für den Anfangswert $y(0)=5$ lösen wir die Gleichung

$$ y(0) = C \cdot e^{0} \overset{!}{=} 5$$

nach $C$ auf und erhalten $C = 5$. Damit ist die spezielle Lösung für $y(0)=5$ 

$$y(x) = 5 \cdot e^{2x^3}.$$

```
````

```{admonition} Übung 11.3
:class: miniexercise
Bestimmen Sie die Lösung des Anfangwertproblemes

$$\dot{x} = e^{t-x} \quad \text{ für } \quad x(1)=1.$$
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung:

$$x(t) = \ln(e^t + C)$$

Spezielle Lösung für $x(1)=1$:

$$x(t) = t$$
```{dropdown} Lösungsweg
Trennung der Variablen:

$$\frac{dx}{dt} e^x = e^t \quad \Rightarrow e^x \, dx = e^t \, dt$$

Unbestimmte Integration der beiden Seiten:

$$\int e^x \, dx = \int e^t \, dt \quad \Rightarrow e^x + c_1 = e^t + c_2$$

Setze $C=c_2-c_1$ und löse nach $x$ auf:

$$x(t) = \ln(e^t + C)$$

Für den Anfangswert $x(1)=1$ lösen wir die Gleichung

$$x(1) = \ln(e^1 + C) \overset{!}{=} 1$$

nach $C$ auf und erhalten $C = 0$. Damit ist die spezielle Lösung für $x(1)=1$

$$x(t) = \ln(e^t) = t.$$
```
````

```{admonition} Übung 11.4
:class: miniexercise
Bestimmen Sie die Lösung des Anfangwertproblemes

$$9x\dot{x} - 4t = 0 \quad \text{ für } \quad x(1.5)=-1.$$
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung:

$$x(t) = \pm \sqrt{\frac{4}{9}t^2 + \frac{2}{9}c}$$

Spezielle Lösung für $x(1.5)=-1$:

$$x(t) = - \frac{2}{3}t$$

```{dropdown} Lösungsweg
Trennung der Variablen:

$$9x\frac{dx}{dt} = 4t \quad \Rightarrow 9x \, dx = 4t \, dt$$

Unbestimmte Integration der beiden Seiten:

$$\int 9x \, dx = \int 4t \, dt \quad \Rightarrow \frac{9}{2}x^2 + c_1 = 2t^2 + c_2$$

Setze $C = c_2 - c_1$ und löse nach $x$ auf:

$$x(t) = \pm \sqrt{\frac{4}{9}t^2 + \frac{2}{9}c}$$

Für den Anfangswert $x(1.5)=-1$ lösen wir die Gleichung

$$x(1.5) = \pm \sqrt{\frac{4}{9}t^2 + \frac{2}{9}c} \overset{!}{=} -1$$

nach $C$ auf und erhalten $C=0$. Damit ist die spezielle Lösung $x(1.5)=-1$

$$x(t) = - \frac{2}{3}t.$$
```
````

```{admonition} Übung 11.5
:class: miniexercise
Bestimmen Sie die Lösung des Anfangwertproblems

$$t\cdot \dot{x} + \dot{x} - x = 1 \quad \text{für} \quad x(3)=3.$$
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung:

$$x(t) = C\cdot (t+1) - 1$$

Spezielle Lösung für $x(3)=3$

$$x(t) = t$$
```{dropdown} Lösungsweg
Trennung der Variablen:

$$\frac{1}{x + 1} \frac{dx}{dt} = \frac{1}{t+1} \quad 
\Rightarrow \frac{1}{x+1} \, dx = \frac{1}{t+1} \, dt$$

Unbestimmte Integration der beiden Seiten:

$$\int \frac{1}{x+1} \, dx = \int \frac{1}{t+1} \, dt \quad
\Rightarrow \ln |x + 1| + c_1 = \ln |t+1| + c_2$$

Setze $\tilde{C} = c_2 - c_1$ und löse nach $x$ auf:

$$|x+1| = |t+1| \cdot e^{\tilde{C}} \quad 
\Rightarrow x(t) = C\cdot (t+1) - 1$$

Dabei wurden die Betragsstriche weggelassen, da die postitive Konstante $e^{\tilde{C}}$ durch eine reelle Zahl $C$ ersetzt wurde, die die drei möglichen Lösungen vereinigt.

Für den Anfangswert $x(3)=3$ lösen wir die Gleichung

$$x(3) = C\cdot (3+1) - 1 \overset{!}{=} 3$$

nach $C$ auf und erhalten $C=1$. Damit ist die spezielle Lösung für $x(3)=3$

$$x(t) = t.$$
```
````

```{admonition} Übung 11.6
:class: miniexercise
Bestimmen Sie die Lösung des Anfangwertproblems

$$x\cdot \dot{x} -\sin(t) = 0 \quad \text{für} \quad x\left(\frac{\pi}{2}\right)=2.$$
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung:

$$x(t) = \pm \sqrt{-2\cos(t) + 2C}$$

Spezielle Lösung für $x(\pi/2)=2$

$$x(t) = \sqrt{-2\cos(t) + 4}$$
```{dropdown} Lösungsweg
Trennung der Variablen:

$$x\cdot\frac{dx}{dt} = \sin(t) \quad 
\Rightarrow x \; dx = \sin(t) \, dt $$

Unbestimmte Integration der beiden Seiten:

$$\int x \; dx = \int \sin(t) \, dt \quad
\Rightarrow \frac{1}{2}x^2 + c_1 = -\cos(t) + c_2 $$

Setze $C=c_2-c_1$ und löse nach $x$ auf:

$$x(t) = \pm \sqrt{-2\cos(t) + 2C}.$$

Für den Anfangswert $x(\frac{\pi}{2})=2$ lösen wir die Gleichung

$$x\left(\frac{\pi}{2}\right) =\pm \sqrt{-2\cos(\frac{\pi}{2}) + 2C}  \overset{!}{=} 2$$

und erhalten $C=2$. Damit ist die spezielle Lösung für $x(\frac{\pi}{2})=2$

$$x(t) = \sqrt{-2\cos(t) + 4}.$$
```
````

```{admonition} Übung 11.7
:class: miniexercise
Lösen Sie die exakte Differentialgleichung

$$y \, y'- e^{5x} = 0.$$
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung:

$$y(x) = \pm \sqrt{\frac{2}{5} e^{5x} + C}$$
```{dropdown} Lösungsweg
Wir setzen 

$$p(x,y) = -e^{5x} \quad \text{ und } \quad q(x,y) = y.$$

Dann testen wir, ob die Exaktheitsbedingung erfüllt ist:

\begin{align*}
\frac{\partial p}{\partial y} &= 0 \\
\frac{\partial q}{\partial x} &= 0.
\end{align*}

Das ist der Fall. Als nächstes wird $p(x,y)=-e^{5x}$ nach $x$ integriert:

$$F(x,y) = \int -e^{5x} \, dx = -\frac{1}{5} e^{5x} + C(y).$$

Jetzt wird $F(x,y)$ partiell nach $y$ abgeleitet und mit $q(x,y)=y$ gleichgesetzt:

$$\frac{\partial F}{\partial y} = C'(y) \overset{!}{=} y.$$

Aus dieser Gleichung wird $C(y)$ berechnet:

$$C(y) = \int C'(y) \, dy = \int y \, dy = \frac{1}{2}y^2 + c_1.$$

Zuletzt wird aus $F(x,y) = \tilde{c}$ nach $y$ aufgelöst (mit $C=\tilde{c}-c_1$):

$$-\frac{1}{5} e^{5x} + \frac{1}{2} y^2 = C \quad
\Rightarrow y(x) = \pm \sqrt{\frac{2}{5} e^{5x} + C}$$
```
````

```{admonition} Übung 11.8
:class: miniexercise
Lösen Sie die exakte Differentialgleichung

$$9y \, y' = 4x.$$
```

````{admonition} Lösung
:class: miniexercise, toggle
Allgemeine Lösung

$$y(x) = \pm \frac{\sqrt{2}}{3} \sqrt{2x^2 + C}$$
```{dropdown} Lösungsweg
Wir setzen 

$$p(x,y) = -4x \quad \text{ und } \quad q(x,y) = 9y.$$

Dann testen wir, ob die Exaktheitsbedingung erfüllt ist:

\begin{align*}
\frac{\partial p}{\partial y} &= 0 \\
\frac{\partial q}{\partial x} &= 0.
\end{align*}

Das ist der Fall. Als nächstes wird $p(x,y)=-4x$ nach $x$ integriert:

$$F(x,y) = \int -4x \, dx = -2x^2 + C(y).$$

Jetzt wird $F(x,y)$ partiell nach $y$ abgeleitet und mit $q(x,y)=9y$ gleichgesetzt:

$$\frac{\partial F}{\partial y} = C'(y) \overset{!}{=} 9y.$$

Aus dieser Gleichung wird $C(y)$ berechnet:

$$C(y) = \int C'(y) \, dy = \int 9y \, dy = \frac{9}{2}y^2 + c_1.$$

Zuletzt wird aus $F(x,y) = \tilde{c}$ nach $y$ aufgelöst (mit $C=\tilde{c}-c_1$):

$$-2x^2 + \frac{9}{2} y^2 = C \quad
\Rightarrow y(x) = \pm \frac{\sqrt{2}}{3} \sqrt{2x^2 + C}$$
```
````
