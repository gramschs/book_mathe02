# 4.1 Berechnung Taylorreihe

Im Kapitel über Potenzreihen haben wir uns bereits mit der Frage beschäftigt, in
welchem Intervall eine Potenzreihe eine gegebene Funktion gut approximiert. Was
uns aber noch fehlt ist die Frage, wie wir zu solchen Potenzreihen kommen. Daher
gibt es in diesem Kapitel eine Anleitung dazu.

## Lernziele 

```{admonition} Lernziele
:class: tip
* Sie kennen die Formel für ein **Taylorpolynom der Ordnung n** auswendig:

$$T_n(x) =\sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!} \cdot (x-x_0)^k.$$

* Sie kennen die Formel für die **Taylorreihe** auswendig:

$$T(x)=\sum_{k=0}^{\infty} \frac{f^{(k)}(x_0)}{k!} (x-x_0)^k.$$

```


## Taylorpolynom

Für Funktionen, die genügend oft differenzierbar sind, gibt es ein Kochrezept
zur Berechnung der Koeffizienten der dazugehörigen Potenzreihe. Um dieses
Kochrezept anzuwenden, beschäftigen wir uns zunächst mit dem sogenannten
Taylorpolynom.

```{admonition} Was ist ... ein Taylorpolynom?
Ein **Taylorpolynom** zu einer Funktion $f$ kann nur gebildet werden, wenn die Funktion $f$ n-mal stetig differenzierbar ist. Wenn das aber der Fall ist, dann wird noch ein Entwicklungspunkt $x_0$ gewählt. Das Taylorpolynom $T_n$ zu $f$ vom Grad $n$ am Entwicklungspunkt $x_0$ ist dann:

\begin{align*}
T_n(x) &=f(x_0) + \frac{f'(x_0)}{1!}(x-x_0)^1 + \frac{f''(x_0)}{2!}(x-x_0)^2 + \ldots \\
       &=\sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!} \cdot (x-x_0)^k.
\end{align*}

Dabei steht $k!$ für die Fakultät der Zahl $k$.
```

Hier gibt es ein Video, das die Fakultät $k!$ erklärt.

```{dropdown} Video zu "Fakultät" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/nVdUcZmmU7w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
(ref04_sec01_kochrezept)=
## Kochrezept zur Berechnung von Taylorpolynomen

1. Erst einmal folgende Frage beantworten: Bis zu welchem Polynomgrad $n$ soll
   die Funktion $f(x)$ approximiert werden? $\rightarrow n$ aufschreiben
2. Die ersten $n$ Ableitungen der Funktion $f$ bestimmen, also $f'(x), f''(x),
   f'''(x), f^{(iv)}(x), \ldots$.
3. Die Koeffizienten ausrechnen, indem nun der Entwicklungspunkt $x_0$ in die
   Funktion $f$ und in die Ableitungen eingesetzt wird.
4. Die Fakultäten ausrechnen.
5. Alles in die Formel für das Taylorpolynom einsetzen.

Probieren wir das an einem Beispiel aus. Die Funktion $f(x)=\sin(x)$ soll durch
ein Taylorpolynom Grad 3 am Entwicklungspunkt $x_0=0$ approximiert werden.

Schritt 1: Wir halten fest, der Grad ist 3 ($n=3$), d.h. wir brauchen die
ersten drei Ableitungen.

Schritt 2: Wir bilden die ersten drei Ableitungen: 

\begin{align*} 
f'(x)  &= \cos(x) \\
f''(x) &= -\sin(x) \\
f^{(3)}(x) &= -\cos(x) \end{align*}

Schritt 3: Wir rechnen die Koeffizienten des Taylorpolynoms aus, indem wir $x_0
= 0$ in die Funktion und die ersten drei Ableitungen einsetzen: 

\begin{align*}
f(0) &= \sin(0) = 0 \\
f'(0) &= \cos(0) = 1 \\
f''(0) &= - \sin(0) = 0 \\
f^{(3)}(0) &= -\cos(0) = -1 \end{align*}

Schritt 4: Die Fakultäten bis 3 werden ausgerechnet:

$$0!=1, \quad 1!=1, \quad 2!=2, \quad 3!=6.$$

Schritt 5: Wir setzen alles in die Formel für das Taylorpolynom ein:
\begin{align*} T_3(x) &= f(x_0) + f'(x_0)\cdot (x-x_0) + \frac{f''(x_0)}{2}\cdot
(x-x_0)^2 + \frac{f^{(3)}(x_0)}{6} \cdot (x-x_0)^3 = \\
    &= \sin(0) + 1\cdot (x-0) + \frac{0}{2}\cdot (x-0)^2 + \frac{-1}{6}\cdot (x-0)^3 = \\
    &= x - \frac{1}{6}x^3.
\end{align*}

Am besten das folgende Video gucken :-)

```{dropdown} Video zu "Taylorpolynom berechnen" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/o95cOqnLekw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Taylorreihe

Und was ist nun die Taylorreihe? Ganz einfach, ein Taylorpolynom, das bis
Unendlich geht, sieht nur kompliziert aus, wenn man es formal aufschreibt.

```{admonition} Was ist ... eine Taylorreihe?
Zu einer Funktion $f$, die unendlich oft differenzierbar ist, kann die folgende Potenzreihe

$$T(x)=\sum_{k=0}^{\infty} \frac{f^{(k)}(x_0)}{k!} (x-x_0)^k$$

gebildet werden. Diese Potenzreihe wird Taylorreihe zu $f$ am Entwicklungspunkt $x_
0$ genannt.
```

