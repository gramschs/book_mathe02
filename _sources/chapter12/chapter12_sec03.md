# 12.3 Lösung inhomogene lineare DGL 1. Ordnung

Homogene lineare Differentialgleichungen beschreiben natürliche Prozesse ohne
äußere Einflüsse. In der Praxis wirken jedoch oft externe Kräfte: eine von außen
angelegte Spannung, eine Wärmequelle oder eine mechanische Anregung. Diese
äußeren Einwirkungen führen zu inhomogenen linearen Differentialgleichungen,
deren Lösung wir mit der Methode der Variation der Konstanten bestimmen können.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können eine **inhomogene lineare Differentialgleichung 1. Ordnung** lösen.
* Sie können das Lösungsverfahren **Variation der Konstanten** anwenden, um die
  Lösung einer linearen Differentialgleichung zu bestimmen.
* Sie verstehen die **Lösungsstruktur** inhomogener linearer
  Differentialgleichungen.
```

## Wie wird eine inhomogene lineare Differentialgleichung 1. Ordnung gelöst?

Betrachten wir eine inhomogene lineare Differentialgleichung 1. Ordnung:

$$a_1(x)y' + a_0(x) y = r(x).$$

Die Grundidee des Lösungsverfahren ist, dass sich die allgemeine Lösung der inhomogenen linearen DGL aus zwei Teilen zusammensetzt:

$$y(x)=y_h(x)+y_p(x).$$

Dabei ist

* $y_h(x)$ die homogene Lösung (löst die Gleichung ohne Störfunktion) und
* $y_p(x)$ partikuläre Lösung (eine spezielle Lösung der inhomogenen Gleichung).

**Schritt 1:** homogene Lösung bestimmen

Zunächst lösen wir die zugehörige homogene Gleichung (Störfunktion weggelassen):

$$a_1(x)y' + a_0(x) y = 0.$$

Die homogene Lösung kennen wir bereits aus Kapitel 12.2:

$$y_h(x)=C \cdot e^{-\int \frac{a_0(x)}{a_1(x)}\, dx}.$$

Um auch kenntlich zu machen, dass diese die Lösung der homogenen
Differentialgleichung ist, wird diese Lösung mit einem kleinen "h" markiert. Wie
üblich enthält die homogene Lösung eine Integrationskonstante $C\in\mathbb{R}$.

**Schritt 2:** Variation der Konstanten

Um eine partikuläre Lösung der inhomogenen Gleichung zu finden, verwenden wir
einen cleveren Ansatz: Wir variieren die Konstante $C$, indem wir sie durch eine
unbekannte Funktion $C(x)$ ersetzen. Der Lösungsansatz für die inhomogene
Gleichung lautet daher:

$$y(x)=C(x) \cdot e^{-\int \frac{a_0(x)}{a_1(x)}\, dx}.$$

Warum funktioniert das? Die homogene Lösung erfüllt bereits den "homogenen Teil"
der Differentialgleichung. Durch die Variation von $C$ zu $C(x)$ erhält die
Lösung die nötige Flexibilität, um auch die Störfunktion $r(x)$ zu
"kompensieren".

**Schritt 3:** Bestimmung von $C(x)$

Um die noch fehlende Funktion $C(x)$ zu bestimmen, leiten wir den Lösungsansatz
ab und setzen das Ergebnis in die ursprüngliche Differentialgleichung ein.
Dadurch entsteht eine neue Differentialgleichung für die unbekannte Funktion
$C(x)$, die wir durch Integration lösen können.

## Beispiel zur Lösung einer inhomogenen linearen DGL 1. Ordnung

Gegeben ist die inhomogene lineare Differentialgleichung 1. Ordnung

$$y'+3y=x^2.$$

*Schritt 1:* Die homogene Lösung ist

$$y_h(x)=C\cdot e^{-3x}.$$

*Schritt 2*: Wir ersetzen die Konstante $C$ durch die Funktion $C(x)$ und
erhalten den Ansatz:

$$y(x)=C(x)\cdot e^{-3x}.$$

*Schritt 3:* Als nächstes wird dieser Lösungsansatz mit der Prodduktregel
abgeleitet

$$y'(x)=C'(x)e^{-3x} + C(x)\cdot (-3) e^{-3x}$$

und in die ursprüngliche Differentialgleichung eingesetzt:

$$C'(x) \, e^{-3x} -3 C(x) \, e^{-3x} + 3C(x)\cdot e^{-3x} = x^2.$$

Wir vereinfachen zuerst die Gleichung

$$C'(x)\, e^{-3x} - 3 C(x) \, e^{-3x} + 3C(x)\cdot e^{-3x} = x^2$$

zu

$$ C'(x)\, e^{-3x} = x^2 \quad \Rightarrow \quad C'(x)=x^2\cdot e^{3x}.$$

Danach integrieren wir auf beiden Seiten unbestimmt nach $x$, indem wir zweimal
die partielle Integrationsregel anwenden:

\begin{multline*}
C(x)= \left[x^2\cdot\frac{1}{3}e^{3x}\right] -\int 2x \frac{1}{3}e^{3x}\, dx = \\
= \left[x^2\cdot\frac{1}{3}e^{3x}\right] - \left[2x\cdot\frac{1}{9}e^{3x}\right] + \int 2\cdot  \frac{1}{3}e^{3x} \, dx = \\
= \frac{1}{27}e^{3x}(9x^2 - 6x + 2) + C_1
\end{multline*}

Nachdem wir nun die Funktion $C(x)$ bestimmt haben, setzen wir diese Funktion in
den Lösungsansatz ein und haben damit die allgemeine Lösung der inhomogenen
Differentialgleichung bestimmt:

$$y(x)= C_1e^{-3x} + \frac{1}{3}x^2 - \frac{2}{9}x + \frac{2}{27}.$$

Wir prüfen unsere Lösung durch Einsetzen in die ursprüngliche
Differentialgleichung:

* $y'(x) = -3C_1e^{-3x} + \frac{2}{3}x - \frac{2}{9}$
* $y'(x) + 3y(x) = -3C_1e^{-3x} + \frac{2}{3}x - \frac{2}{9} + 3C_1e^{-3x} + 3
  \cdot \frac{1}{3}x^2 - 3 \cdot \frac{2}{9}x + 3 \cdot \frac{2}{27} = x^2$

```{admonition}  Wie wird eine inhomogene lineare DGL 1. Ordnung gelöst?
:class: note
Die inhomogene lineare DGL

$$a_1(x)y' + a_0(x)y = r(x)$$

lösen wir mit den folgenden Schritten:

1. Homogene Lösung bestimmen: $y_h(x) = C \cdot e^{-\int \frac{a_0(x)}{a_1(x)} \, dx}$
2. Ansatz mit Variation der Konstanten: $y(x) = C(x) \cdot e^{-\int \frac{a_0(x)}{a_1(x)} \, dx}$
3. Ableiten und in die ursprüngliche DGL einsetzen
4. $C(x)$ bestimmen durch Integration der entstehenden Gleichung
5. Allgemeine Lösung hat die Form: $y(x) = y_h(x) + y_p(x)$
```

```{dropdown} Video zu "Differentialgleichung inhomogen lösen" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/AWdLkNZJZ70" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Inhomogene lineare DGL 1. Ordnung – Variation der Konstanten" von Sciencebarbie
<iframe width="560" height="315" src="https://www.youtube.com/embed/DD8blQLaHDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir die Methode der Variation der Konstanten
kennengelernt, mit der sich inhomogene lineare Differentialgleichungen 1.
Ordnung systematisch lösen lassen. Die Lösung setzt sich stets aus der homogenen
Lösung (beschreibt das natürliche Verhalten des Systems) und einer partikulären
Lösung (kompensiert die äußere Störung) zusammen. Weil lineare
Differentialgiechungen in der Technik häufig eingesetzt werden, betrachten wir
im nächsten Kapitel ein System aus linearen Differentialgleichungen.
