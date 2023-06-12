# 12.1 Lineare DGL 1. Ordnung

Differentialgleichungen 1. Ordnung haben wir bereits in den vorherigen Kapiteln
kennengelernt. Ein spezieller Typ von Differentialgleichung, der in den
Ingenieurwissenschaften sehr häufig verwendet wird, ist die **lineare
Differentialgleichung**. Obwohl es auch lineare Differentialgleichungen höherer
Ordnung gibt, beschränken wir uns in dieser Vorlesung auf lineare
Differentialgleichungen 1. Ordnung. Unser erstes Ziel in diesem Kapitel ist es
zu lernen, wie man erkennt, ob eine gegebene Differentialgleichung von diesem
Typ ist.


## Lernziele
```{admonition} Lernziele
:class: important
* Sie können bei einer gegebenen Differentialgleichung entscheiden, ob es sich
  um eine **lineare Differentialgleichung** handelt oder nicht.
* Sie wissen, was die **Störfunktion** einer linearen Differentialgleichung ist.
* Sie können bei einer gegebenen linearen Differentialgleichung entscheiden, ob
  diese eine **homogene** oder eine **inhomogene** Differentialgleichung ist.
```


## Lineare Differentialgleichungen 1. Ordnung

Eine lineare Differentialgleichung ist eine Differentialgleichung, in der die
Funktion und ihre Ableitungen ausschließlich linear auftreten. Das bedeutet, sie
werden beispielsweise nicht quadriert, es gibt keine Produkterme und sie
erscheinen nicht innerhalb von Funktionen wie Sinus oder Exponentialfunktion
oder anderen nichtlinearen Funktionen.

```{admonition} Was ist ... eine lineare DGL 1. Ordnung?
:class: note
Formal können wir eine lineare Differentialgleichung 1. Ordnung in der Form 

$$a_1(x)y' + a_0(x)y = r(x)$$

darstellen. Die rechte Seite $r(x)$ wird **Störfunktion** genannt.
```

**Beispiel 1:** Die Differentialgleichung

$$3x \cdot y' - \sin(x)\cdot y = x^2$$

ist eine lineare Differentialgleichung 1. Ordnung. Zwar treten in dieser
Differentialgleichung nichtlineare Terme auf ($\sin(x)$ und $x^2$), doch
beziehen sich diese ausschließlich auf die Variable $x$ und nicht auf die
gesuchte Funktion $y$ oder ihre Ableitung $y'$.

**Beispiel 2:** Die Differentialgleichung

$$3x \cdot y' - x\cdot \sin(y) = x^2$$

ist hingegen keine lineare Differentialgleichung, sondern eine nichtlineare
Differentialgleichung 1. Ordnung, da die gesuchte Funktion $y$ innerhalb der
nichtlinearen Sinus-Funktion $\sin(y)$ auftritt.
 

## Störfunktion entscheidet über homogen und inhomogen

Bei linearen Differentialgleichungen lassen sich Lösungsmethoden anwenden, die
auf der Theorie von linearen Gleichungssystemen beruhen. Bei der Lösung von
solchen Gleichungssystemen ist es entscheidend zu unterscheiden, ob das
Gleichungssystem homogen oder inhomogen ist. Daher adaptieren wir diese beiden
Begriffe auch für lineare Differentialgleichungen.

```{admonition} Was ist ... eine homogene lineare DGL?
:class: note
Eine lineare Differentialgleichung wird **homogen** genannt, wenn die
Störfunktion gleich der Nullfunktion ist. Ansonsten wird sie **inhomogen**
genannt.
```

**Beispiel 1:** Die Differentialgleichung

$$3x \cdot y' - \sin(x)\cdot y = 0$$

ist eine homogene lineare Differentialgleichung 1. Ordnung. Die rechte Seite,
also die Störfunktion, ist überall Null.

**Beispiel 2:** Die Differentialgleichung

$$3x \cdot y' - \sin(x)\cdot y = x^2$$

ist hingegen eine inhomogene lineare Differentialgleichung 1. Ordnung. Die
rechte Seite, also die Störfunktion $r(x)=x^2$, ist nicht die Nullfunktion.

```{dropdown} Video zu "Differentialgleichungen, linear/nicht linear, homogen/inhomogen" von Daniel Jung
<iframe width="560" height="315" src="https://www.youtube.com/embed/dlAVRF4jWHA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```