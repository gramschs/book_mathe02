# 11.4 Exakte Differentialgleichungen

In diesem Kapitel werden wir uns mit exakten Differentialgleichungen
beschäftigen. 

## Lernziele

```{admonition} Lernziele
:class: important
* Sie können anhand des Exaktheitskriterium überprüfen, ob eine
  Differentialgleichung 1. Ordnung der Form
  
  $$p(x, y) + q(x, y) \cdot y' = 0$$ 

  exakt ist.
* Sie können eine exakte Differentialgleichung lösen.
```

## Was ist eine exakte Differentialgleichung?

Bei den exakten Differentialgleichungen handelt es sich um
Differentialgleichungen 1. Ordnung. Wenn die Differentialgleichung in die Form 

$$p(x, y) + q(x, y) \cdot y' = 0$$

gebracht werden kann und wenn zusätzlich die sogenannte **Exaktheitsbedingung**

$$\frac{\partial p(x, y)}{\partial
y} = \frac{\partial q(x, y)}{\partial x}$$

erfüllt ist, dann wird die Differentialgleichung **exakt** genannt.

## Beispiel einer exakten Differentialgleichung

Die Differentialgleichung

$$(y - x) + (y+x)\cdot y' = 0$$

ist von 1. Ordnung und lässt sich mit

\begin{align*}
p(x, y) &= y - x\\
q(x, y) &= y + x
\end{align*}

in der oben beschriebenen Form schreiben. Als nächstes wird überprüft, ob die
Exaktheitsbedingung erfüllt ist.

\begin{align*}
\frac{\partial p(x, y)}{\partial y} &= \frac{\partial}{\partial y}(y - x) = 1, \\
\frac{\partial q(x, y)}{\partial x} &= \frac{\partial}{\partial x}(y + x) = 1. 
\end{align*}

Beide partielle Ableitungen sind gleich und daher ist die Differentialgleichung
exakt.

## Wie werden exakte Differentialgleichugnen gelöst?

Liegt eine exakte Differentialgleichung vor, so wird die Differentialgleichung
oft etwas informell mit dem Differentialquotienten $y'=\frac{dy}{dx}$
folgendermaßen notiert:

$$p(x, y) + q(x, y) \frac{dy}{dx} = 0 \quad 
\Rightarrow \quad p(x,y) \, dx + q(t, x) \, dy = 0. $$

Das erinnert an das totale Differential. Für die Lösungsidee starten wir mit
einer Funktion $F$, die von zwei Variablen abhängt, nämlich $x_1$ und $x_2$, und
für die gilt:

$$F(x_1, x_2) = c.$$

Dabei ist $c\in\mathbb{R}$ eine reelle Konstante. 

Nun soll die erste Variable $x_1$ gleich $x$ sein, also $x_1 = x$. Die zweite
Variable soll der Funktionswert $y(x)$ sein, also $x_2=y(x)$. Damit ist $F$ eine
Funktion, die eigentlich nur von $x$ abhängt. Einmal direkt und einmal indirekt
als verkettete Funktion. Die erste Ableitung nach $x$ muss mit der
mehrdimensionalen Kettenregel berechnet werden:

$$F'(x, y(x)) = \left(\frac{\partial F}{\partial x}, \, \frac{\partial F}{\partial y}\right) \cdot 
\begin{pmatrix} 1 \\ y' \end{pmatrix} 
= \frac{\partial F}{\partial x} + \frac{\partial F}{\partial y} y'.$$

Wird die rechte Seite der Gleichung $F(x_1, x_2) = c$ abgeleitet, ist dies Null.
Damit gilt für die erste Ableitung der Funktion $F(x,y)$

$$\frac{\partial F}{\partial x} + \frac{\partial F}{\partial y} y' = 0.$$

Das ist genau die Form der exakten Differentialgleichung mit

\begin{align*}
p(x,y) &= \frac{\partial F(x,y)}{\partial x} \\
q(x,y) &= \frac{\partial F(x,y)}{\partial y}
\end{align*}

Aber wir kommen wir nun auf $F(x,y)$?

Wir integrieren die erste Funktion $p(x,y)$ nach $dx$. Die dabei entstehende
Integrationskonstante kann noch von $y$ abhängen. Wird nämlich partiell nach $x$
abgeleitet, so werden Terme mit $y$ nämlich Null. Deshalb schreiben wir dafür
$C(y)$ und erhalten

$$F(x,y) = \int p(x,t) \, dx + C(y).$$

Jetzt leiten wir diese Funktion partiell nach $y$ ab. Dabei erhalten wir zum
einen die partielle Ableitung des Integrals $\int p(x,t) \, dx$, zum anderen die
Ableitung $C'(y)$. Das Ergebnis muss $q(x,y)$ sein. Aus dieser Gleichung wird
dann $C(y)$ durch Integration nach $y$ bestimmt. Sobald $F(x,y)$ eindeutig
bestimmt ist, wird dann 

$$F(x,y) = c$$

gesetzt und nach $y$ aufgelöst.

## Beispiel zur Lösung einer exakten Differentialgleichung

Wir betrachten erneut die exakte Differentialgleichung

$$(y - x) + (y+x)\cdot y' = 0.$$

Wir haben oben die Exaktheitsbedingung schon nachgerechnet und können daher
direkt den Ansatz

$$F(x,y) = c$$

mit 

$$\frac{\partial F(x,y)}{\partial x} = y - x$$

verwenden. Durch Integration nach $x$ erhalten wir

$$F(x,y) = \int p(x,y) \, dx + C(y) = \int (y-x)\, dx + C(y) 
= yx -\frac{1}{2}x^2 + C(y).$$

Partiell ableiten nach $y$ und gleichsetzen mit $q(x,y)=y+x$ liefert

$$x+C'(y) = y+x.$$

Damit erhalten wir 

$$C'(y)=y \quad \Rightarrow C(y) = \int y\, dy = \frac{1}{2}y^2.$$

Damit ist

$$F(x,y) = yx -\frac{1}{2}x^2 + \frac{1}{2}y^2  = c.$$

Jetzt wird noch nach $y$ aufgelöst:

\begin{align*}
yx -\frac{1}{2}x^2 + \frac{1}{2}y^2  = c \qquad &| \cdot 2 \\
2yx - x^2 + y^2 = 2c \qquad &| +2x^2 \\
y^2 + 2xy + x^2 = 2c + 2x^2 \qquad & \\
(y+x)^2 = 2c + 2x^2 \qquad & | \sqrt{} \\
y + x = \pm \sqrt{2c + 2x^2} \qquad & | -x \\
y(x) = \pm \sqrt{2c + 2x^2} - x \\
\end{align*}

Die allgemeine Lösung der Differentialgleichung $(y - x) + (y+x)\cdot y' = 0$
ist

$$y(x) = \pm \sqrt{2c + 2x^2} - x.$$


```{dropdown} Video zu "Exakte Differentialgleichung" von Lernkompass
<iframe width="560" height="315" src="https://www.youtube.com/embed/PGiwJ57E1nc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```