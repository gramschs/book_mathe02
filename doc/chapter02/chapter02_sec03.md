# 2.3 Bogenlänge

Nachdem wir bisher das Integral dazu genutzt haben, Flächen zu berechnen, wird
das Integral in diesem Abschnitt dazu genutzt, Längen zu berechnen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was die **Bogenlänge** eines Funktionsgraphens ist.
* Sie können die Bogenlänge eines Funktionsgraphens $f(x)$ einer stetig
  differenzierbaren Funktion $f$ zwischen dem Startpunkt $(a,f(a))$ und dem
  Endpunkt $(b,f(b))$ mit der folgenden Formel berechnen:

$$\text{Bogenlänge} = \int_{a}^{b} \sqrt{1+(f'(x))^2}\, dx.$$
```

## Länge eines Funktionsgraphens

```{admonition} Was ist ... die Bogenlänge?
:class: note
Die Bogenlänge eines Funktionsgraphens ist die Strecke, die man zwischen Start
und Ziel zurücklegt. Start und Ziel sind dabei zwei Punkte, die beide auf dem
Funktionsgraphen liegen.
```

## Wie wird die Bogenlänge berechnet?

Solange wir nicht mit einem Kilometerzähler einen Funktionsgraphen abfahren,
brauchen wir ein anderes Hilfsmittel, um die Streckenlänge zu berechnen. Für
Funktionen, die stetig differenzierbar sind, gibt es eine passende Formel.
Stetig differenzierbare Funktion heißt, dass die Funktion eine 1. Ableitung
haben muss und diese Ableitung soll wiederum stetig sein. Die üblichen
Funktionen in den Ingenieurwissenschaften erfüllen diese Bedingung, so dass Sie
sich im Normalfall keine Gedanken um diese Bedingung machen müssen.

```{admonition} Kochrezept zur Berechnung der Bogenlänge
:class: note
Wenn die Bogenlänge des Funktionsgraphens $f(x)$ vom Startpunkt $(a,f(a))$ bis zum Endpunkt $(b,f(b))$ berechnet werden soll und die Funktion $f$ stetig differenzierbar ist, gehen Sie folgenermaßen vor:

1. Berechnen Sie die 1. Ableitung $f'$.
2. Quadrieren Sie die 1. Ableitung und versuchen Sie, den Term $\sqrt{1+\left(f'(x)\right)^2}$ so weit wie möglich zu vereinfachen.
3. Berechnen Sie dann das folgende Integral (oft müssen Sie dabei die Substitutionsregel benutzen):

$$\text{Bogenlänge} = \int_{a}^{b} \sqrt{1+(f'(x))^2}\, dx.$$
```

## Beispiel zur Berechnung der Bogenlänge

Als nächstes betrachten wir die Funktion $f(x)=x^{\frac{3}{2}}+1$ für positive
reelle Zahlen $x\geq 0$. Wir wählen als

* Start $a=1 \Rightarrow f(1)=1^{\frac{3}{2}}+1 =2$ und als
* Ziel $b=4 \Rightarrow f(4)=4^{\frac{3}{2}}+1 = 8+1 = 9$,

also den Start $(1,2)$ und das Ziel $(4,9)$. Die Formel für die Bogenlänge
beinhaltet den Term $(f'(x))^{2}$, also das Quadrat der 1. Ableitung. Diesen
Term berechnen wir vorab in einer Nebenrechnung. Zuerst wird die 1. Ableitung
berechnet:

$$f(x)=x^{\frac{3}{2}} + 1 \Rightarrow f'(x)= \frac{3}{2}x^{\frac{1}{2}} = \frac{3}{2}\sqrt{x}.$$

Damit erhalten wir

$$(f'(x))^{2} = \big( \frac{3}{2}\sqrt{x} \big)^{2} = \frac{9}{4}x.$$

Der Term $\sqrt{1+\frac{9}{4}x}$ lässt sich leider nicht weiter vereinfachen, so dass für die Berechnung des Integrals

$$L = \int_{1}^{4} \sqrt{1 + \frac{9}{4}x}\, dx$$

die Substitutionsregel benutzt werden muss. Wir setzen $z = 1 + \frac{9}{4}x$. Dann gilt

\begin{align*}
L & = \int_{1}^{4} \sqrt{1 + \frac{9}{4}x}\, dx = \\
  & = \int \sqrt{z} \cdot \frac{4}{9} \, dz  = \frac{4}{9}\cdot\frac{2}{3} \left[ z^{\frac{3}{2}}\right] = \\
  & = \frac{8}{27} \left[\left(1+\frac{9}{4}x\right)^{\frac{3}{2}}\right]_{1}^{4} = \\
  & \approx 7.6337.
\end{align*}

In dem folgenden Video wird ein zweites Beispiel vorgeführt.

```{dropdown} Video "Wie lang ist die Kurve" von Mathematrick
<iframe width="560" height="315" src="https://www.youtube.com/embed/xYr6zDAgIo8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Wie kommt man auf die Formel zur Berechnung der Bogenlänge?

Um zu erklären, wie die Formel zur Berechnung der Bogenlänge enstanden ist, betrachten wir das folgende Beispiel: $f(x)=x^3-4x^2+2x+5$. Der Start soll bei $(1,4)$ liegen, Endpunkt ist $(4,13)$. Die einfachste Näherung der Bogenlänge ist die Luftlinie, also die die direkte Strecke zwischen Start und Ziel. Das lässt sich mit dem Satz des Pythagoras berechnen:

$$L \approx \sqrt{\Delta x^2 + \Delta y^2} = \sqrt{(4-1)^2 + (13-4)^2} = \sqrt{9+81} = \sqrt{108}.$$

Dies ist nur eine grobe Näherung an die echte Bogenlänge. Besser wird es mit zwei Zwischenstopps.

$$L \approx \sqrt{(\Delta x_1)^2 + (\Delta y_1)^2} + \sqrt{(\Delta x_2)^2 + (\Delta y_2)^2}  + \sqrt{(\Delta x_3)^2 + (\Delta y_3)^2} .$$

Zwei Zwischenstopps ergeben drei Luftlinienstücke, deren Summe eine Schätzung für die echte Bogenlänge ist. Noch besser wird es, wenn es noch mehr Zwischenstopps gibt. Am einfachsten ist es, wenn wir immer den gleichen Abstand auf der x-Achse für die Zwischenstopps wählen, nämlich $\Delta x = \frac{b-a}{N}$. Dann sind es $N$ Luftlinienstücke, die aufsummiert werden.

\begin{align*}
L \approx L_1 + L_2 + \dots + L_N &= \sqrt{(\Delta x)^2 + (\Delta y_1)^2} + \sqrt{(\Delta x)^2 + (\Delta y_2)^2} + \ldots + \sqrt{(\Delta x)^2 + (\Delta y_N)^2} \\
& = \sum_{i=1}^{N} \sqrt{(\Delta x)^2 + (\Delta y_i)^2}.
\end{align*}

Jetzt wird ein Trick angewandet. Der Term $(\Delta x)^2$ wird ausgeklammert:

$$L \approx \sum_{i=1}^{N} \sqrt{\big(1+\frac{(\Delta y_i)^2}{(\Delta x)^2}\big)\cdot (\Delta x)^2}.$$

Somit kann die Wurzel $\sqrt{(\Delta x)^2}$ vereinfacht werden ud wir haben

$$L \approx \sum_{i=1}^{N} \sqrt{\left(1+\left(\frac{\Delta y_i}{\Delta x}\right)^2\right)}\cdot\Delta x.$$

Das war aber nicht der eigentliche Grund, warum wir den Trick mit dem Ausklammern angewendet haben. Der wahre Grund ist, dass nun der Term

$$\frac{\Delta y_i}{\Delta x}$$

unter der Wurzel steht (etwas präziser steht $\big(\frac{\Delta y_i}{\Delta x}\big)^2$ unter der Wurzel). Und das ist ein Term, den wir bereits sehr gut kennen. Er wird Differenzenquotient genannt. Der Differenzenquotient beschreibt die Steigung der Sekante.

Wenn wir jetzt mehr und mehr Zwischenstopps einfügen, passiert Folgendes. Aus der Summe wird ein Integral. Wenn die Funktion $f$ differenzierbar ist und die 1. Ableitung stetig, konvergiert der Deifferenzenquotient gegen den Differentialquotienten $\frac{dy}{dz}$, also die 1. Ableitung. Und die Differenz $\Delta x$ wird zum Differential $dx$. Im Grenzwert steht dann also Folgendes da:

$$L = \lim_{N\to\infty} \sum_{i=1}^{N} \sqrt{1 + \left(\frac{\Delta y_i}{\Delta x}\right)^2} \Delta x = \int_{a}^{b} \sqrt{1+f'(x)}\, dx.$$

Und so kann man die Formel zur Berechnung der Bogenlänge begründen.
