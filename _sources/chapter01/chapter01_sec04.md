# 1.4 Integration durch Substitution

Auch verkettete Funktionen lassen sich nicht so einfach integrieren. Wenn $F$
eine Stammfunktion der Funktion $f$ ist, dann gilt für die der verketten
Funktion $F\circ g$ die Kettenregel:

$$\big(F(g(x))\big)^{\prime} = F'(g(x)) \cdot g'(x) = f(g(x))\cdot g'(x).$$

Die Umkehrung davon ist die Integration durch Substitution.

## Lernziele

```{admonition} Lernziele
:class: goals
Sie können die Substitutionsregel

$$\int_{a}^{b} f(g(x))\cdot g^{\prime}(x) \, dx = \int_{g(a)}^{g(b)} f(z) \,
dz$$

anwenden.
```

## Substitutionsregel

Die Idee der Substitutionsregel ist es, die Kettenregel sozusagen umzukehren.
Wir gehen jetzt davon aus, dass die Funktion $f(g(x))\cdot g^{\prime}(x)$ auf
dem Intervall $[a,b]$ integriert werden soll, also die rechte Seite der obigen
Kettenregel. Dann ist das Ergebnis

$$\int_{a}^{b} f(g(x))\cdot g^{\prime}(x) \, dx = \int_{g(a)}^{g(b)} f(z) \,
dz.$$

Das klappt übrigens nur, wenn die Funktion $g$ stetig differenzierbar ist. In
den Ingenieurswissenschaften ist das aber meistens der Fall, so dass diese
Einschränkung kein Problem darstellt. Problematisch ist dahingegen, dass
meistens nur die verkette Funktion ohne den Term $g'(x)$ im Integral steht.
Daher muss sehr oft der Integrand passend erweitert werden, um ihn erstmal auf
die Form

$$f(g(x))\cdot g^{\prime}(x)$$

zu bringen.

## Beispiel für Integration durch Substitution

Wir wollen die Funktion $\sqrt{1+3x^2}\cdot x$ auf dem Intervall $[0,1]$
integrieren, also

$$\int_{0}^{1} \sqrt{1+3x^2}\cdot x \, dx$$

ausrechnen.

Da die Funktion $g(x)=1+3x^2$ in die Wurzelfunktion $f(x)=\sqrt{x}$ eingesetzt
wird, liegt eine verkettete Funktion vor: $f(g(x)) = \sqrt{1+3x^2}$. Wir müssen
als erstes den Integranden so umformen, dass noch mit der Ableitung
$g'(x)=\left(1+3x^2\right)=6x$ multipliziert wird. Tatsächlich wird ja mit $x$
multipliziert, aber dummerweise nicht mit $6x$. Also ergänzen wir noch die
fehlende $6$ im Integranden und teilen aber wieder durch $6$, da wir ja den
Integranden nicht verändern wollen. Zusammengefasst also

$$\int_{0}^{1} \sqrt{1+3x^2}\cdot x \, dx =
\textcolor{red}{\frac{1}{6}}\int_{0}^{1} \sqrt{1+3x^2}\cdot \textcolor{red}{6}x \, dx.$$

Für das so umgeschriebene Integral dürfen wir die Substitutionsregel anwenden.
Dazu müssen noch die untere und obere neuen Integrationsgrenzen ausgerechnet
werden:

* untere Grenze: $x = 0 \Rightarrow g(0) = 1+3\cdot 0^2 = 1$
* obere Grenze: $x = 1 \Rightarrow g(1) = 1 + 3\cdot 1^2 = 4$

Wir erhalten also:

$$\frac{1}{6} \int_{0}^{1} \sqrt{1+3x^2}\cdot 6x \, dx =
\frac{1}{6} \int_{\textcolor{red}{1}}^{\textcolor{red}{4}} \sqrt{z} \, dz. $$

Die Wurzelfunktion zu integrieren ist aber nicht so schwer, also

$$ \frac{1}{6} \int_{1}^{4} \sqrt{z} \, dz = \frac{1}{6} \big[
\frac{2}{3}z^{\frac{3}{2}} \big] = \frac{1}{9} \big( 4^{\frac{3}{2}} -
1^{\frac{3}{2}}\big) = \frac{7}{9}.$$

Somit haben wir das Ergebnis

$$\int_{0}^{1} \sqrt{1+3x^2}\cdot x \, dx = \frac{7}{9}.$$

## Weiteres Lernmaterial

Integration durch Substitution ist nicht einfach. Daher folgen hier einige
Videos zur Vertiefung.

```{dropdown} Video "Integration durch Substition I" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/Bd7rrWT3fRA"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video "Integration durch Substition II" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/EJH2_GfoguI"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video "Integration durch Substition III" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/FHgo5FEM2bs"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video "Integration durch Substition IV" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/fffJ6Y5OYNA"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video "Integration durch Substition" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/0j55gTZVwy0"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
