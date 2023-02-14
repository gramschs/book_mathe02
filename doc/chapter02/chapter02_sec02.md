# Fläche zwischen zwei Graphen

Bisher haben wir das Integral benutzt, um den orientierten Flächeninhalt
zwischen einer Funktion und der x-Achse zu bestimmen. In diesem Abschnitt
erweitern wir diese Idee, um den Flächeninhalt zwischen zwei Funktionen zu
bestimmen, genauer gesagt zwischen den zwei Funktionsgraphen.

## Lernziele

```{admonition} Lernziele
:class: hint
* Sie wissen, wie man mit dem bestimmten Integral $\int_{a}^{b} f(x)\, dx$ den
  Flächeninhalt zwischen der Kurve $f(x)$, der x-Achse und den parallelen
  Geraden $x=a$ und $x=b$ berechnet, wenn 
    * die Kurve oberhalb der x-Achse liegt,
    * die Kurve unterhalb der x-Achse liegt oder
    * die Kurve teils oberhalb und teils unterhalb der x-Achse liegt. 

* Sie wissen, wie man den Flächeninhalt zwischen zwei Kurven $f(x)$ und $g(x)$
  berechnet. 
```

## Flächeninhalt zwischen Kurve und x-Achse

Das Integral wurde in der Mathematik 1 als der orientierte Flächeninhalt
zwischen Funktionsgraph $f(x)$ und x-Achse eingeführt. Liegen die Funktionswerte
$f(x)$ alle oberhalb der x-Achse wie in dem nachfolgendem Beispiel, so ist der
orientierte Flächeninhalt gleich dem Flächeninhalt. Damit ist die gesuchte Fläche 
$A$ also

$$A = \int_{a}^{b} f(x) \, dx.$$

Das bestimmte Integral lässt sich am einfachsten über eine Stammfunktion $F$
berechnen. Damit gilt für den Flächeninhalt $A$ einer Funktion $f$ im Ingervall
$[a,b]$ die folgende Formel:

$$A = \int_{a}^{b} f(x) \, dx = F(b)- F(a).$$

Beispiel: In der folgenden Abbildung ist der Funktionsgraph $f(x)$ der Funktion
$f(x)=x^2+1$ zu sehen. Berechnet werden soll der rot gefärbte Flächeninhalt $A$
zwischen $f(x)$ und der x-Achse mit den Grenzen $x = -2$ und $x = 3$.

<div id="chap02_sec02_fig01" class="jxgbox" style="width:75%; aspect-ratio:16/9; margin: 0 auto;"></div>
<script type="text/javascript">
    board = JXG.JSXGraph.initBoard('chap02_sec02_fig01', 
        {boundingbox:[-5, 20, 5, -2], axis:true, showCopyright: false, showNavigation: false});
    let graph = board.create('functiongraph', [function(x) {return x**2+1;}, -5, 5], {strokeWidth:2, strokeColor:'#000000'});
    let area  = board.create('integral', [[-2.0, 3.0], graph],
        {fillColor:'#f06666'});
</script><br>

In dem Beispiel liegen alle Funktionswerte $f(x)$ komplett oberhalb der x-Achse,
d.h. alle Funktionswerte $f(x)$ sind positiv. Um nun den Flächeninhalt zwischen
$f(x)$ und der x-Achse mit den Grenzen $x=-2$ und $x=3$ zu berechnen, wird also
folgendermaßen gerechnet: 

$$A = \int_{-2}^{3} f(x)\, dx = \int_{-2}^{3} x^2 + 1 \, dx =
\big[\frac{1}{3}x^3+x\big]_{-2}^{3}=\frac{50}{3}\approx 16.6667.$$

Übrigens, wenn Sie in dem obigen Plot die beiden Grenzen $x=a$ und $x=b$
symbolisiert durch die beiden roten Punkte verschieben, wird der aktuelle
Flächeninhalt berechnet.

Als nächstes wird die Funktion $f$ an der x-Achse gespiegelt. Die gespiegelte
Funktion nennen wir $g$, also

$$g(x)= -f(x) = -x^2-1.$$ 

<div id="chap02_sec02_fig02" class="jxgbox" style="width:75%; aspect-ratio:16/9; margin: 0 auto;"></div>
<script type="text/javascript">
    board2 = JXG.JSXGraph.initBoard('chap02_sec02_fig02', 
        {boundingbox:[-5, 2, 5, -20], axis:true, showCopyright: false, showNavigation: false});
    let graph2 = board2.create('functiongraph', [function(x) {return -x*x-1;}, -5, 5], {strokeWidth:2, strokeColor:'#000000'});
    let area2  = board2.create('integral', [[-2.0, 3.0], graph2],
        {fillColor:'#669cbe'});
</script><br>

Wenn wir jetzt naiv den Flächeninhalt wiederum als das bestimmte Integral
berechnen, erhalten wir

$$\int_{-2}^{3} g(x)\, dx = \int_{-2}^{3} -x^2 - 1 \, dx =
\big[-\frac{1}{3}x^3-x\big]_{-2}^{3}=-\frac{50}{3}\approx -16.6667.$$

Negative Flächen gibt es nicht. Das Integral ist nicht der Flächeninhalt,
sondern der *orientierte* Flächeninhalt des Funktionsgraphens $g(x)$ mit der
x-Achse und daher negativ. Andererseits wissen wir ja, dass die gesuchte Fläche
zwischen $g(x)$ und der x-Achse (hier blau gefärbt) genauso groß sein muss wie
die der Flächeninhalt der Funktion $f(x)$ mit der x-Achse in der ersten
Abbildung (rot gefärbt), da wir die Funktion $f(x)$ ja nur an der x-Achse
gespiegelt haben. Also nehmen wir einfach den ursprünglichen Flächeninhalt. Oder
anders ausgedrückt, wir spiegeln die Funktion $g$ wieder, so dass die
Funktionswerte der gespiegelten Funktion komplett oberhalb der x-Achse liegen.

Die Formel zur Berechnung des Flächeninhaltes einer Funktion, die komplett
unterhalb der x-Achse liegt, lautet:

$$A = \textcolor{red}{-} \int_{a}^{b} f(x)\, dx = \textcolor{red}{-} \big(F(b)-F(a)\big).$$

Komplizierter wird es, wenn die Funktion oberhalb und unterhalb der x-Achse
liegt wie beispielsweise bei der Funktion $f(x)=x^2-1$. 

<div id="chap02_sec02_fig03" class="jxgbox" style="width:75%; aspect-ratio:16/9; margin: 0 auto;"></div>
<script type="text/javascript">
    board3 = JXG.JSXGraph.initBoard('chap02_sec02_fig03', 
        {boundingbox:[-5, 20, 5, -2], axis:true, showCopyright: false, showNavigation: false});
    let graph3 = board3.create('functiongraph', [function(x) {return x*x-1;}, -5, 5], {strokeWidth:2, strokeColor:'#000000'});
    let area3a = board3.create('integral', [[-2.0, -1.0], graph3], {fillColor:'#f06666'});
    let area3b = board3.create('integral', [[-1.0, 1.0],  graph3], {fillColor:'#669cbe'});
    let area3c = board3.create('integral', [[1.0, 3.0],   graph3], {fillColor:'#f06666'});
</script><br>

Würden wir jetzt einfach das bestimmte Integral im Intervall $[-2,3]$ berechnen, so erhielten wir

$$\int_{-2}^{3} f(x)\, dx = \int_{-2}^{3} x^2-1\, dx = \frac{20}{3} \approx 6.6667.$$ 

Das ist zuwenig! Bereits die Fläche zwischen $f(x)$ und der x-Achse im Intervall
$[1,3]$ alleine hat schon den Flächeninhalt $\frac{20}{3}\approx 6.6667$. Wir
gehen jetzt etwas sorgfältiger vor und untersuchen, wo die Funktion oberhalb und
wo sie unterhalb der x-Achse liegt. Die obige Abbildung hilft schon für eine
erste Einschätzung, wo $f(x)$ positiv ist und in welchem Intervall $f(x)$
negativ ist. Der Vorzeichenwechsel erfolgt bei den Nullstellen.

$$x^2-1 = 0 \quad \Rightarrow \quad x_1 = -1 \text{ und } x_2 = +1.$$

Daher wird jetzt das Intervall $[-2,3]$ in drei Teilintervalle unterteilt:

* $I_1 = [-2, -1]$ (also von $a=-2$ bis zur 1. Nullstelle)
* $I_2 = [-1, +1]$ (also von der 1. Nullstelle bis zur 2. Nullstelle)
* $I_3 = [+1, +3]$ (also von der 2. Nullstelle bis $b=3$) 

Das bestimmte Integral im 1. Teilintervall ist positiv, im 2. Teilintervall ist
es negativ und im 3. Teilintervall wieder positiv:

* $\int_{-2}^{-1} f(x) \, dx = + \frac{4}{3} \approx 1.3333$,
* $\int_{-1}^{1} f(x) \, dx = - \frac{4}{3} \approx - 1.3333$,
* $\int_{1}^{3} f(x) \, dx = + \frac{20}{3} \approx 6.6667$.

Da ein Integral über ein Intervall gleich der Summe der Integrale über die
Teilintervalle ist, erhalten wir

$$\int_{-2}^{3} f(x) \, dx = \frac{4}{3} - \frac{4}{3} + \frac{20}{3} = \frac{20}{3}.$$

Die ersten beiden Integrale ergeben in Summe 0, da ist die Fläche verloren
gegangen. Der mittlere Teil, wo das Integral einen negativ orientierten
Flächeninhalt liefert, muss an der x-Achse gespiegelt werden bzw. der
orientierte Flächeninhalt muss mit (-1) multipliziert werden. Der korrekte
Flächeninhalt ist daher

$$A = \frac{4}{3} \textcolor{red}{+} \frac{4}{3} + \frac{20}{3} = \frac{28}{3}.$$

```{admonition} Kochrezept zur Berechnung des Flächeninhaltes zwischen einer Kurve und der x-Achse
Ist der Flächeninhalt $A$ zwischen einer Kurve $f(x)$ und der x-Achse mit den Grenzen $x=a$ und $x=b$ gesucht, gehen Sie folgendermaßen vor:

1. Fertigen Sie eine Skizze der Funktion an, um zu ermitteln, wo $f(x)$ oberhalb und wo unterhalb der x-Achse verläuft.
2. Berechnen Sie die Nullstellen der Funktion $f$. Unterteilen Sie damit das Intervall $[a,b]$ in Teilintervalle $I_1, I_2, \ldots$, so dass die Funktion $f$ in einem solchen Teilintervall komplett oberhalb oder komplett unterhalb der x-Achse liegt.
3. Berechnen Sie dann in jedem Teilintervall das Integral einzeln. Wenn die Funktion in dem Intervall negativ ist, multiplizieren Sie anschließend den orientierten Flächeninhalt mit (-1). Das Ergebnis sind die (positiven!) Teilfläche $A_1, A_2, \ldots$.
4. Addieren Sie zuletzt alle Teilflächen $A = A_1 + A_2 + \dots$. Das Gesamtergebnis ist der gesuchte Flächeninhalt $A$. 
```

## Beispiel für die Berechnung des Flächeninhaltes Kurve mit x-Achse

Berechnen Sie den Flächeninhalt $A$ der Funktion $f(x)=x^3-3x^2+2x$ im Intervall
$[0,2]$. Vergleichen Sie Ihr Ergebnis anschließend mit dem Lösungsweg in dem
folgenden Video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/BsI9LD3IQvo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

