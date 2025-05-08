# 6.4 Höhere partielle Ableitungen und Hesse-Matrix

In den vorangegangenen Kapiteln haben wir uns mit Funktionen mehrerer Variablen
und deren partiellen Ableitungen erster Ordnung beschäftigt. Wie bei Funktionen
einer Variablen können wir auch bei Funktionen mehrerer Variablen höhere
Ableitungen bilden, indem wir den Ableitungsprozess mehrfach hintereinander
ausführen. Diese höheren Ableitungen sind insbesondere für Anwendungen wie
Extremwertprobleme und Stabilitätsanalysen im Maschinenbau von großer Bedeutung.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können **höhere partielle Ableitungen** berechenen.
* Sie wissen, was mit **gemischten partiellen Ableitungen** gemeint ist.
* Sie kennen den **Satz von Schwarz** und wissen, wie Sie ihn zur Vereinfachung
  von Berechnungen anwenden können.
* Sie können die **Hesse-Matrix** berechnen.
```

## Was sind höhere partielle Ableitungen?

Im vorherigen Kapitel haben wir für die Funktion $f(x,y) = x^3 + y^3 - x^2 +
2y^2 - 5x + y + 3$ die partiellen Ableitungen erster Ordnung berechnet:

\begin{align}
\frac{\partial f(x,y)}{\partial x} &= 3x^2 - 2x - 5, \\
\frac{\partial f(x,y)}{\partial y} &= 3y^2 + 4y + 1.
\end{align}

Diese partiellen Ableitungen sind selbst wieder Funktionen von $x$ und $y$, die
wir erneut ableiten können. Dadurch erhalten wir partielle Ableitungen zweiter
Ordnung. Bei einer Funktion mit zwei Variablen gibt es vier mögliche
Kombinationen für partielle Ableitungen zweiter Ordnung:

1. Zweimal nach $x$ ableiten:

  $$\frac{\partial^2 f(x,y)}{\partial x^2} =
   \frac{\partial}{\partial x}\left(\frac{\partial f(x,y)}{\partial x}\right) =
   \frac{\partial}{\partial x}(3x^2 - 2x - 5) = 6x - 2$$

2. Zuerst nach $x$, dann nach $y$ ableiten:

  $$\frac{\partial^2 f(x,y)}{\partial
   y \partial x} = \frac{\partial}{\partial y}\left(\frac{\partial
   f(x,y)}{\partial x}\right) = \frac{\partial}{\partial y}(3x^2 - 2x - 5) = 0$$

3. Zuerst nach $y$, dann nach $x$ ableiten:

  $$\frac{\partial^2 f(x,y)}{\partial
   x \partial y} = \frac{\partial}{\partial x}\left(\frac{\partial
   f(x,y)}{\partial y}\right) = \frac{\partial}{\partial x}(3y^2 + 4y + 1) = 0$$

4. Zweimal nach $y$ ableiten:

  $$\frac{\partial^2 f(x,y)}{\partial y^2} =
   \frac{\partial}{\partial y}\left(\frac{\partial f(x,y)}{\partial y}\right) =
   \frac{\partial}{\partial y}(3y^2 + 4y + 1) = 6y + 4$$

Beachten Sie die Schreibweise, die kennzeichnet, nach welcher Variable in
welcher Reihenfolge abgeleitet wird. Die Variable, nach der zuerst abgeleitet
wird, steht im Nenner des Differentialquotienten weiter rechts.

Die Ableitungen, bei denen nach verschiedenen Variablen differenziert wird (wie
bei den Kombinationen 2 und 3 oben), werden als **gemischte partielle
Ableitungen** bezeichnet. Sie geben Aufschluss darüber, wie die Änderungsrate in
eine Richtung von der anderen unabhängigen Variable beeinflusst wird.

Der Prozess des partiellen Ableitens kann fortgesetzt werden, um Ableitungen
dritter, vierter oder noch höherer Ordnung zu bilden. Die Notation wird
entsprechend erweitert, zum Beispiel:

$$\frac{\partial^3 f(x,y)}{\partial x^2 \partial y} = \frac{\partial}{\partial
y}\left(\frac{\partial^2 f(x,y)}{\partial x^2}\right) = \frac{\partial}{\partial
y}(6x - 2) = 0$$

Bei unseren bisherigen Überlegungen sind die partiellen Ableitungen für eine
Funktion von zwei unabhängigen Variablen gebildet worden. Bei drei unabhängigen
Variablen werden die Variablen oft mit $x$, $y$ und $z$ bezeichnet. Bei vier
oder mehr unabhängigen Variablen wird oft die Vektorschreibweise verwendet, also
bei $n$ Variablen

$$f(x_1, x_2, \ldots, x_n) = \ldots .$$

Die partielle Ableitung nach $x_i$ wird dann als $\frac{\partial f}{\partial
x_i}$ geschrieben, und höhere partielle Ableitungen folgen demselben Schema.

```{dropdown} Video "Höhere partielle Ableitungen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/2FDtjWmMjc8"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Der Satz von Schwarz

Bei der Berechnung gemischter partieller Ableitungen kann es mühsam sein, alle
möglichen Kombinationen auszurechnen. Glücklicherweise gibt es unter bestimmten
Voraussetzungen eine wichtige Vereinfachung, die auf dem **Satz von Schwarz**
beruht.

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

Der Satz von Schwarz erlaubt es uns, viele Berechnungen von gemischten
partiellen Ableitungen zu vereinfachen, da wir die Reihenfolge der
Differentiationen so wählen können, wie es für die Rechnung am günstigsten ist.

## Die Hesse-Matrix

Höhere partielle Ableitungen können schnell sehr unübersichtlich werden. Für die
zweiten partiellen Ableitungen ist es üblich, diese sortiert in einer Tabelle zu
notieren. Diese Tabelle in Matrixform wird **Hesse-Matrix** genannt.

Für eine Funktion von zwei Variablen $x$ und $y$ hat die Hesse-Matrix die
folgende Form:

$$H_{f}(x,y) =
\begin{pmatrix}
\frac{\partial^2f(x,y)}{\partial x \partial x}
  & \frac{\partial^2f(x,y)}{\partial x \partial y} \\
\frac{\partial^2f(x,y)}{\partial y \partial x}
  & \frac{\partial^2f(x,y)}{\partial y \partial y} \\
\end{pmatrix}$$

Für eine Funktion von drei Variablen $x$, $y$ und $z$ erhalten wir

$$H_{f}(x,y,z) =
\begin{pmatrix}
\frac{\partial^2f(x,y,z)}{\partial x \partial x}
  & \frac{\partial^2f(x,y,z)}{\partial x \partial y}
  & \frac{\partial^2f(x,y,z)}{\partial x \partial z} \\
\frac{\partial^2f(x,y,z)}{\partial y \partial x}
  & \frac{\partial^2f(x,y,z)}{\partial y \partial y}
  & \frac{\partial^2f(x,y,z)}{\partial y \partial z} \\
\frac{\partial^2f(x,y,z)}{\partial z \partial x}
  & \frac{\partial^2f(x,y,z)}{\partial z \partial y}
  & \frac{\partial^2f(x,y,z)}{\partial z \partial z} \\
\end{pmatrix}$$

Allgemein hat die Hesse-Matrix die folgende Form.

```{admonition} Was ist ... die Hesse-Matrix?
:class: note
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
Hesse-Matrix eine $2\times 2$-Matrix, bei drei Variablen eine $3 \times
3$-Matrix und bei $n$ Variablen eine $n\times n$-Matrix.

Die Hesse-Matrix hat eine Reihe wichtiger Eigenschaften, die wichtigste ist ihre
Symmetrie. Aufgrund des Satzes von Schwarz ist die Hesse-Matrix symmetrisch.

Betrachten wir nun ein Beispiel mit drei Variablen, wie es häufig im
dreidimensionalen Raum für Maschinenbauanwendungen vorkommt:

$$f(x,y,z) = x^2 + 2y^2 + 3z^2 + 2xy - xz + 4yz$$

Die partiellen Ableitungen erster Ordnung sind:

\begin{align*}
\frac{\partial f}{\partial x} &= 2x + 2y - z \\
\frac{\partial f}{\partial y} &= 4y + 2x + 4z \\
\frac{\partial f}{\partial z} &= 6z - x + 4y
\end{align*}

Die Hesse-Matrix ergibt sich durch Berechnung aller zweiten partiellen Ableitungen:

\begin{align*}
\frac{\partial^2 f}{\partial x^2} &= 2 & \frac{\partial^2 f}{\partial x \partial y} &= 2 & \frac{\partial^2 f}{\partial x \partial z} &= -1 \\
\frac{\partial^2 f}{\partial y \partial x} &= 2 & \frac{\partial^2 f}{\partial y^2} &= 4 & \frac{\partial^2 f}{\partial y \partial z} &= 4 \\
\frac{\partial^2 f}{\partial z \partial x} &= -1 & \frac{\partial^2 f}{\partial z \partial y} &= 4 & \frac{\partial^2 f}{\partial z^2} &= 6
\end{align*}

Damit erhalten wir die Hesse-Matrix:

$$H_f(x,y,z) =
\begin{pmatrix}
2 & 2 & -1 \\
2 & 4 & 4 \\
-1 & 4 & 6
\end{pmatrix}$$

Beachten Sie, dass die Hesse-Matrix symmetrisch ist, wie vom Satz von Schwarz vorhergesagt.

```{dropdown} Video "Hesse-Matrix und Satz von Schwarz" von MathePeter
<iframe width="560" height="315" src="https://www.youtube.com/embed/02OmgH5vJCA?si=2UjeYkn3rp_Uzbhv"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

```{dropdown} Video "Hesse-Matrix" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/vFlpLRPcqp8?si=3Gi_k9gPf7lZktp6"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video "Hesse-Matrix" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/4Vy4HDLU7nU"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir höhere partielle Ableitungen und die Hesse-Matrix
kennengelernt, die entscheidende Werkzeuge für die Analyse von Funktionen
mehrerer Variablen darstellen. Im nächsten Kapitel werden wir sehen, wie wir
Richtungsableitungen mit Hilfe des Gradienten berechnen können.
