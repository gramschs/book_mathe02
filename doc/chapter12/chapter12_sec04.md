# 12.4 Homogene Systeme linearer DGL 1. Ordnung 

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```


## Was ist ein System von Differentialgleichungen?

Wir betrachten in dieser Vorlesung nur Systeme von 2 DGL, die homogen, lineaer und von 1. Ordnung sind.

Ein System von Differentialgleichungen
\begin{align*}
y_1' &= a_{11}y_1 + a_{12}y_2 \\ 
y_2' &= a_{21}y_1 + a_{22}y_2
\end{align*}
heißt homogenes System von Differentialgleichungen 1. Ordnung mit konstanten Koeffizienten.

Es werden also zwei Funktionen $y_1$ und $y_2$ gesucht. Beide gesuchten Funktionen kommen mit der 1. Ableitung vor, in Summe hat das System damit die 2. Ordnung.

<!-- #region -->
## Wie wird ein System 2. Ordnung gelöst?

Bilde die **charakteristische Gleichung**

$$\det(A-\lambda E) = \begin{vmatrix} a_{11}-\lambda & a_{12} \\ a_{21} & a_{22}-\lambda \end{vmatrix}$$

und berechne die Nullstellen $\lambda_1$ und $\lambda_2$ (=Eigenwerte).

Es gibt drei mögliche Lösungen:

* 2 Nullstellen, d.h. $\lambda_1 \neq \lambda_2$ reell
* 1 Nullstelle, d.h. $\lambda_1 = \lambda_2$ reell
* 0 Nullstellen, d.h. $\lambda_1 \neq \lambda_2$ komplex, weil für die komplexen Zahlen eine quadratische Gleichung immer zwei Lösungen hat

Je nachdem, welcher dieser dieser Fälle eintritt, lauten die Lösungen wie folgt.

### 2 Nullstellen

Es gilt also $\lambda_1 \neq \lambda_2$ reell.

1. Lösungsfunktion: $y_1(x)=C_1\cdot e^{\lambda_1 x} + C_2\cdot e^{\lambda_2 x}$ 

2. Lösungsfunktion erhalten wir, indem wir die $y_1$ in die 1. DGL einsetzen und dann nach $y_2$ auflösen:

$$y_2(x)=\frac{1}{a_{12}}(y_1' - a_{11} y_1) $$

### 1 Nullstelle 

Es gilt also $\lambda_1 = \lambda_2 = \alpha$ reell.

1. Lösungsfunktion: $y_1(x)=(C_1+C_2 x) \cdot e^{\alpha x} $

2. Lösungsfunktion erhalten wir wiederum als

$$y_2(x)=\frac{1}{a_{12}}(y_1' - a_{11} y_1) $$


### 0 Nullstellen

Es gilt also $\lambda_1 \neq \lambda_2$ komplex, die komplexen Nullstellen können geschrieben werden als $\lambda_{1/2}=\alpha \pm \omega i$. 

1. Lösungsfunktion: $y_1(x)=e^{\alpha x}\left(C_1\sin(\omega x) + C_2 \cos(\omega x)\right) $

2. Lösungsfunktion erhalten wir wiederum als

$$y_2(x)=\frac{1}{a_{12}}(y_1' - a_{11} y_1) $$

<!-- #endregion -->

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/u1Jm4YXF11c
```
