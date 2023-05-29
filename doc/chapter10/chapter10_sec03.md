# 10.3 Dreifachintegral

Ein Volumenintegral ist eine spezielle Art von Integral, das oft im Maschinenbau
auftritt. Es ist eine Erweiterung des Konzepts des Flächenintegrals auf
dreidimensionale Räume. Insbesondere bei der Berechnung von Massen,
Schwerpunkten oder Trägheitsmomenten von Körpern werden Volumenintegrale
gebraucht. In diesem Kapitel führen wir das Volumenintegral ein und zeigen die
Berechnung in kartesischen Koordinaten durch ein Dreifachintegral. In nächsten
Kapitel werden wir dann die Anwendungen des Volumenintegrals kennenlernen.

## Lernziele

```{admonition} Lernziele
:class: important
Sie können ein **Volumenintegral** als **Dreifachintegral** (in kartesischen Koordinaten) berechnen.
```

## Volumenintegral

Ein Volumenintegral ist ein Integral, bei dem das Integrationsgebiet
dreidimensional ist. Es wird also eine Funktion $f:\mathbb{R}^3\to\mathbb{R}$
über ein Volumen integriert. Die mathematische Notation für das Volumenintegral
ist

$$\iiint_{V} f(x,y,z) \, dV.$$

Konkret wird das Volumenintegral berechnet, indem ein Koordinatensystem eingeführt wird, das Integrationsgebiet $V$ durch Randfunktionen beschrieben wird und das Volumenelement $dV$ durch Linienelemente ausgedrückt wird. Im nächsten Abschnitt schauen wir uns das für kartesische Koordinaten an.

## Berechnung durch Dreifachintegral

Wir verwenden ein kartesisches Koordinatensystem mit den drei Koordinatenachsen $e_x$, $e_y$ und $e_z$. Dann versuchen wir, die Ränder des Integrationsgebietes $V$ durch Funktionen zu beschreiben.

```{figure} pics/part10_skizze_dreifachintegral.svg
---
width: 600px
name: part10_skizze_dreifachintegral
---
Skizze: Integrationsgebiet des Volumenintegrals 
```

**Integrationsgebiet durch Funktionen beschreiben**
   
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


**Drei einzelne Integrationen durchführen**

Jetzt werden die drei Integrale einzeln berechnet. Zunächst wird das innere
Integral

$$M(x,y) = \int_{z = F_{u}(x,y)}^{z = F_{o}(x,y)} f(x,y,z)\, dz$$

durch Integration nach $z$ ausgrechnet. Das Ergebnis dieser Integration ist eine
Funktion, die noch von $x$ und $y$ abhängt. Wir nennen diese $M(x,y)$. Sie wird
in das mittlere Integral eingesetzt und dann wird nach $y$ integriert.

$$I(x) =  \int_{y=g_{u}(x)}^{y=g_{o}(x)} M(x,y) \, dy.$$

Das Ergebnis ist eine Funktion, die nur noch von $x$ abhängt und diw wir $I$
nennen. Dann wird auch noch das äußere Integral berechnet,

$$V = \int_{x=a}^{x=b} I(X) \, dx,$$

so dass am Ende das Ergebnis eine Zahl ist.


In dem folgenden Video wird der Unterschied Doppelintegral zu Dreifachintegral
erklärt.

```{dropdown} Video zu "Doppelintegral vs. Dreifachintegral" von Daniel Jung
<iframe width="560" height="315" src="https://www.youtube.com/embed/Ec6xuobv8Mk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

Hier wird ein Dreifachintegral ausgerechnet, indem die drei Integrationen
nacheinander durchgeführt werden:

```{dropdown} Video zu "Mehrdimensionale Integrale: Dreifachintegrale in kartesischen Koordinaten" von Holger Schmidt
<iframe width="560" height="315" src="https://www.youtube.com/embed/HZRAUqbVKeQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

Ein weiteres Beispiel finden Sie hier.

```{dropdown} Video zu "Übungsblatt 9, Aufgabe A1" von Dr.-Ing. Denis Busch
<iframe width="560" height="315" src="https://www.youtube.com/embed/mY6Z8TQe2iQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
