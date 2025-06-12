# 10.4 Anwendungen Dreifachintegral

Nun betrachten wir die wichtigsten Anwendungen des Dreifachintegrals in der Ingenieurspraxis. Dreifachintegrale ermöglichen es uns, verschiedene physikalische und geometrische Eigenschaften dreidimensionaler Körper zu berechnen: Volumen, Masse und Schwerpunkt. Weitere wichtige Anwendungen wie Trägheitsmomente und Flächenmomente werden ausführlich in der Vorlesung Technische Mechanik behandelt.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können mit einem Dreifachintegral das **Volumen** $V$ eines Körpers berechnen:
$$V=\iiint_{V}1\,dV$$
* Sie können mit einem Dreifachintegral die **Masse** $M$ eines Körpers mit bekannter Dichte berechnen:
$$M = \iiint_{V} \rho(x, y, z) \, dV$$
* Sie können mit drei Dreifachintegralen den **Schwerpunkt** $S(x_S,y_S,z_S)$ eines homogenen Körpers berechnen:
$$x_S = \frac{1}{V}\iiint_{V}x\, dV, \qquad y_S = \frac{1}{V}\iiint_{V}y\, dV, \qquad z_S = \frac{1}{V}\iiint_{V}z\, dV$$
```

## 10.4.1 Volumen berechnen

Die Berechnung des Volumens eines dreidimensionalen Körpers ist eine der direktesten Anwendungen des Volumenintegrals. Hierbei ist die Funktion, die integriert wird, einfach die Konstante 1. Das Volumen $V$ eines Körpers ist dann das Integral über den gesamten Körper:

$$V = \iiint_{V} 1 \, dV$$

### Beispiel 1: Volumen einer Halbkugel

**Aufgabe**: Berechnen Sie das Volumen einer Halbkugel mit Radius $R = 2$.

**Lösung**:

Wir betrachten eine Halbkugel, die auf der $xy$-Ebene liegt und deren Mittelpunkt im Koordinatenursprung ist. Die Halbkugel wird durch die Ungleichung $x^2 + y^2 + z^2 \leq R^2$ mit $z \geq 0$ beschrieben.

**Integrationsgrenzen bestimmen**:
- Für festes $z \in [0, R]$ ist der Querschnitt ein Kreis mit Radius $r(z) = \sqrt{R^2 - z^2}$
- Für festen Wert von $z$ und $x \in [-\sqrt{R^2 - z^2}, +\sqrt{R^2 - z^2}]$ gilt: $y \in [-\sqrt{R^2 - z^2 - x^2}, +\sqrt{R^2 - z^2 - x^2}]$

**Dreifachintegral aufstellen**:
$$V = \int_{z=0}^{R} \int_{x=-\sqrt{R^2-z^2}}^{+\sqrt{R^2-z^2}} \int_{y=-\sqrt{R^2-z^2-x^2}}^{+\sqrt{R^2-z^2-x^2}} 1 \, dy \, dx \, dz$$

**Integration durchführen**:

**Inneres Integral** (nach $y$):
$$M(x,z) = \int_{y=-\sqrt{R^2-z^2-x^2}}^{+\sqrt{R^2-z^2-x^2}} 1 \, dy = 2\sqrt{R^2-z^2-x^2}$$

**Mittleres Integral** (nach $x$):
$$I(z) = \int_{x=-\sqrt{R^2-z^2}}^{+\sqrt{R^2-z^2}} 2\sqrt{R^2-z^2-x^2} \, dx$$

Dieses Integral entspricht der Fläche eines Halbkreises mit Radius $\sqrt{R^2-z^2}$:
$$I(z) = \frac{\pi}{2} \cdot (R^2-z^2)$$

**Äußeres Integral** (nach $z$):
$$V = \int_{z=0}^{R} \frac{\pi}{2} \cdot (R^2-z^2) \, dz = \frac{\pi}{2} \int_{0}^{R} (R^2-z^2) \, dz$$

$$= \frac{\pi}{2} \left[R^2z - \frac{z^3}{3}\right]_0^R = \frac{\pi}{2} \left(R^3 - \frac{R^3}{3}\right) = \frac{\pi}{2} \cdot \frac{2R^3}{3} = \frac{\pi R^3}{3}$$

Mit $R = 2$: $V = \frac{\pi \cdot 2^3}{3} = \frac{8\pi}{3}$

**Kontrolle**: Das Volumen einer Halbkugel ist $V = \frac{1}{2} \cdot \frac{4}{3}\pi R^3 = \frac{2\pi R^3}{3} = \frac{2\pi \cdot 8}{3} = \frac{16\pi}{3}$ 

*Korrektur*: $V = \frac{2\pi R^3}{3} = \frac{2\pi \cdot 8}{3} = \frac{16\pi}{3}$ ✓

## 10.4.2 Berechnung von Masse

Die Berechnung der Masse eines Körpers mit bekannter Dichte ist eine weitere wichtige Anwendung von Volumenintegralen. Wenn wir die Dichte $\rho(x, y, z)$ des Körpers an jedem Punkt kennen, können wir die Masse $M$ des Körpers berechnen, indem wir die Dichte über das gesamte Volumen des Körpers integrieren:

$$M = \iiint_{V} \rho(x, y, z) \, dV$$

**Spezialfall**: Bei einem homogenen Körper mit konstanter Dichte $\rho$ vereinfacht sich dies zu:
$$M = \rho \cdot V = \rho \iiint_{V} 1 \, dV$$

### Beispiel 2: Masse eines Kegels mit linearer Dichteverteilung

**Aufgabe**: Ein Kegel mit Grundradius $R = 3$ und Höhe $h = 4$ hat eine linear mit der Höhe zunehmende Dichte $\rho(z) = \rho_0(1 + z)$ mit $\rho_0 = 2$ kg/m³. Berechnen Sie die Gesamtmasse.

**Lösung**:

Der Kegel liegt mit der Grundfläche in der $xy$-Ebene (Kreis mit Radius 3) und die Spitze bei $(0, 0, 4)$. Für eine gegebene Höhe $z$ ist der Radius des kreisförmigen Querschnitts: $r(z) = R\left(1 - \frac{z}{h}\right) = 3\left(1 - \frac{z}{4}\right)$

**Integrationsgrenzen**:
- $z \in [0, 4]$
- Für festes $z$: $x^2 + y^2 \leq r(z)^2 = 9\left(1 - \frac{z}{4}\right)^2$

**Dreifachintegral in kartesischen Koordinaten**:
$$M = \int_{z=0}^{4} \int_{x=-r(z)}^{+r(z)} \int_{y=-\sqrt{r(z)^2-x^2}}^{+\sqrt{r(z)^2-x^2}} \rho_0(1 + z) \, dy \, dx \, dz$$

**Vereinfachung durch Flächenintegral**: 
Da die Dichte nur von $z$ abhängt, können wir das Doppelintegral über die Kreisfläche durch $\pi r(z)^2$ ersetzen:

$$M = \int_{z=0}^{4} \rho_0(1 + z) \cdot \pi r(z)^2 \, dz = \int_{z=0}^{4} 2(1 + z) \cdot \pi \cdot 9\left(1 - \frac{z}{4}\right)^2 \, dz$$

$$= 18\pi \int_{z=0}^{4} (1 + z)\left(1 - \frac{z}{4}\right)^2 \, dz$$

Ausmultiplizieren: $\left(1 - \frac{z}{4}\right)^2 = 1 - \frac{z}{2} + \frac{z^2}{16}$

$$(1 + z)\left(1 - \frac{z}{2} + \frac{z^2}{16}\right) = 1 - \frac{z}{2} + \frac{z^2}{16} + z - \frac{z^2}{2} + \frac{z^3}{16}$$
$$= 1 + \frac{z}{2} - \frac{7z^2}{16} + \frac{z^3}{16}$$

**Integration**:
$$M = 18\pi \int_{0}^{4} \left(1 + \frac{z}{2} - \frac{7z^2}{16} + \frac{z^3}{16}\right) dz$$

$$= 18\pi \left[z + \frac{z^2}{4} - \frac{7z^3}{48} + \frac{z^4}{64}\right]_0^4$$

$$= 18\pi \left(4 + 4 - \frac{7 \cdot 64}{48} + \frac{256}{64}\right) = 18\pi \left(8 - \frac{28}{3} + 4\right)$$

$$= 18\pi \left(12 - \frac{28}{3}\right) = 18\pi \cdot \frac{8}{3} = 48\pi \text{ kg}$$

**Ergebnis**: $M = 48\pi \approx 150.8$ kg

## 10.4.3 Berechnung des Schwerpunktes

Die Berechnung des Schwerpunktes $S(x_S, y_S, z_S)$ eines dreidimensionalen Körpers erfolgt analog zur Berechnung des Schwerpunktes von Flächen, indem Volumenintegrale jeweils mit den Integranden $x$, $y$ und $z$ berechnet werden.

**Für homogene Körper** (konstante Dichte):
\begin{align}
x_S &= \frac{1}{V} \iiint_{V} x \, dV \\
y_S &= \frac{1}{V} \iiint_{V} y \, dV \\
z_S &= \frac{1}{V} \iiint_{V} z \, dV
\end{align}

**Für inhomogene Körper** (variable Dichte $\rho(x,y,z)$):
\begin{align}
x_S &= \frac{1}{M} \iiint_{V} x \cdot \rho(x,y,z) \, dV \\
y_S &= \frac{1}{M} \iiint_{V} y \cdot \rho(x,y,z) \, dV \\
z_S &= \frac{1}{M} \iiint_{V} z \cdot \rho(x,y,z) \, dV
\end{align}

wobei $M$ die Gesamtmasse ist.

### Beispiel 3: Schwerpunkt einer Halbkugel

**Aufgabe**: Bestimmen Sie den Schwerpunkt einer homogenen Halbkugel mit Radius $R$, die auf der $xy$-Ebene liegt.

**Lösung**:

Aus Symmetriegründen liegen $x_S$ und $y_S$ im Koordinatenursprung: $x_S = y_S = 0$.

Wir berechnen nur $z_S$:
$$z_S = \frac{1}{V} \iiint_{V} z \, dV$$

Mit dem Volumen der Halbkugel $V = \frac{2\pi R^3}{3}$ (aus Beispiel 1) erhalten wir:

$$z_S = \frac{3}{2\pi R^3} \iiint_{V} z \, dV$$

**Dreifachintegral**:
$$\iiint_{V} z \, dV = \int_{z=0}^{R} \int_{x=-\sqrt{R^2-z^2}}^{+\sqrt{R^2-z^2}} \int_{y=-\sqrt{R^2-z^2-x^2}}^{+\sqrt{R^2-z^2-x^2}} z \, dy \, dx \, dz$$

Da $z$ konstant bezüglich $x$ und $y$ ist:
$$= \int_{z=0}^{R} z \underbrace{\int_{x=-\sqrt{R^2-z^2}}^{+\sqrt{R^2-z^2}} \int_{y=-\sqrt{R^2-z^2-x^2}}^{+\sqrt{R^2-z^2-x^2}} 1 \, dy \, dx}_{=\pi(R^2-z^2)} dz$$

$$= \int_{z=0}^{R} z \cdot \pi(R^2-z^2) \, dz = \pi \int_{z=0}^{R} z(R^2-z^2) \, dz$$

$$= \pi \int_{z=0}^{R} (R^2z - z^3) \, dz = \pi \left[\frac{R^2z^2}{2} - \frac{z^4}{4}\right]_0^R$$

$$= \pi \left(\frac{R^4}{2} - \frac{R^4}{4}\right) = \pi \cdot \frac{R^4}{4}$$

**Schwerpunkt**:
$$z_S = \frac{3}{2\pi R^3} \cdot \frac{\pi R^4}{4} = \frac{3R}{8}$$

**Ergebnis**: Der Schwerpunkt liegt bei $S\left(0, 0, \frac{3R}{8}\right)$.

## 10.4.4 Weitere Anwendungen

Dreifachintegrale haben noch viele weitere wichtige Anwendungen in der Technik:

**Trägheitsmomente**: Die Berechnung von Trägheitsmomenten für rotierende Körper erfolgt mit Integralen der Form:
- Axiales Trägheitsmoment um die $z$-Achse: $I_z = \iiint_V (x^2 + y^2) \rho \, dV$
- Polares Trägheitsmoment: $J_p = \iiint_V r^2 \rho \, dV$

**Flächenmomente und Widerstandsmomente**: Diese sind wichtig für Festigkeitsberechnungen in der Strukturmechanik.

**Weitere physikalische Größen**: Potentielle Energie, elektrische/magnetische Felder in der Elektrotechnik.

Die detaillierte Behandlung dieser Anwendungen erfolgt in den Vorlesungen Technische Mechanik I-III sowie in spezialisierten Fächern wie Festigkeitslehre und Dynamik.

Das folgende Video geht auf die Bedeutung und Anwendung der Doppel- und Dreifachintegrale ein und zeigt deren praktische Relevanz in den Ingenieurswissenschaften.

```{dropdown} Video zu "Mehrdimensionale Integration | Bedeutung und Anwendung" von MathePeter
<iframe width="560" height="315" src="https://www.youtube.com/embed/H1Pj4SMVZ8s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{admonition} Weiteres Lernmaterial
:class: seealso
* Übungsaufgaben zu Volumen-, Masse- und Schwerpunktberechnungen
* Anwendungen in der Technischen Mechanik: Statik und Dynamik starrer Körper
* Berechnungsbeispiele aus der Konstruktionslehre
```