# Übungen


```{admonition} Übung 4.1
:class: tip
Berechnen Sie das Taylorpolynom der Ordnung 3 

$$f(x) = \frac{1}{x+1}$$

für die Entwicklungspunkte $x_0 = 0$ und $x_0 = 1$. 
```
````{admonition} Lösung
:class: tip, toggle
Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=0$ ist 
 \begin{equation*} 
    T_{3}(x) = 1-x+x^2-x^3 .
 \end{equation*} 

 Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=1$ ist 
 \begin{equation*} 
    T_{3}(x)=  \frac{1}{2}
    -\frac{1}{4}\cdot(x-1)^{1}
    +\frac{1}{8}\cdot(x-1)^{2}
    -\frac{1}{16}\cdot(x-1)^{3}.
 \end{equation*} 
```{dropdown} Lösungsweg
Die ersten drei Ableitungen von $f(x) = \frac{1}{x+1}$ lauten: 
 \begin{align*} 
 f^\prime(x)&=-\frac{1}{{\left(x+1\right)}^2} \\ 
 f^{\prime \prime}(x)&=\frac{2}{{\left(x+1\right)}^3} \\ 
 f^{(3)}(x)&=-\frac{6}{{\left(x+1\right)}^4} 
  \end{align*} 
 Die allgemeine Darstellung eines Taylorpolynoms von $f$ vom Grad 3 im Entwicklungspunkt $x_0$ lautet 
 \begin{equation*} 
    T_{3}(x)\  =\  f(x_0)
         +\frac{f^\prime(x_0)}{1!}(x-x_0)^{1}
         +\frac{f^{\prime\prime}(x_0)}{2!}(x-x_0)^{2}
         +\frac{f^{(3)}(x_0)}{3!}(x-x_0)^{3}.
 \end{equation*} 
Es gilt für $x_0=0$:

$$f(0) = 1, \quad f'(0)=-1, \quad f''(0)= 2, \quad f^{(3)}(0)=-6.$$

Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=0$ ist 
 \begin{equation*} 
    T_{3}(x)=  1
   -1 \cdot(x-0)^{1}
 + 1 \cdot(x-0)^{2}
   -1 \cdot(x-0)^{3} = 1-x+x^2-x^3 .
 \end{equation*} 
 Es gilt für $x_0=1$:

 $$f(1) = \frac{1}{2}, \quad f'(1)=-\frac{1}{4}, \quad f''(1)= \frac{1}{4}, \quad f^{(3)}(1)=-\frac{6}{16}.$$

 Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=1$ ist 
 \begin{equation*} 
    T_{3}(x)=  \frac{1}{2}
    -\frac{1}{4}\cdot(x-1)^{1}
    +\frac{1}{8}\cdot(x-1)^{2}
    -\frac{1}{16}\cdot(x-1)^{3}.
 \end{equation*} 
```
````

```{admonition} Übung 4.2
:class: tip
Berechnen Sie das Taylorpolynom der Ordnung 3 

$$f(x) = \sqrt{x+1}$$

für die Entwicklungspunkte $x_0 = 0$ und $x_0 = 1$. 
```
````{admonition} Lösung
:class: tip, toggle
 Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=0$ ist 
 \begin{equation*} 
    T_{3}(x)
    = 1 + \frac{1}{2}x -\frac{1}{8}x^2 +\frac{1}{16}x^3.
 \end{equation*} 

Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=1$ ist 
 \begin{equation*} 
    T_{3}(x)=  \sqrt{2}
    +\frac{\sqrt{2}}{4}\cdot(x-1)^{1}
    -\frac{\sqrt{2}}{32}\cdot(x-1)^{2}
    +\frac{\sqrt{2}}{128}\cdot(x-1)^{3}\ .
 \end{equation*} 
```{dropdown} Lösungsweg
Die ersten drei Ableitungen von $f(x) = \sqrt{x+1}$ lauten: 
 \begin{align*} 
 f^\prime(x)&=\frac{1}{2\,\sqrt{x+1}} \\ 
 f^{\prime \prime}(x)&=-\frac{1}{4\,{\left(x+1\right)}^{3/2}} \\ 
 f^{(3)}(x)&=\frac{3}{8\,{\left(x+1\right)}^{5/2}} 
  \end{align*} 
 Die allgemeine Darstellung eines Taylorpolynoms von $f$ vom Grad 3 im Entwicklungspunkt $x_0$ lautet 
 \begin{equation*} 
    T_{3}(x)\  =\  f(x_0) 
         +\frac{f^\prime(x_0)}{1!}(x-x_0)^{1}
         +\frac{f^{\prime\prime}(x_0)}{2!}(x-x_0)^{2}
         +\frac{f^{(3)}(x_0)}{3!}(x-x_0)^{3}.
 \end{equation*} 
 Es gilt für $x_0=0$:

$$f(0) = 1, \quad f'(0)=\frac{1}{2}, \quad f''(0)=-\frac{1}{4}, \quad f^{(3)}(0)=\frac{3}{8}.$$

 Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=0$ ist 
 \begin{equation*} 
    T_{3}(x)=  1
    +\frac{1}{2}\cdot(x-0)^{1}
    -\frac{1}{8}\cdot(x-0)^{2}
    +\frac{1}{16}\cdot(x-0)^{3}
    = 1 + \frac{1}{2}x -\frac{1}{8}x^2 +\frac{1}{16}x^3.
 \end{equation*} 
Es gilt für $x_0=1$:

$$f(1) = \sqrt{2}, \quad f'(1)=\frac{\sqrt{2}}{4}, \quad f''(1)=-\frac{\sqrt{2}}{16}, \quad f^{(3)}(1)=\frac{3\sqrt{2}}{64}.$$

Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=1$ ist 
 \begin{equation*} 
    T_{3}(x)=  \sqrt{2}
    +\frac{\sqrt{2}}{4}\cdot(x-1)^{1}
    -\frac{\sqrt{2}}{32}\cdot(x-1)^{2}
    +\frac{\sqrt{2}}{128}\cdot(x-1)^{3}\ .
 \end{equation*} 
```
````

```{admonition} Übung 4.3
:class: tip
Berechnen Sie das Taylorpolynom der Ordnung 3 

$$f(x) = \ln((1+x)^2)$$

für den Entwicklungspunkt $x_0 = 0$. 
```
````{admonition} Lösung
:class: tip, toggle
Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=0$ ist 
 \begin{equation*} 
    T_{3}(x) = 2x - x^{2} +\frac{2}{3}x^{3}.
 \end{equation*} 
```{dropdown} Lösungsweg
Die ersten drei Ableitungen von $f(x) = \ln((1+x)^2)$ lauten: 
\begin{align*}
f'(x)  &= \frac{2}{1+x}\\
f''(x) &= -\frac{2}{(1+x)^2} \\
f^{(3)}(x) &= \frac{4}{(1+x)^3}
\end{align*}
Die allgemeine Darstellung eines Taylorpolynoms von $f$ vom Grad 3 im Entwicklungspunkt $x_0$ lautet 
\begin{equation*} 
    T_{3}(x)\  =\  f(x_0) 
         +\frac{f^\prime(x_0)}{1!}(x-x_0)^{1}
         +\frac{f^{\prime\prime}(x_0)}{2!}(x-x_0)^{2}
         +\frac{f^{(3)}(x_0)}{3!}(x-x_0)^{3}.
\end{equation*} 
Es gilt für $x_0=0$:

$$f(0) = 0, \quad f'(0)=2, \quad f''(0)=-2, \quad f^{(3)}(0)=4.$$

Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=0$ ist 
 \begin{equation*} 
    T_{3}(x)= 0
    +2\cdot(x-0)^{1}
    -(x-0)^{2}
    +\frac{2}{3}\cdot(x-0)^{3}
= 2x - x^{2} +\frac{2}{3}x^{3}.
 \end{equation*} 
```
````

```{admonition} Übung 4.4
:class: tip
Berechnen Sie das Taylorpolynom der Ordnung 3 

$$f(x) = \ln\left(\frac{1+x}{1-x} \right)$$

für den Entwicklungspunkt $x_0 = 0$. 
```
````{admonition} Lösung
:class: tip, toggle
Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=0$ ist 
 \begin{equation*} 
    T_{3}(x) = 2x +\frac{2}{3}x^{3}.
 \end{equation*}
```{dropdown} Lösungsweg
Die ersten drei Ableitungen von $f(x) = \ln\left(\frac{1+x}{1-x} \right)$ lauten: 
\begin{align*}
f'(x)  &= -\frac{2}{x^2-1}\\
f''(x) &= \frac{4x}{(x^2-1)^2} \\
f^{(3)}(x) &= -\frac{4(3x^2+1)}{(x^2-1)^3}
\end{align*}
Die allgemeine Darstellung eines Taylorpolynoms von $f$ vom Grad 3 im Entwicklungspunkt $x_0$ lautet 
\begin{equation*} 
    T_{3}(x)\  =\  f(x_0) 
         +\frac{f^\prime(x_0)}{1!}(x-x_0)^{1}
         +\frac{f^{\prime\prime}(x_0)}{2!}(x-x_0)^{2}
         +\frac{f^{(3)}(x_0)}{3!}(x-x_0)^{3}.
\end{equation*} 
Es gilt für $x_0=0$:

$$f(0) = 0, \quad f'(0)=2, \quad f''(0)=0, \quad f^{(3)}(0)=4.$$

Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=0$ ist 
 \begin{equation*} 
    T_{3}(x)= 0
    +2\cdot(x-0)^{1}
    +0\cdot(x-0)^{2}
    +\frac{4}{6}\cdot(x-0)^{3}
= 2x +\frac{2}{3}x^{3}.
 \end{equation*} 
```
````

```{admonition} Übung 4.5
:class: tip
Berechnen Sie das Taylorpolynom der Ordnung 3 

$$f(x) = \sin(x^2)$$

für den Entwicklungspunkt $x_0 = 0$. 
```
````{admonition} Lösung
:class: tip, toggle
Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=0$ ist 
 \begin{equation*} 
 T_{3}(x) =  x^2.
 \end{equation*}  
```{dropdown} Lösungsweg
Die ersten drei Ableitungen von $f(x) = \sin(x^2)$ lauten: 
 \begin{align*} 
 f^\prime(x)&=2\,x\,\cos\left(x^2\right) \\ 
 f^{\prime \prime}(x)&=2\,\cos\left(x^2\right)-4\,x^2\,\sin\left(x^2\right) \\ 
 f^{(3)}(x)&=-12\,x\,\sin\left(x^2\right)-8\,x^3\,\cos\left(x^2\right) 
  \end{align*} 
 Die allgemeine Darstellung eines Taylorpolynoms von $f$ vom Grad 3 im Entwicklungspunkt $x_0$ lautet 
 \begin{equation*} 
    T_{3}(x)\  =\  \frac{f(x_0)}{0!} 
         +\frac{f^\prime(x_0)}{1!}(x-x_0)^{1}
         +\frac{f^{\prime\prime}(x_0)}{2!}(x-x_0)^{2}
         +\frac{f^{(3)}(x_0)}{3!}(x-x_0)^{3}.
 \end{equation*} 
Es gilt für $x_0=0$:

$$f(0) = 0, \quad f'(0)=0, \quad f''(0)=2, \quad f^{(3)}(0)=0.$$
 
 Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=0$ ist 
 \begin{equation*} 
 T_{3}(x)=  0
 + 0 \cdot(x-0)^{1}
 + \frac{2}{2} \cdot(x-0)^{2}
 + \frac{0}{6} \cdot(x-0)^{3}
 = x^2.
 \end{equation*}  
```
````

```{admonition} Übung 4.6
:class: tip
Berechnen Sie das Taylorpolynom der Ordnung 3 

$$f(x)=x^3\,\left(\ln\left(x\right)-3\right)$$

für den Entwicklungspunkt $x_0 = 3$. 
```
````{admonition} Lösung
:class: tip, toggle
Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=3$ ist 
 \begin{equation*} 
    T_{3}(x)=  27\,\ln\left(3\right)-81
    +(27\,\ln\left(3\right)-72)\cdot(x-3)^{1}
    +(9\,\ln\left(3\right)-\frac{39}{2})\cdot(x-3)^{2}
    +(\ln\left(3\right)-\frac{7}{6})\cdot(x-3)^{3}\ .
\end{equation*} 
```{dropdown} Lösungsweg
Die ersten drei Ableitungen von $f(x)=x^3\,\left(\ln\left(x\right)-3\right)$ lauten: 
 \begin{align*} 
 f^\prime(x)&=3\,x^2\,\left(\ln\left(x\right)-3\right)+x^2 \\ 
 f^{\prime \prime}(x)&=5\,x+6\,x\,\left(\ln\left(x\right)-3\right) \\ 
 f^{(3)}(x)&=6\,\ln\left(x\right)-7 
  \end{align*} 
 Die allgemeine Darstellung eines Taylorpolynoms von $f$ vom Grad 3 im Entwicklungspunkt $x_0$ lautet 
 \begin{equation*} 
    T_{3}(x)\  =\  \frac{f(x_0)}{0!} 
         +\frac{f^\prime(x_0)}{1!}(x-x_0)^{1}
         +\frac{f^{\prime\prime}(x_0)}{2!}(x-x_0)^{2}
         +\frac{f^{(3)}(x_0)}{3!}(x-x_0)^{3}.
 \end{equation*} 
Es gilt für $x_0=3$:

$$f(3) = 27\ln(3)-81, \; f'(3)=27\ln(3)-72, \; f''(3)=18\ln(3)-39, \; f^{(3)}(3)=6\ln(3)-7.$$

 Das Taylorpolynom von $f$ im Entwicklungspunkt $x_{0}=3$ ist 
 \begin{equation*} 
    T_{3}(x)=  27\,\ln\left(3\right)-81
    +(27\,\ln\left(3\right)-72)\cdot(x-3)^{1}
    +(9\,\ln\left(3\right)-\frac{39}{2})\cdot(x-3)^{2}
    +(\ln\left(3\right)-\frac{7}{6})\cdot(x-3)^{3}\ .
\end{equation*} 
```
````

## Weitere Übungsaufgaben

Gerne können Sie sich mit dem MATEX-Aufgabengenerator weitere Übungsaufgaben generieren:

* [Übungsaufgaben Taylorpolynome Grad 1 bis Grad 4 einstellbar](https://lx4.mint-kolleg.kit.edu/MATeX/generatorview.php?data=M2pQQmg2bW9rcWV2THpFY0lXeWo5Zz09)



