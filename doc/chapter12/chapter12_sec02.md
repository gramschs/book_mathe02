# 12.2 Lösung homogene lineare DGL 1. Ordnung

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```



## Wie wird eine homogene lineare DGL 1. Ordnung gelöst?

Zuerst betrachten wir eine homogene lineare DGL 1. Ordnung, also

$$a_1(x)y' + a_0(x)y = 0.$$

Das ist eine separable DGL und die allgemeine Lösung lautet

$$y_h(x)=C \cdot e^{-\int \frac{a_0(x)}{a_1(x)}\, dx}.$$

Beispiel:

Gegeben ist die homogene lineare DGL 1. Ordnung

$$y'+3y=0,$$

also $a_1(x)=1$ und $a_0(x)=3$. Damit ist die allgemeine homogene Lösung der DGL

$$y_h(x)=C \cdot e^{-\int \frac{3}{1}\, dx} = C\cdot e^{-3x}.$$

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/Sm0Go9IioJ4
```
