# 5.3 Wichtige Potenzreihen

Es gibt einige wichtige Taylorreihen, die in den Ingenieurwissenschaften sehr
häufig zur Approximation bestimmter Funktionen verwendet werden. Im Folgenden
werden wir uns mit einigen dieser Taylorreihen beschäftigen.

## Lernziele

```{admonition} Lernziele
:class: goals
Sie kennen die wichtigsten Potenz- bzw. Taylorreihen.
```

## Die Exponential- und Logarithmusfunktion

Die Taylorreihe für die Exponentialfunktion $f(x)=e^x$ am Entwicklungspunkt
$x_0=0$ ist:

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \ldots = \sum_{k=0}^{\infty}
\frac{x^k}{k!}.$$

Der Konvergenzradius ist unendlich, d.h. die Approximation der
Exponentialfunktion durch ihre Taylorreihe gilt für alle reellen Zahlen
$x\in\mathbb{R}$.

Die Logarithmusfunktion $f(x)=\ln(x)$ ist nur für positive reelle Zahlen $x > 0$
definiert. Daher können wir nicht den üblichen Entwicklungspunkt $x_0=0$ nehmen,
sondern nehmen stattdessen $x_0=1$. Die Taylorreihe lautet dann

$$\ln(x) = (x-1) - \frac{(x-1)^2}{2}x^2 + \frac{(x-1)^3}{3} - \ldots =
\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{k}(x-1)^k.$$

Die Taylorreihe der Logarithmusfunktion hat den Konvergenzradius 1, d.h. die
Approximation ist nur im Konvergenzbereich $0 < x \leq 2$ gültig.


## Die Sinus- und Kosinusfunktion

Die Taylorreihe der Sinusfunktion $f(x)=\sin(x)$ am Entwicklungspunkt $x_0=0$
lautet:

$$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \ldots = \sum_{k=0}^{\infty} 
(-1)^k \frac{x^{2k+1}}{(2k+1)!}.$$ 

Der Konvergenzradius ist unendlich, d.h. die Approximation der
Sinusfunktion durch ihre Taylorreihe gilt für alle reellen Zahlen
$x\in\mathbb{R}$.

Die Kosinusfunktion $f(x)=\cos(x)$ hat die Taylorreihe

$$\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} x^4 - \ldots =
\sum_{k=0}^{\infty} (-1)^k \frac{x^{2k}}{(2k)!}.$$

Der Konvergenzradius ist unendlich, d.h. die Approximation der
Kosinusfunktion durch ihre Taylorreihe gilt für alle reellen Zahlen
$x\in\mathbb{R}$.