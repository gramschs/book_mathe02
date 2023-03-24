# Reihen und Potenzreihen

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

In diesem Kapitel lernen Sie die grundlegenden Begriffe zu Reihen kennen. Neben einigen Beispielen vor allem zu geometrischen und harmonischen Reihen widmen wir uns der Konvergenz von Reihen.

```{admonition} Lernziele
:class: tip
* Sie können den Fachbegriff **Reihe** erklären.
* Sie können den Fachbegriff **Partialsumme** einer Reihe erklären.
* Sie kennen als Beispiel für Reihen die
    * **arithmetische Reihe**,
    * **geometrische Reihe** und
    * **harmonische Reihe**.
* Sie können den Fachbegriff **alternierende Reihe** erklären.
* Sie können den Fachbegriff **Konvergenz** einer Reihe erklären.
* Sie können mit den **Konvergenzkriterien** überprüfen, ob eine Reihe konvergiert, indem Sie die folgenden Kriterien anwenden können:
    * **Leibniz-Kriterium für alternierende Reihen**, 
    * **Quotientenkriterium** oder
    * **Wurzelkriterium**.
* Sie können den Fachbegriff **absolut konvergente Reihe** erklären.
```


## Reihen werden aus Folgen gebildet

In dem folgenden Video werden sowohl die grundlegenden Begriffe zum Thema Reihen erklärt als auch das Thema Konvergenz und Divergenz von Reihen erläutert.


```{admonition} Video
:class: seealso
https://www.youtube.com/embed/1vQ67chDVbU
```

## Bekannte Beispiele sind die geometrische und die harmonische Reihe

In den folgenden beiden Videos werden zunächst die geometrische Reihe und dann die harmonische Reihe erklärt.

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/y_9ccgrwTZo
```

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/n2ELwRkgKhc
```

## Konvergiert die Reihe oder divergiert sie?

In dem ersten Video wird zunächst auf die Konvergenz von Reihen eingegangen. Danach werden die Kriterien zur Bestimmung der Konvergenz
* Leibniz-Kriterium,
* Wurzelkriterium und
* Quotientenkriterium 

vorgestellt.

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/aGnAseEnfG0
```

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/_8_Q6g8-QxA
```

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/G1GSAFrd6mE
```

## Zusatzmaterial

Wer es musikalisch mag, kann auch gerne sich den Mathe-Song von DorFuchs zur Konvergenz der geometrischen Reihe anhören:

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/2TCDiK7GpNM
```

Hier wird ein Beispiel zur Konvergenz von Reihen mit dem Quotientenkriterium erklärt:

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/p3BPRuk0Wwk
```

## Potenzreihen 

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

Polynome haben schöne Eigenschaften, vor allem sind sie einfach abzuleiten oder zu integrieren. In der Praxis ist es daher oft sinnvoll, "schwierige" Funktionen durch Polynome zu ersetzen, auch wenn man dafür Fehler macht.

Diese Vorgehensweise wird **Approximation** genannt, zu deutsch Annäherung. Für Zahlen haben Sie dies schon kennengelernt. Wenn Sie beispielsweise den Flächeninhalt $A$ eines Kreises mit Radius $r = 3 \,\text{m}$ berechnen wollen, so gilt $A = \pi \cdot r^2 = 9\pi$. Da aber $\pi$ unendlich viele Nachkommastellen hat, legen Sie fest, wie genau die Annäherung an den wahren Flächeninhalt sein soll, indem Sie die Anzahl der Nachkommastellen festlegen. Reichen Ihnen beispielsweise 2 Nachkommastellen, also $\pi \approx 3.14$, so erhalten Sie $A = 28.27 \,\text{m}^2$.

In diesem Kapitel geht es um Potenzreihen und die Approximation von Funktionen durch Potenzreihen. Um den Inhalt dieses Kapitels zu verstehen, werden Kentnisse zu

* Reihen, insbesondere die geometrische Reihe
* Konvergenz von Reihen
* Konvergenzkriterien für Reihen wie beispielsweise
    * Quotientenkriterium
    * Wurzelkriterium
    
vorausgesetzt.


```{admonition} Lernziele
:class: tip
* Sie können den Unterschied zwischen einer **Potenzreihe** und einer Reihe erklären.
* Sie können die **spezielle Darstellungsform einer Potenzreihe** 

$$p(x)=\sum_{k=0}^{\infty}a_k x^k$$
auswendig aufschreiben.
* Sie können die **allgemeine Darstellungsform einer Potenzreihe** 

$$p(x)=\sum_{k=0}^{\infty}a_k (x-x_0)^k$$
auswendig aufschreiben und erklären, was ein **Entwicklungspunkt** ist.
* Sie können erklären, was der **Konvergenzbereich** einer Potenzreihe ist.
* Sie können den Konvergenzbereich einer Potenzreihe geometrisch interpretieren und anhand des **Konvergenzradius** entscheiden, ob eine Potenzreihe konvergiert oder divergiert oder berechnen, was in den **Randpunkten** passiert.
* Sie kennen zwei Formeln auswendig, um den Konvergenzradius $r$ einer Potenzreihe zu berechnen, nämlich

$$r = \lim_{k\to\infty}\left| \frac{a_k}{a_{k+1}}\right| \quad \text{ und } \quad r = \lim_{k\to\infty}\frac{1}{\sqrt[k]{|a_k|}},$$

und können diese auch anwenden. 
```


## Potenzreihen sind auch nur Reihen, aber Reihen von Potenzfunktionen

Bisher haben wir Zahlenfolgen aufsummiert und die Folge der Partialsummen als Reihe bezeichnet. Nun summieren wir Potenzfunktionen auf. Zur Erinnerung, Potenzfunktionen (manchmal auch kurz als Potenz bezeichnet) sind die Funktionen

$$1, x^1, x^2, x^3, \ldots.$$

````{prf:definition}
:label: def:04a:01
Eine **Potenzreihe** ist eine Reihe vom Typ

$$p(x)=a_0 + a_1x + a_2x^2 + a_3 x^3 + \ldots = \sum_{k=0}^{\infty}a_k x^k.$$

Die reellen Zahlen $a_0, a_1, a_2, \ldots$ nennt man **Koeffizienten** der Potenzreihe.
````


Etwas allgemeiner formulieren wir die Potenzreihe als

$$p(x)=a_0 + a_1\cdot(x-x_0) + a_2\cdot(x-x_0)^2 + a_3\cdot(x-x_0)^3+\ldots = \sum_{k=0}^{\infty}a_k (x-x_0)^k.$$

Dabei wird der spezielle Punkt $x_0$ in der Industrie **Arbeitspunkt** genannt, in der Mathematik sagen wir aber **Entwicklungspunkt**.


## Manchmal kann man eine Funktion mit einer Potenzreihe approximieren, manchmal nicht

Experiment:

1. Gehen Sie mit Ihrem Mauszeiger auf das GeoGebra-Applet und klicken Sie darauf (ggf. auf den Pfeil klicken), um es zu aktivieren.
2. Schauen Sie sich zunächst die Approximation der Kosinusfunktion an. Schieben Sie den Slider für n von 1 bis 30 und beobachten Sie? Ab wann ist Ihrer Meinung nach die Potenzreihe eine gute Approximation der Kosinusfunktion? 
3. Ändern Sie jetzt die Funktion und geben Sie `f(x) = ln(x)` ein. Schieben Sie den Schieberegler wieder von 1 bis 30. Was beobachten Sie diesmal?

```{admonition} GeoGebra
:class: seealso
https://www.geogebra.org/m/s9SkCsvC
```

## Der Konvergenzradius entscheidet, ob und wo eine Funktion durch Potenzreihen approximiert werden kann

Die folgenden Erklärvideos erklären, wann eine Potenzreihe gegen eine Funktion konvergiert und wie die beiden Konvergenzkriterien
* Quotientenkriterium
* Wurzelkriterium

funktionieren.


```{admonition} Video
:class: seealso
https://www.youtube.com/embed/69PgueE9CI0
```

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/yO2mP5aToMU
```

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/ConZiKDKA9Q
```
