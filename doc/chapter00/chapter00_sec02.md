# Rechenregeln Ableitungen

In diesem Kapitel beschäftigen wir uns damit, wie die mühsame Methode der
Grenzwertbildung aus einer Folge von Differenzenquotienten vereinfacht werden
kann. Dazu betrachten wir die Ableitungen von grundlegenden Funktionen. Mit
Hilfe von Ableitungsregeln können daraus die Ableitungen von komplizierteren
Funktionen gebildet werden.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was eine **Ableitungsfunktion** ist.
* Sie kennen von grundlegenden Funktionen die Ableitungsfunktionen auswendig.
* Sie beherrschen die folgenden Ableitungsregeln:
  * Faktorregel
  * Summenregel
  * Produktregel
  * Quotientenregel
  * Kettenregel
```

## Die Ableitungsfunktion

Im letzten Kapitel haben wir den Differentialquotienten bzw. die Ableitung an
einer einzelnen Stelle berechnet. In diesem Abschnitt wollen wir dieses Vorgehen
auf ein Intervall verallgemeinern. Wir betrachten dazu als Beispiel die Funktion
$f(x) = x^2$. Zunächst berechnen wir die Ableitung an einer einzelnen Stelle,
beispielsweise für $x_1 = 2$. Dazu bilden wir den Grenzwert der Folge der
Differentialquotienten:

\begin{align*}
f'(2)
&= \lim_{x_2 \to 2} \frac{f(x_2) - f(2)}{x_2 - 2} = \\
&= \lim_{x_2 \to 2} \frac{x_2^2 - 4}{x_2 - 2} = \\
&= \lim_{x_2 \to 2} \frac{(x_2 - 2) \cdot (x_2 + 2)}{x_2 - 2} = \\
&= \lim_{x_2 \to 2} x_2 + 2 = \\
&= 4.
\end{align*}

Jetzt verallgemeinern wir die Grenzwertbildung auf beliebige Stellen
$x\in\mathbb{R}$. Die Vorgehensweise zur Berechnung des Grenzwertes bleibt dabei
gleich:

\begin{align*}
f'(x)
&= \lim_{x_2 \to x} \frac{f(x_2) - f(x)}{x_2 - x} = \\
&= \lim_{x_2 \to x} \frac{x_2^2 - x^2}{x_2 - x} = \\
&= \lim_{x_2 \to x} \frac{(x_2 - x) \cdot (x_2 + x)}{x_2 - x} = \\
&= \lim_{x_2 \to x} x_2 + x = \\
&= 2x.
\end{align*}

Wir haben also zu jeder Stelle $x\in\mathbb{R}$ einen Wert für die Ableitung
$f'(x)$ an dieser Stelle gefunden, nämlich $f'(x) = 2x$. Damit ist $f'$ eine
Funktion, denn jedem x-Wert wird eindeutig ein y-Wert f'(x) zugeordnet. Diese
Erkenntnis klingt erst einmal banal, hilft ungemein bei der konkreten Berechnung
von Ableitungen. Für häufig vorkommene Funktionen sind deren
Ableitungsfunktionen in Tabellen hinterlegt. Und wie wir in den nächsten
Abschnitten sehen werden, können viele komplizierte Funktionen aus einfachen
Grundfunktionen zusammengesetzt werden. Kennen wir die Ableitungsfunktionen der
Grundfunktionen, können wir so wieder die Ableitungsfunktion der komplizierten
Funktion zusammensetzen.

```{admonition} Was ist ... die Ableitungsfunktion?
:class: note
Wenn für eine Funktion $f$ an jeder Stelle ihrer Definitionsmenge die Ableitung
existiert, kann eine neue Funktion gebildet werden, die jedes $x$ aus der
Definitionsmenge auf die Ableitung $f'(x)$ abbildet. Diese Funktion $f'$ wird
Ableitungsfunktion von $f$ genannt.
```

## Ableitungen von wichtigen Grundfunktionen

Eine **konstante Funktion** ist besonders leicht abzuleiten, denn die Ableitung
ist an jeder Stelle Null:

$$f(x)=C \Rightarrow f'(x)=0.$$

Beispiel:

$$f(x) = 5 \Rightarrow f'(x) = 0.$$

Die Ableitung einer Potenzfunktion ergibt wieder eine Potenzfunktion, allerdings
wird der Exponent um Eins verringert und der alte Exponent wird ein neuer
Vorfaktor. Für natürliche Exponenten $n\in\mathbb{N}$ lautet die
Ableitung:

$$f(x)=x^{n} \Rightarrow f'(x)=n\cdot x^{n-1}.$$

Die Wurzelfunktion ist etwas schwieriger abzuleiten.

$$f(x)=\sqrt{x} \Rightarrow f'(x)=\frac{1}{2\sqrt{x}}.$$

Tatsächlich kann die Wurzelfunktion auch als Potenzfunktion interpretiert
werden, also $\sqrt{x} = x^{\frac{1}{2}}$. Für Potenzfunktionen, bei denen der
Exponent ein Bruch oder gar eine reelle Zahl ist, gelten dieselben
Ableitungsregeln wie für Potenzfunktionen mit natürlichem Expoenten. Die einzige
Einschränkung dabei ist, dass $x$ positiv sein muss.

$$f(x) = x^{r} \Rightarrow f'(x) = r\cdot x^{r-1}, \quad x >0.$$

Mit diesem Wissen kann die Ableitung der Wurzelfunktion auch folgendermaßen
berechnet werden:

$$f(x) = x^{\frac{1}{2}} \Rightarrow f'(x) = \frac{1}{2} x^{-\frac{1}{2}} = \frac{1}{2} \frac{1}{x^{\frac{1}{2}}} = \frac{1}{2}\frac{1}{\sqrt{x}}.$$

Die Liste der Ableitungen der trigonometrischen Funktionen lautet:
\begin{align*}
f(x)=\sin(x) &\Rightarrow f'(x)=\cos(x) \\
f(x)=\cos(x) &\Rightarrow f'(x)=-\sin(x) \\
f(x)=\tan(x) &\Rightarrow f'(x)=\frac{1}{\cos^2(x)} \\
f(x)=\cot(x) &\Rightarrow f'(x)=-\frac{1}{\sin^2(x)} \\
\end{align*}

Am einfachsten lässt sich die Exponentialfunktion ableiten, sie bleibt sie
selbst.

$$f(x)=e^{x}=\exp(x) \Rightarrow f'(x)=e^{x}=\exp(x).$$

Zum Abschluss der Liste mit den wichtigsten Ableitungsfunktionen notieren wir
noch die Ableitung der Logarithmsfunktion:

$$f(x)=\ln(x) \Rightarrow f'(x)=\frac{1}{x}.$$

```{dropdown} Video zu "Wichtige Ableitungen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/Jf7-EVLjpZg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Faktorregel und Summenregel

Als nächstes betrachten wir die Ableitung von zusammengesetzten Funktionen. Wird
eine Funktion mit einer konstanten reellen Zahl multipliziert, so muss auch ihre
Ableitung mit dieser Zahl multipliziert werden.

```{admonition} Was ist ... die Faktorregel?
:class: note
Die Faktorregel ist eine Rechenregel zur Berechnung von Ableitungen. Wird eine
Funktion mit einer konstanten reellen Zahl multipliziert, so muss auch ihre
Ableitungsfunktion mit dieser Zahl multipliziert werden.

$$(C\cdot f(x))' = C\cdot f'(x).$$
```

```{dropdown} Video zu "Faktorregel" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/RqSJcYYeRf4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

Wenn zwei Funktionen addiert werden, die beide differenzierbar sind, ist die
Summe ebenfalls wieder ableitbar. Wie die Summe abgeleitet werden muss, gibt die
Summenregel vor.

```{admonition} Was ist ... die Summenregel?
:class: note
Die Summenregel ist eine Rechenregel zur Berechnung von Ableitungen. Sind zwei
Funktionen differenzierbar, so ist auch ihre Summe differenzierbar. Die
Ableitungsfunktion ist dann die Summe der einzeln abgeleiteten Funktionen.


$$(f(x)+g(x))' = f'(x) + g'(x).$$ 
```

Gibt es einen Differenzenregel? Eine eigene Differenzenregel brauchen wir nicht,
denn wir können die Faktorregel mit der Summenregel kombinieren.

$$(f(x) - g(x))' = (f(x) + (-1)\cdot g(x))' = f'(x) + (-1)\cdot g'(x) = f'(x) -
g'(x).$$

```{dropdown} Video zu "Summenregel" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/KOoPcV7enYA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Produktregel und Quotientenregel

Etwas komplizierter wird es, wenn Funktionen miteinander multipliziert oder
dividiert werden.

```{admonition} Was ist ... die Produktregel?
:class: note
Die Produktregel ist eine Rechenregel zur Berechnung von Ableitungen. Sind zwei
Funktionen differenzierbar, so ist auch ihr Produkt differenzierbar. Die
Ableitung des Produktes wird dann folgendermaßen berechnet:

$$(f(x)\cdot g(x))' = f'(x)\cdot g(x) + f(x)\cdot g'(x).$$
```

```{dropdown} Video zu "Produktregel" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/I1jECE16wzo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

```{admonition} Was ist ... die Quotientenregel?
:class: note
Die Quotientenregel ist eine Rechenregel zur Berechnung von Ableitungen. Sind
zwei Funktionen differenzierbar, so ist auch ihr Quotient differenzierbar (falls
durch die Nennerfunktion geteilt werden darf). Die Ableitung des Quotienten wird
dann folgendermaßen berechnet:

$$\left(\frac{f(x)}{g(x)}\right)' = \frac{f'(x)\cdot g(x) - f(x)\cdot g'(x)}{g(x)^2}.$$
```

```{dropdown} Video zu "Quotientenregel" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/ydbsCKqIbNw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Kettenregel

Wird eine Funktion $g$ in einer andere Funktion $f$ eingesetzt, so nennen wir
diesen Vorgang "Verketten" und das Ergebnis ist die verkettete Funktion $f(g)$.

```{admonition} Was ist ... die Kettenregel?
:class: note
Die Kettenregel ist eine Rechenregel zur Berechnung von Ableitungen. Sind zwei
Funktionen differenzierbar, so ist auch ihre Verkettung differenzierbar. Die
Ableitung der verketteten Funktion wird dann folgendermaßen berechnet:

$$\left(f(g(x))\right)' = f'\left(g(x)\right) \cdot g'(x).$$
```

```{dropdown} Video zu "Kettenregel" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/E_4Obqxxr8E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir uns damit beschäftigt, wie Ableitungen berechnet
werden können, wenn ihre Ableitungsfunktion bekannt ist. Zu grundlegenden
Funktionen sollte man die Ableitungsfunktionen auswendig wissen. Wenn eine
komplizierte Funktion aus einfachen Grundfunktionen zusammengesetzt ist, können
wir dann ihre Ableitung durch Anwenden der Ableitungsregeln (Faktorregel,
Summenregel, Produktregel, Quotientenregel oder Kettenregel) bilden.
