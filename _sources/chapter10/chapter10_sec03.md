# 7.3 Dreifachintegral

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

## Lernziele

```{admonition} Lernziele
:class: tip
* Sie können ein **Dreifachintegral** (in kartesischen Koordinaten) berechnen.
* Sie können mit einem Dreifachintegral das Volumen $V$ eines Körpers berechnen

$$V=\iiint_{V}1\,dV.$$

* Sie können mit drei Dreifachintegralen den Schwerpunkt $S(x_S,y_S,z_S)$ eines Körpers berechnen:

$$x_S = \frac{1}{V}\iiint_{V}x\, dV, \qquad y_S = \frac{1}{V}\iiint_{V}y\, dV \qquad \text{und} \quad z_S = \frac{1}{V}\iiint_{V}z\, dV.$$
```

## Dreifachintegral

Ein Dreifachintegral wird durch drei Integrationen berechnet:

$$\iiint_{V}f(x,y,z)\, dV = \int_{x=a}^{x=b} \int_{y=g_{u}(x)}^{y=g_{o}(x)} \int_{z = F_{u}(x,y)}^{z = F_{o}(x,y)} f(x,y,z)\, dz \, dy \, dx.$$

Dabei bedeuten die Bezeichnungen:

* $F_{o}(x,y)$: obere Fläche 
* $F_{u}(x,y)$: untere Fläche
* $g_{o}(x)$: obere Grenzkurve 
* $g_{u}(x)$: untere Grenzkurve

wie man auch der folgenden Abbildung entnehmen kann:

```{figure} pics/part10_skizze_dreifachintegral.svg
---
width: 600px
name: part10_skizze_dreifachintegral
---
Skizze Dreifachintegral
```

In dem folgenden Video wird der Unterschied Doppelintegral zu Dreifachintegral erklärt.

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/Ec6xuobv8Mk
```

Hier wird ein Dreifachintegral ausgerechnet, indem die drei Integrationen nacheinander durchgeführt werden:

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/HZRAUqbVKeQ
```
