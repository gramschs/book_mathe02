# Übungen

```{admonition} Übung 6.1
:class: miniexercise
Berechnen Sie die ersten partiellen Ableitungen.

a) $f(x,y)=e^{x}\cdot e^{y}$ <br>
b) $f(x,y)=e^{xy}$ <br>
c) $f(x,y)=\sin(x)\cos(y)$ <br>
d) $f(x_1,x_2,x_3) = \frac{1}{2x_1^2+\sqrt{x_2^2+x_3^2}}$ <br>
```

````{admonition} Lösung
:class: miniexercise, toggle
a) $f(x,y)=e^{x}\cdot e^{y} = e^{x+y}$

$$\frac{\partial f}{\partial x}=e^{x+y} \quad \text{ und } \quad \frac{\partial f}{\partial y}=e^{x+y}$$

<hr style="height:3px;border-width:0;color:gray;background-color:gray">

b) $f(x,y)=e^{xy}$

$$\frac{\partial f}{\partial x}=y \cdot e^{xy} \quad \text{ und } \quad \frac{\partial f}{\partial y}=x \cdot e^{xy}$$

<hr style="height:3px;border-width:0;color:gray;background-color:gray">

c) $f(x,y)=\sin(x)\cos(y)$

$$\frac{\partial f}{\partial x}=\cos(x)\cos(y) \quad \text{ und } \quad \frac{\partial f}{\partial y}=-\sin(x)\sin(y)$$

<hr style="height:3px;border-width:0;color:gray;background-color:gray">

d) $f(x_1,x_2,x_3) = \frac{1}{2x_1^2+\sqrt{x_2^2+x_3^2}}$

Wir wenden die Kettenregel an:

\begin{align*}
\frac{\partial f}{\partial x_1} &= -\frac{1}{(2x_1^2+\sqrt{x_2^2+x_3^2})^2} \cdot 4x_1 \\
&= -\frac{4x_1}{(2x_1^2+\sqrt{x_2^2+x_3^2})^2}
\end{align*}

\begin{align*}
\frac{\partial f}{\partial x_2} &= -\frac{1}{(2x_1^2+\sqrt{x_2^2+x_3^2})^2} \cdot \frac{x_2}{\sqrt{x_2^2+x_3^2}} \\
&= -\frac{x_2}{(2x_1^2+\sqrt{x_2^2+x_3^2})^2 \cdot \sqrt{x_2^2+x_3^2}}
\end{align*}

\begin{align*}
\frac{\partial f}{\partial x_3} &= -\frac{1}{(2x_1^2+\sqrt{x_2^2+x_3^2})^2} \cdot \frac{x_3}{\sqrt{x_2^2+x_3^2}} \\
&= -\frac{x_3}{(2x_1^2+\sqrt{x_2^2+x_3^2})^2 \cdot \sqrt{x_2^2+x_3^2}}
\end{align*}
````

```{admonition} Übung 6.2
:class: miniexercise
Berechnen Sie die zweiten partiellen Ableitungen. Verifizieren Sie jeweils
explizit, dass das Ergebnis unabhängig von der Reihenfolge der
Differentiationsschritte ist (Satz von Schwarz).

a) $f(x,y)=x^3+y^3 + x^2y^2+xy+1$ <br>
b) $f(x,y,z)=\frac{1}{\sqrt{x^2+y^2+z^2}}$ 
```

````{admonition} Lösung
:class: miniexercise, toggle
:class: miniexercise, toggle
a) $f(x,y)=x^3+y^3 + x^2y^2+xy+1$ 

**Schritt 1:** Berechnung der ersten partiellen Ableitungen:
\begin{align*}
\frac{\partial f}{\partial x} &= 3x^2+2xy^2+y \\
\frac{\partial f}{\partial y} &= 3y^2+2x^2y+x 
\end{align*}

**Schritt 2:** Berechnung der zweiten partiellen Ableitungen:
\begin{align*}
\frac{\partial^2 f}{\partial x^2} &= \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right) = \frac{\partial}{\partial x}(3x^2+2xy^2+y) = 6x + 2y^2 \\
\frac{\partial^2 f}{\partial x \partial y} &= \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right) = \frac{\partial}{\partial y}(3x^2+2xy^2+y) = 4xy + 1 \\
\frac{\partial^2 f}{\partial y \partial x} &= \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right) = \frac{\partial}{\partial x}(3y^2+2x^2y+x) = 4xy + 1 \\
\frac{\partial^2 f}{\partial y^2} &= \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right) = \frac{\partial}{\partial y}(3y^2+2x^2y+x) = 6y + 2x^2
\end{align*}

**Verifikation des Satzes von Schwarz:**
Da $\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x} = 4xy + 1$, ist der Satz von Schwarz bestätigt.

<hr style="height:3px;border-width:0;color:gray;background-color:gray">

b) $f(x,y,z)=\frac{1}{\sqrt{x^2+y^2+z^2}}$ 

**Schritt 1:** Berechnung der ersten partiellen Ableitungen:

\begin{align*}
\frac{\partial f}{\partial x} &= -\frac{1}{(\sqrt{x^2+y^2+z^2})^2} \cdot \frac{\partial}{\partial x}(\sqrt{x^2+y^2+z^2}) \\
&= -\frac{1}{x^2+y^2+z^2} \cdot \frac{1}{2}(x^2+y^2+z^2)^{-1/2} \cdot 2x \\
&= -\frac{1}{x^2+y^2+z^2} \cdot \frac{x}{\sqrt{x^2+y^2+z^2}} \\
&= -\frac{x}{(x^2+y^2+z^2)^{3/2}}
\end{align*}

Analog berechnen wir:
\begin{align*}
\frac{\partial f}{\partial y} &= -\frac{y}{(x^2+y^2+z^2)^{3/2}} \\
\frac{\partial f}{\partial z} &= -\frac{z}{(x^2+y^2+z^2)^{3/2}}
\end{align*}

**Schritt 2:** Berechnung der zweiten partiellen Ableitungen:

Für die reinen zweiten Ableitungen:
\begin{align*}
\frac{\partial^2 f}{\partial x^2} &= \frac{\partial}{\partial x}\left(-\frac{x}{(x^2+y^2+z^2)^{3/2}}\right) \\
&= -\frac{\partial}{\partial x}\left(\frac{x}{(x^2+y^2+z^2)^{3/2}}\right) \\
&= -\left[\frac{1}{(x^2+y^2+z^2)^{3/2}} + x \cdot \frac{\partial}{\partial x}\left(\frac{1}{(x^2+y^2+z^2)^{3/2}}\right)\right] \\
&= -\left[\frac{1}{(x^2+y^2+z^2)^{3/2}} + x \cdot \left(-\frac{3}{2}\right)(x^2+y^2+z^2)^{-5/2} \cdot 2x\right] \\
&= -\frac{1}{(x^2+y^2+z^2)^{3/2}} + \frac{3x^2}{(x^2+y^2+z^2)^{5/2}} \\
&= \frac{-1 \cdot (x^2+y^2+z^2) + 3x^2}{(x^2+y^2+z^2)^{5/2}} \\
&= \frac{-x^2-y^2-z^2 + 3x^2}{(x^2+y^2+z^2)^{5/2}} \\
&= \frac{2x^2-y^2-z^2}{(x^2+y^2+z^2)^{5/2}}
\end{align*}

Durch analoges Vorgehen erhalten wir:
\begin{align*}
\frac{\partial^2 f}{\partial y^2} &= \frac{2y^2-x^2-z^2}{(x^2+y^2+z^2)^{5/2}} \\
\frac{\partial^2 f}{\partial z^2} &= \frac{2z^2-x^2-y^2}{(x^2+y^2+z^2)^{5/2}}
\end{align*}

Für die gemischten Ableitungen:
\begin{align*}
\frac{\partial^2 f}{\partial x \partial y} &= \frac{\partial}{\partial x}\left(-\frac{y}{(x^2+y^2+z^2)^{3/2}}\right) \\
&= -\frac{\partial}{\partial x}\left(\frac{y}{(x^2+y^2+z^2)^{3/2}}\right) \\
&= -y \cdot \frac{\partial}{\partial x}\left(\frac{1}{(x^2+y^2+z^2)^{3/2}}\right) \\
&= -y \cdot \left(-\frac{3}{2}\right)(x^2+y^2+z^2)^{-5/2} \cdot 2x \\
&= \frac{3xy}{(x^2+y^2+z^2)^{5/2}}
\end{align*}

Und für die umgekehrte Reihenfolge:
\begin{align*}
\frac{\partial^2 f}{\partial y \partial x} &= \frac{\partial}{\partial y}\left(-\frac{x}{(x^2+y^2+z^2)^{3/2}}\right) \\
&= -\frac{\partial}{\partial y}\left(\frac{x}{(x^2+y^2+z^2)^{3/2}}\right) \\
&= -x \cdot \frac{\partial}{\partial y}\left(\frac{1}{(x^2+y^2+z^2)^{3/2}}\right) \\
&= -x \cdot \left(-\frac{3}{2}\right)(x^2+y^2+z^2)^{-5/2} \cdot 2y \\
&= \frac{3xy}{(x^2+y^2+z^2)^{5/2}}
\end{align*}

Die übrigen gemischten Ableitungen ergeben:
\begin{align*}
\frac{\partial^2 f}{\partial x \partial z} = \frac{\partial^2 f}{\partial z \partial x} &= \frac{3xz}{(x^2+y^2+z^2)^{5/2}} \\
\frac{\partial^2 f}{\partial y \partial z} = \frac{\partial^2 f}{\partial z \partial y} &= \frac{3yz}{(x^2+y^2+z^2)^{5/2}}
\end{align*}

**Verifikation des Satzes von Schwarz:**
Wir können beobachten, dass:
\begin{align*}
\frac{\partial^2 f}{\partial x \partial y} &= \frac{\partial^2 f}{\partial y \partial x} = \frac{3xy}{(x^2+y^2+z^2)^{5/2}} \\
\frac{\partial^2 f}{\partial x \partial z} &= \frac{\partial^2 f}{\partial z \partial x} = \frac{3xz}{(x^2+y^2+z^2)^{5/2}} \\
\frac{\partial^2 f}{\partial y \partial z} &= \frac{\partial^2 f}{\partial z \partial y} = \frac{3yz}{(x^2+y^2+z^2)^{5/2}}
\end{align*}

Damit ist der Satz von Schwarz für alle gemischten Ableitungen bestätigt, da die partiellen Ableitungen zweiter Ordnung unabhängig von der Reihenfolge der Differentiation sind.
````

```{admonition} Übung 6.3
:class: miniexercise
Berechnen Sie die dritten partiellen Ableitungen. Nutzen Sie aus, dass das
Ergebnis unabhängig von der Reihenfolge der Differentiationsschritte ist
(warum?):

$$f(x,y,z)=x^2y^2z^2+x^3+y^3+z^3.$$

Hinweis: wie viele partielle Ableitungen 3. Ordnung gibt es bei drei Variablen?
Wie viele muss man explizit ausrechnen?
```

````{admonition} Lösung
:class: miniexercise, toggle
Der Satz von Schwarz besagt, dass bei stetigen gemischten partiellen Ableitungen
die Reihenfolge der Differentiation keine Rolle spielt. Unsere Funktion
$f(x,y,z)=x^2y^2z^2+x^3+y^3+z^3$ ist beliebig oft stetig differenzierbar, daher
gilt der Satz für alle Ableitungen.

Bei drei Variablen $x$, $y$ und $z$ gibt es theoretisch $3^3 = 27$ mögliche
Kombinationen für die dritten Ableitungen. Aufgrund des Satzes von Schwarz sind
jedoch viele dieser Kombinationen gleichwertig. Es genau 10 Möglichkeiten:

1. $(3,0,0)$: dreimal nach $x$ ableiten
2. $(2,1,0)$: zweimal nach $x$, einmal nach $y$
3. $(2,0,1)$: zweimal nach $x$, einmal nach $z$
4. $(1,2,0)$: einmal nach $x$, zweimal nach $y$
5. $(1,1,1)$: je einmal nach $x$, $y$ und $z$
6. $(1,0,2)$: einmal nach $x$, zweimal nach $z$
7. $(0,3,0)$: dreimal nach $y$
8. $(0,2,1)$: zweimal nach $y$, einmal nach $z$
9. $(0,1,2)$: einmal nach $y$, zweimal nach $z$
10. $(0,0,3)$: dreimal nach $z$

**Schritt 1:** Berechnung der ersten partiellen Ableitungen:
\begin{align*}
\frac{\partial f}{\partial x} &= 2xy^2z^2 + 3x^2 \\
\frac{\partial f}{\partial y} &= 2x^2yz^2 + 3y^2 \\
\frac{\partial f}{\partial z} &= 2x^2y^2z + 3z^2 \\
\end{align*}

**Schritt 2:** Berechnung der zweiten partiellen Ableitungen:
\begin{align*}
\frac{\partial^2 f}{\partial x^2} &= 2y^2z^2 + 6x \\
\frac{\partial^2 f}{\partial x \partial y} &= 4xyz^2 \\
\frac{\partial^2 f}{\partial x \partial z} &= 4xy^2z \\
\frac{\partial^2 f}{\partial y^2} &= 2x^2z^2 + 6y \\
\frac{\partial^2 f}{\partial y \partial z} &= 4x^2yz \\
\frac{\partial^2 f}{\partial z^2} &= 2x^2y^2 + 6z \\
\end{align*}

**Schritt 3:** Berechnung der 10 unterschiedlichen dritten partiellen Ableitungen:

1. Dreimal nach $x$ ableiten:
\begin{align*}
\frac{\partial^3 f}{\partial x^3} &= \frac{\partial}{\partial x}\left(\frac{\partial^2 f}{\partial x^2}\right) = \frac{\partial}{\partial x}(2y^2z^2 + 6x) = 6
\end{align*}

2. Zweimal nach $x$, einmal nach $y$:
\begin{align*}
\frac{\partial^3 f}{\partial y \partial x^2} &= \frac{\partial}{\partial y}\left(\frac{\partial^2 f}{\partial x^2}\right) = \frac{\partial}{\partial y}(2y^2z^2 + 6x) = 4yz^2
\end{align*}

3. Zweimal nach $x$, einmal nach $z$:
\begin{align*}
\frac{\partial^3 f}{\partial z \partial x^2} &= \frac{\partial}{\partial z}\left(\frac{\partial^2 f}{\partial x^2}\right) = \frac{\partial}{\partial z}(2y^2z^2 + 6x) = 4y^2z
\end{align*}

4. Einmal nach $x$, zweimal nach $y$:
\begin{align*}
\frac{\partial^3 f}{\partial y^2 \partial x} &= \frac{\partial}{\partial y}\left(\frac{\partial^2 f}{\partial x \partial y}\right) = \frac{\partial}{\partial y}(4xyz^2) = 4xz^2
\end{align*}

5. Je einmal nach $x$, $y$ und $z$:
\begin{align*}
\frac{\partial^3 f}{\partial z \partial y \partial x} &= \frac{\partial}{\partial z}\left(\frac{\partial^2 f}{\partial x \partial y}\right) = \frac{\partial}{\partial z}(4xyz^2) = 8xyz
\end{align*}

6. Einmal nach $x$, zweimal nach $z$:
\begin{align*}
\frac{\partial^3 f}{\partial z^2 \partial x} &= \frac{\partial}{\partial z}\left(\frac{\partial^2 f}{\partial x \partial z}\right) = \frac{\partial}{\partial z}(4xy^2z) = 4xy^2
\end{align*}

7. Dreimal nach $y$ ableiten:
\begin{align*}
\frac{\partial^3 f}{\partial y^3} &= \frac{\partial}{\partial y}\left(\frac{\partial^2 f}{\partial y^2}\right) = \frac{\partial}{\partial y}(2x^2z^2 + 6y) = 6
\end{align*}

8. Zweimal nach $y$, einmal nach $z$:
\begin{align*}
\frac{\partial^3 f}{\partial z \partial y^2} &= \frac{\partial}{\partial z}\left(\frac{\partial^2 f}{\partial y^2}\right) = \frac{\partial}{\partial z}(2x^2z^2 + 6y) = 4x^2z
\end{align*}

9. Einmal nach $y$, zweimal nach $z$:
\begin{align*}
\frac{\partial^3 f}{\partial z^2 \partial y} &= \frac{\partial}{\partial z}\left(\frac{\partial^2 f}{\partial y \partial z}\right) = \frac{\partial}{\partial z}(4x^2yz) = 4x^2y
\end{align*}

10. Dreimal nach $z$ ableiten:
\begin{align*}
\frac{\partial^3 f}{\partial z^3} &= \frac{\partial}{\partial z}\left(\frac{\partial^2 f}{\partial z^2}\right) = \frac{\partial}{\partial z}(2x^2y^2 + 6z) = 6
\end{align*}

**Zusammenfassung der 10 verschiedenen Werte:**
\begin{align*}
\frac{\partial^3 f}{\partial x^3} &= 6 \\
\frac{\partial^3 f}{\partial y \partial x^2} &= 4yz^2 \\
\frac{\partial^3 f}{\partial z \partial x^2} &= 4y^2z \\
\frac{\partial^3 f}{\partial y^2 \partial x} &= 4xz^2 \\
\frac{\partial^3 f}{\partial z \partial y \partial x} &= 8xyz \\
\frac{\partial^3 f}{\partial z^2 \partial x} &= 4xy^2 \\
\frac{\partial^3 f}{\partial y^3} &= 6 \\
\frac{\partial^3 f}{\partial z \partial y^2} &= 4x^2z \\
\frac{\partial^3 f}{\partial z^2 \partial y} &= 4x^2y \\
\frac{\partial^3 f}{\partial z^3} &= 6
\end{align*}

Gemäß dem Satz von Schwarz haben wir damit alle 27 möglichen partiellen
Ableitungen dritter Ordnung berechnet, die auf diese 10 verschiedenen Werte
zurückgeführt werden können.
````

```{admonition} Übung 6.4
:class: miniexercise
Berechnen Sie die Hesse-Matrix für die folgenden Funktionen:

a) $f(x,y) = x^2y + xy^2 - 3x^2 + 2y^2$ <br>
b) $f(x,y,z) = x^2 + y^2 + z^2 - 2xy - 2xz + 3yz$ <br>
c) $f(x,y) = \sin(xy) + x^2 - y^2$ <br>
```

```{admonition} Lösung
:class: miniexercise, toggle
:class: miniexercise, toggle
a) $f(x,y) = x^2y + xy^2 - 3x^2 + 2y^2$

**Schritt 1:** Berechnung der ersten partiellen Ableitungen:
\begin{align*}
\frac{\partial f}{\partial x} &= 2xy + y^2 - 6x \\
\frac{\partial f}{\partial y} &= x^2 + 2xy + 4y
\end{align*}

**Schritt 2:** Berechnung der zweiten partiellen Ableitungen:
\begin{align*}
\frac{\partial^2 f}{\partial x^2} &= 2y - 6 \\
\frac{\partial^2 f}{\partial x \partial y} &= 2x + 2y \\
\frac{\partial^2 f}{\partial y \partial x} &= 2x + 2y \\
\frac{\partial^2 f}{\partial y^2} &= 2x + 4
\end{align*}

**Schritt 3:** Aufstellung der Hesse-Matrix:

$$H_f(x,y) = 
\begin{pmatrix}
2y - 6 & 2x + 2y \\
2x + 2y & 2x + 4
\end{pmatrix}$$

<hr style="height:3px;border-width:0;color:gray;background-color:gray">

b) $f(x,y,z) = x^2 + y^2 + z^2 - 2xy - 2xz + 3yz$

**Schritt 1:** Berechnung der ersten partiellen Ableitungen:
\begin{align*}
\frac{\partial f}{\partial x} &= 2x - 2y - 2z \\
\frac{\partial f}{\partial y} &= 2y - 2x + 3z \\
\frac{\partial f}{\partial z} &= 2z - 2x + 3y
\end{align*}

**Schritt 2:** Berechnung der zweiten partiellen Ableitungen:
\begin{align*}
\frac{\partial^2 f}{\partial x^2} &= 2 \\
\frac{\partial^2 f}{\partial x \partial y} &= -2 \\
\frac{\partial^2 f}{\partial x \partial z} &= -2 \\
\frac{\partial^2 f}{\partial y \partial x} &= -2 \\
\frac{\partial^2 f}{\partial y^2} &= 2 \\
\frac{\partial^2 f}{\partial y \partial z} &= 3 \\
\frac{\partial^2 f}{\partial z \partial x} &= -2 \\
\frac{\partial^2 f}{\partial z \partial y} &= 3 \\
\frac{\partial^2 f}{\partial z^2} &= 2
\end{align*}

**Schritt 3:** Aufstellung der Hesse-Matrix:

$$H_f(x,y,z) = 
\begin{pmatrix}
2 & -2 & -2 \\
-2 & 2 & 3 \\
-2 & 3 & 2
\end{pmatrix}$$

Beachten Sie, dass diese Hesse-Matrix konstant ist, d.h. sie hängt nicht von den Werten von $x$, $y$ und $z$ ab.

<hr style="height:3px;border-width:0;color:gray;background-color:gray">

c) $f(x,y) = \sin(xy) + x^2 - y^2$

**Schritt 1:** Berechnung der ersten partiellen Ableitungen:
\begin{align*}
\frac{\partial f}{\partial x} &= y\cos(xy) + 2x \\
\frac{\partial f}{\partial y} &= x\cos(xy) - 2y
\end{align*}

**Schritt 2:** Berechnung der zweiten partiellen Ableitungen:
\begin{align*}
\frac{\partial^2 f}{\partial x^2} &= \frac{\partial}{\partial x}(y\cos(xy) + 2x) \\
&= \frac{\partial}{\partial x}(y\cos(xy)) + \frac{\partial}{\partial x}(2x) \\
&= y \cdot \frac{\partial}{\partial x}(\cos(xy)) + 2 \\
&= y \cdot (-\sin(xy)) \cdot \frac{\partial}{\partial x}(xy) + 2 \\
&= y \cdot (-\sin(xy)) \cdot y + 2 \\
&= -y^2\sin(xy) + 2
\end{align*}

\begin{align*}
\frac{\partial^2 f}{\partial x \partial y} &= \frac{\partial}{\partial y}(y\cos(xy) + 2x) \\
&= \frac{\partial}{\partial y}(y\cos(xy)) + \frac{\partial}{\partial y}(2x) \\
&= \cos(xy) + y \cdot \frac{\partial}{\partial y}(\cos(xy)) + 0 \\
&= \cos(xy) + y \cdot (-\sin(xy)) \cdot \frac{\partial}{\partial y}(xy) \\
&= \cos(xy) + y \cdot (-\sin(xy)) \cdot x \\
&= \cos(xy) - xy\sin(xy)
\end{align*}

\begin{align*}
\frac{\partial^2 f}{\partial y \partial x} &= \frac{\partial}{\partial x}(x\cos(xy) - 2y) \\
&= \frac{\partial}{\partial x}(x\cos(xy)) + \frac{\partial}{\partial x}(-2y) \\
&= \cos(xy) + x \cdot \frac{\partial}{\partial x}(\cos(xy)) + 0 \\
&= \cos(xy) + x \cdot (-\sin(xy)) \cdot \frac{\partial}{\partial x}(xy) \\
&= \cos(xy) + x \cdot (-\sin(xy)) \cdot y \\
&= \cos(xy) - xy\sin(xy)
\end{align*}

\begin{align*}
\frac{\partial^2 f}{\partial y^2} &= \frac{\partial}{\partial y}(x\cos(xy) - 2y) \\
&= \frac{\partial}{\partial y}(x\cos(xy)) + \frac{\partial}{\partial y}(-2y) \\
&= x \cdot \frac{\partial}{\partial y}(\cos(xy)) - 2 \\
&= x \cdot (-\sin(xy)) \cdot \frac{\partial}{\partial y}(xy) - 2 \\
&= x \cdot (-\sin(xy)) \cdot x - 2 \\
&= -x^2\sin(xy) - 2
\end{align*}

**Schritt 3:** Aufstellung der Hesse-Matrix:

$$H_f(x,y) = 
\begin{pmatrix}
-y^2\sin(xy) + 2 & \cos(xy) - xy\sin(xy) \\
\cos(xy) - xy\sin(xy) & -x^2\sin(xy) - 2
\end{pmatrix}$$
```
