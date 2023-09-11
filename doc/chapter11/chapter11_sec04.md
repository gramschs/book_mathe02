# 11.4 Anwendungen Dreifachintegral

Nun kommen Anwendungen des Dreifachintegrals. 

## Lernziele

```{admonition} Lernziele
:class: important
* Sie können mit einem Dreifachintegral das Volumen $V$ eines Körpers berechnen

$$V=\iiint_{V}1\,dV.$$

* Sie können mit drei Dreifachintegralen den Schwerpunkt $S(x_S,y_S,z_S)$ eines Körpers berechnen:

$$x_S = \frac{1}{V}\iiint_{V}x\, dV, \qquad y_S = \frac{1}{V}\iiint_{V}y\, dV \qquad \text{und} \quad z_S = \frac{1}{V}\iiint_{V}z\, dV.$$
```

## Volumen berechnen

Die Berechnung des Volumens eines dreidimensionalen Körpers ist eine der direktesten Anwendungen des Volumenintegrals. Hierbei ist die Funktion, die integriert wird, einfach die Konstante 1. Das Volumen $V$ eines Körpers ist dann das Integral über den gesamten Körper, d.h.,

$$V = \iiint_{V} 1 \, dV.$$

## Berechnung von Masse

Die Berechnung der Masse eines Körpers mit bekannter Dichte ist eine weitere
wichtige Anwendung von Volumenintegralen. Wenn wir die Dichte $\rho(x, y, z)$
des Körpers an jedem Punkt kennen, können wir die Masse $M$ des Körpers
berechnen, indem wir die Dichte über das gesamte Volumen des Körpers
integrieren:

$$M = \iiint_{V} \rho(x, y, z) \, dV.$$

## Berechnung des Schwerpunktes

Die Berechnung des Schwerpunktes $S(x_S, y_S, z_S)$ eines dreidimensionalen
Körpers erfolgt analog zur Berechnung des Schwerpunktes von Flächen, indem das
Volumenintegral jeweils über die Funktionen $x$, $y$ und $z$ berechnet wird. Dabei wird vorausgesetzt, dass wir einen homogenen Körper betrachten, dessen Dichte konstant ist.

\begin{align*}
x_s &= \frac{1}{V} \iiint_{V} x \, dV, \\
y_s &= \frac{1}{V} \iiint_{V} y \, dV, \\
z_s &= \frac{1}{V} \iiint_{V} z \, dV. \\
\end{align*}

Das folgende Video geht auf die Bedeutung und Anwendung der Doppel- und
Dreifachintegrale ein.

```{dropdown} Video zu "Mehrdimensionale Integration | Bedeutung und Anwendung" von MathePeter
<iframe width="560" height="315" src="https://www.youtube.com/embed/H1Pj4SMVZ8s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```