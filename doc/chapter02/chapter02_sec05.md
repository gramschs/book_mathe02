# Übungen

```{admonition} Übung 2.1
:class: miniexercise
Berechnen Sie den Mittelwert der Funktion $f(x)=\frac{1}{2}x^2 +1$ im Intervall $[0,2]$.
```

````{admonition} Lösung
:class: miniexercise, toggle
$$m = \frac{1}{2-0}\int_{0}^{2}\frac{1}{2}x^2 +1 \, dx = \frac{5}{3} \approx 1.6666$$
```{dropdown} Lösungsweg
<iframe width="560" height="315" src="https://www.youtube.com/embed/Y4cPEgR3LUg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
````

```{admonition} Übung 2.2
:class: miniexercise
Berechnen Sie den Mittelwert $\bar{f}$ der Funktion $f(x)=mx+n$ auf einem beliebigen Intervall $[a,b]$. Interpretieren Sie das Ergebnis geometrisch.
```

````{admonition} Lösung
:class: miniexercise, toggle
$$\bar{f} = \frac{1}{2}\left(f(a)+f(b)\right) $$ 
Der Mittelwert der linearen Funktion $f(x)=mx+n$ ist gerade das arithmetische Mittel der beiden Funktionswerte $f(a)$ und $f(b)$ an den Intervallgrenzen.
```{dropdown} Lösungsweg
Der Mittelwert einer Funktion $f$ im Intervall $[a,b]$ wird folgendermaßen berechnet:

$$\bar{f} = \frac{1}{b-a}\int_{a}^{b} f(x) \, dx.$$

Wir setzen die lineare Funktion $f(x)=mx+n$ in die Formel ein und erhalten:

\begin{align*}
\bar{f}
&= \frac{1}{b-a}\int_{a}^{b} mx+n \, dx = \\
&= \frac{1}{b-a} \left[\frac{1}{2}mx^2 + nx \right]_{a}^{b} = \\
&= \frac{1}{b-a} \left( (\frac{1}{2}mb^2 + nb) - (\frac{1}{2}ma^2 + na) \right) = \\
&= \frac{1}{b-a} \left( \frac{1}{2}\, m\, (b^2 - a^2) + n \, (b - a) \right) = \\
&= \frac{1}{2} m (b+a) + n = \\
&= \frac{1}{2} m b + \frac{1}{2} m a + \frac{1}{2}n + \frac{1}{2}n = \\
&= \frac{1}{2} (mb+n) + \frac{1}{2} (ma+n) = \\
&= \frac{1}{2} f(b) + \frac{1}{2} f(a).
\end{align*}

Der Mittelwert der linearen Funktion $f(x) = mx+n$ ist gleich dem arithmetischen Mittel der beiden Funktionswerte $f(a)$ und $f(b)$.
```
````

```{admonition} Übung 2.3
:class: miniexercise
Berechnen Sie den Flächeninhalt $A$, der zwischen dem Graphen der Funktion 

$$f(x)=x^2-x$$

und der x-Achse eingeschlossen ist. Fertigen Sie zuerst eine Skizze an.
```

````{admonition} Lösung
:class: miniexercise, toggle
$$A = \frac{1}{6}$$
```{dropdown} Lösungsweg
![solution03_03](pics/solution03_03.png)
```
````

```{admonition} Übung 2.4
:class: miniexercise
Berechnen Sie den Flächeninhalt $A$, der zwischen dem Graphen der Funktion 

$$f(x)=x(x-1)(x-3)$$

und der x-Achse eingeschlossen ist. Fertigen Sie zuerst eine Skizze an.
```

````{admonition} Lösung
:class: miniexercise, toggle
$$A = \frac{37}{12}$$
```{dropdown} Lösungsweg
Skizze des Funktionsgraphens:

![solution03_04_plot](pics/plot_exercise_03_04.png)

* Nullstellen berechnen: $f(x) = x(x-1)(x-3) = 0$ lösen
* Nullstellen: $x_1 = 0$, $x_2 = 1$ und $x_3 = 3$
* Erster Flächeninhalt:

$$A_1 = \int_{0}^{1} x^3 - 4x^2 + 3x \, dx = \frac{5}{12}$$

* Zweiter Flächeninhalt (negativ orientiert):

$$A_2 = \int_{1}^{3} x^3 - 4x^2 + 3x \, dx = -\frac{8}{3}$$

* Gesamtflächeninhalt: $A = A_1 + (-1)\cdot A_2 = \frac{37}{12}$
```
````

```{admonition} Übung 2.5
:class: miniexercise
Berechnen Sie den Flächeninhalt $A$, der zwischen den beiden Graphen der Funktionen 

$$f(x)=-\frac{1}{4}x^2+16 \quad \text{ und } \quad g(x)=-3x$$

eingeschlossen ist. Fertigen Sie zuerst eine Skizze an.
```

````{admonition} Lösung
:class: miniexercise, toggle
$$A = \frac{1000}{3}=333.33$$
```{dropdown} Lösungsweg
Skizze der beiden Funktionsgraphen:

![solution03_05_plot](pics/plot_exercise_03_05.png)

* Schnittpunkte berechnen: $f(x) = g(x)$ lösen
* Schnittpunkte: $x_1 = -4$ und $x_2 = 16$
* Flächeninhalt:

$$A = \int_{-4}^{16} \left(-\frac{1}{4}x^2 + 16\right) - \left(-3x \right)  \, dx = \frac{1000}{3}$$
```
````

```{admonition} Übung 2.6
:class: miniexercise
Berechnen Sie den Flächeninhalt $A$, der zwischen den beiden Graphen der Funktionen 

$$f(x)=-x^2+2x+\frac{1}{2} \quad \text{ und } \quad g(x)=x+2$$

und den parallelen Geraden $x=-2$ und $x=\frac{5}{2}$ eingeschlossen ist. Fertigen Sie zuerst eine Skizze an.
```

````{admonition} Lösung
:class: miniexercise, toggle
$$A = \frac{27}{2}= 13.5$$
```{dropdown} Lösungsweg
Skizze der beiden Funktionsgraphen:

![solution03_06_plot](pics/plot_exercise_03_06.png)

* $g$ ist oberhalb von $f$
* Flächeninhalt:

$$A = \int_{-2}^{5/2} \left( x+2 \right) - \left(-x^2+2x+\frac{1}{2} \right)  \, dx = \frac{27}{2}$$

```
````

```{admonition} Übung 2.7
:class: miniexercise
Berechnen Sie den Flächeninhalt $A$, der zwischen den beiden Graphen der Funktionen 

$$f(x)=-3x^2+x-1 \quad \text{ und } \quad g(x)=4\cdot (x-\frac{1}{4})^2-\frac{5}{4}$$

eingeschlossen ist. Fertigen Sie zuerst eine Skizze an.
```

````{admonition} Lösung
:class: miniexercise, toggle
$$A = \frac{9}{98}\approx 0.091837$$
```{dropdown} Lösungsweg
Skizze der beiden Funktionsgraphen:

![solution03_07_plot](pics/plot_exercise_03_07.png)

* Schnittpunkte berechnen: $f(x) = g(x)$ lösen
* Schnittpunkte: $x_1 = 0$ und $x_2 = \frac{3}{7}$
* Flächeninhalt:

$$A = \int_{0}^{3/7} \left(-3x^2+x-1\right) - \left(4\cdot (x-\frac{1}{4})^2-\frac{5}{4} \right)  \, dx = \frac{9}{98}$$

```
````

```{admonition} Übung 2.8
:class: miniexercise
Berechnen Sie den Flächeninhalt $A$, der zwischen den beiden Graphen der Funktionen 

$$f(x)=2\sin(x) \quad \text{ und } \quad g(x)=-\frac{4\sqrt{2}}{3\pi}x + \frac{4\sqrt{2}}{3}$$

eingeschlossen ist. Fertigen Sie zuerst eine Skizze an. Benutzen Sie einen Taschenrechner.
```

````{admonition} Lösung
:class: miniexercise, toggle
$$A = 4+2\sqrt{2} - \frac{3\pi}{2\sqrt{2}}\approx 3.49626$$
```{dropdown} Lösungsweg
Skizze der beiden Funktionsgraphen:

![solution03_08_plot](pics/plot_exercise_03_08.png)

* Schnittpunkte berechnen: $f(x) = g(x)$ lösen
* Schnittpunkte: $x_1 = \frac{\pi}{4}$,  $x_2 = \pi$ und $x_3 = \frac{7\pi}{4}$
* Erster Flächeninhalt:

$$A_1 = \int_{\pi/4}^{\pi} \left( 2\sin(x)\right) - \left(-\frac{4\sqrt{2}}{3\pi}x + \frac{4\sqrt{2}}{3} \right)  \, dx = -\frac{3}{4\sqrt{2}}\pi + 2 + \sqrt{2}$$

* Zweiter Flächeninhalt:

$$A_2 = \int_{\pi}^{\frac{7\pi}{4}} \left(-\frac{4\sqrt{2}}{3\pi}x + \frac{4\sqrt{2}}{3} \right) -
\left(2\sin(x) \right) \, dx = -\frac{3}{4\sqrt{2}}\pi + 2 + \sqrt{2}$$

* Gesamter Flächeninhalt:

$$A = A_1 + A_2 = \frac{1}{4}\left(-3\sqrt{2}\pi + 16 + 8\sqrt{2} \right) \approx 3.49626$$

```
````

```{admonition} Übung 2.9
:class: miniexercise
Berechnen Sie die Bogenlänge $L$ der Funktion $f(x)=x$ im Intervall $[0,1]$.
```

````{admonition} Lösung
:class: miniexercise, toggle
$$L = \sqrt{2} \approx 1.4142$$
```{dropdown} Lösungsweg
* Ableitung: $f'(x)=1$
* Bogenlänge: 

$$L = \int_{0}^{1} \sqrt{1+(1)^2}\, dx = \int_{0}^{1} \sqrt{2}\, dx = \sqrt{2}$$

```
````

```{admonition} Übung 2.10
:class: miniexercise
Berechnen Sie die Bogenlänge $L$ der Funktion $f(x)=x^{\frac{3}{2}}$ im Intervall $[0,1]$.
```

````{admonition} Lösung
:class: miniexercise, toggle
$$L \approx 1.4397$$
```{dropdown} Lösungsweg
* Ableitung: $f'(x) = \frac{3}{2} x^{\frac{1}{2}}$
* Bogenlänge:

$$L = \int_{0}^{1} \sqrt{1+(\frac{3}{2} x^{\frac{1}{2}})^2}\, dx = 
\int_{0}^{1} \sqrt{1+\frac{9}{4} x}\, dx  $$

* Substitution: $z = 1 + \frac{9}{4} x$, d.h. $dx = \frac{4}{9} dz$
* Daraus folgt:

$$L = \int_{0}^{1} \sqrt{1+\frac{9}{4} x}\, dx = \left[\frac{8}{27}\left(\frac{9x}{4}+1\right)^{3/2} \right]_{0}^{1} = \frac{1}{27}(13\sqrt{13}-8) \approx 1.4397.
$$

```
````

```{admonition} Übung 2.11
:class: miniexercise
Berechnen Sie das Volumen $V$ des Rotationskörpers, das entsteht, wenn die Funktion $f(x)=-x^2+4$ im Intervall $[-2,2]$ um die x-Achse gedreht wird.
```

````{admonition} Lösung
:class: miniexercise, toggle

$$V = 2\pi\cdot \frac{256}{15}\approx 107.23$$
```{dropdown} Lösungsweg
![solution03_11p](pics/solution03_11plot.png)
![solution03_11](pics/solution03_11.png)
```
````

```{admonition} Übung 2.12
:class: miniexercise
Berechnen Sie das Volumen $V$ des Rotationskörpers, das entsteht, wenn die Funktion $f(x)=\sin(x)+1$ im Intervall $[0,\frac{3\pi}{2}]$ um die x-Achse gedreht wird.
```

````{admonition} Lösung
:class: miniexercise, toggle

$$V = \pi\left((\frac{3\pi}{2}-0+\frac{3\pi}{4})-(0-2+0)\right)\approx 28.4898$$
```{dropdown} Lösungsweg
![solution03_12p](pics/solution03_12plot.png)
![solution03_12](pics/solution03_12.png)
```
````
