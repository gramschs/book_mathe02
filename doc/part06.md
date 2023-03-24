# Funktionen von mehreren Variablen und partielle Ableitungen

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

Bisher haben wir nur Funktionen kennengelernt, bei denen eine reelle Zahl in die Funktionsvorschrift hineingesteckt wurde und eine reelle Zahl herauskam. Die mathematische Schreibweise dafür ist $f:\mathbb{R}\rightarrow\mathbb{R}$.

Doch die Welt ist nicht so eindimensional. Die folgende Abbildung zeigt die durchschnittliche Solarstrahlung in Deutschland. Dies ist mathematisch gesehen eine Funktion von mehereren Variablen, nämlich Längen- und Breitengrad, also $f:\mathbb{R}^2\rightarrow\mathbb{R}$.

```{figure} pics/part06_solar_map.png
---
width: 600px
name: fig_part06_solar_map
---
Solarstrahlung in Deutschland

([Quelle:](https://commons.wikimedia.org/wiki/File:SolarGIS-Solar-map-Germany-de.png) "Solar Radiation Map: Globalstrahlung Deutschland, SolarGIS 2011", Autor: SolarGIS Lizenz: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/))
```

In diesem Part werden wir uns zunächst mehrdimensionale Funktionen ansehen und uns erarbeiten, was in diesem Zusammenhang partielle Ableitungen sind.



## Lernziele

```{admonition} Lernziele
:class: tip
* Sie können erklären, was eine **Funktion von mehreren unabhängigen Variablen** ist. 
* Sie können eine Funktion $f:\mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R}$ als Fläche im Raum zeichnen.
* Sie können die **Schnittkurvendiagramme** einer Funktion $z = f(x,y)$ zeichnen.
* Sie können die **partiellen Ableitungen** einer Funktion berechnen.
* Sie wissen, wann es erlaubt ist, die Differentiationsreihenfolge zu vertauschen (Stichwort: **Satz von Schwarz**).
```


## Mehrdimensionale Funktionen

Leider ist es gar nicht so einfach, Funktionen von mehreren Variablen zu zeichnen. Eine Funktion von zwei Variablen kann man noch ganz gut zeichnen, indem man beispielsweise die Funktionswerte durch Farben darstellt oder die Funktionswerte als Höhe (z-Achse) einzeichnet. Bei drei und gar mehr Variablen klappt es mit Zeichnungen nicht mehr.

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/oJdN_Ics6qs
```

In der folgenden Datenvisualisierung sehen Sie als Beispiel einen Paraboloiden. Die dazugehörige Funktion lautet

$$f(x,y) = x^2 + y^2.$$

Die Visualisierung von Funktionen nennen wir auch **Plot** der Funktion, so wie der englische Begriff lautet. Dieser Plot vereinigt eigentlich zwei Darstellungsvarianten in einer Grafik. Zum einen werden die Funktionswerte $f(x,y)$ als z-Koordinate (Höhe) dargestellt. Zum anderen werden die Funktionswerte zusätzlich über die Farbe visualisiert.

Drehen Sie den Paraboloiden solange, bis Sie von oben auf die xy-Ebene sehen. Dann verschwinden die Höheninformationen und nur noch die Farbinformation bleibt übrig.

```python tags=["remove-input"]
HTML('assets/fig_part06_paraboloid.html')
```

## Partielle Ableitungen

Was genau meint jetzt wiederum der Fachbegriff partiell? Partiell heißt ja auf deutsch teilweise, vielleicht ist Ihnen der Begriff von einer partiellen Sonnenfinsternis geläufig. Bei Funktionen von mehreren Variablen ist der Ableitungsbegriff komplizierter als bei Funktionen von einer Variable, wie in dem folgenden Video erklärt wird.

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/4ppZE30P2Yw
```

Die partielle Ableitung wird also gebildet, indem nur eine der mehreren Variablen als echte Variable angesehen wird und die übrigen Variablen als Konstanten aufgefasst werden. 



````{prf:definition}
:label: def:06:01
Die partielle Ableitung der Funktion $f(x,y)$ nach $x$ an der Stelle $(x_0,y_0)$ ist definiert als

$$\frac{\partial f}{\partial x}(x_0,y_0) = \lim_{\Delta x\rightarrow 0}\frac{f(x_0+\Delta x, y_0) - f(x_0, y_0)}{\Delta x}.$$

Die partielle Ableitung der Funktion $f(x,y)$ nach $y$ an der Stelle $(x_0,y_0)$ ist definiert als

$$\frac{\partial f}{\partial y}(x_0,y_0) = \lim_{\Delta y \rightarrow 0}\frac{f(x_0, y_0 +\Delta y) - f(x_0, y_0)}{\Delta y}.$$

Falls die Funktion von mehr als zwei Variablen abhängt, wird dieses Schema fortgeführt.
````

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/KqpLPQvboPY
```

## Beispiele für das partielle Ableiten

Die folgenden Videos zeigen Beispiele für das Berechnen der partiellen Ableitungen.


```{admonition} Video
:class: seealso
https://www.youtube.com/embed/9R8xrRuWyTw
```

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/i59FBLtGpng
```

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/N0Y9E0wdLKk
```

## Was sind höhere partielle Ableitungen?

Eine eindimensionale Funktion kann man oft nicht nur einmal, sondern zweimal, dreimal, manchmal sogar unendlichmal oft ableiten. Das geht natürlich nur, wenn nach dem Ableiten eine Funktion herauskommt, die wieder ableitbar ist, sonst muss man aufhören.

Bei Funktionen, die von mehreren Variablen abhängen, kann man die partiellen Ableitungen mischen. Beispielsweise leiten wir eine Funktion partiell nach x ab und die Funktion, die dadurch entstanden ist leiten wir nun partiell nach y ab. 

Bei zwei Variablen und partiellen Ableitungen der Ordnung 2 hätten wir dann folgende Kombinationsmöglichkeiten:

* Ableitung nach x und dann Ableitung nach x 
* Ableitung nach x und dann Ableitung nach y
* Ableitung nach y und dann Ableitung nach x
* Ableitung nach y und dann Ableitung nach y

Bei höheren partiellen Ableitungen können wir nicht einfach zwei Striche an die Funktion schreiben, sondern müssen genau angeben, in welcher Reihenfolge nach welcher Variable abgeleitet werden soll. Deshalb schreiben wir

* Ableitung nach x und dann Ableitung nach x: $\frac{\partial^2}{\partial x \partial x}f(x,y)$
* Ableitung nach x und dann Ableitung nach y: $\frac{\partial^2}{\partial y \partial x}f(x,y)$
* Ableitung nach y und dann Ableitung nach x: $\frac{\partial^2}{\partial x \partial y}f(x,y)$
* Ableitung nach y und dann Ableitung nach y: $\frac{\partial^2}{\partial y \partial y}f(x,y)$

Die Richtung, nach der zuerst abgeleitet wird, steht weiter rechts.

Wenn wir nun uns die Kombinationsmöglichkeiten für partielle Ableitungen 3. Ordnung ansehen, stellen wir fest, dass da einige Kombinationen möglich sind, genaugenommen 27. Glücklicherweise gibt es einen Trick, einige der Kombinationen kann man sich sparen. Dieser Trick wird in der Mathematik der **Satz von Schwarz** genannt. Im nächsten Video sehen Sie dazu eine Erläuterung.



```{admonition} Video
:class: seealso
https://www.youtube.com/embed/XgkmktejS_Y
```
