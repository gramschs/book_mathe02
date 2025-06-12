# 10.3 Dreifachintegral

Ein Volumenintegral ist eine spezielle Art von Integral, das oft im Maschinenbau
auftritt. Es ist eine Erweiterung des Konzepts des Flächenintegrals auf
dreidimensionale Räume. Insbesondere bei der Berechnung von Massen,
Schwerpunkten oder Trägheitsmomenten von Körpern werden Volumenintegrale
gebraucht. In diesem Kapitel führen wir das Volumenintegral ein und zeigen die
Berechnung in kartesischen Koordinaten durch ein Dreifachintegral. Im nächsten
Kapitel werden wir dann die Anwendungen des Volumenintegrals kennenlernen.

## Lernziele

```{admonition} Lernziele
:class: goals
Sie können ein **Volumenintegral** als **Dreifachintegral** (in kartesischen Koordinaten) berechnen.
```

## Was ist ein Volumenintegral?

Ein Volumenintegral ist ein Integral, bei dem das Integrationsgebiet
dreidimensional ist. Es wird also eine Funktion $f:\mathbb{R}^3\to\mathbb{R}$
über ein Volumen integriert. Die mathematische Notation für das Volumenintegral
ist

$$\iiint_{V} f(x,y,z) \, dV.$$

Konkret wird das Volumenintegral berechnet, indem ein Koordinatensystem
eingeführt wird, das Integrationsgebiet $V$ durch Randfunktionen beschrieben
wird und das Volumenelement $dV$ durch Linienelemente ausgedrückt wird. Im
nächsten Abschnitt schauen wir uns das für kartesische Koordinaten an.

## Berechnung durch Dreifachintegral

Wir verwenden ein kartesisches Koordinatensystem mit den drei Koordinatenachsen
$e_x$, $e_y$ und $e_z$. Dann versuchen wir, die Ränder des Integrationsgebietes
$V$ durch Funktionen zu beschreiben.

```{figure} pics/part11_skizze_dreifachintegral.svg
---
width: 600px
name: part11_skizze_dreifachintegral
---
Skizze: Integrationsgebiet des Volumenintegrals 
```

### Integrationsgebiet durch Funktionen beschreiben

Der Deckel und der Boden des  Volumens $V$ sind Funktionen, die von $x$ und $y$
abhängen. In der Skizze sind sie blau eingefärbt. Wir bezeichnen sie
folgendermaßen:

* $F_{o}(x,y)$: obere Fläche
* $F_{u}(x,y)$: untere Fläche

Als nächstes beschreiben wir das Gebiet $A$, aus dem die Werte für $(x,y)$
kommen dürfen. In der Skizze ist das das rot eingefärbte Gebiet in der xy-Ebene.
Um das Gebiet zu beschreiben, werden die obere und die untere Grenzfunktion
beschrieben:

* $g_{o}(x)$: obere Grenzfunktion und
* $g_{u}(x)$: untere Grenzfunktion.

Die x-Werte wiederum, die in die beiden Grenzfunktionen eingesetzt werden
dürfen, stammen aus dem Intervall $[a,b]$.

Das Volumenintegral kann jetzt durch drei Integrationen berechnet werden:

$$\iiint_{V}f(x,y,z)\, dV =
\int_{x=a}^{x=b} \left(
    \int_{y=g_{u}(x)}^{y=g_{o}(x)} \left(
        \int_{z = F_{u}(x,y)}^{z = F_{o}(x,y)} f(x,y,z)\, dz \right) \, dy
    \right) \, dx.$$

### Drei einzelne Integrationen durchführen

Jetzt werden die drei Integrale einzeln berechnet. Zunächst wird das innere
Integral

$$I_{1}(x,y) = \int_{z = F_{u}(x,y)}^{z = F_{o}(x,y)} f(x,y,z)\, dz$$

durch Integration nach $z$ ausgrechnet. Das Ergebnis dieser Integration ist eine
Funktion, die noch von $x$ und $y$ abhängt. Wir nennen diese $I_{1}(x,y)$. Sie
wird in das mittlere Integral eingesetzt und dann wird nach $y$ integriert.

$$I_{2}(x) =  \int_{y=g_{u}(x)}^{y=g_{o}(x)} I_{1}(x,y) \, dy.$$

Das Ergebnis ist eine Funktion, die nur noch von $x$ abhängt, und die wir $I_3$
nennen. Dann wird auch noch das äußere Integral berechnet,

$$V = \int_{x=a}^{x=b} I_3(x) \, dx,$$

so dass am Ende das Ergebnis eine Zahl ist.

In dem folgenden Video wird der Unterschied Doppelintegral zu Dreifachintegral
erklärt.

```{dropdown} Video zu "Doppelintegral vs. Dreifachintegral" von Daniel Jung
<iframe width="560" height="315" src="https://www.youtube.com/embed/Ec6xuobv8Mk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture;
web-share" allowfullscreen></iframe>
```

## Beispiel Berechnung Dreifachintegral

Wir berechnen das folgende Dreifachintegral

$$\iiint_V (2x + 3y - z) \, dV$$

wobei das Integrationsgebiet $V$ durch folgende Bedingungen beschrieben wird:

* $0 \leq x \leq 2$, d.h. $x$ variiert zwischen 0 und 2,
* $0 \leq y \leq x$, d.h. für jeden $x$-Wert ist $y$ zwischen 0 und $x$
  begrenzt,
* $0 \leq z \leq x + y$, d.h. für jedes Paar $(x,y)$ ist $z$ zwischen 0 und $x +
  y$ begrenzt.

Damit erhalten wir in kartesischen Koordinaten

$$\iiint_V (2x + 3y - z) \, dV = \int_{x=0}^{x=2} \int_{y=0}^{y=x}
\int_{z=0}^{z=x+y} (2x + 3y - z) \, dz \, dy \, dx.$$

**Schritt 1**: Inneres Integral (Integration nach $z$)

$$I_1(x,y) = \int_{z=0}^{z=x+y} (2x + 3y - z) \, dz$$

Da $2x + 3y$ konstant bezüglich $z$ ist, gilt

\begin{align*}
I_1(x,y) &= \int_{z=0}^{z=x+y} 2x \, dz + \int_{z=0}^{z=x+y} 3y \, dz -
    \int_{z=0}^{z=x+y} z \, dz\\
&= 2x \cdot \big[z\big]_{z=0}^{z=x+y} + 3y \cdot \big[z\big]_{z=0}^{z=x+y} -
    \left[\frac{z^2}{2}\right]_{z=0}^{z=x+y}\\
&= 2x(x+y) + 3y(x+y) - \frac{(x+y)^2}{2}\\
&= (x+y)(2x + 3y) - \frac{(x+y)^2}{2}\\
&= (x+y)\left(2x + 3y - \frac{x+y}{2}\right)\\
&= (x+y)\left(\frac{4x + 6y - x - y}{2}\right)\\
&= (x+y)\left(\frac{3x + 5y}{2}\right)\\
\end{align*}

und mit Ausmultiplizieren erhalten wir

$$I_1(x,y) = \frac{3x^2 + 8xy + 5y^2}{2}.$$

**Schritt 2**: Mittleres Integral (Integration nach $y$)

Wir ziehen den konstanten Faktor $\frac{1}{2}$ vor das Integral und integrieren
nach $y$:

\begin{align*}
I_2(x) &= \frac{1}{2} \int_{y=0}^{y=x} 3x^2 + 8xy + 5y^2 \, dy\\
&= \frac{1}{2} \left[3x^2y + 8x\frac{y^2}{2} + 5\frac{y^3}{3}\right]_{y=0}^{y=x}\\
&= \frac{1}{2} \left[3x^2y + 4xy^2 + \frac{5y^3}{3}\right]_{y=0}^{y=x}\\
&= \frac{1}{2} \left(3x^3 + 4x^3 + \frac{5x^3}{3}\right)\\
&= \frac{1}{2} \left(7x^3 + \frac{5x^3}{3}\right)\\
&= \frac{1}{2} \left(\frac{21x^3 + 5x^3}{3}\right)\\
&= \frac{1}{2} \cdot \frac{26x^3}{3} = \frac{26x^3}{6} = \frac{13x^3}{3},\\
\end{align*}

also

$$I_2(x) = \frac{13x^3}{3}.$$

**Schritt 3**: Äußeres Integral (Integration nach $x$)

\begin{align*}
I_3 &= \int_{x=0}^{x=2} \frac{13x^3}{3} \, dx\\
&=\frac{13}{3} \int_{x=0}^{x=2} x^3 \, dx\\
&= \frac{13}{3} \left[\frac{x^4}{4}\right]_{x=0}^{x=2} = \frac{52}{3}.
\end{align*}

Damit lautet das Endergebnis

$$\iiint_V (2x + 3y - z) \, dV = \frac{52}{3}.$$

In den folgenden Videos werden weitere Beispiele vorgerechnet.

```{dropdown} Video zu "Mehrdimensionale Integrale: Dreifachintegrale in kartesischen Koordinaten" von Holger Schmidt
<iframe width="560" height="315" src="https://www.youtube.com/embed/HZRAUqbVKeQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

```{dropdown} Video zu "Übungsblatt 9, Aufgabe A1" von Dr.-Ing. Denis Busch
<iframe width="560" height="315" src="https://www.youtube.com/embed/mY6Z8TQe2iQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

Die Berechnung des Volumens eines Quaders mittels eines Dreifachintegrals ist
ein sehr einfaches Beispiel, insbesondere weil die Funktion, über die integriert
wird, konstant ist. Im nächsten Kapitel werden wir weitere Anwendungen des
Dreifachintegrals kennenlernen.
