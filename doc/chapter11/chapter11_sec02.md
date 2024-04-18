# 11.2 Doppelintegral in Polarkoordinaten

Im letzten Kapitel haben wir Punkte durch kartesische Koordinaten und durch
Polarkoordinaten beschrieben. In diesem Kapitel wird das Flächenintegral in zwei
Integrale mit Polarkoordinaten umgeschrieben und dadurch berechnet.

## Lernziele

```{admonition} Lernziele
:class: goals
Sie können ein Doppelintegral in kartesischen Koordinaten in ein Doppelintegral in Polarkoordinaten umrechnen, d.h.

$$\iint_{A}f(x,y)\, dA = \int_{\varphi=\alpha}^{\varphi=\beta}
\left( \int_{r=r_\text{innen}(\varphi)}^{r=r_\text{außen}(\varphi)}f(r, \varphi) \cdot r\, dr \right) \, d\varphi.$$

Die Integration erfolgt dabei in zwei Schritten, zuerst kommt die innere Integration über $r$, danach die äußere Integration über $\varphi$.
```

## Doppelintegral in Polarkoordinaten

Um ein Doppelintegral in kartesischen Koordinaten zu berechnen, werden als
versucht, die Ränder des Integrationsgebietes mit dem folgenden Schema zu
beschreiben. Für x wird ein Intervall $[a,b]$ genommen und für y wird der obere
Rand des Integrationsgebietes durch eine obere Funktion $f_{\text{oben}}(x)$ und
der untere Rand durch eine untere Funktion $f_{\text{unten}}(x)$ beschrieben.
Soll das Doppelintegral in Polarkoordinaten ausgedrückt werden, wird für den
Winkel $\varphi$ ein Intervall von Winkeln $[\alpha, \beta]$ genommen und für
$r$ wird der äußere Rand des Integrationsgebietes durch die äußere Funktion
$f_{\text{außen}}(\varphi)$ und der innere Rand durch eine innere Funktion
$f_{\text{innen}}(\varphi)$ beschrieben. Es gibt nur einen Unterschied. Bei
kartesischen Koordinaten wird dann das Flächenelement $dA$ zum Produkt aus den
Linienelementen $dy$ und $dx$, also

$$dA = dy \; dx.$$

Bei Polarkoordinaten jedoch muss das Flächenelement $dA$ noch mit $r$
multipliziert werden, also

$$dA = r \, dr \, d\varphi.$$

Damit erhalten wir das Doppelintegral in Polarkoordinaten als

$$\iint_{A}f(x,y)\, dA = \int_{\varphi=\alpha}^{\varphi=\beta}
\left( \int_{r=r_\text{innen}(\varphi)}^{r=r_\text{außen}(\varphi)}f(r, \varphi) \cdot r\, dr \right) \, d\varphi.$$

In dem folgenden Video wird sehr ausführlich der Flächeninhalt eines Halbkreises
sowohl mit einem Doppelintegral in kartesischen Koordinaten als auch einem
Doppelintegral in Polarkoordinaten erklärt. Nicht verwirren lassen, in dem Video
wird das Doppelintegral Bereichsintegral genannt.


```{dropdown} Video zu "Bereichsintegrale / Doppelintegrale | Polarkoordinaten" von LernKompass - Mathe einfach erklärt
<iframe width="560" height="315" src="https://www.youtube.com/embed/CghdXlwr5aY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
