# 11.3 Separable Differentialgleichungen

Eine besondere Klasse von Differentialgleichungen sind die separablen
Differentialgleichungen. Dieses Kapitel bietet eine Einführung in die separablen
Differentialgleichungen und zeigt, wie man sie löst.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was eine **separable** Differentialgleichung ist.
* Sie können das Lösungsverfahren **Trennung der Variablen** anwenden, um eine
  separable Differentialgleichung zu lösen.
```

## Was sind separable Differentialgleichungen?

Damit eine Differentialgleichung **separabel** ist, müssen zwei Bedingungen
erfüllt sein.

1. Die Differentialgleichung muss von 1. Ordnung sein.
2. Die rechte Seite (vorausgesetzt die 1. Ableitung der gesuchten Funktion steht
   links) lässt sich als ein Produkt von zwei Funktionen so umformen, dass eine
   Funktion nur von der Variablen $x$ abhängt und die andere Funktion nur Terme
   mit $y$ enthält, also

$$y' = f(x)\cdot g(y).$$

## Beispiel für eine separable Differentialgleichung

Die Differentialgleichung

$$y'= 5\, y \, x$$

ist eine separable Differentialgleichung. Sie ist von 1. Ordnung. Außerdem kann
die rechte Seite in ein Produkt umgeschrieben werden, bei dem ein Faktor eine
Funktion von $x$ ist, nämlich $f(x) = 5x$, und der andere Faktor nur von $y$
selbst abhängt, nämlich $g(y)=y$, also

$$y' = 5x \cdot y.$$

## Wie werden separable Differentialgleichungen gelöst?

Eine separable Differentialgleichung

$$y' = f(x)\cdot g(y)$$

lässt sich schrittweise wie folgt lösen:

1. Ersetzen Sie $y'$ durch den Differentialquotienen $\frac{dy}{dx}$.
2. Trennen Sie die Variablen, d.h. bringen Sie alle Terme mit $y$ nach links und
   alle Terme mit $x$ auf die rechte Seite der Gleichung.
3. Integrieren Sie auf beiden Seiten unbestimmt, d.h. suchen Sie die
   Stammfunktion.
4. Lösen Sie nach $y$ auf, falls das möglich ist.

## Beispiel für die Lösung einer separablen Differentialgleichung

Wir betrachten erneut die separable Differentialgleichung

$$y' = 5x \cdot y.$$

**Schritt 1:** Zuerst ersetzen wir die 1. Ableitung durch den
Differentialquotienten

$$\frac{dy}{dx} = 5x \cdot y.$$

**Schritt 2:** Als nächstes trennen wir die Variablen:

$$\frac{1}{y} \, dy = 5x \, dx.$$

**Schritt 3:** Dann integrieren wir die linke Seite nach $dy$ und die rechte
Seite nach $dx$:

$$
\int \frac{1}{y} \, dy = \int 5x \, dx \quad
\Rightarrow  \ln |y| + C_1 = \frac{5}{2} x^2 + C_2
$$

**Schritt 4:** Wir lösen nach $y$ auf. Zuerst sortieren wir die
Integrationskonstante $C_1$ nach rechts und nennen die dadurch entstandene
Differenz $C_2 - C_1$ einfach nur $\tilde{C}$

$$\Rightarrow  \ln |y| = \frac{5}{2} x^2 + \tilde{C}.$$

Nun verwenden wir den Trick, die linke und rechte Seite als Exponenten für die
Exponentialfunktion zu nutzen:

$$\Rightarrow e^{\ln(|y|)} = e^{\frac{5}{2} x^2 + \tilde{C}}.$$

Da die Exponentialfunktion die Umkehrfunktion der Logarithmusfunktion ist, gilt
nämlich $e^{\ln(|y|)} = |y|$ und wir sind durch diesen Trick den Logarithmus
losgeworden:

$$\Rightarrow |y(x)| = e^{\frac{5}{2} x^2 + \tilde{C}}.$$

Um eine spezielle Lösung zu erhalten, muss aufgrund von Zusatzinformationen die
Integrationskonstante $\tilde{C}$ bestimmt werden. Etwas leichter kann die
Konstante bestimmt werden, wenn sie nicht im Exponent steht. Wir schreiben daher
die allgemeine Lösung noch etwas um:

$$|y(x)| = e^{\frac{5}{2} x^2 + \tilde{C}} = e^{\frac{5}{2} x^2} \cdot
e^{\tilde{C}}.$$

Die rechte Seite ist positiv. Wenn wir die Betragsstriche weglassen, erhalten
wir die beiden Lösungen

\begin{align*}
y_1(x) &= +e^{\tilde{C}} \cdot e^{\frac{5}{2} x^2}, \\
y_2(x) &= -e^{\tilde{C}} \cdot e^{\frac{5}{2} x^2}.
\end{align*}

Gleichzeitig ist auch $y_3(x)=0$ eine Lösung der Differentialgleichung. Daher
müssten wir eigentlich drei Lösungen der Differentialgleichung notieren. Wenn
wir aber eine neue Konstante $C \in \mathbb{R}$ einführen, die sozusagen
$+e^{\tilde{C}}$ und $-e^{\tilde{C}}$ sowie die Null ersetzt, dann können wir
auch vereinfacht als allgemeine Lösung der Differentialgleichung $y' = 5x \cdot
y$ die Lösung

$$y(x) = C e^{\frac{5}{2}x^2} \quad \text{ mit } C\in\mathbb{R}$$

notieren.

```{dropdown} Video zu "Lösung separable Differentialgleichung"
<iframe src="https://frankfurt-university.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=bc52e263-cf13-4313-8f1f-ad53009d2b3c&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>
```

```{dropdown} Video zu "Differentialgleichung lösen" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/Sm0Go9IioJ4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
