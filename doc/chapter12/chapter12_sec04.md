# 12.4 Homogene Systeme aus zwei linearen DGL 1. Ordnung

In Natur und Technik wird häufig nicht nur eine Differentialgleichung benötigt,
um einen Prozess zu beschreiben, sondern viele Differentialgleichungen. Dabei
kann es sein, dass die gesuchten Funktionen in mehreren Differentialgleichungen
vorkommen. Es entsteht ein System von Differentialgleichungen. Wir beschränken
uns in diesem Kapitel auf den einfachsten Fall, der auftreten kann.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können erklären, was ein **System von Differentialgleichungen** ist.
* Sie können ein **System von linearen Differentialgleichungen 2. Ordnung** lösen.
```

## Was ist ein System von Differentialgleichungen?

Sind mehrere Differentialgleichungen gekoppelt, d.h. die gesuchten Funktionen
treten in verschiedenen Gleichungen gleichzeitig auf, so sprechen wir von einem
**System von Differentialgleichungen**.

Wir betrachten homogene Systeme von zwei linearen Differentialgleichungen 1.
Ordnung mit konstanten Koeffizienten:

\begin{align*}
y_1' &= a_{11}y_1 + a_{12}y_2 \\
y_2' &= a_{21}y_1 + a_{22}y_2
\end{align*}

Hier werden zwei Funktionen $y_1$ und $y_2$ gesucht, die miteinander gekoppelt
sind. Da jede Gleichung die Ordnung 1 hat, bezeichnen wir das System als System
der Ordnung 2.

Die Koeffizienten lassen sich in einer **Koeffizientenmatrix** zusammenfassen:

$$A =
\begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{pmatrix}$$

Dadurch können wir das System kompakt als **Matrix-Vektor-Gleichung** schreiben:

$$\begin{pmatrix} y_{1}'\\ y_{2}' \end{pmatrix} =
\begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \end{pmatrix} \cdot
\begin{pmatrix} y_1 \\ y_2 \end{pmatrix}$$

## Wie wird ein System 2. Ordnung gelöst?

Von einzelnen homogenen linearen Differentialgleichungen wissen wir, dass deren
Lösungen Exponentialfunktionen sind. Diese Erkenntnis übertragen wir auf das
System und wählen als Lösungsansatz:

$$y_1 = C_1 \, e^{\lambda x} \quad \text{ und }
\quad y_2 = C_2 \, e^{\lambda x}.$$

Dabei haben wir drei unbekannte Konstanten, nämlich $C_1$, $C_2$ und $\lambda$.
Die beiden Konstanten $C_1$ und $C_2$ werden unsere Integrationskonstanten
werden. Da wir ein System 2. Ordnung haben, brauchen wir zwei
Integrationskonstanten. Aber $\lambda$ muss noch bestimmt werden. Wir machen
weiter und bilden die erste Ableitung der beiden Ansatzfunktionen

$$y_1'= C_1 \, \lambda e^{\lambda x} \quad \text{ und }
\quad y_2' = C_2 \, \lambda e^{\lambda x}.$$

Setzen wir nun beide Ansatzfunktionen in das System von Differentialgleichungen
ein, so erhalten wir

\begin{align*}
C_1 \, \lambda e^{\lambda x} &= a_{11} C_1 \, e^{\lambda x} + a_{12} C_2 \, e^{\lambda x} \\
C_2 \, \lambda e^{\lambda x} &= a_{21} C_1 \, e^{\lambda x} + a_{22} C_2 \, e^{\lambda x}
\end{align*}

Wir teilen durch $e^{\lambda x}$ und erhalten

\begin{align*}
C_1 \, \lambda  &= a_{11} C_1 + a_{12} C_2 \\
C_2 \, \lambda  &= a_{21} C_1 + a_{22} C_2
\end{align*}

Bringen wir die Terme $C_1 \, \lambda$ und $C_2 \, \lambda$ jeweils auf die
rechte Seite und schreiben das Gleichungssystem in Matrixform, so erhalten wir

$$
\begin{pmatrix}
a_{11} - \lambda & a_{21} \\
a_{21} & a_{22} - \lambda
\end{pmatrix} \cdot
\begin{pmatrix} C_1 \\ C_2 \end{pmatrix} =
\begin{pmatrix} 0 \\ 0 \end{pmatrix}.$$

Wenn die Determinante dieses linearen Gleichungssystems ungleich Null ist, dann
kommen nur $C_1 = C_2 = 0$ als Lösung infrage. Damit wären aber auch $y_1$ und
$y_2$ die Nullfunktionen. Das System von Differentialgleichungen hat also nur
dann Funktionen als Lösung, wenn die Determinante dieses Gleichungssystems Null
ist.

Wir setzen also

$$\det \begin{pmatrix}
a_{11} - \lambda & a_{12} \\
a_{21} & a_{22} - \lambda
\end{pmatrix} \overset{!}{=} 0$$

an und bestimmen $\lambda$ so, dass die Determinante Null ist. Diese Gleichung
wird **charakteristische Gleichung** genannt und folgendermaßen notiert:

$$(a_{11}-\lambda) \cdot (a_{22}-\lambda) - a_{21} \, a_{12} = 0.$$

Die charakteristische Gleichung $(a_{11}-\lambda)(a_{22}-\lambda) - a_{21}a_{12}
= 0$ ist eine quadratische Gleichung für $\lambda$. Je nach Art der Lösungen
unterscheiden wir drei Fälle:

* 2 Nullstellen, d.h. $\lambda_1 \neq \lambda_2$ reell,
* 1 Nullstelle, d.h. $\lambda_1 = \lambda_2$ reell,
* 0 Nullstellen, d.h. $\lambda_1 \neq \lambda_2$ komplex, weil für die komplexen Zahlen eine quadratische Gleichung immer zwei Lösungen hat.

Je nachdem, welcher dieser dieser Fälle eintritt, lauten die beiden
Lösungsfunktionen wie folgt.

**1. Fall: 2 Nullstellen**

Es gilt also $\lambda_1 \neq \lambda_2$ reell.

1. Lösungsfunktion: $y_1(x)=C_1\cdot e^{\lambda_1 x} + C_2\cdot e^{\lambda_2 x}$

2. Lösungsfunktion: erhalten wir, indem wir die $y_1$ in die 1. DGL einsetzen und dann nach $y_2$ auflösen:

$$y_2(x)=\frac{1}{a_{12}}(y_1' - a_{11} y_1) $$

**2. Fall: 1 Nullstelle**

Es gilt also $\lambda_1 = \lambda_2 = \alpha$ reell.

1. Lösungsfunktion: $y_1(x)=(C_1+C_2 x) \cdot e^{\alpha x} $

2. Lösungsfunktion:

$$y_2(x)=\frac{1}{a_{12}}(y_1' - a_{11} y_1) $$

**3. Fall: 0 Nullstellen**

Es gilt also $\lambda_1 \neq \lambda_2$ komplex, die komplexen Nullstellen können geschrieben werden als $\lambda_{1/2}=\alpha \pm \omega i$.

1. Lösungsfunktion: $y_1(x)=e^{\alpha x}\left(C_1\sin(\omega x) + C_2 \cos(\omega x)\right) $

2. Lösungsfunktion:

$$y_2(x)=\frac{1}{a_{12}}(y_1' - a_{11} y_1) $$

## Beispiel zur Lösung eines Systems 2. Ordnung

Wir betrachten das homogene System 2. Ordnung

\begin{align*}
y_1' &= -8y_1 - 2y_2 \\
y_2' &= 15y_1 + 5y_2
\end{align*}

mit der Koeffizientenmatrix

$$A = \begin{pmatrix} -8 & -2 \\ 15 & 5 \end{pmatrix}.$$

Die Nullstellen der charakteristischen Gleichung

$$\det (A-\lambda I) = 0$$

sind $\lambda_1 = -5$ und $\lambda_2 = 2$.

Der erste Fall liegt vor und damit ist die erste Lösungsfunktion

$$y_1(x) = C_1 \, e^{-5x} + C_2 \, e^{2x}.$$

Wir berechnen die erste Ableitung, da wir $y_1'$ für die Berechnung von $y_2$
brauchen:

$$y_1'(x) = -5 C_1 e^{-5x} + 2 C_2 e^{2x}.$$

Die zweite Lösungsfunktion ist damit

$$y_2(x) = \frac{1}{-2} \big(y_1' - (-8)\cdot y_1\big) =
\big(\frac{5}{2}C_1+8\big) e^{-5x} + (8-C_2) e^{2x}.$$

## Zusammenfassung

In diesem Kapitel haben wir gelernt, homogene Systeme linearer
Differentialgleichungen durch die Eigenwertmethode zu lösen. Der
Exponentialansatz führt zur charakteristischen Gleichung, deren Eigenwerte das
Verhalten des Systems bestimmen.
