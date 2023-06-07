# 8.3 Extremwerte

Neben der Linearisierung einer mehrdimensionalen Funktion ist auch die
Berechnung von Minima (Tiefpunkten) und Maxima (Hochpunkten) interessant für die
Praxis. Extremwerte können für beliebig mehrdimensionale skalarwertige
Funktionen existieren, aber wir beschränken uns in diesem Kapitel auf Funktionen
von zwei unabhängigen Variablen.

## Lernziele

```{admonition} Lernziele
:class: important
Sie wissen, dass drei Bedingungen überprüft werden müssen, um zu entscheiden, ob die Funktion $f:\mathbb{R}^2\to\mathbb{R}$ Extremwerte hat.
1. Ein Punkt $(x_0,y_0)$ ist ein Kandidatat für eine Extremstelle, wenn die folgende erste Bedingung erfüllt ist:

$$\frac{\partial f(x_0,y_0)}{\partial x} = 0 \quad \text{ und } \quad 
\frac{\partial f(x_0,y_0)}{\partial y} = 0.$$

2. Damit der Kandidat $(x_0,y_0)$ auch wirklich ein Extremwert ist, muss zusätzlich
  die Determinante der Hesse-Matrix positiv sein, also:
  
$$\det(H_f(x_0, y_0)) = \frac{\partial^2 f(x_0, y_0)}{\partial x\partial x}\cdot
\frac{\partial^2 f(x_0,y_0)}{\partial y \partial y} - \left(\frac{\partial^2
f(x_0,y_0}{\partial x \partial y}\right)^2 > 0.$$

3. Zuletzt entscheidet dann das Vorzeichen von dem Term $\frac{\partial^2 f(x_0,y_0)}{\partial x \partial y}$ darüber, ob ein Minimum oder ein Maximum vorliegt:
  
\begin{align*}
\frac{\partial^2 f(x_0, y_0)}{\partial x \partial x} < 0 & \qquad \Rightarrow \text{relatives Maximum} \\
\frac{\partial^2 f(x_0, y_0)}{\partial x \partial x} > 0 & \qquad \Rightarrow \text{relatives Minimum} \\
\end{align*}
```

## Extremwerte bei eindimensionalen Funktionen

Betrachten wir zunächst eine eindimensionale Funktion
$f:\mathbb{R}\to\mathbb{R}$. Um herauszufinden, welche x-Werte als Extrema
(Maximum/Hochpunkt oder Minimum/Tiefpunkt) möglich sind, wird die 1. Ableitung
Null gesetzt:

$$f'(x)=0.$$

Diese Bedingung ist *notwendig*, damit überhaupt ein Maximum oder Minimum
vorliegen kann. Leider reicht diese Bedingung noch nicht aus. Alle Nullstellen
der 1. Ableitung sind *mögliche* Extrema, es könnten aber auch Sattelpunkte sein
wie in der folgenden Abbildung der Funktion $f(x)=x^3$:


```{figure} pics/fig08_sattelpunkt1D.svg
---
width: 300px
name: fig_part06_sattelpunkt1D
---
Sattelpunkt
```

Daher müssen wir noch zusätzliche Bedingungen überprüfen, bevor wir entscheiden
können, ob ein Minimum oder Maximum vorliegt. Die möglichen Extremwerte müssen
noch zusätzlich mit der 2. Ableitung geprüft werden:

* Der Punkt $x_0$ ist ein **Maximum/Hochpunkt**, wenn
    * die 1. Ableitung Null ist, d.h. $f'(x_0) = 0$ und
    * die 2. Ableitung **negativ** ist, d.h. $f''(x_0) < 0$. 
* Der Punkt $x_0$ ist ein **Minimum/Tiefpunkt**, wenn
    * die 1. Ableitung Null ist, d.h. $f'(x_0) = 0$ und
    * die 2. Ableitung **positiv** ist, d.h. $f''(x_0) > 0$.
    
Diese beiden Bedingungen nennt man dann **hinreichende** Bedingungen. 

Achtung: Wenn allerdings die zweite Ableitung Null ist, also $f''(x_0) = 0$,
kann man keine Entscheidung treffen und muss weitere Bedingungen überprüfen.

Dieses Prozedere übertragen wir jetzt auf Funktionen von zwei Variablen.


## Extremwerte bei mehrdimensionalen Funktionen

Die notwendige Bedingung für Extremwerte eindimensionaler Funktion lässt sich
sofort auf mehrdimensionale Funktionen übertragen. Wir müssen uns nur in
Erinnerung rufen, dass die 1. Ableitung eindimensionaler Funktionen dem
Gradienten entspricht. Und da der Gradient der Zeilenvektor ist, der alle
partielle Ableitungen zusammenfasst, lautet die **notwendige Bedingung für einen
Extremwert** der skalarwertigen Funktion $f$

$$\frac{\partial f(x_0, y_0)}{\partial x} = 0 \quad \text{ und }
\quad \frac{\partial f(x_0,y_0)}{\partial y} = 0.$$

Diese Gleichung können wir auch vektoriell schreiben:

$$\nabla f(x_0,y_0) = \left( \frac{\partial f(x_0, y_0)}{\partial
x},\frac{\partial f(x_0,y_0)}{\partial y}\right) = (0,0).$$

Der Gradient der Funktion muss der Nullvektor sein, so wie die 1. Ableitung Null
sein muss.

Das folgende Video erläutert nochmal die notwendige Bedingung, der Dozent zeigt
jedoch gleich die Bedingung für eine Funktion, die von beliebig vielen Variablen
abhängt. Das ist eine Verallgemeinerung von der oben vorgestellten Bedingung.

```{dropdown} Video zu "Notwendige Bedingung für Extremwerte" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/A_f5qpyl0bk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

Im folgenden Video werden mehrere  Beispiele vorgerechnet.

```{dropdown} Video zu "Beispiele notwendige Bedingung" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/AMYCKnbgU3s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

Wenn die notwendige Bedingung erfüllt ist, also die partiellen Ableitungen 1.
Ordnung Null sind, dann reicht das noch nicht aus. Zusätzlich muss noch die
folgende **hinreichende Bedingung** gelten: Die **Determinante der Hesse-Matrix
ist positiv**.

$$\det(H_f\,(x_0,y_0)) = \frac{\partial^2 f(x_0,y_0)}{\partial x\partial x}\cdot
\frac{\partial^2 f(x_0,y_0)}{\partial y \partial y} 
- \left(\frac{\partial^2 f(x_0,y_0)}{\partial x \partial y}\right)^2 > 0.$$

Sobald durch die zweite Bedingung geklärt ist, dass tatsächlich ein Extremwert
vorliegt, muss noch berechnet werden, ob ein Maximum (Hochpunkt) oder ein
Minimum (Tiefpunkt) vorliegt. Dazu muss das Vorzeichen der reinen 2. partiellen
Ableitung nach $x$ überprüft werden, also das Vorzeichen von $\frac{\partial^2
f(x_0,y_0)}{\partial x\partial x}$. Es gilt:

\begin{align*} \frac{\partial^2 f(x_0,y_0)}{\partial x\partial x} < 0 &
\qquad \Rightarrow \text{Maximum (Hochpunkt)} \\
\frac{\partial^2 f(x_0,y_0)}{\partial x\partial x} > 0 & \qquad
\Rightarrow \text{Minimum (Tiefpunkt)} \\
\end{align*}

Das folgende Video zeigt erneut die hinreichende Bedingung etwas allgemeiner als
unsere obigen Betrachtungen.

```{dropdown} Video zu "Hinreichende Bedingung für Extremwerte" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/eT0nrz_Mujo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

Da die Bestimmung von Extremwerten ein schwiriges, aber sehr wichtiges Thema
ist, folgen noch weitere Videos der Universität Köln, in denen Beispiel
vorgerechnet werden.

```{dropdown} Video zu "Beispiel 1a Extremwerte" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/oGWN1pZaJBc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Beispiel 1b Extremwerte" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/8IF5uLY7Gwk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Beispiel 1c Extremwerte" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/khMbyiPsSS4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Beispiel 2 Extremwerte" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/MGV0uSj8lbg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Kochrezept zur Bestimmung der Extrema mehrdimensionaler Funktionen

Falls die Extremstellen einer Funktion $f$ gesucht sind, können Sie
folgendermaßen vorgehen:

1. Berechnen Sie die partiellen Ableitungen der Funktion.
2. Setzen Sie aus den partiellen Ableitungen den Gradienten zusammen.
3. Lösen Sie die Gleichung $\nabla f(x,y) = (0,0)$. Oder anders ausgedrückt, setzen sie alle partiellen Ableitungen gleich Null und bestimmen Sie die Nullstellen.
4. Untersuchen Sie für **jeden** Punkt aus Schritt 3 die Hessematrix:

    * Berechnen Sie die Hesse-Matrix für diesen Punkt.
    * Berechnen Sie die Determinante der Hesse-Matrix für diesen Punkt und prüfen Sie, ob sie positiv ist.
    * Wenn die Determinante positiv ist, dann berechnen Sie das Vorzeichen von 
    
    $$\frac{\partial^2 f(x_0,y_0)}{\partial x\partial x}.$$
    
    * Entscheiden Sie dann anhand des Vorzeichens, ob ein Minimum (Tiefpunkt) oder ein Maximum (Hochpunkt) vorliegt.

## Ausführliches Beispiel

Als Beispiel betrachten wir die Funktion 

$$f(x,y) = \frac{1}{1+x^2+y^2}.$$

Als erstes berechnen wir die partiellen Ableitungen nach $x$ und $y$:

\begin{align*}
\frac{\partial f(x,y)}{\partial x} &= \frac{-2x}{(1 + x^2 + y^2)^2} \\
\frac{\partial f(x,y)}{\partial y} &= \frac{-2y}{(1 + x^2 + y^2)^2} \\
\end{align*}

Der Gradient der Funktion $f$ lautet also

$$\nabla f(x,y) = \left(\frac{-2x}{(1 + x^2 + y^2)^2}, \frac{-2y}{(1 + x^2 +
y^2)^2} \right).$$

Jetzt werden der Gradient bzw. die partiellen Ableitungen Null gesetzt und wir
erhalten die beiden folgenden Gleichungen:

\begin{align*}
\frac{-2x}{(1 + x^2 + y^2)^2} &= 0 \\
\frac{-2y}{(1 + x^2 + y^2)^2} &= 0 \\
\end{align*}

Wir multiplizieren bei jeder Gleichung mit dem Nenner $(1 + x^2 + y^2)^2$ und
erhalten direkt die Nullstelle der 1. Gleichung $x = 0$ und die Nullstelle der
2. Gleichung $y = 0$. Damit kommt nur ein einziger Kandidat als Extremstelle
infrage nämlich

$$(x_0, y_0) = (0,0).$$

Nun wird die Hesse-Matrix berechnet. Dazu werden die 2. partiellen Ableitungen
gebildet:

\begin{align*}
\frac{\partial^2 f(x,y)}{\partial x \partial x} &= \frac{6x^2 - 2(y^2+1)}{(1 + x^2 + y^2)^3} \\
\frac{\partial^2 f(x,y)}{\partial y \partial x} &= \frac{8xy}{(1 + x^2 + y^2)^3} \\
\frac{\partial^2 f(x,y)}{\partial x \partial y} &= \frac{8xy}{(1 + x^2 + y^2)^3} \\
\frac{\partial^2 f(x,y)}{\partial y \partial y} &= -\frac{2(x^2 - 3y^2 +1)}{(x^2 + y^2 + 1)^3} \\
\end{align*}

Damit lautet die Hesse-Matrix:

$$H_{f}(x,y) =
\begin{pmatrix}
\frac{6x^2 - 2(y^2+1)}{(1 + x^2 + y^2)^2} & \frac{8xy}{(1 + x^2 + y^2)^3} \\
\frac{8xy}{(1 + x^2 + y^2)^3} & -\frac{2(x^2 - 3y^2 +1)}{(x^2 + y^2 + 1)^3} \\
\end{pmatrix}.
$$

Nun werden alle Kandidaten nacheinander in die Hesse-Matrix eingesetzt. Da wir aber nur einen einzigen Kandidaten haben, setzen wir jetzt den Punkt $(0,0)$ ein und erhalten

$$H_{f}(0,0) = 
\begin{pmatrix}
-2 & 0 \\
0 & -2 \\
\end{pmatrix}. 
$$

Davon berechnen wir die Determinante und testen, ob sie positiv ist:

$$\det 
\begin{pmatrix}
-2 & 0 \\
0 & -2 \\
\end{pmatrix} = (-2)\cdot (-2) - (0 \cdot 0) = + 4 > 0.$$

Damit ist der Punkt $(0,0)$ eine Extremstelle. Jetzt bleibt nur noch die
Überprüfung, ob ein Minimum oder ein Maximum vorliegt. Das Vorzeichen von 

$$\frac{\partial^2 f(x,y)}{\partial x \partial x}$$

an der Stelle $(0,0)$ ist negativ, da 

$$\frac{\partial^2 f(0,0)}{\partial x \partial x} = -2.$$

Damit hat die Funktion $f$ an der Stelle $(0,0)$ ein Maximum (Hochpunkt).

Das folgende Video zeigt ein weiteres Beispiel.

```{dropdown} Video zu "Extremwerte mehrdimensionaler Funktionen" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/GwyPVdoQ37g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```