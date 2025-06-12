# 10.4 Anwendungen Dreifachintegral

Nun betrachten wir Anwendungen des Dreifachintegrals.

## Lernziele

```{admonition} Lernziele
:class: goals
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

Die Berechnung des Schwerpunktes $S(x_s, y_s, z_s)$ eines dreidimensionalen
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

## Beispiel: Volumen eines Quaders

Wir berechnen das Volumen eines Quaders mit den Kantenlängen $a = 2$, $b = 3$
und $c = 4$ mithilfe eines Dreifachintegrals.

Das Volumen eines Körpers berechnet sich durch das Integral der konstanten
Funktion $f(x,y,z) = 1$ über das entsprechende Volumen:

$$V = \iiint_{Quader} 1 \, dV$$

**Schritt 1**: Integrationsgebiet beschreiben

Der Quader erstreckt sich von:

- $x = 0$ bis $x = a = 2$
- $y = 0$ bis $y = b = 3$
- $z = 0$ bis $z = c = 4$

**Schritt 2**: Integrationsgrenzen festlegen

Entsprechend unserer Notation:

- Äußeres Integral: $x \in [0, 2]$ (d.h. $a = 0$, $b = 2$)
- Mittleres Integral: $y \in [0, 3]$ (d.h. $g_u(x) = 0$, $g_o(x) = 3$)
- Inneres Integral: $z \in [0, 4]$ (d.h. $F_u(x,y) = 0$, $F_o(x,y) = 4$)

**Schritt 3**: Dreifachintegral aufstellen

$$V = \int_{x=0}^{x=2} \left( \int_{y=0}^{y=3} \left( \int_{z=0}^{z=4} 1 \, dz
\right) dy \right) dx$$

**Schritt 4**: Integration durchführen

Inneres Integral (nach $z$):

$$I_1(x,y) = \int_{z=0}^{z=4} 1 \, dz = [z]_0^4 = 4 - 0 = 4$$

Das Ergebnis ist die konstante Funktion $I_1(x,y) = 4$.

Mittleres Integral (nach $y$):

$$I_2(x) = \int_{y=0}^{y=3} I_1(x,y) \, dy = \int_{y=0}^{y=3} 4 \, dy = 4 \cdot
[y]_0^3 = 4 \cdot (3 - 0) = 12$$

Das Ergebnis ist die konstante Funktion $I_3(x) = 12$.

Äußeres Integral (nach $x$):

$$V = \int_{x=0}^{x=2} I_3(x) \, dx = \int_{x=0}^{x=2} 12 \, dx = 12 \cdot [x]_0^2
= 12 \cdot (2 - 0) = 24$$

Das Volumen des Quaders ist $V = 24$ Volumeneinheiten. Zur Kontrolle berechnen
wir das Volumen mit der aus der Geometrie bekannten Formel $V = a \cdot b \cdot
c$ und erhalten

$$V = a \cdot b \cdot c = 2 \cdot 3 \cdot 4 = 24.$$

## Zusammenfassung und Ausblick

Mit diesen Anwendungen von Dreifachintegralen schließen wir das Kapitel
mehrdimensionale Integration ab und widmen uns nun Differentialgleichungen.
