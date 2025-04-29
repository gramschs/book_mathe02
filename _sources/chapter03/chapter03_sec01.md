# 3.1 Reihen

Reihen sind sehr spezielle Folgen. Falls Sie Ihr Wissen über Folgen auffrischen
wollen, können Sie die Internetseite [Folgen, Grenzwerte und
Stetigkeit](https://gramschs.github.io/book_mathe01/chapter09/sec00.html)
aus der Mathematik 1 Vorlesung als Startpunkt nehmen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können den Fachbegriff **Partialsumme** einer Reihe erklären.
* Sie können den Fachbegriff **Reihe** erklären.
* Sie wissen, was eine **konvergente** Reihe ist und wie der Grenzwert bezeichnet wird.
* Sie wissen, was eine **divergente** Reihe ist. 
* Sie kennen als Beispiel für Reihen
    * die **geometrische Reihe** und
    * die **harmonische Reihe**.
```

## Was ist eine Partialsumme und was ist eine Reihe?

Das Lieblingsbeispiel vieler Mathematiker:innen zur Einführung von Reihen ist
das vom griechischem Philosophen
[Zenon](https://de.wikipedia.org/wiki/Zenon_von_Elea) beschriebene Paradoxon von
[Achilles und der
Schildkröte](https://de.wikipedia.org/wiki/Achilles_und_die_Schildkröte). Wir
betrachten hier rein mathematische Beispiele.

Eine Reihe wird aus einer Folge gebildet. Als Beispiel betrachten wir die Folge
$(a_k)$ mit $a_k=\left(\frac{1}{2}\right)^{k}$. Explizit hingeschrieben lautet
die Folge $(a_k)$ also: $\frac{1}{2}$, $\frac{1}{4}$, $\frac{1}{8}$,
$\frac{1}{16}$, $\frac{1}{32}$, usw. Daraus bilden wir eine neue Folge, die wir
$(s_n)$ bezeichnen, indem wir Summen nach dem folgenden Schema bilden:

\begin{align*} s_1 &= a_1 = \frac{1}{2}\\
s_2 &= a_1 + a_2 =  \frac{1}{2} + \frac{1}{4} = \frac{3}{4}\\
s_3 &= a_1 + a_2 + a_3 = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} = \frac{7}{8}\\
\vdots\\
s_n &= a_1 + a_2 + \ldots + a_n =  \frac{1}{2} + \frac{1}{4} + \dots +
\left(\frac{1}{2}\right)^{n} \end{align*}

Jedes Folgenglied $(s_n)$ enthält Summen. Jede dieser Summen wird
**Partialsumme** genannt. Die Folge aus Partialsummen wird **Reihe** genannt.

```{admonition} Was ist ... eine Reihe?
:class: note
Eine Reihe ist eine Folge, die aus einer anderen Folge durch Summation gebildet wird. Etwas präziser formuliert starten wir mit einer Folge $(a_k)$ und bilden draus die Folge der Partialsummen nach dem Schema

$$s_n = a_1 + a_2 + \ldots + a_n = \sum_{k=1}^{n} a_k.$$

Die Folge $(s_n)$ wird dann Reihe zu der Folge $(a_k)$ genannt.
```

## Konvergenz und Divergenz von Reihen

Reihen sind also nichts anderes als Folgen. Allerdings haben Reihen eine
besondere Struktur, da sie ja sehr systematisch durch Summation aus Folgen
gebildet werden. Das hilft später, Kriterien für die Konvergenz und Divergenz
von Reihen zu finden, die diese Systematik ausnutzen.

```{admonition} Was ist ... eine konvergente Reihe?
:class: note
Eine Reihe wird konvergent genannt, wenn die Folge der Partialsummen gegen einen Grenzwert konvergiert. Dieser Grenzwert wird dann mit dem mathematischen Symbol

$$\sum_{k=1}^{\infty} a_k$$

bezeichnet. 
```

Im Falle von Konvergenz wird also einfach der Limes $\lim_{n \to \infty}$
weggelassen und der Index $n$ durch das Unendlich-Symbol $\infty$ ersetzt, wie
die rot markierten Bezeichnungen zeigen:

$$\lim_{n \to \infty} s_n = \lim_{\textcolor{red}{n \to \infty}}
\sum_{k=1}^{\textcolor{red}{n}} a_k = \sum_{k=1}^{\textcolor{red}{\infty}}
a_k.$$

Eigentlich darf diese Bezeichnung nur dann verwendet werden, wenn die Reihe auch
wirklich konvergiert. Oft wird diese Bezeichnung aber auch für Reihen im
Allgemeinen verwendet.

```{admonition} Was ist ... eine divergente Reihe?
:class: note
Eine Reihe wird divergent genannt, wenn die Folge der Partialsummen divergiert, also *nicht* gegen einen Grenzwert konvergiert.
```

```{dropdown} Video zu Reihen - Einführung, Konvergenz und Divergenz
<iframe width="560" height="315" src="https://www.youtube.com/embed/1vQ67chDVbU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Bekannte Reihen

Manche Reihen sind wichtiger als andere und haben daher einen eigenen Namen. Die
geometrische Reihe gehört zu diesen wichtigen Reihen. Sie heißt geometrische
Reihe, weil sie aus der geometrischen Folge gebildet wird. Ebenfalls wichtig ist
die harmonische Reihe. Wir werden beide Reihen in den folgenden Abschnitten
betrachten.

### Die geometrische Reihe

Zur Erinnerung: eine Folge heißt geometrische Folge, wenn der Quotient zweier
benachbarter Folgenglieder eine konstante Zahl ist. Wird also $a_2$ durch $a_1$
geteilt, kommt eine Zahl heraus, die wir $q$ nennen. Und wird $a_3$ durch $a_2$
geteilt, dann kommt auch $q$ heraus. Und das gleiche gilt für $a_{4} / a_{3}$
und für $a_{5} / a_{4}$, es kommt immer $q$ heraus, also

$$\frac{a_{k+1}}{a_k} = q.$$

Das bedeutet aber auch, dass alle Folgenglieder $a_k$ auf das erste Folgenglied
$a_1$ zurückgeführt werden können:

\begin{align*} a_1 &= a_1 \\
a_2 &= a_1 \cdot q \\
a_3 &= a_2 \cdot q = \left( a_1 \cdot q \right) \cdot q = a_1 \cdot q^2 \\
a_4 &= a_3 \cdot q = \left( a_1 \cdot q^2 \right) \cdot q = a_1 \cdot q^3 \\
\vdots \\
a_{k} &= a_{k-1} \cdot q = a_1 \cdot q^{k-1} \\ \end{align*}

Damit haben wir folgende Partialsummen:

\begin{align*} s_1 &= a_1 \\
s_2 &= a_1 + a_2 = a_1 + a_1 \cdot q = a_1 \cdot \big(1 + q\big) \\
s_3 &= a_1 + a_2 + a_3 = a_1 + a_1 \cdot q + a_1 \cdot q^2 = a_1 \cdot \big(1 +
q + q^2\big) \\
\vdots \\
s_n &= a_1 + a_2 + \dots + a_n = a_1 + a_1 \cdot q + \ldots + a_1 \cdot q^{n-1}
= a_1 \cdot \big(1 + q + \ldots q^{n-1}\big) \\
\end{align*}

```{admonition} Was ist ... die geometrische Reihe?
:class: note
Die geometrische Reihe ist die Folge $(s_n)$ der Partialsummen

$$s_n = 1 + q + q^2 + q^3 + \ldots + q^{n-1} = \sum_{k=0}^{n} q^{k}.$$
```

Falls Sie sich wundern, dass wir diesmal mit $k=0$ als Index anfangen, das ist
einfach praktischer, weil $q^{0} = 1$ gilt und wir uns umständliche
Schreibweisen sparen können.

Was die Konvergenz bzw. Divergenz anbelangt, es kommt auf die Zahl $q$ an, ob
die geometrische Reihe konvergiert oder divergiert.

```{admonition} Wann konvergiert die geometrische Reihe?
:class: note
Wenn der Betrag der Zahl $q$ kleiner als Eins ist, also $|q|<1$ gilt, dann konvergiert die geometrische Reihe und ihr Grenzwert ist

$$\sum_{k=0}^{\infty} q^k = \frac{1}{1-q}.$$

Für $|q|\geq 1$ divergiert die geometrische Reihe.
```

```{dropdown} Video zu geometrische Reihe
<iframe width="560" height="315" src="https://www.youtube.com/embed/y_9ccgrwTZo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Mathe-Song zur geometrischen Reihe von DorFuchs
<iframe width="560" height="315" src="https://www.youtube.com/embed/2TCDiK7GpNM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

### Die harmonische Reihe

Jetzt haben wir uns das Beispiel einer konvergenten Reihe angesehen
(zumindest, wenn $|q|<1$), jetzt kommt eine berühmte divergente Reihe, die
harmonische Reihe.

```{admonition} Was ist ... die harmonische Reihe?
:class: note
Die harmonische Reihe wird aus der Summe der harmonischen Folge $a_k = \frac{1}{k}$ gebildet:

$$s_n = \frac{1}{1} + \frac{1}{2} + \frac{1}{3} + \ldots + \frac{1}{n} = \sum_{k=1}^{n} \frac{1}{k}.$$

Sie ist divergent.
```

```{dropdown} Video zu harmonische Reihe
<iframe width="560" height="315" src="https://www.youtube.com/embed/n2ELwRkgKhc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir Reihen betrachtet, die aus Zahlenfolgen generiert
werden. Bei Reihen stellt sich immer die Frage, ob die Reihe konvergiert oder
divergiert. Für die sehr bekannte geometrische Reihe haben wir ein Kriterium
angegeben, wann diese Reihe konvergiert. Die harmonische Reihe divergiert. Im
nächsten Kapitel werden wir uns mit Konvergenzkriterien beschäftigen, um für
beliebige Reihen das Konvergenzverhalten bestimmen zu können.
