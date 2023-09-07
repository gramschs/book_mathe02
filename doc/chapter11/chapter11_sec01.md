# 11.1 Grundbegriffe


In diesem Abschnitt führen wir zunächst die grundlegenden Begriffe rund um das
Thema Differentialgleichungen anhand eines einfachen Beispieles ein. 

## Lernziele

```{admonition} Lernziele
:class: important
* Sie wissen, was eine **Differentialgleichung** ist.
* Sie kennen verschiedene Schreibweisen zur Formulierung von Differentialgleichungen.
* Sie können die **Ordnung einer Differentialgleichung** ablesen.
* Sie können erklären, was eine **gewöhnliche Differentialgleichung** und was eine **partielle Differentialgleichung** ist.
* Sie können unterscheiden, ob eine Differentialgleichung in der **expliziten Form** oder der **impliziten Form** formuliert wurde.
```

## Eine Differentialgleichung ist auch nur eine Gleichung

Bisher haben wir Gleichungen kennengelernt, bei denen nach einer oder mehreren
reellen Zahlen gesucht wurde. Die reellen Zahlen, die die Gleichung erfüllen,
nennen wir Lösung der Gleichung. Damit ist gemeint, dass man die gefundene
reelle Zahl, also die Lösung, in die Gleichung einsetzt und überprüft, ob linke
und rechte Seite übereinstimmen.

Beispielsweise wird die Gleichung

$$ x^2 - x - 6 = 0$$

von zwei reellen Zahlen erfüllt, nämlich $x_1 = -2$ und $x_2=3$. Wir können
beide Zahlen in die Gleichung einsetzen und erhalten $x_1^2 -x_1 - 6 = 4 + 2 - 6
= 0$ und $x_2^2 - x_2 - 6 = 9 -3 - 6 = 0$. Damit sind beide Zahlen eine Lösung
dieser Gleichung. Wie wir jedoch auf die Lösung der Gleichung kommen, durch
Raten, ein systematisches Verfahren oder durch den Computer, ist ein eigenes
mathematisches Thema. Auch ist nicht von vornherein klar, ob die Gleichung
überhaupt lösbar ist und wie viele Lösungen es ggf. gibt.


Gerade in den Ingenieurwissenschaften wird oft nicht eine Zahl gesucht, sondern
eine Funktion! Und oft spielen Ableitungen dabei eine wichtige Rolle. Ein
simples mathematisches Beispiel für eine Gleichung mit einer Funktion und einer
Ableitung ist die folgende Gleichung:

$$f''(x) = -f(x).$$

Gesucht wird also eine Funktion, die zweimal abgeleitet die Funktion selbst
wieder ergibt, nur mit umgekehrten Vorzeichen. Eine Funktion, die diese
Gleichung löst, ist die Sinus-Funktion. Probieren wir es aus und bilden erst
einmal die Ableitungen:

$$f(x) = \sin(x) \quad \Rightarrow f'(x) = \cos(x) \quad \Rightarrow f''(x) =
-\sin(x).$$

Eingesetzt in die Gleichung erhalten wir also $-\sin(x) = -\sin(x)$. Damit
erfüllt die Sinus-Funktion die Gleichung $f''(x) = -f(x).$ 


```{admonition} Mini-Übung
:class: tip
Welche der folgenden Funktionen ist erfüllt die Gleichung

$$f''(x) = - f(x)?$$

a) $f(x) = \cos(x)$ <br>
b) $f(x) = e^x$ <br>
c) $f(x) = \sin(x) + 3\cos(x)$ <br>

```

```{admonition} Lösung
:class: tip, toggle
a) ableiten: $f(x)=\cos(x) \quad \Rightarrow f'(x)=-\sin(x) \quad \Rightarrow f''(x)=-\cos(x)$ <br>
eingesetzt: $-\cos(x) = -\cos(x)$ erfüllt die Gleichung

b) ableiten: $f(x)=e^x \quad \Rightarrow f'(x)=e^x \quad \Rightarrow f''(x)=e^x$ <br>
eingesetzt: $e^x \neq -e^x$ erfüllt die Gleichung nicht

c) ableiten: 
\begin{align*}
f(x) &=\sin(x)+3\cos(x) \\
\Rightarrow \quad f''(x)&=\cos(x)-3\sin(x) \\
\Rightarrow \quad f''(x)&=-\sin(x)-3\cos(x)
\end{align*} 

eingesetzt: $-\sin(x)-3\cos(x) = -\left(\sin(x)+3\cos(x)\right)$ erfüllt die Gleichung
```


Wir übernehmen die Begriffe für Gleichungen reeller Zahlen nun für diese neue
Art von Gleichungen, die sogenannten Differentialgleichungen.


```{admonition} Was ist ... eine Differentialgleichung?
Eine Gleichung, bei der eine Funktion gesucht wird und ihre Ableitungen in der Gleichung ebenfalls vorkommen, nennen wir **Differentialgleichung**. Oft kürzen wir das Wort Differentialgleichung mit DGL ab.
```

```{dropdown} Video zu "Gewöhnliche Differentialgleichung"
<iframe src="https://frankfurt-university.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=2df731d3-5569-405e-b6ed-b0180090a481&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>
```

(sec_11_01_b)=
## Es gibt viele Schreibweisen für DGL

So wie Gleichungen für Zahlen mit unterschiedlichen Variablen formuliert werden,
werden auch bei Differentialgleichungen unterschiedliche Schreibweisen benutzt.
Meistens werden die Bezeichnungen aus dem Anwendungskontext übernommen.

Zunächst einmal können die Bezeichnungen für die Variablen der gesuchten
Funktion variieren. In dem obigen Beispiel 

$$f''(x)=-f(x)$$

wurde als Variablenname $x$ benutzt. Die Variablen der gesuchten Funktion werden
als **unabhängige Variablen** bezeichnet. Die gesuchte Funktion wird auch als
**abhängige Variable** bezeichnet, obwohl es sich um eine Funktion handelt.
Sollte es sich jedoch um eine Funktion in Abhängigkeit einer zeitlichen Größe
handeln, würde die DGL wohl eher als

$$f''(t)=-f(t)$$

formuliert werden. Bei zeitlichen Ableitungen wird in den
Ingenieurwissenschaften auch eher ein Punkt über den Funktionsnamen gesetzt, um
anzudeuten, dass eine zeitliche Größe betrachtet wird, also

$$\ddot{f}(t)=-f(t).$$

Auch würde wohl auch eher die gesuchte Funktion mit $x$ bezeichnet werden, also

$$\ddot{x}(t)=-x(t).$$

Oft finden wir auch die Schreibweise mit dem Differentialoperator und der
Bezeichnung $y$ für die gesuchte Funktion, also

$$\frac{d^2y}{dt^2}=-y(t).$$

Und da die unabhängige Variable nicht so wichtig ist, weil es bei
Differentialgleichungen um die unbekannte Funktion geht, wird sie manchmal
weggelassen, also

$$y''=-y.$$

Alle Schreibweisen – so unterschiedlich sie auch wirken mögen – drücken dieselbe
Frage aus: welche Funktion muss zweimal abgeleitet werden, damit sie das
Negative von sich selbst ist?



(sec_11_01_a)=
## Die Ordnung entscheidet über die Anzahl der Integrationskonstanten

Als wir verschiedene Funktionen daraufhin überprüft haben, ob sie die
Differentialgleichung

$$y''(x) = - y(x)$$

erfüllen, haben wir schon festgestellt, dass es mehrere Funktionen geben kann,
die passen. Wir schauen uns nun ein etwas einfacheres Beispiel an:

$$y''(x) = -\sin(x).$$

Auf der rechten Seite kommt die gesuchte Funktion $y(x)$ nicht mehr vor, sondern
sie steht nur noch als 2. Ableitung auf der linken Seite der Gleichung. Ein
einfacher Ansatz, um die DGL zu lösen ist, auf beiden Seiten unbestimmt zu
integrieren. Wir erhalten

$$\int y''(x)\, dx = \int -\sin(x)\, dx \quad \Rightarrow \quad y'(x) = \cos(x)
+ C_1.$$

Die Integrationskonstante, die eigentlich auch auf der linken Seite entstanden
wäre, haben wir dabei schon auf die rechte Seite gebracht. Nun haben wir eine
DGL mit der 1. Ableitung der gesuchten Funktion. Wir integrieren einfach noch
einmal unbestimmt auf beiden Seiten und bekommen

$$\int y'(x)\, dx = \int \cos(x) + C_1 \, dx \quad \Rightarrow \quad y(x) =
\sin(x) + C_1 x + C_2.$$

Die gefundene Funktion $y(x)=\sin(x)+C_1 x + C_2$ ist nicht nur *eine* Funktion,
sondern eine ganze Schar von Funktionen. Es können zwei verschiedene Parameter
$C_1$ und $C_2$ gewählt werden. Mathematisch gesehen gibt es bei der Wahl der
Parameter keine Einschränkungen; wir könnten jede reelle Zahl wählen. Daher gibt
es unendlich viele Lösungen der Differentialgleichung.


```{admonition} Mini-Übung
:class: tip
Überprüfen Sie, ob die folgenden drei Variationen von $C_1$ und $C_2$ tatsächlich die DGL

$$y''(x)=-\sin(x)$$

erfüllen.

a) $C_1 = 1$ und $C_2 = 0$, also $y_1(x) = \sin(x) + x$ <br>
b) $C_1 = 0$ und $C_2 = 1$, also $y_2(x) = \sin(x) + 1$ <br>
c) $C_1 = -2$ und $C_2 = 3$, also $y_3(x) = \sin(x) -2x + 3$<br>
```

````{admonition} Lösung
:class: tip, toggle
Um zu überprüfen, ob die gegebenen Variationen die DGL $y''(x) = -\sin(x)$
erfüllen, müssen wir die zweite Ableitung jeder Funktion berechnen und
überprüfen, ob sie gleich $-\sin(x)$ ist.

a) $y_1(x) = \sin(x) + x$
\begin{align*}
\Rightarrow \quad y_1'(x)  &= \cos(x) + 1 \\
\Rightarrow \quad y_1''(x) &= -\sin(x) 
\end{align*}

Da $y_1''(x) = -\sin(x)$ gilt, erfüllt $y_1$ die DGL.

b) $y_2(x) = \sin(x) + 1$
\begin{align*}
\Rightarrow \quad y_2'(x) &= \cos(x) \\
\Rightarrow \quad y_2''(x) &= -\sin(x) 
\end{align*}

Da $y_2''(x) = -\sin(x)$ gilt, erfüllt $y_2$ ebenfalls die DGL.

c) $y_3(x) = \sin(x) - 2x + 3$
\begin{align*}
\Rightarrow \quad y_3'(x)  &= \cos(x) - 2 \\
\Rightarrow \quad y_3''(x) &= -\sin(x) 
\end{align*}

Da $y_3''(x) = -\sin(x)$ gilt, erfüllt auch $y_3$ die DGL.

Alle drei Funktionen erfüllen die Differentialgleichung $y''(x) = -\sin(x)$ und
sind daher Lösungen der Differentialgleichung.
````

Durch dieses Beispiel haben wir zwei Sachen kennengelernt, die typisch für
Differentialgleichungen sind:

* Um die gesuchte Funktion einer Differentialgleichung zu finden, müssen wir
  integrieren.
* Je höher die Ableitung der gesuchten Funktion ist, desto öfter müssen wir
  integrieren. Und je öfter wir integrieren müssen, desto mehr
  Integrationskonstanten entstehen.

Der Grad der höchsten Ableitung der gesuchten Funktion ist so wichtig, dass
Differentialgleichungen danach eingeteilt werden. Wir halten daher folgende
Definition fest. 


```{admonition} Was ist ... die Ordnung einer Differentialgleichung?
Die höchste vorkommene Ableitung der gesuchten Funktion nennen wir **Ordnung** der Differentialgleichung.
```

```{dropdown} Video zu "Ordnung einer gewöhnlichen Differentialgleichung"
<iframe src="https://frankfurt-university.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=e9c4b3da-35c2-4320-babb-b0180090ad24&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>
```

## Gewöhnlich betrachten wir gewöhnliche DGL

Im Zusammenhang mit Differentialgleichungen werden häufig die beiden Adjektive
gewöhnlich und partiell verwendet. Eines vorneweg, in diesem und in den nächsten
Kapiteln werden wir nur gewöhnliche Differentialgleichungen betrachten.

Die gesuchte Funktion der Differentialgleichung kann von einer unabhängigen
Variable abhängen, also eindimensional sein, aber auch von mehreren unabhängigen
Variablen abhängen, also mehrdimensional sein. Dementsprechend können normale
Ableitungen in der Differentialgleichung auftreten, wie wir es in den oben
stehenden Beispielen gesehen haben, oder partielle Ableitungen. 

Eine Differentialgleichung, bei der nur Ableitungen nach einer Variable
vorkommen, heißt **gewöhnliche Differentialgleichung**. Kommen in der
Differentialgleichungen Ableitungen nach mehreren unabhängigen Variablen vor, so
nennen wir diese Gleichung **partielle Differentialgleichung**. Hier sehen Sie
ein Beispiel für eine partielle DGL, in der Ableitungen nach dem Ort $x$ und der
Zeit $t$ vorkommen:

$$\frac{\partial u(x,t)}{\partial t} - a^2 \frac{\partial^2 u(x,t)}{\partial
x^2} = 0.$$

```{admonition} Was ist ... eine gewöhnliche Differentialgleichung?
Eine Differentialgleichung, bei der die gesuchte Funktion nur von einer
unabhängigen Variable abhängt, wird als **gewöhnliche Differentialgleichung**
bezeichnet. Kommen in der Differentialgleichungen Ableitungen nach mehreren
unabhängigen Variablen vor, so nennen wir diese Gleichung **partielle
Differentialgleichung**. 
```

Die Beispiele, die wir bisher betrachtet haben, waren so formuliert, dass die
höchste Ableitung auf der linken Seite stand und alle anderen Terme auf der
rechten Seite der Gleichung. Das muss aber nicht so sein. Eine
Differentialgleichung, die nach der höchsten Ableitung aufgelöst ist, nennen wir
**explizite Differentialgleichung**. Ein Beispiel für eine explizite DGL ist

$$y'' = -3y' + 2y.$$

Ist hingegen die DGL *nicht* nach der höchsten Ableitung aufgelöst, so
bezeichnen wir diese als **implizite Differentialgleichung**. Wir können das
Beispiel umformen zu

$$y'' + 3y' -  2y = 0.$$

Es war einfach, die explizite Differentialgleichung in eine implizite
Differentialgleichung umzuformen. Leider lässt sich nicht jede implizite
Differentialgleichung in eine explizite DGL umformen.

```{dropdown} Video zu "Explizite und implizite Differentialgleichungen"
<iframe src="https://frankfurt-university.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=f685aee3-bac5-4459-839e-b01800ec5f8a&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>
```

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir die grundlegenden Konzepte von
Differentialgleichungen behandelt. Da es sich um eine Einführung zum Thema
handelt, haben wir uns zunächst damit beschäftigt, was eine
Differentialgleichung ist und welche Schreibweisen es für
Differentialgleichungen gibt. Obwohl in dieser Vorlesung nur gewöhnliche
Differentialgleichungen thematisiert werden, sind wir auf den Unterschied
zwischen gewöhnlichen und partiellen Differentialgleichungen eingegangen.
Zusätzlich haben wir uns mit der Ordnung einer Differentialgleichung beschäftigt
und wie sie die Anzahl der Integrationskonstanten beeinflusst. Im nächsten
Kapitel wird es darum gehen, wie aus unendlich vielen Lösungen einer
Differentialgleichung eine spezielle Lösung herausgesucht wird.
