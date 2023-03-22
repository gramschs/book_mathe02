# Partielle Integration

Wird ein Produkt abgeleitet, ist es etwas komplizierter. Es darf nicht einfach
jeder Faktor für sich abgeleitet werden, sondern es gilt die Produktregel:

$$\left( u(x)\cdot v(x)\right)^{\prime} = u^{\prime}(x)\cdot v(x) +
u(x)\cdot v^{\prime}(x).$$

Da Integration die Umkehrung der Ableitung ist, dürfen Produkte auch nicht
einfach so integriert werden. Dafür gibt es die Produktregel für Integrale, die
offiziell **partielle Integration** heißt.

## Lernziele

```{admonition} Lernziele
:class: hint
Sie können ein Produkt von zwei Funktionen $u\cdot v$ mit der partiellen
Integrationsregel im Intervall $[a,b]$ integrieren: 

$$\int_{a}^{b} u(x) \cdot
v'(x) \, dx = \big[u(x)\cdot v(x)\big]_{a}^{b} 
- \int_{a}^{b} v(x) \cdot u'(x) \, dx.$$
```

## Integrieren von Produkten

Die partielle Integration kann durch folgende Formel ausgedrückt werden:

$$\int_{a}^{b} u(x) \cdot v'(x) \, dx = \big[u(x)\cdot v(x)\big]_{a}^{b} 
- \int_{a}^{b} v(x) \cdot u'(x) \, dx.$$

Hierbei sind $u(x)$ und $v(x)$ zwei Funktionen, deren Produkt integriert werden
soll, und $u'(x)$ und $v'(x)$ sind die Ableitungen von $u(x)$ und $v(x)$.

## Beispiel für partielle Integration

Ein Beispiel für die Anwendung der partiellen Integration ist die Berechnung des
Integrals 

$$\int_{0}^{\pi} \sin(x)\cdot 2x \, dx.$$

Als erstes müssen wir auswählen, welche Funktion $u$ sein soll und was $v$. Wir wählen

$$u(x)=2x \quad \text{ und } \quad v'(x)=\sin(x).$$

Dann werden in einer Nebenrechnung die Ableitung $u^{\prime}$ von $u$ und eine
Stammfunktion $v$ von $v^{\prime}$ ausgerechnet:

$$u^{\prime}(x) = 2 \quad \text{ und } \quad v(x)=-\cos(x).$$

Das wird alles in die obige Formel eingesetzt:

$$\int_{0}^{\pi} \sin(x)\cdot 2x \, dx = \big[2x \cdot \cos(x)\big]_{0}^{\pi} -
\int_{0}^{\pi} 2 \cdot (-\cos(x)) \, dx.$$

Aber von der Funktion $v(x)=-\cos(x)$ kennen wir ebenfalls eine Stammfunktion,
nämlich $V(x)=-\sin(x)$. Daher kann das bestimmte Integral $\int_{0}^{\pi} 2
\cdot (-\cos(x)) \, dx$ noch weiter ausgerechnet werden und insgesamt gilt dann:

$$\int_{0}^{\pi} \sin(x)\cdot 2x \, dx = \big[2x \cdot \cos(x)\big]_{0}^{\pi} -
2 \big[-\sin(x)\big]_{0}^{\pi}.$$

Jetzt werden obere und untere Grenze eingesetzt und die Differenz gebildet. Das
Ergebnis ist

$$\int_{0}^{\pi} \sin(x)\cdot 2x \, dx = 2\pi.$$

Achtung: Hätten wir eine andere Wahl getroffen, nämlich 

$$u(x)=\sin(x) \quad \text{ und } \quad v'(x)=2x,$$

dann wäre die Suche nach der Stammfunktion von $v'$ zwar einfacher gelaufen (das
wäre $v(x)=x^2$ gewesen), aber insgesamt wäre es zu kompliziert, denn wir hätten

$$\int_{0}^{\pi} \sin(x)\cdot 2x \, dx = \big[\sin(x)\cdot x^2 \big]_{0}^{\pi} -
\int_{0}^{\pi} \cos(x)\cdot x^2 \, dx.$$

Das letzte Integral kann nicht gelöst werden.

## Weiteres Lernmaterial

Hier finden Sie noch zwei Videos, in denen die partielle Integration erklärt
wird und an Beispielen vorgeführt wird.

<iframe width="560" height="315" src="https://www.youtube.com/embed/s-IDbDtRAbg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/LlGrOTQ9TlU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>