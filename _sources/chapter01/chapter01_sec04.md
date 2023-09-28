# 1.4 Extremwerte mit Nebenbedingung

Im letzten Abschnitt haben wir uns mit Extremwerten beschäftigt. An die
Variablen selbst haben wir aber keinerlei Bedingungen gestellt. In der Praxis
kommt es aber oft vor, dass Einschränkungen an die Variablen gestellt werden.
Diese werden als eine zusätzliche Gleichung formuliert. In diesem Kapitel lernen
wir zuerst, was Extremwerte mit Nebenbedingungen sind. Dann beschäftigen wir uns
mit der »Eliminationsmethode« zur Lösung von Extremwertproblemen mit
Nebenbedingungen.


## Lernziele

```{admonition} Lernziele
:class: important
* Sie wissen, was ein **Extremwertproblem mit Nebenbedingung** ist.
* Sie können ein Extremwertproblem mit Nebenbedingung durch die
  **Eliminationsmethode** lösen.
```


## Was sind Extremwertprobleme mit Nebenbedingung?

Eine Funktion zu maximieren oder zu minimieren ohne weitere Einschränkung ist in
der Praxis oft unrealistisch. Natürlich würde jeder gerne reich sein und das
Einkommen maximieren. Aber ist man auch bereit, die notwendigen Überstunden zu
leisten oder für einen besser bezahlten Job umzuziehen?

Wir betrachten ein Beispiel aus der Geometrie. Ein Draht der Länge l = 1 m soll
zu einem Rechteck gebogen werden. Wie müssen die Seitenlängen $x$ und $y$
gewählt werden, damit der Flächeninhalt des Rechtecks maximal ist?

Als erstes übersetzen wir die Angaben der Textaufgabe in eine Funktion und eine
Gleichung. Wir fangen mit der Gleichung an, die als **Nebenbedingung**
bezeichnet wird. Die Länge des Drahtes ist vorgegeben und entspricht dem Umfang
des Rechtecks. Es gilt also

$$2\cdot x + 2 \cdot y = 1.$$

Das Ziel ist ein maximaler Flächeninhalt. Wir bezeichnen den Flächeninhalt mit
$A$. Er berechnet sich mit der Formel

$$A = x \cdot y.$$

Aus der Nebenbedingung und der Formel für den Flächeninhalt basteln wir uns eine
Funktion, die sogenannte **Zielfunktion**. Als erstes entscheiden wir uns für
eine Variable (z.B. $x$). Dann lösen wir die Nebenbedingung nach der anderen
Variablen auf (hier also $y$). Aus der Nebenbedingung $2\cdot x + 2 \cdot y = 1$
wird also:

$$y = \frac{1}{2} \left(1 - 2\cdot x\right) = -x + \frac{1}{2}.$$

Dann setzen die nach $y$ aufgelöste Gleichung in die Formel für $A$ ein:

$$A(x) = x \cdot (-x+\frac{1}{2}).$$

Die Funktion $A$ wird Zielfunktion genannt, weil sie das Ziel (maximaler
Flächeninhalt) beschreibt. Sie hängt nur noch von der Variablen $x$ ab, $y$ ist
eliminiert worden.

Würden wir jetzt ohne weitere Einschränkungen das Maximum dieser Funktion
suchen, so müssten wir die Seitenlängen $x$ (und damit auch $y$) unendlich groß
wählen. Ein Minimum liegt offensichtlich vor, wenn $x = 0$ (und damit auch $y =
0$) ist. Aber das Minimum ist ja nicht gesucht. Erst durch die Nebenbedingung,
dass die Länge des Drahtes 1 m ist, ist die Suche nach einem Maximum sinnvoll.
Daher werden diese Art von Problemstellungen **Extremwertprobleme mit
Nebenbedingung** genannt.


## Eliminationsmethode

Für die Lösung von Extremwertproblemen mit Nebenbedingungen gibt es mehrere
Strategien. Im Folgenden betrachten wir die sogenannte **Eliminationsmethode**.
Gehen Sie wie folgt vor, wenn Sie ein Extremwertproblem mit Nebenbedingungen
lösen wollen.

1. Formulieren Sie die Nebenbedingung als Gleichung.
2. Lösen Sie die Nebenbedingung nach einer Variable auf.
3. Formulieren Sie die Zielfunktion (nutzen Sie dabei die nach einer Variablen
   aufgelöste Nebenbedingung).
4. Bestimmen Sie die Extremwerte der Zielfunktion.
5. Beantworten Sie mit diesen Erkenntnissen die ursprüngliche Frage.

Schritt 1, 2 und 3 haben wir für das Beispiel mit dem Draht schon durchgeführt.
Aus der Nebenbedingung $2x + 2y = 1$ und der Formel für Flächeninhalte von
Rechtecken $A = x\cdot y$ haben wir die Zielfunktion

$$A(x) = x \cdot (-x+\frac{1}{2})$$

hergeleitet. Jetzt vereinfachen wir die Funktion noch, indem wir
ausmultiplizieren:

$$A(x) = x \cdot (-x+\frac{1}{2}) = -x^2 + \frac{1}{2}x.$$

Nun folgt Schritt 4, die Bestimmung der Extremwerte. Dazu bilden wir die 1.
Ableitung der Zielfunktion:

$$A'(x) = -2 x + \frac{1}{2}.$$

Für die Suche nach Kandidaten für Extremstellen setzen wir $A'(x) = 0$ und
bestimmen die Nullstellen:

\begin{align*}
-2x + \frac{1}{2} &= 0 \\
\Rightarrow x &= \frac{1}{4}.\\
\end{align*}

Als nächstes überprüfen wir, ob $x = \frac{1}{4}$ wirklich ein Extremum ist,
indem wir die 2. Ableitung bilden

$$A''(x) = -2$$

und dann die Stelle $x = \frac{1}{4}$ in die 2. Ableitung einsetzen:

$$A''(\frac{1}{4}) = -2.$$

Da die 2. Ableitung an der Stelle $x = \frac{1}{4}$ negativ ist, können wir
schlussfolgern, dass $x = \frac{1}{4}$ eine Extremstelle ist und dass die
Funktion $A$ an dieser Stelle ein Maximum hat.

Damit haben wir die erste Seitenlänge $x$ gefunden. Jetzt fehlt noch Schritt 5,
die Beantwortung der ursprünglichen Frage. Es war ja nach beiden Seitenlängen
gefragt. Aus der Nebenbedingung

$$2\cdot x + 2 \cdot y = 1$$

erhalten wir afür $x = \frac{1}{4}$ sofort, dass $y=\frac{1}{4}$ gelten muss.

Das vom Flächeninhalt her maximale Rechteckt mit einer Drahtlänge von 1 m
entsteht, wenn der Draht zu einem Quadrat gebogen wird, bei dem jede Seite eine
Länge von 0.25 m hat.

In dem folgenden Video können Sie sich eine vergleichbare Aufgabenstellungen
ansehen.

```{dropdown} Video zu "Extremwertaufgaben" von Magda liebt Mathe
<iframe width="560" height="315" src="https://www.youtube.com/embed/4D4hpF8w69Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Extremwertaufgabe Beispiel" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/pXm_6ZxGVp8?si=vPA9Bg38JD7B4HEk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Extremwertaufgabe Quader maximales Volumen" von MAthematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/i3z1sK4JqYA?si=9t3rOsZFQYouLbr6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```


## Zusammenfassung und Ausblick

In diesem Kapitel haben Sie gelernt, was ein Extremwertproblem mit
Nebenbedingung ist und wie man es löst. Tatsächlich verbirgt sich hinter der
Zielfunktion ursprünglich eine Funktion, die von zwei Variablen abhängt. Wir
werden auf das Thema Extremwertprobleme mit Nebenbedingungen noch einmal
zurückkommen, wenn wir Extremwertberechnungen von mehrdimensionalen Funktionen
behandeln. 