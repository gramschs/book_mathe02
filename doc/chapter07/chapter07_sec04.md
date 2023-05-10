# 7.4 Mehrdimensionale Kettenregel

Nachdem wir die Begriffe vektorwertige Funktion und Jacobi-Matrix kennengelernt
haben, können wir nun das Thema Kettenregel für mehrdimensionale Funktionen
angehen.

## Lernziele

```{admonition} Lernziel
Sie können die **mehrdimensionale Kettenregel** anwenden.
```

## Verkettung von Funktionen

Was genau passiert, wenn wir mehrdimensionale Funktionen verketten? Die
"Verkettung" von eindimensionalen Funktionen haben wir bereits kennengelernt.
Eine Funktion wird auf das Ergebnis einer anderen Funktion angewendet. Im Falle
eindimensionaler Funktionen könnten wir zum Beispiel zwei Funktionen $g(x)=x^2$
und $f(x)=\sin(x)$ betrachten und sie verkettet als 

$$(f\circ g)(x) = f(g(x)) = \sin(x^2)$$

ausdrücken. Das bedeutet, dass wir zuerst die Funktion $g$ auf $x$ und dann die
Funktion $f$ auf das Ergebnis $g(x)$ anwenden.

Bei mehrdimensionalen Funktionen ist das Konzept ähnlich, aber es wird etwas
komplexer, da wir jetzt mehrere Eingaben haben. Angenommen, wir haben eine
Funktion 

$$g(r, \varphi) = 
\begin{pmatrix} 
r\cdot \sin(\varphi) \\ 
r\cdot \cos(\varphi)
\end{pmatrix}$$

und eine Funktion 

$$f(x,y) = \begin{pmatrix} x^2 + y^2 \\ x\cdot y \\ x^2 - y^2 \end{pmatrix}$$

und wir wollen sie verkettet darstellen. In diesem Fall würde die Verkettung so
aussehen: 

$$(f\circ g)(r, \varphi) = \begin{pmatrix} \left(r\cdot \sin(\varphi)\right)^2 +
\left(r\cdot \cos(\varphi)\right)^2 \\ \left(r\cdot \sin(\varphi)\right)\cdot
\left(r\cdot \cos(\varphi)\right) \\
\left(r\cdot \sin(\varphi)\right)^2 - \left(r\cdot \cos(\varphi)\right)^2
\end{pmatrix} = 
\begin{pmatrix} 
r^2 \\ 
r^2 \cdot \sin(\varphi) \cos(\varphi) \\
r^2 \cdot \left( \sin^2(\varphi) - \cos^2(\varphi)\right)
\end{pmatrix}$$

Das bedeutet, dass wir zuerst die Funktion $g$ auf $r$ und $\varphi$ anwenden
und dann die Funktion $f$ auf das Ergebnis, also auf $x = r\cdot \sin(\varphi)$
und $y = r\cdot \cos(\varphi)$.


## Mehrdimensionale Kettenregel

Zur Erinnerung, die eindimensionale Kettenregel lautet wie folgt: Die Ableitung
der verketten Funktion $f(g(x))$ ist äußere Ableitung mal innere Ableitung, d.h.

$$f(g(x))' = f'(g(x))\cdot g'(x).$$

In mehreren Dimensionen wird diese Regel durch die Verwendung von
Jacobi-Matrizen erweitert. Die Jacobi-Matrix ist eine Matrix, die alle ersten
partiellen Ableitungen einer mehrdimensionalen Funktion enthält. 

Die mehrdimensionale Kettenregel lautet dann: Wenn wir zwei Funktionen $f$ unf
$g$ haben, die miteinander verkettet zu $f\circ g$ werden, dann ist die
Jacobi-Matrix der verketteten Funktion   gleich dem Produkt der Jacobi-Matrix
von $f$ nach $g$ und der Jacobi-Matrix von $g$ nach $\vec{x}$:

$$J_{f\circ g}(\vec{x}) = J_{f}(g(\vec{x})) \cdot J_g(\vec{x}).$$

Dabei ist $J_{f}$ die Jacobi-Matrix von $f$ ausgewertet an der Stelle
$g(\vec{x})$ und $J_{g}$ die Jacobi-Matrix von $g$ ausgewertet an der Stelle
$\vec{x}$.

Diese Regel erlaubt es uns, die Ableitung einer verketteten Funktion zu
berechnen, selbst wenn diese Funktion aus mehreren ineinander verschachtelten
Funktionen besteht, die jeweils von mehreren Variablen abhängen.

Wir betrachten erneut das obige Beispiel und bilden zuerst die beiden
Jacobi-Matrizen:

$$J_{g}(r, \varphi) = 
\begin{pmatrix} 
\sin(\varphi) & r\cdot\cos(\varphi)\\ 
\cos(\varphi) & -r\cdot\sin(\varphi)
\end{pmatrix}$$

und

$$ J_{g}(x,y) = 
\begin{pmatrix} 
2x & 2y \\ 
y & x \\ 
2x & -2y \\ 
\end{pmatrix}$$

Dann ist die Jacobi-Matrix der verketteten Funktion

\begin{align*}
J_{f\circ}(r,\varphi) &= J_{f}(g(r,\varphi)) \cdot J_{g}(r, \varphi) = \\
&= 
\begin{pmatrix}
2r\cdot\sin(\varphi) & 2r\cdot \cos(\varphi) \\
r\cdot\cos(\varphi) & r\cdot\sin(\varphi) \\
2r\cdot\sin(\varphi) & -2r\cdot\cos(\varphi) \\
\end{pmatrix} \cdot
\begin{pmatrix}
\sin(\varphi) & r\cos(\varphi) \\
\cos(\varphi) & -r\cdot\sin(\varphi)
\end{pmatrix} = \\
&= 
\begin{pmatrix}
2r & 0 \\
2r\sin(\varphi)\cos(\varphi) & r^2\left(\cos^2(\varphi)-\sin^2(\varphi) \right)\\
2r\left(\sin^2(\varphi)-\cos^2(\varphi)\right) & 4r^2\sin(\varphi)\cos(\varphi) \\
\end{pmatrix}
\end{align*}

Das gleiche Ergebnis erhalten wir, wenn wir direkt die Jacobi-Matrix der
verketteten Funktion berechnen. Manchmal ist es einfacher, die Jacobi-Matrizen
der inneren und äußeren Funktion auszurechnen und das Produkt zu bilden, und
manchmal ist die direkte Berechnung der Jacobi-Matrix der verketteten Funktion
einfacher. 

```{dropdown} Video zu "Mehrdimensionale Kettenregel" von Prof. Hoever
<iframe width="560" height="315" src="https://www.youtube.com/embed/LkWAGcGGDD8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
