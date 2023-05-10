# Linearisierung/Tangentialebene und Extremwerte

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

Für eindimensionale Funktionen haben wir die Linearisierung und die Annährung einer Funktion durch eine Tangente bereits kennengelernt. Am einfachsten lässt sich die Tangente einer eindimensionalen Funktion berechnen, indem wir das 1. Taylor-Polynom im Entwicklungspunkt $x_0$ berechnen:

$$f(x) \approx f(x_0) + f'(x_0)\cdot (x-x_0).$$

Aus der Tangente wird für eine Funktion $f: \mathbb{R}^2 \rightarrow \mathbb{R}$ eine Tangentialebene. 

Neben der Linearisierung einer mehrdimensionalen Funktion ist auch die Berechnung von Minima (Tiefpunkten) und Maxima (Hochpunkten) interessant für die Praxis. In diesem Kapitel lernen wir, was die 2. Ableitung einer mehrdimensionalen Funktion ist und wie sie genutzt werden kann, um Extremwerte zu berechnen.




## Lernziele

```{admonition} Lernziele
:class: important
* Sie können eine skalarwertige Funktion $f(x,y)$ in einem Arbeitspunkt $(x_0,y_0)$ **linearisieren** oder anders ausgedrückt, ihre **Tangentialebene**

$$T_1(x,y) = f(x_0,y_0) + \frac{\partial f(x_0,y_0)}{\partial x} (x-x_0) + \frac{\partial f(x_0,y_0)}{\partial y}(y-y_0)$$

ausrechnen.
* Sie kennen die **notwendige Bedingung für einen Extremwert** der skalarwertigen Funktion $f(x,y)$

$$\frac{\partial f(x_0, y_0)}{\partial x} = 0 \quad \text{ und } \quad \frac{\partial f(x_0,y_0)}{\partial y} = 0.$$

* Sie können die **Hesse-Matrix** einer Funktion ausrechnen.
* Sie kennen die **hinreichende Bedingung für einen Extremwert** der skalarwertigen Funktion $f(x,y)$, nämlich
    * Die partiellen Ableitungen 1. Ordnung verschwinden in $(x_0,y_0)$, d.h.
    
    $$\frac{\partial f(x_0, y_0)}{\partial x} = 0 \quad \text{ und } \quad \frac{\partial f(x_0,y_0)}{\partial y} = 0.$$
    
    * Die partiellen Ableitungen 2. Ordnung genügen der Ungleichung (= Determinante der Hesse-Matrix)
    
$$\det(H_f(x_0,y_0)) = \frac{\partial^2 f(x_0,y_0)}{\partial x\partial x}\cdot \frac{\partial^2 f(x_0,y_0)}{\partial y \partial y} - \left(\frac{\partial^2 f(x_0,y_0}{\partial x \partial y}\right)^2 > 0.$$

* Das Vorzeichen von $\frac{\partial^2 f(x_0,y_0)}{\partial x\partial x}$ entscheidet dann über die Art des Extremwerts:
\begin{align*}
\frac{\partial^2 f(x_0,y_0)}{\partial x\partial x} < 0 & \qquad \Rightarrow \text{relatives Maximum} \\
\frac{\partial^2 f(x_0,y_0)}{\partial x\partial x} > 0 & \qquad \Rightarrow \text{relatives Minimum} \\
\end{align*}
```

<!-- #region -->
## Linearisierung/Tangentialebene

Ziel dieses Abschnitts ist es, eine skalarwertige Funktion $f(x,y)$ in einem Arbeitspunkt $(x_0,y_0)$ zu **linearisieren** oder anders ausgedrückt, ihre **Tangentialebene**


$$T_{f,1}(x,y) = f(x_0,y_0) + \frac{\partial f(x_0,y_0)}{\partial x} (x-x_0) + \frac{\partial f(x_0,y_0)}{\partial y}(y-y_0)$$

auszurechnen.

Mit Hilfe des Gradienten können wir die Gleichung der Tangentialebene auch vektoriell schreiben


$$T_{f,1}(x,y) = f(x_0,y_0) + \nabla f(x,y)\cdot \begin{pmatrix}x-x_0\\y-y_0\end{pmatrix}.$$

In dem folgenden Video wird gezeigt, wie aus der Formel für das Taylor-Polynom Grad 1 für eindimensionale Funktionen die Formel für mehrdimensionale Funktionen entsteht.
<!-- #endregion -->

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/RFbjuIDKHG0
```

In dem folgenden Video wird ein Beispiel zur Berechnung der Tangentialebene vorgeführt.

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/Cms3lsrG0cM
```

## Extremwerte bei 1D-Funktionen: notwendige Bedingung und hinreichende Bedingung

Um herauszufinden, welche x-Werte als Extrema (Maximum/Hochpunkt oder Minimum/Tiefpunkt) möglich sind, wird die 1. Ableitung Null gesetzt:

$$f'(x)=0.$$

Diese Bedingung ist *notwendig*, damit überhaupt ein Maximum oder Minimum vorliegen kann. Leider reicht diese Bedingung noch nicht aus. Alle Nullstellen der 1. Ableitung sind *mögliche* Extrema, es könnten aber auch Sattelpunkte sein wie in der folgenden Abbildung der Funktion $f(x)=x^3$:


```{figure} pics/part08_sattelpunkt1D.svg
---
width: 300px
name: fig_part06_sattelpunkt1D
---
Sattelpunkt
```


Daher müssen wir noch zusätzliche Bedingungen überprüfen, bevor wir entscheiden können, ob ein Minimum oder Maximum vorliegt. Die möglichen Extremwerte müssen noch zusätzlich mit der 2. Ableitung geprüft werden:

* Der Punkt $\tilde{x}$ ist ein **Maximum/Hochpunkt**, wenn
    * die 1. Ableitung Null ist, d.h. $f'(\tilde{x})=0$ und
    * die 2. Ableitung **negativ** ist, d.h. $f''(\tilde{x}) < 0$. 
* Der Punkt $\tilde{x}$ ist ein **Minimum/Tiefpunkt**, wenn
    * die 1. Ableitung Null ist, d.h. $f'(\tilde{x})=0$ und
    * die 2. Ableitung **positiv** ist, d.h. $f''(\tilde{x}) > 0$.
    
Diese beiden Bedingungen nennt man dann **hinreichende** Bedingungen. Wenn allerdings die zweite Ableitung Null ist, also $f''(\tilde{x})=0$, kann man keine Entscheidung treffen und muss weitere Bedingungen überprüfen.



## Extremwerte bei mehrdimensionalen Funktionen: notwendige Bedingung

Die notwendige Bedingung für Extremwerte eindimensionaler Funktion lässt sich sofort auf mehrdimensionale Funktionen übertragen. Wir müssen uns nur in Erinnerung rufen, dass die 1. Ableitung eindimensionaler Funktionen dem Gradienten entspricht. Und da der Gradient der Zeilenvektor ist, der alle partielle Ableitungen zusammenfasst, lautet die **notwendige Bedingung für einen Extremwert** der skalarwertigen Funktion $f(x,y)$

$$\frac{\partial f(\tilde{x}, \tilde{y})}{\partial x} = 0 \quad \text{ und } \quad \frac{\partial f(\tilde{x},\tilde{y})}{\partial y} = 0.$$

Diese Gleichung können wir auch vektoriell schreiben:

$$\nabla f(\tilde{x},\tilde{y}) = \left( \frac{\partial f(\tilde{x}, \tilde{y})}{\partial x},\frac{\partial f(\tilde{x},\tilde{y})}{\partial y}\right) = (0,0).$$

Der Gradient der Funktion muss der Nullvektor sein, so wie die 1. Ableitung Null sein muss.


```{admonition} Video
:class: seealso
https://www.youtube.com/embed/A_f5qpyl0bk
```

Hier ein Video, bei dem Beispiele vorgerechnet werden:

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/AMYCKnbgU3s
```

## Hesse-Matrix

Wenn der Gradient das Analogon zur 1. Ableitung ist, gibt es dann etwas Ähnliches für die 2. Ableitung? Ja, allerdings wird es dann eine Matrix, die die 2. partiellen Ableitungen zusammenfasst, die sogenannte **Hesse-Matrix**.

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/4Vy4HDLU7nU
```

## Extremwerte bei mehrdimensionalen Funktionen: hinreichende Bedingung

Wenn die notwendige Bedingung erfüllt ist, also die partiellen Ableitungen 1. Ordnung verschwinden in $(x_0,y_0)$, dann reicht das noch nicht aus. Zusätzlich muss noch die folgende **hinreichende Bedingung** gelten:

* Die **Determinante der Hesse-Matrix ist positiv**

$$\det(H_f\,(x_0,y_0)) = \frac{\partial^2 f(x_0,y_0)}{\partial x\partial x}\cdot \frac{\partial^2 f(x_0,y_0)}{\partial y \partial y} 
- \left(\frac{\partial^2 f(x_0,y_0)}{\partial x \partial y}\right)^2 > 0.$$

* Das Vorzeichen von $\frac{\partial^2 f(x_0,y_0)}{\partial x\partial x}$ entscheidet dann über die Art des Extremwerts:

\begin{align*}
\frac{\partial^2 f(x_0,y_0)}{\partial x\partial x} \textbf{< 0} & \qquad \Rightarrow \text{Maximum} \\
\frac{\partial^2 f(x_0,y_0)}{\partial x\partial x} \textbf{> 0} & \qquad \Rightarrow \text{Minimum} \\
\end{align*}


```{admonition} Video
:class: seealso
https://www.youtube.com/embed/eT0nrz_Mujo
```

## Kochrezept zur Bestimmung der Extrema mehrdimensionaler Funktionen

1. Berechne die partiellen Ableitungen der Funktion.
2. Setze aus den partiellen Ableitungen den Gradienten zusammen.
3. Löse die Gleichung $\nabla f(x,y) = (0,0)$.
4. Untersuche für **jeden** Punkt aus Schritt 3 die Hessematrix:

    * Berechne die Hesse-Matrix für diesen Punkt.
    * Berechne die Determinante der Hesse-Matrix für diesen Punkt und prüfe, ob sie positiv ist.
    * Wenn die Determinante positiv ist, dann berechne das Vorzeichen von 
    
    $$\frac{\partial^2 f(x_0,y_0)}{\partial x\partial x}.$$
    
    * Entscheide anhand des Vorzeichens, ob ein Minimum oder ein Maximum vorliegt.


```{admonition} Video
:class: seealso
https://www.youtube.com/embed/8IF5uLY7Gwk
```

## Ausführliches Beispiel

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/GwyPVdoQ37g
```
