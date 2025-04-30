# 5.3 Beispiele für Fourierreihen

In diesem Kapitel untersuchen wir drei klassische Beispiele für Fourierreihen:
die Rechteckschwingung, die Sägezahnschwingung und die Dreieckschwingung. Diese
Funktionen treten häufig in der Signalverarbeitung und der Physik auf, etwa bei
der Beschreibung von periodischen Signalen oder der Analyse von Schwingungen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können die Fourierreihe einer **Rechteckschwingung** berechnen.
* Sie können die Fourierreihe einer **Sägezahnschwingung** berechnen.
* Sie können die Fourierreihe einer **Dreieckschwingung** berechnen.
```

## Die Rechteckschwingung

Die Rechteckschwingung (manchmal auch Rechteckimpuls oder Rechtecksignal
genannt) ist eine periodische Funktion, die zwischen zwei konstanten Werten
wechselt. Als Beispiel für eine Rechteckschwingung betrachten wir die
Rechteckfunktion

$$f(t) = \begin{cases} 1,  \quad &0 \leq t < \pi,\\
-1, \quad &\pi \leq t < 2\pi, \end{cases}$$

auf dem Intervall $[0, 2\pi]$ und setzen sie periodisch fort. Die Periode ist
daher $T = 2\pi$. Das folgende Applet zeigt eine interaktive Visualisierung der
Rechteckschwingung und der dazugehörigen Fourierreihe.

```{admonition} Interaktives Applet "Fourierreihe Rechteckschwingung"
:class: miniexercise
Das folgende interaktive Applet [Fourierreihe
Rechteckschwingung](https://www.hartundtrocken.de/my-product/interaktiv-fourier-reihe-der-rechtecksfunktion/)
veranschaulicht die Rechteckschwingung sowie ihre Fourierreihe. Experimentieren
Sie mit dem Schieberegler, um zu beobachten, wie sich die Fourierreihe durch
Hinzufügen weiterer Glieder der Reihe der ursprünglichen Rechteckfunktion
annähert.
```

Nun berechnen wir die Fourierkoeffizienten der Rechteckschwingung. Die
allgemeine Formel für den ersten Fourierkoeffizient $a_0$ lautet mit der Periode
$T=2\pi$

$$a_0 = \frac{2}{T} \int_{-T/2}^{T/2} f(t) \, dt =
\frac{1}{\pi}\int_{-\pi}^{\pi}f(t)\,dt.$$

Die Rechteckfunktion ist für zwei Abschnitte definiert, daher teilen wir das
Integral entsprechend in die beiden Intervalle $[-\pi,0]$ und $[0,\pi]$ auf. Im
ersten Intervall $[-\pi, 0]$ ist die Rechteckschwingung konstant $f(t) = -1$, im
zweiten Intervall $[0,\pi]$ ist die Rechteckschwingung konstant $f(t) = 1$.
Somit können wir das Integral folgendermaßen in die Summe zweier Integrale
aufteilen.

\begin{align*}
a_0 &= \frac{1}{\pi}\int_{-\pi}^{\pi}f(t)\,dt \\
&= \frac{1}{\pi}\int_{-\pi}^{0}-1\,dt +\frac{1}{\pi}\int_{0}^{\pi}1\,dt\\
&= \frac{1}{\pi}\Big[-t\Big]_{-\pi}^{0} + \frac{1}{\pi}\Big[t\Big]_{0}^{\pi}\\
&= \frac{1}{\pi}\Big(-0-(+\pi)\Big) + \frac{1}{\pi}\Big(\pi-0\Big) = 0.
\end{align*}

Nun berechnen wir die Fourierkoeffizienten $a_n$ für $n \geq 1$. Dabei benötigen
wir zuerst die Frequenz $\omega$. Da wir als Periode $T=2\pi$ gewählt haben,
gilt

$$\omega = \frac{2\pi}{T} = \frac{2\pi}{2\pi}=1.$$

Setzen wir $T=2\pi$ und $\omega=1$ in die allgemeine Formel der
Fourierkoeffizienten $a_n$ ein und verwenden wir wiederum die Aufteilung in die
beiden Teilintervalle $[-\pi, 0]$ und $[0,\pi]$, dann gilt:

\begin{align*}
a_n &= \frac{2}{T} \int_{-T/2}^{T/2} f(t) \, \cos(n \, \omega \, t) \, dt\\
&= \frac{1}{\pi}\int_{-\pi}^{\pi}f(t) \, \cos(n t) \, dt\\
&= \frac{1}{\pi}\int_{-\pi}^{0} -1\, \cos(n t) \, dt +
\frac{1}{\pi}\int_{0}^{\pi}1 \, \cos(n t) \, dt \\
&= \frac{1}{\pi}\left[-\frac{1}{n} \sin(nt) \right]_{-\pi}^{0} +
\frac{1}{\pi}\left[\frac{1}{n}\sin(nt)\right]_{0}^{\pi}.
\end{align*}

Die Zahl $n$ ist eine natürliche Zahl. Setzen wir $0$ oder Vielfache von $\pi$
in die Sinusfunktion ein, ist das Ergebnis Null, also

$$\sin(0) = \sin(n\cdot \pi) = 0.$$

Damit sind insgesamt alle Fourierkoeffizienten $a_n = 0$. Im nächsten Kapitel
werden wir lernen, wie wir dieses Ergebnis schneller hätten ermitteln können.

Nun berechnen wir die Fourierkoeffizienten

$$b_n = \frac{2}{T} \int_{-T/2}^{T/2} f(t) \, \sin(n \, \omega \, t) \, dt$$

für $n \geq 1$. Wir verwenden erneut den Trick, das Integrationsintervall in
zwei Intervalle aufzuteilen:

\begin{align*}
b_n &= \frac{1}{\pi}\int_{-\pi}^{\pi}f(t)\, \sin(nt)\, dt \\
&=\frac{1}{\pi}\int_{-\pi}^{0}-1\sin(nt)\, dt +
\frac{1}{\pi}\int_{0}^{\pi}1\sin(nt)\, dt\\
&=\frac{1}{\pi}\left[\frac{1}{n}\cos(nt)\right]_{-\pi}^{0} +
\frac{1}{\pi}\left[-\frac{1}{n}\cos(nt)\right]_{0}^{\pi} \\
&= \frac{1}{n\cdot\pi}\Big[\cos(nt)\Big]_{-\pi}^{0} -
\frac{1}{n\cdot\pi}\Big[\cos(nt)\Big]_{0}^{\pi} \\
&= \frac{1}{n\cdot\pi}\Big(\cos(0) - \cos(-n\cdot\pi)\Big) -
\frac{1}{n\cdot\pi} \Big(\cos(n\cdot\pi)-\cos(0)\Big).
\end{align*}

Die Kosinusfunktion ist eine gerade Funktion, also gilt

$$\cos(-n\cdot\pi) = \cos(n\cdot\pi).$$

Darüber hinaus gilt $\cos(0)=1$, so dass wir insgesamt

$$b_n = \frac{2}{n\cdot\pi} - \frac{2}{n\cdot\pi}\cos(n\cdot\pi)$$

erhalten.

Der Funktionswert der Kosinusfunktion an den Stellen $t = n\cdot\pi$ springt
zwischen $-1$ und $1$ hin und her. Ist $n$ ungerade, dann ist
$\cos(n\cdot\pi)=-1$. Ist jedoch $n$ gerade, dann gilt $\cos(n\cdot\pi)=+1$.
Daher gilt für die Fourierkoeffizienten

$$b_n = \begin{cases} 0, \quad & n\text{ gerade}\\
\dfrac{4}{n\cdot\pi}, \quad & n\text{ ungerade}.\end{cases}$$

Jetzt können wir die Fourierreihe bilden:

\begin{align*} f(t) &= \frac{a_0}{2} + \sum_{n=1}^{\infty} \left(a_n \cos(n
\omega t) + b_n \sin(n \omega t) \right)\\
&= \frac{4}{1\cdot\pi}\sin(t) + \frac{4}{3\cdot\pi}\sin(3t) +
\frac{4}{5\cdot\pi}\sin(5t) + \ldots \end{align*}

Es wäre schön, eine kompaktere Angabe für die Fourierreihe zu benutzen. Dazu
benutzen wir den Trick, die ungeraden Zahlen als $2k-1$ darzustellen mit
$k\in\mathbb{N}$. Dann lautet die Fourierreihe nämlich

$$f(t) = \sum_{k=1}^{\infty}\frac{4}{(2k-1)\cdot\pi}\sin((2k-1) t) =
\frac{4}{\pi}\sum_{k=1}^{\infty}\frac{\sin((2k-1)t)}{2k-1}.$$

In dem folgenden Video wird das gleiche Beispiel vorgerechnet.

```{dropdown} Video "Fourier-Reihe der Rechtecksfunktion" von Hart und Trocken
<iframe width="560" height="315" src="https://www.youtube.com/embed/zy2SO_8tV9k?si=rbOAoHqzOhfEpzce" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

Ein weiteres Beispiel für die Berechnung einer Fourierreihe einer
Rechteckschwingung finden Sie in dem folgenden Video.

```{dropdown} Video "Fourierreihe Rechtecksimpuls" von Sciencebarbie
<iframe width="560" height="315" src="https://www.youtube.com/embed/dzkCRqKXZCs"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Die Sägezahnfunktion

Die Berechnungen der Fourierreihe der Sägezahnfunktion sind ähnlich lang wie das
obige Beispiel. Daher verzichten wir hier auf die textliche Erklärung. Bitte
schauen Sie sich das folgende Video an, wo die Fourierreihe detailliert
vorgerechnet wird.

```{dropdown} Video "Fourierreihe Sägezahnfunktion" von Sciencebarbie
<iframe width="560" height="315" src="https://www.youtube.com/embed/wGL_Cxorbac"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Die Dreiecksfunktion

Auch hier verzichten wir auf die textliche Erklärung. Bitte schauen Sie sich das
folgende Video an, wo die Fourierreihe der Dreiecksfunktion ausführlich
erläutert wird.

```{dropdown} Video "Fourierreihe Dreiecksimpuls" von Sciencebarbie
<iframe width="560" height="315" src="https://www.youtube.com/embed/-I0YqzFRldA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Zusammenfassung und Ausblick

Mit den Fourierreihen der Rechteck-, Sägezahn- und Dreieckschwingung haben wir
drei bekannte Beispiele für die Anwendung von Fourierreihen kennengelernt. Bei
der Berechnung der Fourierkoeffizienten der Rechteckschwingung haben wir
festgestellt, dass alle Fourierkoeffizienten des Kosinusanteils Null sind. Das
liegt daran, dass in diesem Beispiel die betrachtete Funktion ungerade war. Das
werden wir im nächsten Kapitel näher untersuchen.
