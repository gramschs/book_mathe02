# 4.2 Konvergenz von Taylorreihen

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

TODO

## Taylor-Restglied 

Wenn wir ein Taylorpolynom zu einer Funktion vorliegen haben, wäre es gut zu wissen, wie gut unsere Approximation ist. Die Formel mit dem sogenannten Taylor-Restglied 

$$f(x) = T_n(x) + \frac{1}{(n+1)!}f^{(n+1)}(u)\cdot(x-x_0)^{n+1},$$

hilft uns dabei, denn jetzt können wir den Fehler abschätzen als

$$|f(x)-T_n(x)| = |\frac{1}{(n+1)!}f^{(n+1)}(u)\cdot(x-x_0)^{n+1}|.$$



Leider ist die Formel nicht ganz so einfach anzuwenden, denn es steckt ein $u$ darin, das nicht genau spezifiziert ist. $u$ ist irgendeine Stelle zwischen dem Entwicklungspunkt $x_0$ und $x$, die man nicht genau kennt. Aber wir können in diesem Bereich einfach das Maximum $M$ von $f^{(n+1)}(u)$ für alle Punkte zwischen $x_0$ und $x$ bilden und dann als Abschätzung das Maximum verwenden:

$$|f(x)-T_n(x)| \leq \frac{1}{(n+1)!}\cdot M \cdot |x-x_0|^{n+1}.$$
 
Eine Erklärung dazu finden Sie in dem folgenden Video.

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/oz1hejsyNlk
```