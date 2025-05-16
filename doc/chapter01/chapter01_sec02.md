# 1.2 Eigenschaften von Integralen

Kennt man die Eigenschaften von Integralen, so kann das so manche Rechnung
erheblich vereinfachen. Im Folgenden werden die wichtigsten Eigenschaften von
Integralen präsentiert.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, wie sich das Integral verändert, wenn die beiden Integrationsgrenzen
  miteinander vertauscht werden:

$$\int_{a}^{b} f(x)\,dx = - \int_{b}^{a} f(x)\, dx.$$

* Sie wissen, dass das Integral Null ist, wenn die untere Integrationsgrenze
  gleich der oberen Integrationsgrenze ist:

$$\int_{a}^{a} f(x)\, dx = 0.\Rule{0 px}{0 em}{1.5 em}$$

* Sie wissen, dass ein Integral mit dem Punkt $c$ in zwei Integrale aufgespalten
  werden kann:

$$\int_{a}^{b} f(x) \,dx = \int_{a}^{c} f(x) \,dx + \int_{c}^{b} f(x) \,dx.
\Rule{0 px}{0 em}{1.5 em}$$

* Sie kennen die **Faktorregel**:

$$\int_{a}^{b} c\cdot f(x)\, dx = c\cdot
\int_{a}^{b} f(x)\, dx.$$

* Sie kennen die **Summenregel**:

$$\int_{a}^{b} f(x) \pm g(x) \, dx = \int_{a}^{b}f(x)\, dx \pm \int_{a}^{b}
g(x)\, dx.$$
```

## Integrationsgrenzen

Als erstes betrachten wir die Eigenschaften von Integralen, wenn der Integrand
$f$ gleich bleibt, aber die Integrationsgrenzen geändert werden.

Werden die beiden Integrationsgrenzen vertauscht, so ändert sich das Vorzeichen
des Integrals. Integrieren wir also die Funktion $f$ von $b$ nach $a$ anstatt
von $a$ nach $b$, müssen wir dieses Integral nur mit $-1$ multiplizieren, um das
ursprüngliche Integral von $a$ nach $b$ zu erhalten. In Formeln sieht das so aus:

$$\int_{a}^{b} f(x)\,dx = - \int_{\textcolor{red}{b}}^{\textcolor{red}{a}}
f(x)\, dx.$$

Gar nicht erst rechnen müssen wir, wenn das Integral über $f$ von $a$ bis $a$
geht. In anderen Worten betrachten wir jetzt ein Integral, bei dem die untere
Integrationsgrenze und die obere Integrationsgrenze zusammenfallen. Wenn wir das
Integral als orientierte Fläche zwischen dem Funktionsgraphen $f(x)$ und der
x-Achse interpretieren, heißt das, dass gar kein Rechteck mehr existiert.
Anstatt eines Rechtecke liegt sozusagen nur noch ein unendlich dünner Strich an
der Stelle $x=a$ vor, weil es ja von $a$ nach $a$ geht. Ein Strich hat keinen
Flächeninhalt, das Integral ist also Null. Als mathematische Formel notiert
heißt das:

$$\int_{\textcolor{red}{a}}^{\textcolor{red}{a}} f(x)\, dx = 0.\Rule{0 px}{0
em}{1.5 em}$$

Weiter geht es... wiederum hilft die Flächeninterpretation weiter. Diesmal
erfinden wir einen neuen Punkt $c$. Dann kann die Fläche zwischen
Funktionsgraph, x-Achse und den Grenzen a und b in zwei Flächen aufgeteilt
werden. Die erste Fläche ist die Fläche zwischen Funktionsgraph und x-Achse von
$a$ nach $c$. Die zweite Fläche ist die Fläche zwischen Funktionsgraph und
x-Achse von $c$ nach $b$. Und beide Flächen zusammen müssen wieder die
ursprüngliche Fläche ergeben. Also:

$$\int_{a}^{b} f(x) \,dx = \int_{a}^{\textcolor{red}{c}} f(x) \,dx +
\int_{\textcolor{red}{c}}^{b} f(x) \,dx. \Rule{0 px}{0 em}{1.5 em}$$

Alle drei Eigenschaften werden nochmal in dem folgenden Video erläutert.

```{dropdown} Video: Eigenschaften/Rechenregeln des Integrals I
<iframe width="560" height="315" src="https://www.youtube.com/embed/BKgcS2wgwu0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Linearität des Integrals

Linearität des Integrals klingt kompliziert, ist es aber nicht. Gemeint sind
damit die folgenden zwei Eigenschaften.

Faktorregel: Wenn die Funktion $f$ mit einer konstanten Zahl $c$ multipliziert
wird und dann integriert werden soll, dann können wir auch zuerst das Integral
von $f$ berechnen und danach das Ergebnis $c$ multiplizieren. Oder anders
ausgedrückt: wenn im Integranden ein konstanter Faktor ist, dann darf man diesen
konstanten Faktor auch vor das Integral ziehen.

$$\int_{a}^{b} c\cdot f(x)\, dx = c\cdot
\int_{a}^{b} f(x)\, dx.$$

Summenregel: Soll die Summe oder die Differenz zweier Funktionen integriert
werden, dürfen auch zuerst die beiden Einzelintegrale berechnet werden und
danach Summe oder Differenz gebildet werden:

$$\int_{a}^{b} f(x) \pm g(x) \, dx = \int_{a}^{b}f(x)\, dx \pm \int_{a}^{b}
g(x)\, dx.$$

In dem folgenden Video werden beide Eigenschaften erläutert und anhand eines
Beispiels demonstriert.

```{dropdown} Video: Eigenschaften/Rechenregeln des Integrals II
<iframe width="560" height="315" src="https://www.youtube.com/embed/eMGWYY96Hno" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

Nachdem wir in diesem Kapitel Eigenschaften von Integralen betrachtet haben,
wenden wir uns Integrationstechniken zu. Zunächst lernen wir die partielle
Integration, im übernächsten Kapitel dann die Integration durch Substitution.
