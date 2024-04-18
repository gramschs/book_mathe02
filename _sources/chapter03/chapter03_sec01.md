# 3.1 Integrieren ist Mitteln

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können den Mittelwert einer Liste von Zahlen berechnen.
* Sie können den Mittelwert einer Funktion in einem Intervall berechnen.
```

## Mittelwert von Zahlen

Ein Auto fährt in der Stadt mit 50 km/h und muss leicht abbremsen. Dabei werden
folgende Geschwindigkeiten gemessen:

<span style="font-weight:normal">Zeit in s</span> | <span style="font-weight:normal">1</span>   | <span style="font-weight:normal">2</span>    | <span style="font-weight:normal">3</span> | <span style="font-weight:normal">4</span> | <span style="font-weight:normal">5</span> | <span style="font-weight:normal">6</span> |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
|Geschwindigkeit in km/h |  50.0    | 48.9  | 45.7 | 41.8 | 40.0 | 45.0 |
|  |

Wenn jetzt danach gefragt wird, mit welcher Durchschnittsgeschwindigkeit das
Auto in diesen sechs Sekunden unterwegs war, bilden wir den Mittelwert. Dazu
addieren wir die sechs Geschwindigkeiten und teilen durch die Anzahl der
Geschwindigkeitsmessungen.

$$\frac{1}{6}\big(50.0 + 48.9 + 45.7 + 41.8 + 40.0 + 45.0 \big) \approx 45.23.$$

Die Durchschnittgeschwindigkeit betrug also 45.23 km/h. Einen guten Eindruck der
einzelnen Messwerte im Vergleich zu ihrem Mittelwert vermittelt das folgende
Streudiagramm. Die blauen Kreise stehen für die gemessenen Werte aus der
Tabelle. Auf der x-Achse sind die Zeitpunkte, auf der y-Achse die
Geschwindigkeiten. Die schwarze Gerade repräsentiert den Mittelwert als
konstante Funktion.

<div id="chap03_sec01_fig01" class="jxgbox" style="width:75%; aspect-ratio:16/9; margin: 0 auto;""></div>
<script type="text/javascript">
    board = JXG.JSXGraph.initBoard('chap03_sec01_fig01', 
        {boundingbox:[-1, 53, 8, 32], axis:false, showCopyright: false});
    let axis0 = board.create('axis', [[0.0, 35.0], [1.0, 35.0]], {name:'Zeit [s]', withLabel:true});
    let axis1 = board.create('axis', [[0.0, 35.0], [0.0, 36.0]], {name:'Geschwindigkeit [km/h]', 
                    withLabel:true, label: {position: 'rt', offset: [-20, -15]}});
    let x_blue = [1.0,  2.0, 3.0,   4.0,  5.0,  6.0]; 
    let y_blue = [50.0, 48.9, 45.7, 41.8, 40.0, 45.0];
    for (let i = 0; i < 6; i++) {
        board.create('point', [x_blue[i], y_blue[i]],
        {name:'', size:3, fillColor:'#005a94', strokeColor:'#005a94', fixed:true});
    }
    board.create('line', [[-.5,45.23],[7.5,45.23]], 
      {straightFirst:false, straightLast:false, strokeWidth:2, strokeColor:'#000000', fixed:true})
</script><br>

Allgemein können wir den Mittelwert von Messwerten folgendermaßen berechnen. Wir
bezeichnen die Anzahl der Messungen mit $N$ und die einzelnen Messungen mit
$y_1, y_2, \ldots, y_N$. Für den Mittelwert führen wir die Abkürzung $\bar{y}$
ein. Dann wird der Mittelwert nach der Formel

$$\bar{y} = \frac{1}{N}\big(y_1 + y_2 + \ldots + y_n \big)$$

berechnet. Um die Pünktchen in der Formel zu sparen, verwenden wir das
Summensymbol $\Sigma$:

$$\bar{y} = \frac{1}{N} \sum_{i=1}^{N} y_i.$$

Zusammenfassend halten wir folgende Definition eines Mittelwertes fest.

```{admonition} Was ist ... der Mittelwert?
:class: note
Der Mittelwert einer Liste von Zahlen ist die Summe der Zahlen geteilt durch ihre Anzahl. Berechnet wird der Mittelwert mit der Formel

$$\bar{y} = \frac{1}{N} \sum_{i=1}^{N} y_i.$$

Dabei ist $\bar{y}$ die Bezeichnung für den Mittelwert, $N$ die Anzahl der Zahlen und $y_i$ sind die einzelnen Zahlen.
```

## Mehr ist besser  

In einer Sekunde kann ganz schön viel passieren. Wir gehen jetzt davon aus, dass
die Geschwindigkeit des Autos zweimal pro Sekunde gemessen wurde und nicht nur
einmal pro Sekunde.

Die Geschwindigkeit zu den Zeitpunkten 1.5 s, 2.5 s, 3.5 s, 4.5 s und 5.5 s
ergänzen unsere bisherigen Messungen und können als rote Kreise in dem folgenden
Diagramm abgelesen werden.

<div id="chap03_sec01_fig02" class="jxgbox" style="width:75%; aspect-ratio:16/9; margin: 0 auto;""></div>
<script type="text/javascript">
var board = JXG.JSXGraph.initBoard('chap03_sec01_fig02', { 
  boundingbox: [-1, 53, 8, 32], axis:false,
  showCopyright: false
});
var l1 = board.create('axis', [[0.0, 35.0], [1.0, 35.0]], {name:'Zeit [s]', withLabel:true});
var l2 = board.create('axis', [[0.0, 35.0], [0.0, 36.0]], {name:'Geschwindigkeit [km/h]', withLabel:true, label: {position: 'rt', offset: [-20, -15]}});
//board.create('functiongraph', [function(x){return 50.0;},0.0, 1.0], {dash:2, strokeWidth:2, strokeColor:'#005a94'});
//board.create('functiongraph', [function(x){return 1/10520*(711*Math.pow(x,4)-4772*Math.pow(x,3)-189*Math.pow(x,2)+11850*x+518400);},1.0, 6.0], {strokeWidth:2,strokeColor:'#005a94'});
//board.create('functiongraph', [function(x){return -5*x*x+70*x-195;},6.0, 7.0], {dash:2, strokeWidth:2,strokeColor:'#005a94'});
var op1 = board.create('point',[1.0,50.0],{name:'', size:3, fillColor:'#005a94', strokeColor:'#005a94', fixed:true});
var op2 = board.create('point',[2.0,48.9],{name:'', size:3, fillColor:'#005a94', strokeColor:'#005a94', fixed:true});
var op3 = board.create('point',[3.0,45.7],{name:'', size:3, fillColor:'#005a94', strokeColor:'#005a94', fixed:true});
var op4 = board.create('point',[4.0,41.8],{name:'', size:3, fillColor:'#005a94', strokeColor:'#005a94', fixed:true});
var op5 = board.create('point',[5.0,40.0],{name:'', size:3, fillColor:'#005a94', strokeColor:'#005a94', fixed:true});
var op6 = board.create('point',[6.0,45.0],{name:'', size:3, fillColor:'#005a94', strokeColor:'#005a94', fixed:true});
var p1 = board.create('point',[1.5,49.7], {name:'49.7 km/h', size:3, fillColor:'#e60000', strokeColor:'#e60000', fixed:true});
var p2 = board.create('point',[2.5,47.5], {name:'47.5 km/h', size:3, fillColor:'#e60000', strokeColor:'#e60000', fixed:true});
var p3 = board.create('point',[3.5,43.7], {name:'43.7 km/h', size:3, fillColor:'#e60000', strokeColor:'#e60000', fixed:true});
var p4 = board.create('point',[4.5,40.4], {name:'40.4 km/h', size:3, fillColor:'#e60000', strokeColor:'#e60000', fixed:true});
var p5 = board.create('point',[5.5,41.3], {name:'41.3 km/h', size:3, fillColor:'#e60000', strokeColor:'#e60000', fixed:true});
board.create('line', [[-.5,44.91],[7.5,44.91]], 
        {straightFirst:false, straightLast:false, strokeWidth:2, strokeColor:'#000000', fixed:true})
</script><br>

An der Berechnung des Mittelwertes ändert sich nicht, aber normalerweise ist er
bei 11 Messungen genauer als bei sechs Messungen. Wir rechnen also 

$$\frac{1}{11}\big(50.0 + 49.7 + 48.9 + 47.5 + 45.7 + 43.7 + 41.8 + 40.4 + 40.0
+ 41.3 + 45 \big) \approx 44.91.$$

Noch genauer würde es werden, wenn wir noch mehr Messwerte hinzunehmen. Der
Mittelwert wäre dann perfekt, wenn wir unendliche viele Messungen hätten. Dann
wäre der Mittelwert der Grenzwert

$$\bar{y} = \lim_{N\to\infty} \frac{1}{N} \sum_{i=1}^{N} y_i.$$

Das setzt aber voraus, dass wir kontinuerlich die Geschwindigkeit messen. Oder
anders ausgedrückt, das setzt voraus, dass wir die Geschwindigkeit als eine
Funktion darstellen können, als ein sogenanntes Zeit-Geschwindigkeitsdiagramm.
Für den perfekten Mittelwert müssen wir also den Mittelwert der Funktion
ausrechnen, aber was ist der Mittelwert einer Funktion?

## Mittelwert einer Funktion

Um einen Weg zu finden, den Mittelwert $m$ einer Funktion $f$ zu berechnen,
starten wir erstmal mit einigen wenigen Messwerten. In unserem Beispiel können
wir die Zeitpunkte, zu denen eine Messung durchgeführt wird, mit $x_1$, $x_2$,
usw. bis $x_N$ ausdrücken. Die dazugehörigen Geschwindigkeitenmessungen bzw.
Funktionswerte bezeichnen wir dann mit $f(x_1)$, $f(x_2)$ usw. bis $f(x_N)$.
Dann gilt für die Berechnung des Mittelwertes

$$m = \frac{1}{N} \sum_{i=1}^{N} f(x_i).$$

Aber eigentlich wollen wir ja den Grenzwert 

$$m = \lim_{N\to\infty} \frac{1}{N} \sum_{i=1}^{N} f(x_i)$$

ausrechnen. Um diesen Grenzwert auszurechnen, wenden wir jetzt zwei Tricks an.
Wenn wir unendlich viele Messungen nehmen, um den Mittelwert auszurechnen,
können wir eine Messung auch weglassen. Bei unendlich vielen Messungen fällt
eine Messung nicht ins Gewicht. Wir lassen die letzte Messung weg. Dadurch
müssen wir nur noch durch $(N-1)$ teilen und bis $N-1$ summieren. Damit schreibt
sich die Formel für den Mittelwert nun als

$$m = \lim_{N\to\infty} \frac{1}{N-1} \sum_{i=1}^{N-1} f(x_i).$$

Das war der erste Trick. Nun erweitern wir die Messungen der Geschwindigkeit mit
dem Bruch $(b-a)/(b-a)$. Dabei ist $a$ der Startpunkt, zu dem die Messungen
beginnen, und $b$ der Endpunkt. Durch $b-a$ wird also das Intervall auf der
x-Achse beschreiben, in dem wir die Funktion $f$ mitteln wollen. Am Wert der
Summe ändert sich nichts, wenn wir jeden Messwert mit dem Bruch $(b-a)/(b-a)$
multiplizieren, da wir ja nur mit 1 multiplizieren. Wir können also mit beiden
Tricks den Mittelwert schreiben als

$$m = \lim_{N\to\infty} \frac{1}{N-1} \sum_{i=1}^{N-1} f(x_i)\cdot \frac{b-a}{b-a}.$$

Wenn in einer Summe jeder Term mit einer konstanten Zahl multipliziert wird,
dürfen wir diese konstante Zahl in die Summe reinmultiplizieren oder
ausklammern. Wir klammern jetzt die Zahl $1/(b-a)$ aus und multiplizieren
stattdessen die Zahl $1/(N-1)$ in die Summe.

$$m = \frac{1}{b-a} \lim_{N\to\infty} \sum_{i=1}^{N-1} f(x_i)\cdot
\frac{b-a}{N-1}.$$

Das Intervall $b-a$ wird also in $(N-1)$ kleine Stückchen unterteilt. Jedes
Stückchen ist dabei gleich groß und könnte mit $\Delta x$ bezeichnet werden. In
der folgenden Grafik zeigen wir das anhand unserer 11 Messwerte. Wir lassen die
letzte Messung weg und erhalten $\Delta x = 0.5 s$. Der Startzeitpunkt ist $a =
1 s$ und der Endzeitpunkt ist $b = 6 s$.

```{figure} pics/chapter03_sec01_fig03.png
---
width: 600px
name: chapter03_sec01_fig03
---
Annäherung des Mittelwertes einer Funktion $f$ über die Summe von Produkten $f(x_i)\cdot \Delta x$ im Intervall $[a,b]$
```

Wir summieren also über die Flächeninhalte $f(x_i)\cdot \Delta x$. Wenn die
Anzahl der Messungen zunimmt, werden die Stückchen $\Delta x$ kleiner, dafür
summieren wir über mehr Rechtecke. Diesen Grenzwert kennen wir schon, es ist der
orientierte Flächeninhalt der Funktion $f$ mit der x-Achse, also das Integral 

$$m = \frac{1}{b-a} \int_{a}^{b} f(x) \, dx.$$

```{admonition} Was ist ... der Mittelwert einer Funktion?
:class: note
Der Mittelwert einer Funktion in einem Intervall ist das bestimmte Integral auf diesem Intervall geteilt durch die Intervall-Länge.

Etwas präziser formuliert berechnet sich der Mittelwert $m$ einer stetigen Funktion $f$ im Intervall $[a,b]$ über die Formel

$$m = \frac{1}{b-a} \int_{a}^{b} f(x) \, dx.$$
```

## Beispiel

Berechnen Sie den Mittelwert der Funktion $f(x) = -0.05x^2+1.2x+7.8$ in dem
Intervall $[0,24]$. Vergleichen Sie anschließend Ihre Ergebnis mit der Rechnung
in dem folgenden Video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/FC-0Z_DIJs8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>