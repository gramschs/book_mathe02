# 8.4 Extremwertprobleme mit Nebenbedingung

Im letzten Abschnitt haben wir uns mit Extremwerten einer mehrdimensionalen
Funktion beschäftigt. An die Variablen haben wir aber keinerlei Bedingungen
gestellt. In der Praxis kommt es aber oft vor, dass Einschränkungen an die
Variablen selbst gestellt werden. Diese werden oft als eine zusätzliche
Gleichung formuliert. In diesem Kapitel lernen wir eine Lösungsmethode kennen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was ein Extremwertproblem mit Nebenbedingung ist.
* Sie wissen, was eine Zielfunktion ist.
* Sie können ein Extremwertproblem mit Nebenbedingung durch die
  Eliminationsmethode lösen.
```

## Was sind Extremwertprobleme mit Nebenbedingung?

Eine Funktion zu maximieren oder zu minimieren ohne weitere Einschränkung ist in
der Praxis oft unrealistisch. Natürlich würde jeder gerne reich sein und das
Einkommen maximieren. Aber ist man auch bereit, die notwendigen Überstunden zu
leisten oder für einen besser bezahlten Job umzuziehen?

Wir betrachten ein Beispiel aus der Geometrie. Ein Draht der Länge l = 1 m soll
zu einem Rechteck gebogen werden. Wie müssen die Seitenlängen $x$ und $y$
gewählt werden, damit der Flächeninhalt des Rechtecks maximal ist?

Als erstes übersetzen wir die Angaben in eine Funktion und eine Gleichung. Das
Ziel ist ein maximaler Flächeninhalt. Wir bezeichnen den Flächeninhalt mit $A$.
Er berechnet sich mit der Formel

$$A(x,y) = x \cdot y.$$

Die Funktion $A$ wird **Zielfunktion** genannt. Sie hängt von zwei Variablen ab.
Würden wir jetzt ohne weitere Einschränkungen das Maximum dieser Funktion
suchen, so müssten wir die Seitenlängen $x$ und $y$ unendlich groß wählen. Ein
Minimum liegt offensichtlich vor, wenn $x = 0$ und $y = 0$. Aber das Minimum ist
ja nicht gesucht.

Erst durch die **Nebenbedingung**, dass die Länge des Drahtes 1 m ist, ist die
Suche nach einem Maximum sinnvoll. Diese Nebenbedingung formulieren wir als
Gleichung, indem wir den Umfang des Rechtecks gleich der Länge des Drahtes
setzen:

$$2\cdot x + 2 \cdot y = 1.$$

Streng genommen haben wir damit den Definitionsbereich der Funktion $A$
eingeschränkt. Das folgende Video erläutert nochmal, was ein Extremwertproblem
mit Nebenbedingungen ist.

```{dropdown} Video zu "Extrema mit Nebenbedingungen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/MMpljay-naE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Eliminationsmethode

Für die Lösung von Extremwertproblemen mit Nebenbedingungen gibt es mehrere
Strategien. Im Folgenden betrachten wir die sogenannte **Eliminationsmethode**.
Gehen Sie wie folgt vor, wenn Sie ein Extremwertproblem mit Nebenbedingungen
lösen wollen.

1. Formulieren Sie die Zielfunktion als Funktion von mehreren Variablen.
2. Formulieren Sie die Nebenbedingung als Gleichung.
3. Lösen Sie die Gleichung nach einer Variable auf.
4. Setzen Sie die aufgelöste Gleichung in die Zielfunktion ein.
5. Jetzt hängt die Zielfunktion von einer Variable weniger ab und die Gleichung
   braucht nicht mehr berücksichtigt werden (sie ist ja indirekt jetzt in der
   Zielfunktion enthalten).
6. Bestimmen Sie die Extremwerte ohne Nebenbedingung.
7. Beantworten Sie mit diesen Erkenntnissen die ursprüngliche Frage.

Schritt 1 und 2 haben wir für das Beispiel mit dem Draht schon durchgeführt.
Also lösen wir jetzt die Gleichung $2\cdot x + 2 \cdot y = 1$ nach $y$ auf:

$$y = \frac{1}{2} \left(1 - 2\cdot x\right) = -x + \frac{1}{2}$$

und setzen die nach $y$ aufgelöste Gleichung in die Zielfunktion ein:

$$\tilde{A}(x) = x \cdot (-x+\frac{1}{2}).$$

Um deutlich zu machen, dass diese neue Funktion nur noch von $x$ abhängt, haben
wir ihr einen neuen Namen gegeben, nämlich $\tilde{A}$. Jetzt vereinfachen wir
die Funktion noch, indem wir ausmultiplizieren:

$$\tilde{A}(x) = x \cdot (-x+\frac{1}{2}) = -x^2 + \frac{1}{2}x.$$

Als letztes folgt Schritt 6, die Bestimmung der Extremwerte. Dazu bilden wir die
erste Ableitung

$$\tilde{A}'(x) = -2 x + \frac{1}{2}.$$

Für die Suche nach Kandidaten für Extremstellen setzen wir $\tilde{A}'(x) = 0$ und
bestimmen die Nullstellen:

\begin{align*}
-2x + \frac{1}{2} &= 0 \\
\Rightarrow x &= \frac{1}{4}.\\
\end{align*}

Als nächstes überprüfen wir, ob $x = \frac{1}{4}$ wirklich ein Extremum ist,
indem wir die 2. Ableitung bilden

$$\tilde{A}''(x) = -2$$

und dann den Punkt $x = \frac{1}{4}$ einsetzen:

$$\tilde{A}''(\frac{1}{4}) = -2.$$

Da die 2. Ableitung an der Stelle $x = \frac{1}{4}$ negativ ist, können wir
schlussfolgern, dass $x = \frac{1}{4}$ eine Extremstelle ist und dass es sich
dabei um ein Maximum (Hochpunkt) handelt.

Damit haben wir die erste Seitenlänge $x$ gefunden. Jetzt fehlt noch Schritt 7,
die Beantwortung der ursprünglichen Frage. Es war ja nach den beiden
Seitenlängen gefragt. Aus der Nebenbedingung

$$2\cdot x + 2 \cdot y = 1$$

erhalten wir aber für $x = \frac{1}{4}$ sofort, dass $y=\frac{1}{4}$ gelten
muss.

Das vom Flächeninhalt her maximale Rechteckt mit einer Drahtlänge von 1 m
entsteht, wenn der Draht zu einem Quadrat gebogen wird, bei dem jede Seite eine
Länge von 0.25 m hat.

Das folgende Video zeigt die Eliminationsmethode.

```{dropdown} Video zu "Eliminationsmethode" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/JOMh6OiGZbA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

In dem folgenden Video werden mögliche Kandidaten für Extrema gesucht. Es wird
allerdings nicht überprüft, ob die Kandidaten wirklich Extremwerte sind.

```{dropdown} Video zu "Beispiel Eliminationsmethode" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/4AFGmSQwpH4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

Ein weiteres Beispiel wird in dem folgenden Video gezeigt.

```{dropdown} Video zu "Extremwertaufgaben" von Magda liebt Mathe
<iframe width="560" height="315" src="https://www.youtube.com/embed/4D4hpF8w69Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
