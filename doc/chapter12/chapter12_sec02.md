# 12.2 Lösung homogene lineare DGL 1. Ordnung

Dieses Kapitel stellt ein Lösungsverfahren vor, um eine homogene lineare
Differentialgleichung 1. Ordnung zu lösen.

## Lernziele

```{admonition} Lernziel
:class: goals
Sie können eine **homogene lineare Differentialgleichung 1. Ordnung** lösen.
```

## Wie wird eine homogene lineare DGL 1. Ordnung gelöst?

Wir betrachten eine homogene lineare Differentialgleichung 1. Ordnung. Da die
Differentialgleichung homogen sein soll, ist die Störfunktion gleich Null. Daher
schreiben wir die Differentialgleichung in der Form

$$a_1(x)y' + a_0(x)y = 0.$$

Gegeben sind also zwei Funktionen $a_1$ und $a_0$, die nur von der Variable $x$
abhängen. Gesucht ist die Funktion $y$.

Die homogene lineare Differentialgleichung 1. Ordnung kann auch als eine
separable Differentialgleichung betrachtet werden. Dazu lösen wir die
Differentialgleichung nach $y'$ auf und erhalten

$$y'= -\frac{a_0(x) y}{a_1(x)} \quad
\Rightarrow \frac{dy}{dx} = -\frac{a_0(x)}{a_1(x)} \, y.$$

Wir trennen die Veränderlichen:

$$\frac{1}{y} \, dy = -\frac{a_0(x)}{a_1(x)} \, dx.$$

Unbestimmte Integration der beiden Seiten liefert

$$\ln |y| + c_1 = - \int \frac{a_0(x)}{a_1(x)} \, dx.$$

Wir bringen $c_1$ auf die rechte Seite der Gleichung und lösen nach $y$ auf:

$$|y(x)| = e^{-\int \frac{a_0(x)}{a_1(x)}\, dx - c_1}.$$

Um die Betragsstriche weglassen zu dürfen, setzen wir $C = \pm e^{-c_1}$
und erhalten als allgemeine Lösung der homogenen Differentialgleichung 1.
Ordnung

$$y(x) = C \, e^{-\int \frac{a_0(x)}{a_1(x)} \, dx}.$$

```{admonition} Wie wird die homogene lineare DGL 1. Ordnung gelöst?
:class: note
Die allgemeine Lösung der homogenen linearen Differentialgleichung 1. Ordnung

$$a_1(x)y' + a_0(x)y = 0$$

wird durch die Trennung der Variablen berechnet und lautet

$$y(x) = C \, e^{-\int \frac{a_0(x)}{a_1(x)} \, dx}.$$
```

## Beispiele zur Lösung einer homogenen linearen DGL 1. Ordnung

**Beispiel 1:** Gegeben ist die homogene lineare DGL 1. Ordnung

$$y'+3y=0,$$

also $a_1(x)=1$ und $a_0(x)=3$. Damit ist die allgemeine Lösung der
Differentialgleichung

$$y(x)=C \cdot e^{-\int \frac{3}{1}\, dx} = C\cdot e^{-3x}.$$

**Beispiel 2:** Gegeben ist die homogene lineare DGL 1. Ordnung

$$y'+xy=0,$$

also $a_1(x)=1$ und $a_0(x)=x$. Damit ist die allgemeine Lösung der
Differentialgleichung

$$y(x)=C \cdot e^{-\int \frac{x}{1} \, dx} = C\cdot e^{-\frac{1}{2}x^2}.$$

```{dropdown} Video zu "DGL 1. Ordnung | Typ 1: linear-homogen" von Lernkompass
<iframe width="560" height="315" src="https://www.youtube.com/embed/rrsyEAGZbw4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Differentialgleichung lösen – DGL 1. Ordnung, homogen" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/Sm0Go9IioJ4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
