# 6.2 Fourierreihen 

Periodische Vorgänge gibt es sowohl in der Natur als auch in der Technik. In der
Technik gehören insbesondere Drehbewegungen dazu. Es ist nicht sinnvoll,
periodische Funktionen durch Potenzreihen bzw. Taylorreihen zu approximieren.
Stattdessen werden wir periodische Funktionen als Überlagerung von Sinus- und
Kosinus-Funktionen approximieren, also sogenannte **Fourierreihen**. 

Die Idee der Fourierreihe wird in dem folgenden Video erklärt.

```{dropdown} Video "Fourierreihe Übersicht" von Daniel Jung
<iframe width="560" height="315" src="https://www.youtube.com/embed/_Hm3yGqWaeo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Lernziele Fourierreihen

```{admonition} Lernziele
:class: important
* Sie können eine periodische Funktion in eine **Fourierreihe** umschreiben.
* Sie können dazu die **Fourierkoeffizienten** berechnen. 
* Sie kennen die Kriterien, wann eine Funktion in eine Fourierreihe entwickelt werden darf.
```

## Trigonometrische Polynome

Bevor uns dem Thema Fourierreihe widmen, klären wir erst einmal den Begriff
**trigonometrisches Polynom**. Wir haben ja bereits im letzten Kapitel die
beiden wichtigsten periodischen Funktionen kennengelernt: Sinus- und
Kosinusfunktion. Beide haben die Periode $2\pi$. Als erstes wollen wir Sinus
und Kosinus so umschreiben, dass sie nicht die Periode $2\pi$ haben, sondern
eine beliebige Periode, die als $T$ abgekürzt wird. Das klappt mit dem folgenden
Trick. Wir nehmen nicht $\sin(x)$, sondern $\sin(\omega \cdot t)$ mit

$$\omega = \frac{2\pi}{T}.$$

Wenn jetzt für $t$ die Periode $T$ eingesetzt wird, ist das das Gleiche wie
$2\pi$. Und $\omega = 1$ ist die normale Sinus-/Kosinusfunktion.

Außerdem können wir die Sinus-/Kosinusfunktionen mit doppelter, dreifacher,
vierfacher ... Frequenz miteinander kombinieren, z.B. so:

$$f(x) = 3\cdot\cos(\omega t) -17\cdot\sin(\omega t) -2\cdot\cos(2\omega t) +
\frac{3}{8}\cdot\sin(2\omega t).$$

Die Funktion $f$ hat die Periode $T = 2\pi$ und wird trigonometrisches Polynom
genannt.

```{admonition} Was ist ... ein trigonometrisches Polynom?
:class: note
Ein trigonometrisches Polynom ist eine Funktion, die als Linearkombination von Sinus- und Kosinusfunktionen geschrieben werden kann:

$$f(x) = \frac{a_0}{2} + a_1 \cos(\omega t) + b_1 \sin(\omega t) + a_2\cos(2\omega t) + b_2\sin(2\omega t) + \ldots + a_n\cos(n\omega t) + b_n\sin(n\omega t).$$

Hierbei sind $a_0$, $a_1$, $b_1$, $a_2$, $b_2$, ..., $a_n$, $b_n$ Konstanten, die bestimmt werden
müssen, um die Funktion f(x) vollständig zu beschreiben. 
```

Und warum nehmen wir $\frac{a_0}{2}$ und nicht einfach $a_0$? Das hat etwas mit
komplexen trigonometrischen Polynomen zu tun, die wir in dieser Vorlesung aber
nicht mehr behandeln. Dennoch halten wir uns an dieser Stelle an die übliche
Schreibweise.

```{dropdown} Video "Vorbereitung Fourierreihe Sinus/Kosinus" von Daniel Jung
<iframe width="560" height="315" src="https://www.youtube.com/embed/Wpp4FSUj9zU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Wie findet man zu einer Funktion das trigonometrische Polynom?

Die Koeffizienten $a_k$ und $b_k$, also die Vorfaktoren vor den Sinus- und den
Kosinusfunktionen im trigonometrischen Polynom heißen **Fourierkoeffizienten**.
Wenn wir einfach irgendwelche Zaheln dafür wählen, ergibt sich dadurch eine
Funktion. Wenn wir aber den umgelehrten Weg gehen wollen, dass die Funktion $f$
durch das trigonometrische Polynom angenähert werden soll, dann müssen wir die
Fourierkoeffizienten nach der folgenden Formel berechnen.

```{admonition} Wie werden die Fourierkoeffizienten berechnet?
:class: note
Wir starten mit einer gegebenen Funktion $f$, die die Periode $T$ und die
Frequenz $\omega = \frac{2\pi}{T}$ hat. Die Fourierkoeffizienten werden dann
berechnet als

\begin{align*}
a_k &= \frac{2}{T} \int_{-T/2}^{T/2} f(t) \, \cos(k \, \omega \, t) \, dt, \quad k = 0, 1, 2, \ldots \\
b_k &= \frac{2}{T} \int_{-T/2}^{T/2} f(t) \, \sin(k \, \omega \, t) \, dt, \quad k = 1, 2, \ldots \\
\end{align*}
```

## Fourierreihe

Wenn wir den Grad $n$ des trigonometrischen Polynoms erhöhen, so können wir
vermuten, dass die Approximation der Funktion $f$ immer besser wird. Tatsächlich
ist es nicht ganz so einfach. Nur wenn die sogenannten **Dirichlet-Bedingungen**
erfüllt sind, konvergiert das trigonometrische Polynom für $n \to \infty$ gegen
die periodische Funktion $f$. Die Dirichlet-Bedingungen lauten:

1. Das Periodenintervall lässt sich in Teilintervall unterteilen, in denen die
   Funktion $f$ stetig und monoton ist. Dabei darf es höchstens endlich viele
   Teilintervalle geben.
2. Bei den Unstetigkeitsstellen existeriet sowohl der linksseitige als auch der
   rechtsseitige Grenzwert. 

Bei allen praktisch vorkommenen Beispielen im Maschinenbau ist dies aber der
Fall. Wenn der Grad $n$ gegen unendlich geht, nennen wir die Reihe Fourierreihe.

```{admonition} Was ist ... die Fourierreihe?
:class: note
Die meisten Funktionen $f$ mit der Periode $T$ und der Kreisfrequenz $\omega$
können als eine unendliche Summe von Sinus- und Kosinusfunktionen approximiert
mit den Fourierkoeffizienten $a_k$ und $b_k$ werden:

$$f(t) = \frac{a_0}{2} + \sum_{k=1}^{\infty} \left(a_k \cos(k \omega t) + b_k
\sin(k \omega t) \right).$$

Diese Funktionenreihe nennt man **Fourierreihe**.
```