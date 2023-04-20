# 4.2 Restglied von Taylorreihen

Taylorreihen und ihre Konvergenzeigenschaften sind für Ingenieure von großer
Bedeutung, da sie bei der Lösung von Differentialgleichungen, der Optimierung
von Funktionen und der numerischen Berechnung von Integralen verwendet werden.
Taylorreihen bieten eine Möglichkeit, Funktionen durch einfachere, polynomiale
Funktionen zu approximieren, die leichter zu handhaben sind. Die Kenntnis des
Restglieds ermöglicht es Ingenieuren, die Genauigkeit der Approximation
abzuschätzen und zu entscheiden, wie viele Terme der Taylorreihe für eine
ausreichend genaue Lösung erforderlich sind.

## Lernziele

```{admonition} Lernziele
:class: tip
Sie können mit dem Restglied der Taylorreihe den Fehler abschätzen, der entsteht, wenn eine Funktion durch ein Taylorpolynom vom Grad n ersetzt wird.
```

## Restglied der Taylorreihe

Die Idee der Taylorreihe ist ja, eine komplizierte Funktion $f$ durch eine
Potenzreihe zu darzustellen. Allerdings ist das Aufsummieren von unendlich
vielen Summanden für die Taylorreihe auch nicht praktikabel. Stattdessen wird in
der Praxis die Taylorreihe ab einem bestimmten Grad abgebrochen. Oder anders
ausgedrückt, als Näherung für die Funktion $f$ in der Umgebung eines
Entwicklugnspunktes $x_0$ wird ein Taylorpolynom vom Grad $n$ genutzt. Aber wie
groß ist eigentlich der Fehler, wenn statt der Funktion $f$ das Taylorpolynom
$T_n$ genommen wird? Welcher Rest bleibt da? Eines ist schon einmal klar. Würden
wir für das Taylorpolynom einen anderen Grad $m$ nehmen, so würde sich auch ein
anderer Fehler ergeben. Der Rest ist also auch vom Grad des Taylorpolynoms
abhängig. Wir fassen zusammen:

```{admonition} Was ist ... das Restglied der Taylorreihe?
Wir nennen die Differenz zwischen der Funktion $f$ und dem dazugehörigen Taylorpolynom $T_n$ vom Grad $n$ das Restglied $R_n$. In Formel ausgedrückt ist das Restglied

$$R_n(x) = f(x) - T_n(x).$$
```

Jetzt haben wir dem Fehler zwar einen neuen Namen gegeben, Restglied, aber das
hilft uns erstmal noch nicht weiter. Allerdings hat ein Mathematiker namens
[Joseph-Louis Lagrange](https://de.wikipedia.org/wiki/Joseph-Louis_Lagrange)
gezeigt, dass für das Restglied die folgende Formel gilt:

$$R_n(x) = f(x) - T_n(x) =
\frac{f^{(n+1)}(\textcolor{red}{z})}{(n+1)!}\cdot(x-x_0)^{n+1},$$

wobei der Punkt $z$ eine Zwischenstelle ist, die irgendwo zwischen $x$ und $x_0$
liegt.

Leider ist die Formel nicht ganz so einfach anzuwenden, denn die Zwischenstelle $z$ ist ja nicht bekannt. Wir wissen nur, dass $z$ irgendwo zwischen dem Entwicklungspunkt $x_0$ und $x$ liegt. Aber egal wo $z$ jetzt wirklich liegt, wir können einfach für alle Werte $z$ die $(n+1)$-te Ableitung 

$$f^{(n+1)}(z)$$

zeichnen. Aus der Zeichnung können wir dann das Maximum $M$ von $f^{(n+1)}(z)$ für alle Punkte zwischen $x_0$ und $x$ ablesen oder anderweitig berechnen. Es gilt also

$$f^{(n+1)}(z) \leq M.$$

Und mit dieser Abschätzung kann jetzt endlich auch der Fehler abgeschätzt
werden, wenn $T_n$ anstatt der Funktion $f$ verwendet werden soll. Da wir nicht
wissen, ob $T_n$ die Funktion $f$ über- oder unterschätzt, wissen wir auch
nicht, ob $R_n(x)$ negativ oder positiv ist. Daher nehmen wir einfach mal den
Betrag von $R_n(x)$, da es ja auch nur um eine grobe Abschätzung des Fehlers
geht.

\begin{align*}
\left|R_n(x) \right| &= \left| f(x) - T_n(x) \right| = \\
    &= \left| \frac{f^{(n+1)}(z)}{(n+1)!}\cdot(x-x_0)^{n+1} \right| \leq\\
    &\leq \frac{M}{(n+1)!} \cdot |x-x_0|^{n+1}.
\end{align*}

Fast fertig, jetzt muss noch ein Maximum von $|x - x_0|$ bestimmt werden. Wir
nennen diese Zahl mal $d$ (wie Distanz). Dann kann der Fehler, der Betrag des
Restglieds des Taylorpolynoms, abgeschätzt werden als

$$\left|R_n(x) \right| \leq  \frac{M}{(n+1)!}\cdot d^{n+1}.$$

Das folgende Video fasst die obigen Erklärungen zusammen.

```{dropdown} Video zu "Taylor Restglied" von Prof. Hoever
<iframe width="560" height="315" src="https://www.youtube.com/embed/oz1hejsyNlk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Beispiel

Probieren wir das an einem Beispiel aus. Die Funktion $f(x)=\sin(x)$ soll durch
ein Taylorpolynom Grad 3 am Entwicklungspunkt $x_0=0$ approximiert werden. Im
Abschnitt [Kochrezept Taylorpolynome](ref04_sec01_kochrezept) haben wir ja schon
das Taylorpolynom $T_{3}$ berechnet als

$$T_3(x) = x - \frac{1}{6}x^3.$$

Die vierte Ableitung der Sinusfunktion ist wieder die Sinusfunktion selbst, also  $f^{(4)}(x) = \sin(x)$.
 
Das Restglied ist also

$$R_3(x) = \frac{\sin(z)}{(3+1)!}\cdot x^{3+1} = \frac{\sin(z)}{24}\cdot x^4.$$

für eine Zwischenstelle $z$ zwischen $0$ und $x$. Wir wählen einen Winkel von
$\alpha = 5^{\circ}$, was im Bogenmaß $\frac{\pi}{36}\approx 0.0873$ rad
entspricht und untersuchen daher die Approximation an der Stelle $x = 0.0873$.
Wenn wir die Sinusfunktion im Intervall $[0, 0.0873]$ zeichnen, so können wir
ablesen, dass das Maximum gerade bei $x = 0.0873$ erreicht wird, also ist

$$M = \sin(0.0873) \approx 0.0872.$$

Der Term $x - 0$ kann durch $m = 0.0873$ abgeschätzt werden, durch den Punkt am
rechten Intervallende, der am weitesten vom Entwicklungspunkt $x_0=0$ entfernt
ist. Also gilt

$$R_3(0.0873) \leq \frac{0.0872}{24}\cdot 0.0873^4 = 2.11 \cdot 10^{-7}.$$

Dieser maximale Fehler ist in den meisten Fällen so klein, dass im Intervall
$[-5^{\circ}, + 5^{\circ}]$ die Sinusfunktion auch durch 

$$sin(x) \approx T_3(x) = x - \frac{1}{6}x^3.$$

In vielen Fällen ist es sogar legitim, die Sinusfunktion nur durch das Taylorpolynom ersten Grades zu approximieren, also

$$\sin(x) \approx T_1(x) = x.$$

Diese Approximation nennt sich
[Kleinwinkelnäherung](https://de.wikipedia.org/wiki/Kleinwinkelnäherung) und
wird beispielsweise bei der Berechnung der Bewegungsgleichung des Fadenpendels
benötigt.

Ein weiteres Beispiel können Sie sich in dem folgenden Video ansehen.

```{dropdown} Video zu "Taylorpolynom, Restglied" von Daniel Jung
<iframe width="560" height="315" src="https://www.youtube.com/embed/Rc_diK5l7iY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```