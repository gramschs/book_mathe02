# 12.3 Lösung inhomogene lineare DGL 1. Ordnung

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```


## Wie wird eine inhomogene lineare DGL 1. Ordnung gelöst?

Nun betrachten wir eine inhomogene lineare DGL 1. Ordnung, also

$$a_1(x)y' + a_0(x) y = r(x).$$

Als erstes lassen wir die Störfunktion weg und berechnen die homogene Lösung

$$y_h(x)=C \cdot e^{-\int \frac{a_0(x)}{a_1(x)}\, dx}.$$

Dann ersetzen wir die Konstante $C$ durch eine Funktion $C(x)$ -- das nennt man **Variation der Konstanten** -- und setzen diese Lösung in die inhomogene DGL ein. Dadurch entsteht eine DGL für die unbekannte Funktion $C(x)$, die wir dann lösen.

Beispiel:

Gegeben ist die inhomogene lineare DGL 1. Ordnung

$$y'+3y=x^2.$$

Die homogene Lösung ist $y_h(x)=C\cdot e^{-3x}$. Wir variieren die Konstante

$$y(x)=C(x)\cdot e^{-3x} \quad \Rightarrow \quad y'(x)=C'(x)e^{-3x} -3 C(x) e^{-3x}$$

und setzen in die DGL ein:

$$C'(x)e^{-3x} -3 C(x) e^{-3x} + 3C(x)\cdot e^{-3x} = x^2.$$

Wir vereinfachen

$$C'(x)e^{-3x} -3 C(x) e^{-3x} + 3C(x)\cdot e^{-3x} = x^2$$

zu

$$ C'(x)e^{-3x} = x^2 \quad \Rightarrow \quad C'(x)=x^2\cdot e^{3x}.$$

Integration auf beiden Seiten:

\begin{multline*}
C(x)= \left[x^2\cdot\frac{1}{3}e^{3x}\right] -\int 2x \frac{1}{3}e^{3x}\, dx = \\
= \left[x^2\cdot\frac{1}{3}e^{3x}\right] - \left[2x\cdot\frac{1}{9}e^{3x}\right] + \int 2\cdot  \frac{1}{3}e^{3x} \, dx = \\
= \frac{1}{27}e^{3x}(9x^2 - 6x + 2) + C_1
\end{multline*}

Allgemeine Lösung der inhomogenen DGL

$$y(x)= C_1e^{-3x} + \frac{1}{3}x^2 - \frac{1}{9}x + \frac{2}{27}.$$


```{admonition} Video
:class: seealso
https://www.youtube.com/embed/AWdLkNZJZ70
```
