---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  main_language: python
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
---

# 1.3 Extremwerte

Beschreibt eine Funktion einen technischen Prozess oder beispielsweise
temperaturabhängige Materialkennwerte, so ist die Information sehr interessant,
ob in einem bestimmten Intervall minimale oder maximale Werte angenommen werden.
In diesem Kapitel beschäftigen wir uns daher damit, die Minima oder Maxima einer
Funktion zu bestimmen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie wissen, was das Minimum oder Maximum einer Funktion ist.
* Sie können Minima oder Maxima von 2x differenzierbaren Funktionen berechnen.
```

## Minimum und Maximum einer Funktion -- was ist das?

Die Funktion $f(x) = x^2 -6x + 11$ hat den folgenden Funktionsgraphen.

```{figure} pics/chapter01_sec03_fig01.png
---
width: 75%
name: fig01_parabel
---
Der kleinste Funktionswert (= Minimum) dieser Parabel $f(x) = x^2 -6x + 11$ ist
2. Er befindet sich an der Stelle $x = 3$. Der dazugehörige Punkt $(3 | 2)$ ist
ein Tiefpunkt.
```

Der kleinste Funktionswert $f(x)$, der vorkommt, ist 2. Es gilt also

$$f(x) \geq 2 \quad \text{ für alle } x\in\mathbb{R}.$$

Einen solchen kleinsten Wert nennen wir **Minimum**. Mathematisch wird das
folgendermaßen notiert:

$$\min_{x\in\mathbb{R}} f(x) = 2.$$

Um zu verdeutlichen, dass in diesem Beispiel die 2 sogar für alle reellen Zahlen
$x\in\mathbb{R}$ der kleinste Funktionswert ist, sagt man oft auch **globales
Minimum**. Es könnte aber auch sein, dass dieser Funktionswert nur in einem
bestimmten Bereich der kleinste Funktionswert ist. Dazu werden wir noch ein
Beispiel betrachten. Wir halten noch fest, dass der Punkt $(3 | 2)$
**Tiefpunkt** genannt wird.

Als zweites Beispiel betrachten wir die Funktion $f(x) = \frac{1}{2}x^3 -3x^2 +
\frac{9}{2}x+2$. Diese Funktion hat kein globales Minimum, denn es werden
Funktionswerte bis $-\infty$ angenommen. Aber die Funktion hat das lokale
Minimum 2 an der Stelle $x = 3$.

```{figure} pics/chapter01_sec03_fig02.png
---
width: 75%
name: fig02_kubisches_polynom
---
Der kleinste Funktionswert (= Minimum) der Funktion $f(x) = \frac{1}{2}x^3 -3x^2 +
\frac{9}{2}x+2$ im Intervall $[2,4]$ ist 2. Da sich das Minimum nur auf dieses
Intervall bezieht und nicht auf die ganze Definitionsmenge, ist es ein lokales
Minimum. Es befindet sich an der Stelle $x = 3$. Der dazugehörige Punkt $(3 |
2)$ ist ein lokaler Tiefpunkt.
```

```{admonition} Was ist ... ein Minimum einer Funktion?
:class: note
Wir betrachten eine reellwertige Funktion $f$ mit der Definitionsmenge
$D\subseteq\mathbb{R}$, also $f: D \rightarrow \mathbb{R}$. Die Funktion $f$ hat
an der Stelle $x_0$ ein **lokales Minimum**, wenn es ein Intervall $I = (a,b)$
gibt, das $x_0$ enthält, und gleichzeitig die Bedingung

$$f(x_0) \leq f(x)$$

für alle  $x\in (a,b)$ erfüllt ist. Gilt sogar 

$$f(x_0) \leq f(x)$$

für alle $x\in D$, dann hat die Funktion $f$ an der Stelle $x_0$ ein
**globales Minimum**.
```

Für das Maximum gilt eine analoge Definition, bei der nur das
Ungleichheitszeichen anders ist.

```{admonition} Was ist ... ein Maximum einer Funktion?
:class: note
Wir betrachten eine reellwertige Funktion $f$ mit der Definitionsmenge
$D\subseteq\mathbb{R}$, also $f: D \rightarrow \mathbb{R}$. Die Funktion $f$ hat
an der Stelle $x_0$ ein **lokales Maximum**, wenn es ein Intervall $I = (a,b)$
gibt, das $x_0$ enthält, und gleichzeitig die Bedingung

$$f(x_0) \geq f(x)$$

für alle  $x\in (a,b)$ erfüllt ist. Gilt sogar 

$$f(x_0) \geq f(x)$$

für alle $x\in D$, dann hat die Funktion $f$ an der Stelle $x_0$ ein
**globales Maximum**.
```

## Wie finden wir Hoch- und Tiefpunkte?

Wir betrachten weiterhin das obige Beispiel, die Funktion $f(x) = \frac{1}{2}x^3
-3x^2 + \frac{9}{2}x+2$. Zeichen wir veschiedene Tangenten ein, so stellen wir
fest, dass die Steigung der Tangente im lokalen Hochpunkt (1|4) und im lokalen
Tiefpunkt (3|2) jeweils Null ist. Für die Stellen $x_{\text{HP}} = 1$ und
$x_{\text{TP}} = 3$ gilt also

$$f'(x_{\text{HP}}) = f'(1) = 0$$

bzw.

$$f'(x_{\text{TP}}) = f'(3) = 0.$$

Tatsächlich gilt diese Aussage für alle differenzierbaren Funktionen. Wenn die
differenzierbare Funktion $f$ an der Stelle $x_0$ ein Minimum oder ein Maximum
hat, dann gilt

$$f'(x_0) = 0.$$

Die Umkehrung dieser Aussage ist allerdings nicht wahr. Wenn die 1. Ableitung
einer differenzierbaren Funktion an der Stelle $x_0$ gleich Null ist, muss sie
dort nicht ein Maximum oder ein Minimum haben.

Die Funktion $f(x)=x^3$ hat die 1. Ableitung $f'(x)=3x^2$. An der Stelle $x_0=0$
ist die 1. Ableitung Null, aber $f$ hat kein Minimum und kein Maximum, auch
nicht an dieser Stelle. Der Punkt $(0,0)$ wird Sattelpunkt genannt.

```{figure} pics/chapter01_sec03_fig03.svg
---
width: 75%
name: chapter01_sec03_fig03
---
Die Funktion $f(x)=x^3$ hat an der Stelle $x_0 = 0$ kein Minimum und auch kein Maximum, obwohl die Steigung der Tangente an dieser Stelle Null ist, also $f'(x)=3x^2 \Rightarrow f'(0)=0$ gilt.
```

Diese Bedingung ist *notwendig*, damit überhaupt ein Maximum oder Minimum
vorliegen kann. Leider reicht diese Bedingung noch nicht aus. Alle Nullstellen
der 1. Ableitung sind *mögliche* Extrema, es könnten aber auch Sattelpunkte
sein.

Daher müssen wir noch zusätzliche Bedingungen überprüfen, bevor wir entscheiden
können, ob ein Minimum oder Maximum vorliegt. Die möglichen Extremwerte müssen
noch zusätzlich mit der 2. Ableitung geprüft werden:

* Die Funktion $f$ hat an der Stelle $x_0$ ein **Maximum**, wenn
  * die 1. Ableitung an dieser Stelle Null ist, d.h. $f'(x_0) = 0$ und
  * die 2. Ableitung an dieser Stelle **negativ** ist, d.h. $f''(x_0) < 0$.
* Die Funktion $f$ hat an der Stelle $x_0$ ein **Minimum**, wenn
  * die 1. Ableitung an dieser Stelle Null ist, d.h. $f'(x_0) = 0$ und
  * die 2. Ableitung an dieser Stelle **positiv** ist, d.h. $f''(x_0) > 0$.

Diese beiden Bedingungen nennt man dann **hinreichende** Bedingungen.

Achtung: Wenn allerdings die zweite Ableitung Null ist, also $f''(x_0) = 0$,
kann man keine Entscheidung treffen und muss weitere Bedingungen überprüfen.
Alternativ gibt es noch das sogenannte **Vorzeichenwechselkriterium**, das hier
nicht weiter ausgeführt wird.

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir uns mit den Begriffen Minimum und Maximum einer
Funktion beschäftigt. Ist eine Funktion differenzierbar, so sind die Nullstellen
der 1. Ableitung Kandidaten für Extrema. Ob tatsächlich ein Extremum (Minimum
oder Maximum) vorliegt, muss einzeln geprüft werden. Für diese Prüfung gibt es
mehrere Kriterien, in dieser Vorlesung verwenden wir den Test mit der 2.
Ableitung. Im nächsten Kapitel beschäftigen wir uns mit Extrema mit
Zusatzbedingung.
