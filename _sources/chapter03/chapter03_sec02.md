# 3.2 Fläche zwischen zwei Graphen

Bisher haben wir das Integral benutzt, um den orientierten Flächeninhalt
zwischen einer Funktion und der x-Achse zu bestimmen. In diesem Abschnitt
erweitern wir diese Idee, um den Flächeninhalt zwischen zwei Funktionen zu
bestimmen, genauer gesagt zwischen zwei Funktionsgraphen. Dazu beginnen wir aber
zunächst mit der Vorgehensweise, wie Flächeninhalte zwischen einem
Funktionsgraphen und der x-Achse berechnet werden.

## Lernziele

```{admonition} Lernziele
:class: important
* Sie wissen, wie man mit dem bestimmten Integral $\int_{a}^{b} f(x)\, dx$ den
  Flächeninhalt zwischen dem Funktionsgraphen $f(x)$, der x-Achse und den parallelen
  Geraden $x=a$ und $x=b$ berechnet, wenn 
    * der Graph oberhalb der x-Achse liegt,
    * der Graph unterhalb der x-Achse liegt oder
    * der Graph teils oberhalb und teils unterhalb der x-Achse liegt. 

* Sie wissen, wie man den Flächeninhalt zwischen den beiden Funktionsgraphen $f(x)$ und $g(x)$
  berechnet. 
```

## Flächeninhalt: Graph oberhalb der x-Achse

Das Integral wurde in der Mathematik 1 als der orientierte Flächeninhalt
zwischen Funktionsgraph $f(x)$ und x-Achse eingeführt. Liegen die Funktionswerte
$f(x)$ alle oberhalb der x-Achse wie in dem nachfolgendem Beispiel, so ist der
orientierte Flächeninhalt gleich dem Flächeninhalt. Damit ist die gesuchte Fläche 
$A$ also

$$A = \int_{a}^{b} f(x) \, dx.$$

Das bestimmte Integral lässt sich am einfachsten über eine Stammfunktion $F$
berechnen. Mit dem Hauptsatz der Differential- und Integralrechnung gilt dann
für den Flächeninhalt $A$ einer Funktion $f$ im Intervall $[a,b]$ die folgende
Formel:

$$A = \int_{a}^{b} f(x) \, dx = F(b)- F(a).$$

Beispiel: In der folgenden Abbildung ist der Funktionsgraph $f(x)$ der Funktion
$f(x)=x^2+1$ zu sehen. Berechnet werden soll der rot gefärbte Flächeninhalt $A$
zwischen $f(x)$ und der x-Achse mit den Grenzen $x = -2$ und $x = 3$.

<div id="chap03_sec02_fig01" class="jxgbox" style="width:75%; aspect-ratio:16/9; margin: 0 auto;"></div>
<script type="text/javascript">
    board = JXG.JSXGraph.initBoard('chap03_sec02_fig01', 
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

In dem folgenden Video wird die Vorgehensweise nochnmal ausführlich erklärt und
ein weiteres Beispiel vorgerechnet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/L3m_jn9w1dU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Flächeninhalt: Graph unterhalb der x-Achse

Als nächstes wird die Funktion $f$ an der x-Achse gespiegelt. Die gespiegelte
Funktion nennen wir $g$, also

$$g(x)= -f(x) = -x^2-1.$$ 

<div id="chap03_sec02_fig02" class="jxgbox" style="width:75%; aspect-ratio:16/9; margin: 0 auto;"></div>
<script type="text/javascript">
    board2 = JXG.JSXGraph.initBoard('chap03_sec02_fig02', 
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

Weitere Erklärungen sowie ein weiteres Beispiel werden ausführlich in dem
folgenden Video präsentiert.

<iframe width="560" height="315" src="https://www.youtube.com/embed/_SA6iZNAKzw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Flächeninhalt: Graph oberhalb und unterhalb der x-Achse

Komplizierter wird es, wenn die Funktion oberhalb und unterhalb der x-Achse
liegt wie beispielsweise bei der Funktion $f(x)=x^2-1$. 

<div id="chap03_sec02_fig03" class="jxgbox" style="width:75%; aspect-ratio:16/9; margin: 0 auto;"></div>
<script type="text/javascript">
    board3 = JXG.JSXGraph.initBoard('chap03_sec02_fig03', 
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

```{admonition} Kochrezept zur Berechnung des Flächeninhaltes zwischen einem Funktionsgraphen und der x-Achse
:class: note
Ist der Flächeninhalt $A$ zwischen dem Funktionsgraphen $f(x)$ und der x-Achse mit den Grenzen $x=a$ und $x=b$ gesucht, gehen Sie folgendermaßen vor:

1. Fertigen Sie eine Skizze der Funktion an, um zu ermitteln, wo $f(x)$ oberhalb und wo unterhalb der x-Achse verläuft.
2. Berechnen Sie die Nullstellen der Funktion $f$. Unterteilen Sie damit das Intervall $[a,b]$ in Teilintervalle $I_1, I_2, \ldots$, so dass die Funktion $f$ in einem solchen Teilintervall komplett oberhalb oder komplett unterhalb der x-Achse liegt.
3. Berechnen Sie dann in jedem Teilintervall das Integral einzeln. Wenn die Funktion in dem Intervall negativ ist, multiplizieren Sie anschließend den orientierten Flächeninhalt mit (-1). Das Ergebnis sind die (positiven!) Teilflächen $A_1, A_2, \ldots$.
4. Addieren Sie zuletzt alle Teilflächen $A = A_1 + A_2 + \dots$. Das Gesamtergebnis ist der gesuchte Flächeninhalt $A$. 
```

Das folgende Video fasst die Vorgehensweise zusammen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/vdSWk1bCnMA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Fläche zwischen zwei Funktionsgraphen

Möchte man den Flächeninhalt berechnen, den zwei Funktionen $f$ und $g$
begrenzen, so könnte man zuerst den Flächeninhalt der ersten Funktion $f$ mit
der x-Achse berechnen und dann davon den zweiten Flächeninhalt des
Funktionsgraphens $g(x)$ mit der x-Achse abziehen. Dazu müsste man aber wissen,
welche Funktion oberhalb der anderen Funktion liegt. Einfacher wird es, wenn die
Differenzfunktion der beiden Funktionen gebildet wird. Die Vorgehensweise ist
dann wie folgt.

```{admonition} Kochrezept zur Berechnung des Flächeninhaltes zwischen zwei Funktionsgraphen
:class: note
Zur Berechnung des Flächeninhaltes zwischen zwei Funktionsgraphen, die wir
$f(x)$ und $g(x)$ nennen, und den Grenzen $x=a$ und $x=b$ gehen wir
folgendermaßen vor.

1. Berechnen Sie die Schnittpunkte $f(x)=g(x)$.
2. Bilden Sie die Differenzfunktion $d(x)=f(x)-g(x)$.
3. Integrieren Sie die die Differenzfunktion $d$ in den Teilintervallen, d.h.
   von a bis zum 1. Schnittpunkt, vom 1. Schnittpunkt bis zum 2. Schnittpunkt,
   usw..
4. Wenn der orientierte Flächeninhalt einer Teilfläche negativ ist,
   multiplizieren Sie mit -1, um den Flächeninhalt zu erhalten.
5. Addieren Sie alle Flächeninhalte, um die Gesamtfläche zu erhalten.
```

Das folgende Video erläutert die Vorgehensweise und erklärt auch, warum die
Integration über die Differenzfunktion den gleichen Flächeninhalt ergibt wie die
gesuchte Fläche zwischen den beiden Funktionsgraphen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/OXQvPFGb9uk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Werden die Schnittpunkte nicht sorgfältig ermittelt und das Intervall, über das
integriert wird, nicht sorgsam aufgeteilt, so passieren leicht Fehler, wie das
folgende Video demonstriert.

<iframe width="560" height="315" src="https://www.youtube.com/embed/nFG5_-kS7fI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

