# 10.2 Doppelintegral in Polarkoordinaten

Im letzten Kapitel haben wir Punkte durch kartesische Koordinaten und durch
Polarkoordinaten beschrieben. In diesem Kapitel wird das Flächenintegral in zwei
Integrale mit Polarkoordinaten umgeschrieben und dadurch berechnet.

## Lernziele

```{admonition} Lernziele
:class: goals
Sie können ein Doppelintegral in kartesischen Koordinaten in ein Doppelintegral in Polarkoordinaten umrechnen, d.h.

$$\iint_{A}f(x,y)\, dA = \int_{\varphi=\alpha}^{\varphi=\beta}
\left(\int_{r=r_\text{innen}(\varphi)}^{r=r_\text{außen}(\varphi)}f(r, \varphi) \cdot r\, dr \right) \, d\varphi.$$

Die Integration erfolgt dabei in zwei Schritten, zuerst kommt die innere Integration über $r$, danach die äußere Integration über $\varphi$.
```

## Doppelintegral in Polarkoordinaten

Doppelintegrale in Polarkoordinaten sind besonders nützlich, wenn das
Integrationsgebiet kreisförmig oder rotationssymmetrisch ist. Solche Formen
kommen im Maschinenbau häufig vor, beispielsweise bei der Berechnung von
Trägheitsmomenten rotierender Scheiben oder Schwerpunkten kreisförmiger
Bauteile.

Um ein Doppelintegral in kartesischen Koordinaten zu berechnen, wird versucht,
die Ränder des Integrationsgebietes mit dem folgenden Schema zu beschreiben. Für
x wird ein Intervall $[a,b]$ genommen und für y wird der obere Rand des
Integrationsgebietes durch eine obere Funktion $f_{\text{oben}}(x)$ und der
untere Rand durch eine untere Funktion $f_{\text{unten}}(x)$ beschrieben.

Soll das Doppelintegral in Polarkoordinaten ausgedrückt werden, wird für den
Winkel $\varphi$ ein Intervall von Winkeln $[\alpha, \beta]$ genommen und für
$r$ wird der äußere Rand des Integrationsgebietes durch die äußere Funktion
$f_{\text{außen}}(\varphi)$ und der innere Rand durch eine innere Funktion
$f_{\text{innen}}(\varphi)$ beschrieben.

Der entscheidende Unterschied liegt im Flächenelement. Bei kartesischen
Koordinaten wird das Flächenelement $dA$ zum Produkt aus den Linienelementen
$dy$ und $dx$, also $dA = dy \, dx$.

Bei Polarkoordinaten entsteht durch die Koordinatentransformation ein
zusätzlicher Faktor $r$. Dies lässt sich geometrisch folgendermaßen verstehen.

```{figure} pics/flaechenelement_polarkoordinaten.svg
---
width: 30%
name: flaechenelement_polarkoordinaten
---
Flächenelement in Polarkoordinaten: Das kleine Flächenstück hat die Seitenlängen $dr$ und $r \, d\varphi$ (Quelle: Von Michael Lenz - Eigenes Werk, CC0, https://commons.wikimedia.org/w/index.php?curid=65154297)
```

Ein kleines Flächenelement in Polarkoordinaten ist näherungsweise ein Rechteck
mit:

- Seitenlänge in radialer Richtung: $dr$
- Seitenlänge in tangentialer Richtung: $r \, d\varphi$ (Bogenlänge)

Daher ergibt sich das Flächenelement in Polarkoordinaten als:

$$dA = r \, dr \, d\varphi.$$

## Transformation des Integrals

Die vollständige Transformation eines Doppelintegrals von kartesischen zu Polarkoordinaten erfordert:

1. **Koordinatentransformation**: $x = r\cos\varphi$, $y = r\sin\varphi$
2. **Funktionssubstitution**: $f(x,y) \rightarrow f(r\cos\varphi, r\sin\varphi)$
3. **Flächenelement**: $dA = dx \, dy \rightarrow r \, dr \, d\varphi$
4. **Integrationsgrenzen**: Anpassung an das neue Koordinatensystem

Damit erhalten wir das Doppelintegral in Polarkoordinaten als

$$\iint_{A}f(x,y)\, dA = \int_{\varphi=\alpha}^{\varphi=\beta}
\left( \int_{r=r_\text{innen}(\varphi)}^{r=r_\text{außen}(\varphi)}f(r, \varphi) \cdot r\, dr \right) \, d\varphi.$$

Zuerst wird über $r$ integriert (inneres Integral), dann über $\varphi$ (äußeres
Integral). Diese Reihenfolge entspricht dem Aufbau des Integrationsgebiets in
Polarkoordinaten.

## Beispiel: Flächeninhalt eines Halbkreises

Wir berechnen den Flächeninhalt eines Halbkreises mit Radius $R$. Das
Integrationsgebiet ist der Halbkreis mit $0 \leq r \leq R$ und $0 \leq \varphi
\leq \pi$. Die Funktion für die Flächenberechnung ist

$$f(x,y) = 1.$$

Damit erhalten wir für das transformierte Integral in Polarkoordinaten

$$A = \iint_{A} 1 \, dA = \int_{\varphi=0}^{\varphi=\pi}
\left(\int_{r=0}^{r=R} 1 \cdot r \, dr\right) \, d\varphi.$$

Wir berechnen zuerst das innere Integral (über $r$):

$$\int_{r=0}^{r=R} r \, dr = \left[\frac{1}{2}r^2\right]_0^R = \frac{1}{2}R^2.$$

Danach berechnen wir das äußere Integral (über $\varphi$)

$$A = \int_{\varphi=0}^{\varphi=\pi} \frac{1}{2}R^2 \, d\varphi =
\frac{1}{2}R^2 \cdot \pi = \frac{\pi}{2}R^2$$

und erhalten somit das aus der Geometrie bekannte Ergebnis $A = \frac{\pi}{2}R^2$.

In dem folgenden Video wird sehr ausführlich der Flächeninhalt eines Halbkreises
sowohl mit einem Doppelintegral in kartesischen Koordinaten als auch einem
Doppelintegral in Polarkoordinaten erklärt. Lassen Sie sich nicht verwirren, in
dem Video wird das Doppelintegral Bereichsintegral genannt.

```{dropdown} Video zu "Bereichsintegrale / Doppelintegrale | Polarkoordinaten" von LernKompass - Mathe einfach erklärt
<iframe width="560" height="315" src="https://www.youtube.com/embed/CghdXlwr5aY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture;
web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

Im nächsten Kapitel kehren wir zu den kartesischen Koordinaten zurück, gehen
dafür aber eine Dimension höher und berechnen Dreifachintegrale.
