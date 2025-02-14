# 6.4 Rechenregeln Fourierreihen

Zuletzt betrachten wir noch einige Eigenschaften von Fourierreihen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, dass sich bei geraden oder ungeraden Funktionen die Berechnung der
  Fourierkoeffizienten vereinfacht.
* Sie können die Summe zweier Fourierreihen bilden.
* Sie können die Ableitung einer Fourierreihe berechnen.
```

## Gerade und ungerade Funktionen

Wenn die Funktion $f$, zu der eine Fourierreihe gesucht ist, bestimmte
Symmetrieeigenschaften hat, kann sich dadurch die Berechnung der
Fourierkoeffizienten vereinfachen.

Ist die Funktion $f$ gerade, gilt also $f(t) = f(-t)$, dann fallen alle Terme
mit der Sinusfunktion weg (die ja ungerade ist). Also gilt automatisch $b_k =
0$. Außerdem ist dann auch das Produkt $f(t)\cdot \cos(k \omega t)$ eine gerade
Funktion, da die Kosinusfunktion ebenfalls gerade ist. Wir brauchen nicht von
$-T/2$ bis $T/2$ integrieren, sondern können auch nur von $0$ bis $T/2$
integrieren und das Ergebnis verdoppeln. Damit erhalten wir für **gerade
Funktionen** $f$ die folgende Fourierreihe:

$$f(t) = \frac{a_0}{2} + \sum_{k=1}^{\infty} a_k \cos(k \omega t)$$

mit den Fourierkoeffizienten

$$a_k = \frac{4}{T}\int_{0}^{T/2} f(t) \cos(k \omega t) \, dt.$$

Für **ungerade Funktionen** $f$, also solche für die $f(t) = -f(-t)$ gilt,
fallen die $a_k$ weg. Es bleibt eine reine Sinusreihe übrig.

$$f(t) = \sum_{k=1}^{\infty} b_k \sin(k \omega t)$$

mit

$$b_k = \frac{4}{T} \int_{0}^{T/2} f(t) \sin(k \omega t) \, dt.$$

```{dropdown} Vide "Fourierreihe: gerade/ungerade" von Daniel Jung
<iframe width="560" height="315" src="https://www.youtube.com/embed/7Uig_X9Lg3s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Addition

Wenn zwei Funktionen $f$ und $g$ die gleiche Periode $T$ haben, so hat die Summe
der beiden Funktionen ebenfalls wieder die Periode $T$. Liegen nun für beide
Funktionen Fourierreihen vor, so dürfen wir auch einfach die
Fourierkoeffizienten addieren, um eine Approximation der Funktion $f+g$ zu
erhalten.

## Ableitung

Wenn eine Funktion $f$ durch eine Fourierreihe dargestellt wird, also

$$f(t) = \frac{a_0}{2} + \sum_{k=1}^{\infty} \left(a_k \cos(k \omega t) + b_k
\sin(k \omega t) \right)$$

gilt, dann ist ihre Ableitung wieder eine Fourierreihe.

$$f'(t) = \sum_{k=1}^{\infty} \left(\alpha_k \cos(k \omega t) + \beta_k
\sin(k \omega t) \right).$$

Allerdings fällt der erste Term $a_0/2$ weg und die neuen Fourierkoeffizienten
$\alpha_k$ und $\beta_k$ können mit den Formeln

\begin{align*}
\alpha_k &= b_k \cdot k \cdot \omega \\
\beta_k  &= -a_k \cdot k \cdot \omega
\end{align*}

berechnet werden.
