# 9.3 Anwendung: Flächenberechnung

Mit dem Doppelintegral kann auch die Fläche eines Gebietes berechnet werden, das
durch zwei Funktionen umrandet wird.

## Lernziele

```{admonition} Lernziele
:class: important
Sie können mit einem Doppelintegral den Flächeninhalt einer Fläche $A$ berechnen.
```

## Anwendungen von Doppelintegralen

Der Flächeninhalt kann mit der Formel

$$A = \iint_{A} 1 \, dA = \int_{x=a}^{x=b} \int_{y=f_u(x)}^{y=f_o(x)} 1 \, dy \,
dx.$$ 

berechnet werden, also $f(x,y)=1$.

## Beispiel Doppelintegral zur Flächenberechnung

Gesucht wird der Flächeninhalt $A$, der durch die Umrandung der beiden Funktionen 

$$f_o(x) = -x + 1$$

und

$$f_u(x) = x^2 - 5$$

entsteht. Aus dem letzten Kapitel wissen wir bereits, dass sich die beiden
Funktionen in den Punkten $(-3,4)$ und $(2,-1)$ schneiden.

```{figure} pics/part09_plot_example02.svg
---
width: 75%
name: part09_plot_example03
---
Gesucht ist der schraffierte Flächeninhalt $A$, der durch die Gerade $f_o(x)=-x+1$ und die Parabel $f_u(x)=x^2-5$ umrandet wird.
```

Der Flächeninhalt $A$ lässt sich mit dem Doppelintegral

$$\iint_{A} 1 \, dA = \int_{x=-3}^{x=2} \left(\int_{y=x^2-5}^{y=-x+1}
1 \; dy\right)dx$$

berechnen.

Zuerst wird das innere Integral $I(x)$ berechnet, indem nach $y$ integriert wird:

\begin{align*}
I(x) &= \int_{y=x^2-5}^{y=-x+1} 1 \, dy = \\
     &= \left[ y \right]_{y=x^2-5}^{y=-x+1} = \\
     &= (-x+1) -(x^2-5) = \\
     &= -x^2-x+6.
\end{align*} 

Das innere Integral $I(x) = -x^2-x+6$ wird nun in das äußere Integral eingesetzt
und nach $x$ integriert:

\begin{align*}
\int_{x=-3}^{x=2} I(x)\, dx &= \int_{x=-3}^{x=2}  -x^2-x+6\, dx =\\
&= \left[-\frac{1}{3}x^3-\frac{1}{2}x^2+6x \right]_{x=-3}^{x=2} = \\
&= \frac{125}{6} \approx 20.8333.
\end{align*}

Damit gilt insgesamt

$$A= \iint_{A}1\, dA = \int_{x=-3}^{x=2} \left(\int_{y=x^2-5}^{y=-x+1}
1 \; dy\right)dx = \frac{125}{6} \approx 20.8333.$$