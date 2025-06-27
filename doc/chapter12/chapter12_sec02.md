# 12.2 Lösung homogene lineare DGL 1. Ordnung

Homogene lineare Differentialgleichungen beschreiben viele natürliche
Abklingprozesse wie beispielsweise das Ausschwingen eines Pendels oder den
radioaktiven Zerfall. Das Besondere an diesen Gleichungen ist, dass sie sich
durch Trennung der Variablen elegant lösen lassen. In diesem Kapitel lernen wir
diese Lösungstechnik kennen.

## Lernziele

```{admonition} Lernziel
:class: goals
Sie können eine homogene lineare Differentialgleichung 1. Ordnung mit der
Lösungsmethode **Trennung der Variablen** lösen.
```

## Wie wird eine homogene lineare DGL 1. Ordnung gelöst?

Betrachten wir eine homogene lineare Differentialgleichung 1. Ordnung. Bei
homogenen Gleichungen ist die Störfunktion gleich Null. Daher schreiben wir die
Differentialgleichung in der Form

$$a_1(x)y' + a_0(x)y = 0.$$

Gegeben sind also zwei Funktionen $a_1$ und $a_0$, die nur von der Variable $x$
abhängen. Gesucht ist die Funktion $y$.

Diese Gleichung kann auch als eine separable Differentialgleichung betrachtet
werden. Dazu stellen wir zunächst nach $y'$ um und erhalten

$$y'= -\frac{a_0(x) y}{a_1(x)} \quad
\Rightarrow \frac{dy}{dx} = -\frac{a_0(x)}{a_1(x)} \, y.$$

Wir trennen die Veränderlichen:

$$\frac{1}{y} \, dy = -\frac{a_0(x)}{a_1(x)} \, dx.$$

Integration der beiden Seiten (mit Integrationskonstante $c_1$) ergibt

$$\ln |y| + c_1 = - \int \frac{a_0(x)}{a_1(x)} \, dx.$$

Wir bringen $c_1$ auf die rechte Seite der Gleichung und lösen nach $y$ auf:

$$|y(x)| = e^{-\int \frac{a_0(x)}{a_1(x)}\, dx - c_1}.$$

Um die Betragsstriche aufzulösen, unterscheiden wir zwei Fälle:

1. Ist $y(x) > 0$, so erhalten wir $y(x) = e^{-\int \frac{a_0(x)}{a_1(x)} \, dx -
c_1}$.
2. Ist $y(x) < 0$, so folgt $y(x) = -e^{-\int \frac{a_0(x)}{a_1(x)} \, dx -
c_1}$.

Da sowohl positive als auch negative Werte möglich sind, fassen wir beide Fälle
zusammen, indem wir $C = \pm e^{-c_1}$ setzen. Dabei kann $C$ eine beliebige
reelle Zahl (auch Null) sein. Somit erhalten wir als allgemeine Lösung

$$y(x) = C \, e^{-\int \frac{a_0(x)}{a_1(x)} \, dx}.$$

```{admonition} Wie wird eine homogene lineare DGL 1. Ordnung gelöst?
:class: note
Die allgemeine Lösung der homogenen linearen Differentialgleichung 1. Ordnung

$$a_1(x)y' + a_0(x)y = 0$$

wird durch die **Trennung der Variablen** berechnet und lautet

$$y(x) = C \, e^{-\int \frac{a_0(x)}{a_1(x)} \, dx}.$$

Dabei ist $C \in \mathbb{R}$ eine beliebige Integrationskonstante.
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
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir gelernt, homogene lineare Differentialgleichungen 1.
Ordnung durch Trennung der Variablen zu lösen. Die Lösung ist stets eine
Exponentialfunktion der Form $y(x) = C \cdot e^{-\int \frac{a_0(x)}{a_1(x)} \,
dx}$, die exponentielles Wachstum oder exponentiellen Zerfall beschreibt. Diese
universelle Lösungsstruktur erklärt, warum exponentiell verlaufende Prozesse in
Natur und Technik so häufig auftreten. Im nächsten Kapitel wenden wir uns
inhomogenen linearen Differentialgleichungen 1. Ordnung zu.
