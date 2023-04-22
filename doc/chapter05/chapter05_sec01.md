# 5.1 Periodische Funktionen

In diesem Kapitel werden wir uns mit periodischen Funktionen beschäftigen.
Insbesondere im Maschinenbau finden sich zahlreiche Anwendungen von periodischen
Funktionen, z.B. in der Technischen Mechanik oder in der Regelungstechnik. Viele
mechanische Systeme, wie z.B. Federsysteme, Pendel oder rotierende Wellen,
führen periodische Schwingungen aus. Auch in der Regelungstechnik werden
periodische Steuergrößen erzeugt, die zur Regelung von Systemen verwendet
werden. Beispiele sind periodische Signale, wie z.B. Rechteck-, Dreieck- oder
Sinusfunktionen. Diese Signale werden verwendet, um elektrische, mechanische
oder hydraulische Systeme zu steuern.

## Lernziele 

```{admonition} Lernziele
:class: tip
* Sie können erklären, was eine **periodische Funktion** ist.
* Sie können Beispiele von periodischen Funktionen nennen wie
    * Sinus- und Kosinusfunktion,
    * Rechteckfunktion,
    * Dreieckfunktion und
    * Sägezahnfunktion.
```

## Periodische Funktionen - was ist das?

Bei einer periodischen Funktion wiederholen sich in regelmäßigen Abständen die Funktionswerte wieder. Der Abstand, nachdem sich die Funktionswerte beginnen zu wiederholen, heißt **Periodendauer**.

```{admonition} Was ist ... eine periodische Funktion?
Eine Funktion heißt periodisch, wenn sich die Funktionswerte regelmäßig wiederholen. Als mathematische Formel ausgedrückt ist eine Funktion $f$ periodisch mit der Periode $p$, wenn gilt:

$$f(x+p) = f(x).$$

```

```{dropdown} Video "Periodische Funktion" von lernflix
<iframe width="560" height="315" src="https://www.youtube.com/embed/e3lpwsKp75Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Beispiele periodischer Funktionen

### Sinus- und Kosinusfunktion

Sinus und Kosinus sind die beiden wichtigsten periodischen Funktionen. Sie werden auch dazu genutzt, um andere periodische Funktionen zu approximieren (Stichwort: Fourierreihe). Beide haben eine Periode von $2\pi$.

```{figure} pics/plot_sinus.pdf
---
width: 600px
name: chap05_plot_sinus
---
Sinusfunktion mit einer Periode $p = 2\pi$
```

### Rechteckfunktion

Die Rechteckfunktion ist eine periodische Funktion, die häufig in der
Signalverarbeitung verwendet wird. Beispielsweise dient sie als Taktsignal für
digitale Prozessoren und Controller. Sie hat eine Periode $p = 1$, bei der die
Funktion zwischen den Werten $1$ und $0$ oszilliert. Die Rechteckfunktion ist
definiert als:

\begin{equation*} 
f(x) = 
\begin{cases} 
1 & \text{ für } 0 \leq x \leq 0.5\\
0 & \text{ für } 0.5 < x < 1 
\end{cases} 
\end{equation*}

```{figure} pics/plot_rechteck.pdf
---
width: 600px
name: chap05_plot_rechteck
---
Rechteckfunktion mit einer Periode $p = 1$
```


```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

### Dreieckfunktion 

Die Dreieckfunktion ist eine periodische Funktion, die ebenfalls in der
Signalverarbeitung häufig vorkommt. Sie hat eine Periode $T$ und oszilliert
zwischen $-1$ und $1$, wobei der Anstieg von $-1$ auf $1$ linear ist und der
Abfall von $1$ auf $-1$ ebenfalls linear ist. Die Dreieckfunktion ist definiert
als:

\begin{equation*} 
f(x) = 
\begin{cases} 
\frac{4x}{T} - 1 & \text{ für } 0 \leq x < \frac{T}{2} \\ 
-\frac{4x}{T} + 3 & \text{ für } \frac{T}{2} \leq x < T 
\end{cases}
\end{equation*}

Die Dreieckfunktion hat auch interessante Eigenschaften in Bezug auf ihre
Fourierreihe und wird oft als Testsignal verwendet, um die Leistung von Filtern
und anderen Signalverarbeitungsalgorithmen zu evaluieren.

### Sägezahnfunktion

Die Sägezahnfunktion ist eine weitere periodische Funktion, die in der
Signalverarbeitung häufig verwendet wird. Sie hat eine Periode $T$ und
oszilliert zwischen $-1$ und $1$, wobei der Anstieg von $-1$ auf $1$ linear ist
und der Abfall von $1$ auf $-1$ plötzlich stattfindet. Die Sägezahnfunktion ist
definiert als:

\begin{equation*} 
f(x) = \frac{2}{T} \cdot \left(x -
\left\lfloor\frac{x}{T}\right\rfloor\cdot T\right) - 1 
\end{equation*}

Die Sägezahnfunktion hat auch interessante Eigenschaften in Bezug auf ihre
Fourierreihe und wird oft als Testsignal verwendet, um die Leistung von Filtern
und anderen Signalverarbeitungsalgorithmen zu evaluieren.