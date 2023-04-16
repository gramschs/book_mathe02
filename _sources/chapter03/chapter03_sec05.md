# Übungen

```{admonition} Übung 3.1
:class: miniexercise
Untersuchen Sie die Reihe 

$$ \sum_{n=1}^\infty -\frac{4\cdot3^{n+3}}{5^n}$$

auf sowohl mit dem Quotienten- als auch dem Wurzelkriterium auf Konvergenz.
```
````{admonition} Lösung
:class: minisolution, toggle
Die Reihe ist (absolut) konvergent. 
```{dropdown} Lösungsweg
Wir definieren $a_n := -\frac{4\cdot 3^{n+3}}{5^n}$. 
 
Wurzelkriterium: 

Zu bestimmen ist der Grenzwert (falls dieser existiert)  
\begin{align*} 
r & = \lim_{n\rightarrow \infty}\sqrt[n]{\left|a_n\right|}
    = \lim_{n\rightarrow \infty}{\left(\frac{4\cdot 3^{n+3}}{5^n}\right)}^{1/n}\\ 
& = \lim_{n\rightarrow \infty}\frac{3\cdot {108}^{1/n}}{5}
    = \frac{3}{5}. 
\end{align*} 
Wegen $r<1$ ist die Reihe (absolut) konvergent. 
 
Quotientenkriterium: 

Zu bestimmen ist der Grenzwert (falls dieser existiert) 
\begin{align*} 
r & = \lim_{n\rightarrow \infty} \left|\frac{a_{n+1}}{a_n}\right|
    =\lim_{n\rightarrow \infty}3^{n+4}\,\frac{1}{3^{n+3}}\,\frac{1}{5^{n+1}}\,5^n\\ 
& = \lim_{n\rightarrow \infty}\frac{3}{5}
    =\frac{3}{5}. 
\end{align*} 
Wegen $r<1$ ist die Reihe (absolut) konvergent.  
```
````

```{admonition} Übung 3.2
:class: miniexercise
Untersuchen Sie die Reihe 

$$\sum_{n=1}^\infty 4\frac{6^n}{{11}^{n+4}}$$

sowohl mit dem Quotienten- als auch dem Wurzelkriterium auf Konvergenz.
```

````{admonition} Lösung
:class: minisolution, toggle
Die Reihe ist (absolut) konvergent. 
```{dropdown} Lösungsweg
Wir definieren $a_n := 4\frac{6^n}{{11}^{n+4}}$. 

Wurzelkriterium: 
 Zu bestimmen ist der Grenzwert (falls dieser existiert)  
\begin{align*} 
r & = \lim_{n\rightarrow \infty}\sqrt[n]{\left|a_n\right|}
    = \lim_{n\rightarrow \infty}{\left(4\frac{6^n}{{11}^{n+4}}\right)}^{1/n}\\ 
& = \lim_{n\rightarrow \infty}\frac{6\,{\left(\frac{4}{14641}\right)}^{1/n}}{11}
    = \frac{6}{11}. 
\end{align*} 
Wegen $r<1$ ist die Reihe (absolut) konvergent. 
 
Quotientenkriterium: 
Zu bestimmen ist der Grenzwert (falls dieser existiert) 
\begin{align*} 
r & = \lim_{n\rightarrow \infty} \left|\frac{a_{n+1}}{a_n}\right|
    =\lim_{n\rightarrow \infty}\frac{6^{n+1}\,{11}^{n+4}\,\frac{1}{{11}^{n+5}}}{6^n}\\ 
& = \lim_{n\rightarrow \infty}\frac{6}{11}
    =\frac{6}{11}. 
\end{align*} 
Wegen $r<1$ ist die Reihe (absolut) konvergent.  
```
````


```{admonition} Übung 3.3
:class: miniexercise
Untersuchen Sie die Reihe 

$$\sum_{n=1}^\infty \frac{\frac{1}{{\left(-8\right)}^{n+2}}\,{10}^{n+4}}{4}$$

sowohl mit dem Quotienten- als auch dem Wurzelkriterium auf Konvergenz.
```

````{admonition} Lösung
:class: minisolution, toggle
Die Reihe ist divergent.
```{dropdown} Lösungsweg
Die Summanden bilden keine Nullfolge, denn 

$$\lim_{n\rightarrow \infty} \left| \frac{\frac{1}{{\left(-8\right)}^{n+2}}\,{10}^{n+4}}{4}\right| =\infty \,.$$

Somit divergiert die Reihe. Die Anwendung des Wurzel- sowie des Quotientenkriteriums erübrigt sich. 
```
````

```{admonition} Übung 3.4
:class: miniexercise
Bestimmen Sie den Konvergenzradius $r$ der Potenzreihe 

$$\sum_{n=1}^{\infty}\frac{8^n}{n}\cdot(x-2)^n.$$

Untersuchen Sie gegebenenfalls die Konvergenz im Randbereich und geben Sie den Konvergenzbereich an.
```
````{admonition} Lösung
:class: minisolution, toggle
Konvergenzradius $r=\frac{1}{8}$ und Konvergenzbereich: $[\frac{15}{8}; \frac{17}{8})$, d.h. $\frac{15}{8} \leq x < \frac{17}{8}$
```{dropdown} Lösungsweg
Tipp bzw. Quelle der Aufgabe:  [YouTube MathemaTrick -- Konvergenzradius bestimmen](https://www.youtube.com/watch?v=gn8jCoSJb24) 

Wir definieren $a_n := \frac{8^n}{n}$. Nach der Formel von Cauchy-Hadamard (Wurzelkriterium) wird der Konvergenzradius $r$ berechnet als

$$r = \lim_{n\rightarrow \infty} \frac{1}{\sqrt[n]{\left|a_n\right|}}$$

Wir rechnen zuerst in einer Nebenrechnung

$$\sqrt[n]{|a_n|} = \sqrt[n]{\left|\frac{8^n}{n}\right|} = \sqrt[n]{\frac{8^n}{n}} = \frac{\sqrt[n]{8^n}}{\sqrt[n]{n}} = \frac{8}{\sqrt[n]{n}}. $$

Eingesetzt in die Wurzel-Formel ist dies

$$r = \lim_{n\rightarrow \infty} \frac{1}{\sqrt[n]{\left|a_n\right|}} = \lim_{n\to \infty} \frac{\sqrt[n]{n}}{8} = \lim_{n\to\infty}\frac{n^{\frac{1}{n}}}{8} = \frac{1}{8}.$$

Die Potenzreihe konvergiert absolut im Intervall $(\frac{15}{8}; \frac{17}{8})$. Das Konvergenzverhalten an den Randpunkten muss jedoch gesondert untersucht werden. 

Durch das Einsetzen einer der Randpunkte in die Potenzreihe reduziert sich diese auf eine Zahlenreihe. Die Konvergenzfrage lässt sich dann mit einem passenden Konvergenz- oder Divergenzkriterium für Reihen angehen. 

Setzt man den linken Randpunkt $x=\frac{15}{9}$ ein, so erhält man: 
\begin{align*}
\sum_{n=1}^{\infty} \frac{8^n}{n}\cdot\left(\frac{15}{8}-2\right)^n 
&= \sum_{n=1}^{\infty} \frac{8^n}{n}\cdot\left(-\frac{1}{8}\right)^n \\
&= \sum_{n=1}^{\infty} \frac{8^n}{n}\cdot \frac{(-1)^n}{8^n} 
+ \sum_{n=1}^{\infty} \frac{(-1)^n}{n}. 
\end{align*}
Diese Reihe konvergiert (gegen $-\ln(2)$), der linke Randpunkt gehört zum Konvergenzbereich.

Setzt man den rechten Randpunkt $x=\frac{17}{8}$ ein, so erhält man: 
\begin{align*}
\sum_{n=1}^\infty \frac{8^n}{n}\cdot\left(\frac{17}{8}-2\right)^n 
&= \sum_{n=1}^{\infty} \frac{8^n}{n}\cdot\left(\frac{1}{8}\right)^n \\
&= \sum_{n=1}^{\infty} \frac{8^n}{n}\cdot\frac{1^n}{8^n} \\
& = \sum_{n=1}^{\infty} \frac{1}{n}.
\end{align*}
Diese Reihe divergiert, der rechte Randpunkt gehört *nicht* zum Konvergenzbereich.

Antwort: Konvergenzradius $r=\frac{1}{8}$ und Konvergenzbereich: $[\frac{15}{8}; \frac{17}{8})$, d.h. $\frac{15}{8} \leq x < \frac{17}{8}$ 
```
````


