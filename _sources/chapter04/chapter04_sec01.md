# 4.1 Berechnung Taylorreihe

Im Kapitel über Potenzreihen haben wir uns bereits mit der Frage beschäftigt, in
welchem Intervall eine Potenzreihe eine gegebene Funktion gut approximiert. Was
uns aber noch fehlt ist die Frage, wie wir zu solchen Potenzreihen kommen. Daher
gibt es in diesem Kapitel eine Anleitung dazu.

```{admonition} Warnung
:class: warning
Achtung, dieser Abschnitt des Vorlesungsskriptes wird gerade überarbeitet!!!
```

## Lernziele 

```{admonition} Lernziele
:class: tip
* Sie kennen die Formel für ein **Taylorpolynom der Ordnung n** auswendig.
* Sie kennen die Formel für die **Taylorreihe** auswendig.
```


## Taylorpolynom

Für Funktionen, die genügend oft differenzierbar sind, gibt es ein Kochrezept
zur Berechnung der Koeffizienten dazugehörigen Potenzreihe. Um dieses Kochrezept
anzuwenden, beschäftigen wir uns zunächst mit dem sogenannten Taylorpolynom.


````{prf:definition}
:label: def:04b:01
Ein **Taylorpolynom** ist eine Potenzreihe für eine Funktion $f(x)$, bei der die Koeffizienten berechnet werden, indem die Entwicklungsstelle $x_0$ in die Ableitungen der Funktion eingesetzt werden, also

$$T(x)=f(x_0) + \frac{f'(x_0)}{1!}(x-x_0)^1 + \frac{f''(x_0)}{2!}(x-x_0)^2 + \ldots. $$

Dabei steht $n!$ für die Fakultät der Zahl $n$.
````



## Kochrezept zur Berechnung von Taylorpolynomen

1. Erst einmal folgende Frage beantworten: Bis zu welchem Polynomgrad $n$ soll die Funktion $f(x)$ approximiert werden? $\rightarrow n$ aufschreiben
2. Die ersten $n$ Ableitungen der Funktion $f$ bestimmen, also $f'(x), f''(x), f'''(x), f^{(iv)}(x), \ldots$.
3. Die Koeffizienten ausrechnen, indem nun der Entwicklungspunkt $x_0$ in die Funktion $f$ und in die Ableitungen eingesetzt wird.
4. Die Fakultäten ausrechnen.
5. Alles in die Formel für das Taylorpolynom einsetzen.

Am besten das folgende Video gucken :-)

```{admonition} Video
:class: seealso
https://www.youtube.com/embed/o95cOqnLekw
```

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

## Taylorreihe

Und was ist nun die Taylorreihe? Ganz einfach, ein Taylorpolynom, das bis Unendlich geht, sieht nur kompliziert aus, wenn man es formal aufschreibt:

$$T(x)=\sum_{i=0}^{\infty} \frac{f^{(n)}(x_0)}{n!} (x-x_0)^n.$$

