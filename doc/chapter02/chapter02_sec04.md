# 2.4 Volumen von Rotationskörpern

In diesem Abschnitt beschäftigen wir uns mit Rotationskörpern. Rotationskörper
werden manchmal auch Drehkörper genannt. Ein Rotationskörper ist ein
dreidimensionales Objekt, das durch die Rotation einer Fläche um eine Achse
erzeugt wird. Der Rotationskörper wird durch die Form der rotierten Fläche sowie
die Achse, um die sie gedreht wird, bestimmt.

## Lernziele 

```{admonition} Lernziele
:class: important
Sie können das **Volumen eines Rotationskörpers** berechnen, der dadurch
entsteht, dass eine Kurve
*  um die x-Achse gedreht wird:

$$V = \pi \int_{a}^{b} f(x)^2 \, dx,$$

*  um die y-Achse gedreht wird:

$$V = \pi \int_{f(a)}^{f(b)} \left(f^{-1}(y) \right)^2 \, dy .$$
```


## Rotation um x-Achse

Die Berechnung des Volumens eines Rotationskörpers kann durch Integration
erfolgen. Die grundlegende Idee ist, dass das Volumen des Rotationskörpers als
Summe von dünnen Scheiben, die senkrecht zur Rotationsachse stehen, dargestellt
werden kann. Die Berechnung des Volumens erfolgt dann durch Integration der
Fläche dieser Scheiben entlang der Rotationsachse.

Konkret betrachten wir nun die Rotation um die x-Achse. Die Fläche, die um die
x-Achse gedreht werden soll, soll oben durch die Funktion $f$, unten durch die
x-Achse sowie links durch die Gerade $x=a$ und rechts durch Gerade $x=b$
begrenzt werden. Dann wird das Volumen $V$ des Rotationskörpers mit der Formel

$$V = \pi \int_a^b f(x)^2 \, dx$$

berechnet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/mk7PZfAmB1g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Rotation um y-Achse

Eine Methode zur Berechnung des Volumens eines Rotationskörpers, der um die
y-Achse gedreht wird, ist die Verwendung der Umkehrfunktion. Wir können die
x-Achse als Rotationsachse betrachten, indem wir die Funktion $f(x)$ durch ihre
Umkehrfunktion $f^{-1}(y)$ ersetzen.

Wenn wir die Funktion $f(x)$ um die y-Achse drehen, erhalten wir einen
Rotationskörper mit der Form des Querschnitts um die y-Achse. Um das Volumen
dieses Rotationskörpers zu berechnen, können wir das Volumen der umgedrehten
Funktion um die x-Achse berechnen. Das Volumen des Rotationskörpers ist dann das
gleiche wie das Volumen des umgedrehten Körpers.

Die Formel zur Berechnung des Volumens eines Rotationskörpers, der um die
y-Achse gedreht wird, ist gegeben durch:

$$V = \pi  \int_c^d  (f^{-1}(y))^2 \, dy ,$$

wobei $c = f(a)$ und $d = f(b)$ die Grenzen der Integration sind und $f^{-1}(y)$ die
Umkehrfunktion von $f(x)$ ist.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Jv1DrugW1nk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>