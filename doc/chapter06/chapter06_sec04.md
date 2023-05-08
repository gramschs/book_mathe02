# 6.4 Höhere partielle Ableitungen und Hesse-Matrix

Eine eindimensionale Funktion kann man oft nicht nur einmal, sondern zweimal,
dreimal, manchmal sogar unendlichmal oft ableiten. Das geht natürlich nur, wenn
nach dem Ableiten eine Funktion herauskommt, die wieder ableitbar ist, sonst
muss man aufhören. Das lässt sich analog auf Funktionen von mehreren Variablen
übertragen.

## Lernziele 

```{admonition} Lernziele
:class: hint
* Sie können **höhere partielle Ableitungen** berechenen.
* Sie wissen, was mit **gemischten partiellen Ableitungen** gemeint ist.
* Sie können die **Hesse-Matrix** berechnen.
* Sie wissen, wann sie bei der Berechnung von höheren partiellen Ableitungen
  sich einige Berechnungen einsparen dürfen, indem Sie den Trick **Satz von
  Schwarz** anwenden können.
```

## Was sind höhere partielle Ableitungen?

Im letzten Kapitel haben wir die Funktion 

$$f(x,y) = x^3 + y^3 - x^2 + 2y^2 - 5x + y + 3$$

partiell zuerst nach $x$ und dann nach $y$ abgeleitet. Das Ergebnis waren die
partiellen Ableitungen:

\begin{align*}
\frac{\partial f(x,y)}{\partial x} &= 3x^2 - 2x - 5, \\
\frac{\partial f(x,y)}{\partial y} &= 3y^2 + 4y + 1.
\end{align*}

Beides sind aber wieder Funktionen von zwei Variablen. Es hindert uns keiner
daran, diese Funktionen erneut abzuleiten. Beispielsweise können wir die 1.
partielle Ableitung von $f$ nach $x$ erneut nach $x$ ableiten. Das Ergebnis ist

$$\frac{\partial^2 f(x,y)}{\partial x^2} = 6x - 2.$$

Wir könnten die Funktion $3x^2 - 2x - 5$ aber auch nach $y$ ableiten und haben
dann

$$\frac{\partial^2 f(x,y)}{\partial y \, \partial x} = 0.$$

Beachten Sie die Schreibweise, die kennzeichnet, nach welcher Variable in
welcher Reihenfolge abgeleitet wird. Die Richtung, nach der zuerst abgeleitet
wird, steht weiter rechts!

Ebensogut hätten wir auch die 1. partielle Ableitung der Funktion $f$ nach $y$
erneut nach $x$ oder $y$ ableiten können. Bei Funktionen von zwei Variablen gibt
es für die sogenannten 2. partiellen Ableitungen die folgenden
Kombinationsmöglichkeiten:

* Ableitung nach x und dann Ableitung nach x
* Ableitung nach x und dann Ableitung nach y
* Ableitung nach y und dann Ableitung nach x
* Ableitung nach y und dann Ableitung nach y

Die zweite und dritte Kombination, bei denen erst nach einer und dann nach der
anderen Variable abgeleitet wird, nennen wir **gemischte partielle
Ableitungen**. 

Bei unseren bisherigen Überlegungen sind die partiellen Ableitungen für eine
Funktion von zwei unabhängigen Variablen gebildet worden. Bei drei unabhängigen
Variablen werden die Variablen oft mit $x$, $y$ und $z$ bezeichnet. Bei vier
oder mehr unabhängigen Variablen wird oft die Vektorschreibweise verwendet, also
bei $n$ Variablen

$$f(x_1, x_2, \ldots, x_n) = \ldots .$$

```{dropdown} Video zu "Höhere partielle Ableitungen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/2FDtjWmMjc8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Hesse-Matrix und der Satz von Schwarz

Höhere partielle Ableitungen können schnell sehr unübersichtlich werden. Für die
2. partiellen Ableitungen ist es üblich, diese sortiert in einer Tabelle zu
notieren. Diese Tabelle in Matrixform wird **Hesse-Matrix** genannt.

In der ersten Spalte stehen alle partiellen Ableitungen, bei denen zuerst nach
$x_1$ abgeleitet wurde. Diese partielle Ableitung kürzen wir mit $f_{x_1}$ ab.
Um die zweiten partiellen Ableitungen von $f_{x_1}$ zu bilden, leiten wir
partiell nach $x_1$ ab und schreiben das in die erste Zeile. Dann wird
$f_{x_1}$ nach $x_2$ abgeleitet und in die 2. Zeile der 1. Spalte geschrieben.
Dann wird $f_{x_1}$ nach $x_3$ abgeleitet und in die 3. Zeile der 1. Spalte
geschrieben. Nachdem alle 2. partiellen Ableitungen gebildet sind, wird $f$ nach
$x_2$ abgeleitet und mit den jeweiligen zweiten partiellen Ableitungen in die
zweite Spalte geschreiben. Dieses Schema wird fortgesetzt.

Für eine Funktion von zwei Variablen $x$ und $y$ erhalten wir:

$$H_{f}(x,y) = 
\begin{pmatrix} 
\frac{\partial^2f(x,y)}{\partial x \partial x} 
  & \frac{\partial^2f(x,y)}{\partial x \partial y} \\
\frac{\partial^2f(x,y)}{\partial y \partial x} 
  & \frac{\partial^2f(x,y)}{\partial y \partial y} \\
\end{pmatrix}$$

Für eine Funktion von drei Variablen $x_1$, $x_2$ und $x_3$ erhalten wir

$$H_{f}(x_1,x_2,x_3) = 
\begin{pmatrix} 
\frac{\partial^2f(x_1,x_2,x_3)}{\partial x_1 \partial x_1} 
  & \frac{\partial^2f(x_1,x_2,x_3)}{\partial x_1 \partial x_2}
  & \frac{\partial^2f(x_1,x_2,x_3)}{\partial x_1 \partial x_3} \\
\frac{\partial^2f(x_1,x_2,x_3)}{\partial x_2 \partial x_1} 
  & \frac{\partial^2f(x_1,x_2,x_3)}{\partial x_2 \partial x_2}
  & \frac{\partial^2f(x_1,x_2,x_3)}{\partial x_2 \partial x_3} \\
\frac{\partial^2f(x_1,x_2,x_3)}{\partial x_3 \partial x_1} 
  & \frac{\partial^2f(x_1,x_2,x_3)}{\partial x_3 \partial x_2}
  & \frac{\partial^2f(x_1,x_2,x_3)}{\partial x_3 \partial x_3} \\
\end{pmatrix}$$

```{admonition} Was ist ... die Hesse-Matrix?
Die Hesse-Matrix gibt es nur für Funktionen $f$ von mehreren Variablen $x_1,
x_2, \ldots, x_n$, die mindestens zweimal partiell differenzierbar sind. Die
Hesse-Matrix besteht aus den 2. partiellen Ableitungen der Funktion $f$, wobei
die 2. partiellen Ableitungen in der folgenden Reihenfolge in der Matrix
angeordnet sind:

$$H_{f}(x_1,x_2,\ldots, x_n) = 
\begin{pmatrix} 
\frac{\partial^2f(x_1,x_2,\ldots, x_n)}{\partial x_1 \partial x_1} 
  & \frac{\partial^2f(x_1,x_2, \ldots, x_n)}{\partial x_1 \partial x_2}
  & \ldots 
  & \frac{\partial^2f(x_1,x_2,\ldots,x_n)}{\partial x_1 \partial x_n} \\
\frac{\partial^2f(x_1,x_2,\ldots,x_n)}{\partial x_2 \partial x_1} 
  & \frac{\partial^2f(x_1,x_2,\ldots,x_n)}{\partial x_2 \partial x_2}
  & \ldots
  & \frac{\partial^2f(x_1,x_2,\ldots,x_n)}{\partial x_2 \partial x_n} \\
  \vdots & \vdots & & \vdots \\
\frac{\partial^2f(x_1,x_2,\ldots,x_n)}{\partial x_n \partial x_1} 
  & \frac{\partial^2f(x_1,x_2,\ldots,x_n)}{\partial x_n \partial x_2}
  & \ldots
  & \frac{\partial^2f(x_1,x_2,\ldots,x_n)}{\partial x_n \partial x_n} \\
\end{pmatrix}$$
```

Die Größe der Hesse-Matrix wird durch die Anzahl der unabhängigen Variablen
bestimmt, von denen die Funktion abhängt. Bei zwei Variablen, ist die
Hesse-Matrix eine 2x2-Matrix, bei drei Variablen eine 3x3-Matrix usw. Auch wenn
die Hesse-Matrix etwas Ordnung und Übersicht in die zweiten partiellen
Ableitungen bringt, ist es doch langwierig, die vielen Kombinationen an
partiellen Ableitungen zu bilden. Noch komplizierter wird es für partielle
Ableitungen der Ordnung 3 oder noch höher.  Glücklicherweise gibt es einen
Trick, einige der Kombinationen kann man sich sparen. Dieser Trick wird in der
Mathematik der **Satz von Schwarz** genannt. 

[Hermann Amandus Schwarz](https://de.wikipedia.org/wiki/Hermann_Amandus_Schwarz)
hat herausgefunden, dass bei Funktionen, die mehrfach stetig differenzierbar
sind, es beim partiellen Ableiten nicht darauf ankommt, in welcher Reihenfolge
nach den einzelnen Variablen abgeleitet wird.

Wir bleiben bei dem Beispiel $f(x,y) = x^3 + y^3 - x^2 + 2y^2 - 5x + y + 3$ ,
das eine beliebig oft stetig differenzierbare Funktion darstellt. Ob zuerst nach
$x$ und dann nach $y$ abgeleitet wird oder zuerst nach $y$ und dann nach $x$
macht keinen Unterschied. Die erste Variante hatten wir ja bereits ausgerechnet:

$$\frac{\partial^2 f(x,y)}{\partial y \, \partial x} = 0.$$

Leiten wir die Funktion $f$ zuerst nach $y$ und dann nach $x$ ab, so erhalten
wir ebenfalls

$$\frac{\partial^2 f(x,y)}{\partial x \, \partial y} = 0.$$

Wir hätten uns diese Berechnung sparen können, da nach dem Satz von Schwarz die
Reihenfolge unwichtig ist und 

$$\frac{\partial^2 f(x,y)}{\partial y \, \partial x} = \frac{\partial^2
f(x,y)}{\partial x \, \partial y}$$

gilt.

```{dropdown} Video zu "Hesse-Matrix" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/4Vy4HDLU7nU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```



