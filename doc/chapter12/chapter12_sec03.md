# 12.3 Lösung inhomogene lineare DGL 1. Ordnung

Nachdem im letzten Kapitel die Lösung einer homogenen linearen
Differentialgleichung 1. Ordnung behandelt wurde, geht es nun um die Lösung
inhomogenr linearer Differentialgleichungen 1. Ordnung.


## Lernziele
```{admonition} Lernziele
:class: important
* Sie können eine **inhomogene lineare Differentialgleichung 1. Ordnung** lösen.
* Sie können das Lösungsverfahren **Variation der Konstanten** anwenden, um die
  Lösung einer linearen Differentialgleichung zu bestimmen.
```


## Wie wird eine inhomogene lineare Differentialgleichung 1. Ordnung gelöst?

Nun betrachten wir eine inhomogene lineare Differentialgleichung 1. Ordnung,
also

$$a_1(x)y' + a_0(x) y = r(x).$$

Obwohl unser Ziel ist, die inhomogene Differentialgleichung zu lösen, lassen wir
zunächst einmal die Störfunktion weg und berechnen die homogene Lösung

$$y_h(x)=C \cdot e^{-\int \frac{a_0(x)}{a_1(x)}\, dx}.$$

Um auch kenntlich zu machen, dass diese die Lösung der homogenen
Differentialgleichung ist, wird diese Lösung mit einem kleinen "h" markiert. Wie
üblich enthält die homogene Lösung eine Integrationskonstante $C\in\mathbb{R}$.
Der Trick, um die inhomogene Differentialgleichung zu lösen, beruht darauf, nun
diese Integrationskonstante zu variieren. Wir ersetzen die Konstante $C$ durch
eine Funktion $C(x)$ -- das nennt man **Variation der Konstanten**. Der
Lösungsansatz für die inhomogene lineare Differentialgleichung1. Ordnung lautet
also

$$y(x)=C(x) \cdot e^{-\int \frac{a_0(x)}{a_1(x)}\, dx}.$$

Um die noch fehlende Funktion $C(x)$ zu bestimmen, leiten wir den Lösungsansatz
einmal ab und setzen das Ergebnis in die Differentialgleichung ein. Dadurch
entsteht eine neue Differentialgleichung für die unbekannte Funktion $C(x)$, die
wir dann lösen.


## Beispiel zur Lösung einer inhomogenen linearen DGL 1. Ordnung

Gegeben ist die inhomogene lineare Differentialgleichung 1. Ordnung

$$y'+3y=x^2.$$

Die homogene Lösung ist $y_h(x)=C\cdot e^{-3x}$. Wir variieren die Konstante und
erhalten den Lösungsansatz

$$y(x)=C(x)\cdot e^{-3x}.$$

Als nächstes wird dieser Lösungsansatz abgeleitet 

$$\Rightarrow \quad y'(x)=C'(x)e^{-3x} + C(x)\cdot (-3) e^{-3x}$$

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

$$y(x)= C_1e^{-3x} + \frac{1}{3}x^2 - \frac{1}{9}x + \frac{2}{27}.$$

```{dropdown} Video zu "Differentialgleichung inhomogen lösen" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/AWdLkNZJZ70" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Inhomogene lineare DGL 1. Ordnung – Variation der Konstanten" von Sciencebarbie
<iframe width="560" height="315" src="https://www.youtube.com/embed/DD8blQLaHDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
