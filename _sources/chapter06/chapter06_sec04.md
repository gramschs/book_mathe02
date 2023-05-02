# 6.4 Höhere partielle Ableitungen

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

## Was sind höhere partielle Ableitungen?

Eine eindimensionale Funktion kann man oft nicht nur einmal, sondern zweimal, dreimal, manchmal sogar unendlichmal oft ableiten. Das geht natürlich nur, wenn nach dem Ableiten eine Funktion herauskommt, die wieder ableitbar ist, sonst muss man aufhören.

Bei Funktionen, die von mehreren Variablen abhängen, kann man die partiellen Ableitungen mischen. Beispielsweise leiten wir eine Funktion partiell nach x ab und die Funktion, die dadurch entstanden ist leiten wir nun partiell nach y ab. 

Bei zwei Variablen und partiellen Ableitungen der Ordnung 2 hätten wir dann folgende Kombinationsmöglichkeiten:

* Ableitung nach x und dann Ableitung nach x 
* Ableitung nach x und dann Ableitung nach y
* Ableitung nach y und dann Ableitung nach x
* Ableitung nach y und dann Ableitung nach y

Bei höheren partiellen Ableitungen können wir nicht einfach zwei Striche an die Funktion schreiben, sondern müssen genau angeben, in welcher Reihenfolge nach welcher Variable abgeleitet werden soll. Deshalb schreiben wir

* Ableitung nach x und dann Ableitung nach x: $\frac{\partial^2}{\partial x \partial x}f(x,y)$
* Ableitung nach x und dann Ableitung nach y: $\frac{\partial^2}{\partial y \partial x}f(x,y)$
* Ableitung nach y und dann Ableitung nach x: $\frac{\partial^2}{\partial x \partial y}f(x,y)$
* Ableitung nach y und dann Ableitung nach y: $\frac{\partial^2}{\partial y \partial y}f(x,y)$

Die Richtung, nach der zuerst abgeleitet wird, steht weiter rechts.

Wenn wir nun uns die Kombinationsmöglichkeiten für partielle Ableitungen 3. Ordnung ansehen, stellen wir fest, dass da einige Kombinationen möglich sind, genaugenommen 27. Glücklicherweise gibt es einen Trick, einige der Kombinationen kann man sich sparen. Dieser Trick wird in der Mathematik der **Satz von Schwarz** genannt. Im nächsten Video sehen Sie dazu eine Erläuterung.



```{admonition} Video
:class: seealso
https://www.youtube.com/embed/XgkmktejS_Y
```
