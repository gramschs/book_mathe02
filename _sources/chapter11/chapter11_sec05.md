# Übungen


```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

```{admonition} Übung 11.1
:class: miniexercise
Bestimmen Sie die Lösung des Anfangwertproblems

$$y \, y'- e^{5x} = 0, \qquad \text{für} \quad y(0)=1.$$
``` 
````{admonition} Lösung
:class: minisolution, toggle
Allgemeine Lösung:

$$y(x) = \pm \sqrt{\frac{2}{5}e^{5x}+c}$$


Spezielle Lösung des Anfangwertproblems:

$$y(x) = \sqrt{\frac{2}{5}e^{5x}+\frac{3}{5}}$$

```{dropdown} Lösungsweg
Trennung nach beiden Seiten:

$$y\frac{dy}{dx} = e^{5x}$$

Unbestimmte Integration:

$$\int y \, dy = \int e^{5x} \, dx \quad \Rightarrow \frac{1}{2}y^2 + c_1 = \frac{1}{5}e^{5x} + c_2$$

Setze $c=c_2-c_1$ und löse nach $y$ auf:

$$y(x) = \pm \sqrt{\frac{2}{5}e^{5x}+2c}.$$

Für den Anfangswert $y(0)=1$ lösen wir die Gleichung

$$1 = \pm \sqrt{\frac{2}{5}e^{0}+2c}$$

nach $c$ auf und erhalten $c=3/10$. Damit ist die spezielle Lösung

$$y(x) = \sqrt{\frac{2}{5}e^{5x}+\frac{3}{10}}.$$

```
````

```{admonition} Übung 11.2
:class: miniexercise
Bestimmen Sie die Lösung des Anfangwertproblems

$$y'- 6yx^2 = 0, \qquad \text{für} \quad y(0)=5.$$
```
````{admonition} Lösung
:class: minisolution, toggle
Allgemeine Lösung: 

$$y(x) = c e^{2x^3}$$

Spezielle Lösung für $y(0)=5$:

$$y(x) = 5 e^{2x^3}.$$
```{dropdown} Lösungsweg
Trennung nach beiden Seiten:

$$\frac{1}{y}\frac{dy}{dx} = 6 x^2$$

Unbestimmte Integration:

$$\int \frac{1}{y} \, dy = \int 6x^2 \, dx \quad \Rightarrow 
\ln |y| + c_1 = 2x^3 + c_2$$

Setze $\tilde{C}=c_2-c_1$ und löse nach $y$ auf:

$$|y| = e^{2x^3 + \tilde{c}} \quad \Rightarrow y(x) = C \cdot e^{2x^3}$$

Für den Anfangswert $y(0)=5$ lösen wir die Gleichung

$$ y(0) = C \cdot e^{0} = 5$$

nach $C$ auf und erhalten $C = 5$. Damit ist die spezielle Lösung

$$y(x) = 5 \cdot e^{2x^3}.$$

```
````

```{admonition} Übung 11.3
:class: miniexercise
Bestimmen Sie die Lösung des Anfangwertproblemes

$$\dot{x} = e^{t-x} \quad \text{ für } x(1)=1.$$
```

````{admonition} Lösung
:class: minisolution, toggle
Allgemeine Lösung:

$$x(t) = \ln(e^t + C)$$

Spezielle Lösung für $x(1)=1$:

$$x(t) = \ln(e^t)$$
```{dropdown} Lösungsweg
Trennung nach beiden Seiten:

$$\frac{dx}{dt} e^x = e^t$$

Unbestimmte Integration:

$$\int e^x \, dx = \int e^t \, dt \quad \Rightarrow e^x + c_1 = e^t + c_2$$

Setze $C=c_2-c_1$ und löse nach $x$ auf:

$$x(t) = \ln(e^t + C)$$

Für den Anfangswert $x(1)=1$ lösen wir die Gleichung

$$x(1) = \ln(e^1 + C) = 1$$

nach $C$ auf und erhalten $C = 0$. Damit ist die spezielle Lösung

$$x(t) = \ln(e^t).$$
```
````



