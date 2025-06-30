# 12.1 Lineare DGL 1. Ordnung

Viele technische Prozesse lassen sich durch lineare Differentialgleichungen
beschreiben: die Entladung eines Kondensators in einem elektrischen Schaltkreis,
die Temperaturregelung in einem Industrieofen oder die Dämpfung von Schwingungen
in einem Fahrzeugfahrwerk. Wir beginnen das Thema lineare
Differentialgleichungen mit den linearen Differentialgleichungen 1. Ordnung.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können bei einer gegebenen Differentialgleichung entscheiden, ob es sich
  um eine **lineare Differentialgleichung** handelt oder nicht.
* Sie wissen, was die **Störfunktion** einer linearen Differentialgleichung ist.
* Sie können bei einer gegebenen linearen Differentialgleichung entscheiden, ob
  diese eine **homogene** oder eine **inhomogene** Differentialgleichung ist.
```

## Lineare Differentialgleichungen 1. Ordnung

Eine lineare Differentialgleichung ist eine Differentialgleichung, in der die
Funktion und ihre Ableitungen nur in der ersten Potenz und nicht als Argument
nichtlinearer Funktionen auftreten. Das bedeutet, sie werden beispielsweise
nicht quadriert, es gibt keine Produkterme und sie erscheinen nicht innerhalb
von Funktionen wie Sinus oder Exponentialfunktion oder anderen nichtlinearen
Funktionen.

```{admonition} Was ist ... eine lineare DGL 1. Ordnung?
:class: note
Formal können wir eine lineare Differentialgleichung 1. Ordnung in der Form 

$$a_1(x)y' + a_0(x)y = r(x)$$

darstellen. Die rechte Seite $r(x)$ heißt **Störfunktion**.
```

Der Begriff **Störfunktion** stammt aus der Regelungstechnik und Physik. Die
Gleichung $a_1(x)y' + a_0(x)y = 0$ würde ein System beschreiben, das sich im
Gleichgewicht befindet. Die rechte Seite $r(x)$ repräsentiert eine äußere
Einwirkung, die dieses Gleichgewicht "stört" und wird daher Störfunktion
genannt.

**Beispiel 1:** Die Differentialgleichung

$$3x \cdot y' - \sin(x)\cdot y = x^2$$

ist eine lineare Differentialgleichung 1. Ordnung. Zwar treten in dieser
Differentialgleichung nichtlineare Terme auf ($\sin(x)$ und $x^2$), doch
beziehen sich diese jedoch nur auf die Variable $x$ und nicht auf die gesuchte
Funktion $y$ oder ihre Ableitung $y'$.

**Beispiel 2:** Die Differentialgleichung

$$3x \cdot y' - x\cdot \sin(y) = x^2$$

ist hingegen keine lineare Differentialgleichung, sondern eine nichtlineare
Differentialgleichung 1. Ordnung, da die gesuchte Funktion $y$ innerhalb der
nichtlinearen Sinus-Funktion $\sin(y)$ auftritt.

Nachdem wir nun lineare von nichtlinearen Differentialgleichungen unterscheiden
können, betrachten wir eine weitere wichtige Klassifikation: homogen und
inhomogen.

## Störfunktion entscheidet über homogen und inhomogen

Bei linearen Differentialgleichungen lassen sich Lösungsmethoden anwenden, die
auf der Theorie von linearen Gleichungssystemen beruhen. Bei der Lösung von
solchen Gleichungssystemen ist es entscheidend zu unterscheiden, ob das
Gleichungssystem homogen oder inhomogen ist. Daher adaptieren wir diese beiden
Begriffe auch für lineare Differentialgleichungen.

```{admonition} Was ist ... eine homogene lineare DGL?
:class: note
Eine lineare Differentialgleichung ist **homogen**, wenn die Störfunktion gleich
der Nullfunktion ist. Ansonsten wird sie **inhomogen** genannt.
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

## Zusammenfassung und Ausblick

In diesem Kapitel haben wir gelernt, lineare Differentialgleichungen der Form
$a_1(x)y' + a_0(x)y = r(x)$ zu erkennen und zwischen homogenen und inhomogenen
Gleichungen zu unterscheiden. Diese Klassifikation ist entscheidend, da lineare
Differentialgleichungen systematische Lösungsverfahren ermöglichen. In den
folgenden Kapiteln werden wir diese Lösungsmethoden entwickeln und anwenden, um
technische Probleme wie Temperaturverläufe, Schwingungen und Regelungsvorgänge
mathematisch zu beschreiben und zu lösen.
