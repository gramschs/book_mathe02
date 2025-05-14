# 7.2 Vektorwertige Funktionen

## Lernziele

```{admonition} Lernziel
:class: goals
Sie wissen, was eine **vektorwertige** Funktion bzw. ein **Vektorfeld** ist.
```

## Begrifflichkeiten

Bis jetzt war es so, dass Funktionen von einer oder mehreren Variablen abhängen,
aber der Funktionswert war bisher immer eine reelle Zahl, also ein Skalar. Daher
nennt man solche Funktionen **skalarwertig**. So wie wir beim Definitionsgebiet
von einem eindimensionalen Definitionsgebiet $x\in \mathbb{R}$ der reellen
Zahlen zu Definitionsgebieten mit mehreren unabhängigen Variablen, also Vektoren
$\vec{x}\in\mathbb{R}^n$ übergegangen sind, können wir das mit den
Funktionswerten auch machen. Sind die Funktionswerte einer Funktion Vektoren, so
nennen wir die Funktion **vektorwertig**.

```{admonition} Was ist ... eine vektorwertige Funktion?
:class: note
Eine vektorwertige Funktion ist eine Funktion, die Vektoren als Wertemenge bzw.
Funktionswerte hat. Jedem Punkt $\vec{x}\in\mathbb{R}^m$ wird eindeutig ein
Vektor $\mathbb{R}^n$ zugeordnet, in mathematischer Notation

$$f:\mathbb{R}^m \rightarrow \mathbb{R}^n.$$ Übrigens, in der Physik wird eine
vektorwertige Funktion auch oft **Vektorfeld** genannt.
```

```{dropdown} Video zu "Vektorwertige Funktionen" von Mathematische Methoden
<iframe width="560" height="315" src="https://www.youtube.com/embed/KUSljbPOK78"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Beispiel Windgeschwindigkeiten

Ein Beispiel aus dem Alltag ist die Wetterkarte mit den prognostizierten
Durchschnittstemperaturen für den morgigen Tag. Zu jeder Position spezifiziert
durch den Breiten- und den Längengrad gibt es eine Temperatur. Die Temperatur
ist eine sogenannte skalare Größe, denn sie wird durch eine einzelne Zahl
dargestellt. Gerade bei Unwetterwarnungen sind jedoch auch Darstellungen des
Windfeldes üblich. Zu jeder Position mit Längen- und Breitengrad wird eine
Windrichtung angegeben, also eine vektorielle Größe. In den Wetterkarten wird
dazu häufig ein Pfeil eingezeichnet ähnlich zu der folgenden Abbildung.

```{figure} pics/fig08_vektorfeld.svg
---
width: 300px
name: fig08_vektorfeld
---
Visualisierung eines Vektorfeldes ([Quelle:](https://commons.wikimedia.org/wiki/File:VectorField.svg) "A portion of the vector field (sin y, sin x)" von Jim.belk. Lizenz: gemeinfrei)
```
