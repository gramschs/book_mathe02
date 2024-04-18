# Übungen

```{admonition} Übung 7.1
:class: miniexercise
Berechnen Sie die ersten partiellen Ableitungen nach den Variablen.
a) $f(x,y)=e^{x}\cdot e^{y}$ <br>
b) $f(x,y)=e^{xy}$ <br>
c) $f(x,y)=\sin(x)\cos(y)$ <br>
d) $f(x_1,x_2,x_3) = \frac{1}{2x_1^2+\sqrt{x_2^2+x_3^2}}$ <br>
```
````{admonition} Lösung
:class: miniexercise, toggle
a) $f(x,y)=e^{x}\cdot e^{y}$

$$\frac{\partial f}{\partial x}=e^x\cdot e^y \quad \text{ und } \quad \frac{\partial f}{\partial y}=e^x\cdot e^y$$

b) $f(x,y)=e^{xy}$

$$\frac{\partial f}{\partial x}=ye^{xy} \quad \text{ und } \quad \frac{\partial f}{\partial y}=xe^{xy}$$

c) $f(x,y)=\sin(x)\cos(y)$

$$\frac{\partial f}{\partial x}=\cos(x)\cos(y) \quad \text{ und } \quad \frac{\partial f}{\partial y}=\sin(x)\left(-\sin(y)\right)$$

d) $f(x_1,x_2,x_3) = \frac{1}{2x_1^2+\sqrt{x_2^2+x_3^2}}$
\begin{align*}
\frac{\partial f}{\partial x_1}&=-\frac{1}{(2x_1^2+\sqrt{x_2^2+x_3^2})^2}\cdot 4x_1 \\
\frac{\partial f}{\partial x_2}&=-\frac{1}{(2x_1^2+\sqrt{x_2^2+x_3^2})^2}\cdot \frac{x_2}{\sqrt{x_2^2+x_3^2}}\\
\frac{\partial f}{\partial x_3}&=-\frac{1}{(2x_1^2+\sqrt{x_2^2+x_3^2})^2}\cdot \frac{x_3}{\sqrt{x_2^2+x_3^2}}
\end{align*}
````

```{admonition} Übung 7.2
:class: miniexercise
Berechnen Sie die zweiten partiellen Ableitungen nach den Variablen. Verifizieren Sie, dass das Ergebnis unabhängig von der Reihenfolge der Differentiationsschritte ist.

a) $f(x,y)=x^3+y^3 + x^2y^2+xy+1$ <br>
b) $f(x,y,z)=\frac{1}{\sqrt{x^2+y^2+z^2}}$ 
```
````{admonition} Lösung
:class: miniexercise, toggle
a) $f(x,y)=x^3+y^3 + x^2y^2+xy+1$ 

1\. partielle Ableitungen:
\begin{align*}
\frac{\partial f}{\partial x} &= 3x^2+2xy^2+y \\
\frac{\partial f}{\partial y} &= 3y^2+2x^2y+x 
\end{align*}
2\. partielle Ableitungen:
\begin{align*}
\frac{\partial^2 f}{\partial x \partial x} &= 6x + 2y^2 \\
\frac{\partial^2 f}{\partial x \partial y} &= \frac{\partial^2 f}{\partial y \partial x} = 4xy + 1 \\
\frac{\partial^2 f}{\partial y \partial y} &= 6y + 2x^2 
\end{align*}

b) $f(x,y,z)=\frac{1}{\sqrt{x^2+y^2+z^2}}$ 

1\. partielle Ableitungen:
\begin{align*}
\frac{\partial f}{\partial x} &= -\frac{x}{\left(\sqrt{x^2+y^2+z^2}\right)^3} \\
\frac{\partial f}{\partial y} &= -\frac{y}{\left(\sqrt{x^2+y^2+z^2}\right)^3} \\
\frac{\partial f}{\partial z} &= -\frac{z}{\left(\sqrt{x^2+y^2+z^2}\right)^3} \\
\end{align*}

2\. partielle Ableitungen:
\begin{align*}
\frac{\partial^2 f}{\partial x \partial x} &= -\frac{1}{\left(\sqrt{x^2+y^2+z^2}\right)^3}+3\frac{x^2}{\left(\sqrt{x^2+y^2+z^2}\right)^5}\\ 
\frac{\partial^2 f}{\partial y \partial y} &= -\frac{1}{\left(\sqrt{x^2+y^2+z^2}\right)^3}+3\frac{y^2}{\left(\sqrt{x^2+y^2+z^2}\right)^5}\\ 
\frac{\partial^2 f}{\partial z \partial z} &= -\frac{1}{\left(\sqrt{x^2+y^2+z^2}\right)^3}+3\frac{z^2}{\left(\sqrt{x^2+y^2+z^2}\right)^5}
\end{align*}
\begin{align*}
\frac{\partial^2 f}{\partial y \partial x} &= \frac{\partial^2 f}{\partial x \partial y} = \frac{3xy}{\left(\sqrt{x^2+y^2+z^2}\right)^5}\\ 
\frac{\partial^2 f}{\partial z \partial x} &= \frac{\partial^2 f}{\partial x \partial z} = \frac{3xz}{\left(\sqrt{x^2+y^2+z^2}\right)^5}\\ 
\frac{\partial^2 f}{\partial z \partial y} &= \frac{\partial^2 f}{\partial y \partial z} = \frac{3yz}{\left(\sqrt{x^2+y^2+z^2}\right)^5}
\end{align*}
````

```{admonition} Übung 7.3
:class: miniexercise
Berechnen Sie die dritten partiellen Ableitungen. Nutzen Sie aus, dass das Ergebnis unabhängig von der Reihenfolge der Differentiationsschritte ist:

$$f(x,y,z)=x^2y^2z^2+x^3+y^3+z^3.$$

Hinweis: wie viele partielle Ableitungen 3. Ordnung gibt es bei drei Variablen? Wie viele muss man explizit ausrechnen?
```
````{admonition} Lösung
:class: miniexercise, toggle
Es gibt insgesamt 27 Ableitungen 3. Ordnung, aber es genügen 10 explizite Ableitungen: xxx, yxx, zxx, yyy, xyy, zyy, zzz, xzz, yzz, xyz.

1\. partielle Ableitungen:
\begin{align*}
\frac{\partial f}{\partial x} &= 2xy^2z^2 + 3x^2 \\
\frac{\partial f}{\partial y} &= 2x^2yz^2 + 3y^2 \\
\frac{\partial f}{\partial z} &= 2x^2y^2z + 3z^2 \\
\end{align*}

Zwischenrechnung 2. partielle Ableitungen:
\begin{align*}
\frac{\partial^2 f}{\partial x \partial x} &= 2y^2z^2 + 6x \\ 
\frac{\partial^2 f}{\partial y \partial y} &= 2x^2z^2 + 6y \\ 
\frac{\partial^2 f}{\partial z \partial z} &= 2x^2y^2 + 6z \\ 
\end{align*}

3\. partielle Ableitungen:
\begin{align*}
\frac{\partial^3f}{\partial x \partial x \partial x} &= 6 \\ 
\frac{\partial^3f}{\partial y \partial x \partial x} &= 4yz^2 \\
\frac{\partial^3f}{\partial z \partial x \partial x} &= 4y^2z 
\end{align*}
\begin{align*}
\frac{\partial^3f}{\partial y \partial y \partial y} &= 6 \\  
\frac{\partial^3f}{\partial x \partial y \partial y} &= 4xz^2 \\
\frac{\partial^3f}{\partial z \partial y \partial y} &= 4x^2z 
\end{align*}
\begin{align*}  
\frac{\partial^3f}{\partial z \partial z \partial z} &= 6 \\  
\frac{\partial^3f}{\partial x \partial z \partial z} &= 4xy^2 \\   
\frac{\partial^3f}{\partial y \partial z \partial z} &= 4x^2y 
\end{align*}
\begin{equation*}
\frac{\partial^3f}{\partial z \partial y \partial x} = 8xyz             
\end{equation*}
````