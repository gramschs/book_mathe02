# 4.2 Konvergenzkriterien für Reihen

In [Kapitel 3.1 Reihen](ref03_sec01) haben wir uns mit Reihen beschäftigt und
die Eigenschaften konvergent und divergent eingeführt. In diesem Kapitel geht es
darum rechnerisch zu bestimmen, ob eine Reihe konvergent oder divergent ist.
Dazu lernen wir verschiedene Kriterien kennen.

## Lernziele

```{admonition} Lernziele
:class: goals
* Sie können das **Nullfolgen-Kriterium** anwenden, um zu überprüfen, ob es überhaupt möglich ist, dass die Reihe konvergiert.
* Sie können mit den **Konvergenzkriterien** überprüfen, ob eine Reihe konvergiert, indem Sie die folgenden Kriterien anwenden können:
    * **Quotientenkriterium** oder
    * **Wurzelkriterium**.
* Sie können den Fachbegriff **absolut konvergente Reihe** erklären.
```

## Das Nullfolgen-Kriterium

Manchmal ist es einfacher zu beschreiben, was ein Gegenstand *nicht* ist. Eine
notwendige (aber nicht hinreichende) Bedingung für die Konvergenz einer Reihe
ist, dass die ursprüngliche Folge $(a_k)$ eine Nullfolge ist, d.h.
$\lim_{k\to\infty} a_k = 0$. Wenn dieser Grenzwert nicht Null ist oder nicht
existiert, divergiert die Reihe.

Was heißt notwendig, aber nicht hinreichend??? Was ist das überhaupt für eine
umständliche Formulierung?

Die Formulierung, "etwas ist notwendig, aber nicht hinreichend" kommt in der
Mathematik öfters vor. Damit ist gemeint, dass eine Bedingung erfüllt sein muss,
damit etwas anderes passiert oder stimmt. Aber alleine reicht diese Bedingung
nicht aus, um sicherzustellen, dass das andere tatsächlich passiert oder stimmt.

Ein Beispiel aus dem Alltag: Angenommen, jemand möchte ein Auto fahren. Eine
notwendige, aber nicht hinreichende Bedingung für das Fahren eines Autos ist,
dass die Person einen gültigen Führerschein besitzt. Der Führerschein ist
notwendig, weil er gesetzlich vorgeschrieben ist, um ein Auto fahren zu dürfen.
Er ist jedoch nicht hinreichend, weil es noch weitere Faktoren gibt, die
erforderlich sind, um tatsächlich Auto fahren zu können, wie zum Beispiel das
Vorhandensein eines funktionierenden Autos oder für eine konkrete Autofahrt eine
angemessene körperliche und geistige Verfassung.

In diesem Beispiel ist der Führerschein eine notwendige Bedingung, weil man ohne
ihn grundsätzlich nicht Auto fahren darf. Er ist jedoch nicht hinreichend, da
das Vorliegen eines Führerscheins allein noch nicht garantiert, dass jemand
tatsächlich ein Auto fahren kann oder darf.

Zurück zum Nullfolgen-Kriterium. Die Bedingung, dass die Folge $(a_k)$ eine
Nullfolge ist, ist notwendig, damit die dazugehörige Reihe konvergieren kann (=
Besitz eines Führerscheins). Aber nur weil die Folge $(a_k)$ eine Nullfolge ist,
heißt es noch lange nicht, dass die Reihe konvergiert, weil vielleicht andere
Bedingungen nicht erfüllt sind (= Autofahrer hat Akohol getrunken). Es ist also
nicht hinreichend.

Zuerst wirkt diese Aussage nicht besonders bedeutend. Aber wir können trotzdem
zwei bedeutsame Schlussfolgen daraus ziehen:

```{admonition} Nullfolgen-Kriterium
:class: note
1. Wenn die Folge der Summanden $(a_k)$ *keine* Nullfolge ist, dann ist die
dazugehörige Reihe auf jeden Fall divergent.
2. Wenn eine Reihe konvergiert, dann muss die zugrundeliegende Folge $(a_k)$ der
   Summanden eine Nullfolge sein.
```

In dem folgenden Video wird die Konvergenz von Reihen nochmal erläutert und
einige Beispiele für konvergente oder divergente Reihen gegeben.

```{dropdown} Video zu Reihenkonvergenz von Prof. Hoever
<iframe width="560" height="315" src="https://www.youtube.com/embed/aGnAseEnfG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```


## Das Quotienten-Kriterium und das Wurzel-Kriterium

Das Quotienten-Kriterium ist ein nützliches Konvergenzkriterium für Reihen, bei
denen die Summanden einen Bruch oder eine Potenz enthalten. Es kann uns helfen,
schnell herauszufinden, ob eine solche Reihe konvergiert oder divergiert, ohne
zuerst komplexere Techniken oder Kriterien anzuwenden.

```{admonition} Quotienten-Kriterium
:class: note
Das Quotienten-Kriterium besagt, dass eine Reihe $\sum_{k=1}^{\infty} a_k$
konvergiert, wenn der Grenzwert

$$r = \lim_{k\to\infty} \left| \frac{a_{k+1}}{a_k} \right|$$

existiert und kleiner als 1 ist. Gilt $r > 1$, so divergiert die Reihe. Gilt
$r = 1$, so versagt das Kriterium und ein anderes Kriterium muss benutzt werden.

Übrigens: Für $r < 1$ ist die Reihe sogar absolut konvergent.
```

Den Begriff **absolute Konvergenz** hatten wir bisher nicht. Absolute Konvergenz
ist mehr als Konvergenz. Nicht nur die Reihe $(s_n)$ mit 

$$s_n = \sum_{k=1}^{n} a_k$$

konvergiert, sogar die Reihe, bei der die Summanden stets positiv sind, weil der
Betrag gebildet wird, also

$$s_n = \sum_{k=1}^{n} \left| a_k \right|$$

konvergiert. Das wird dann absolute Konvergenz genannt.

Ein Beispiel für die Anwendung des Quotienten-Kriteriums ist die folgende Reihe:

$$\sum_{k=1}^{n}\frac{2^k}{k!}.$$

Um das Quotienten-Kriterium anzuwenden, betrachten wir den Bruch der
aufeinanderfolgenden Glieder:

$$\left|\frac{a_{k+1}}{a_k}\right| =
\frac{\frac{2^{k+1}}{(k+1)!}}{\frac{2^k}{k!}} =
\frac{2^{k+1}k!}{2^k(k+1)!} = \frac{2}{k+1}.$$

Da $r = \lim_{k \to \infty} \frac{2}{k+1} = 0 < 1$, konvergiert die Reihe
$\sum_{k=1}^{\infty} \frac{2^k}{k!}$ nach dem Quotienten-Kriterium.

Das Wurzel-Kriterium ist ein weiteres Konvergenzkriterium für Reihen, das
besonders hilfreich ist, wenn die Summanden Potenzen oder Exponentialfunktionen
enthalten. Es ermöglicht uns, schnell festzustellen, ob eine solche Reihe
konvergiert oder divergiert, ohne zunächst komplexere Techniken oder Kriterien
anwenden zu müssen.

```{admonition} Wurzel-Kriterium
:class: note
Das Wurzel-Kriterium besagt, dass eine Reihe $\sum_{k=1}^{\infty} a_k$
konvergiert, wenn der Grenzwert

$$r = \lim_{k\to\infty} \sqrt[k]{|a_k|}$$

existiert und kleiner als 1 ist. Gilt $r > 1$, so divergiert die Reihe. Gilt
$r = 1$, so versagt das Kriterium und ein anderes Kriterium muss benutzt werden.

Übrigens: Für $r < 1$ ist die Reihe sogar absolut konvergent, genau wie beim Quotienten-Kriterium.
```

Als Beispiel betrachten wir die Reihe $(s_n)$ mit

$$s_n = \sum_{k=1}^{n} \left(-\frac{1}{4}\right) \cdot 4^{-k-2} \cdot 2^{k+4}.$$ 

Wir wenden das Wurzel-Kriterium an: 

\begin{align*} 
r & = \lim_{k\rightarrow \infty}\sqrt[k]{\left|a_k\right|} = \\
&  = \lim_{k\rightarrow \infty}\left(\frac{1}{4} \cdot 4^{-k-2} 2^{k+4}\right)^{\left(\frac{1}{k} \right)} = \\ 
& = \lim_{k\rightarrow \infty} \left(4^{-k - 3} 2^{k + 4}\right)^{\left(\frac{1}{k}\right)} = \\
& = \frac{1}{2} . 
 \end{align*} 
 Wegen $r = \frac{1}{2} <1$ ist die Reihe (absolut) konvergent. 

```{dropdown} Video zu Wurzel- und Quotientenkriterium von Prof. Hoever
<iframe width="560" height="315" src="https://www.youtube.com/embed/G1GSAFrd6mE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```

## Ausblick

Tatsächlich gibt es noch einige Kriterien mehr, um die Konvergenz einer Reihe zu
bestimmen. Die bekanntesten Konvergenzkriterien sind:

* Grenzwertkriterium
* Majorantenkriterium
* Minorantenkriterium
* Verdichtungskriterium
* Leibniz-Kriterium

Einen detaillierten Überblick zu weiteren Konvergenzkriterien findet man auf der
Internetseite [Serlo →
Konvergenzkriterien](https://de.wikibooks.org/wiki/Mathe_für_Nicht-Freaks:_Konvergenz_und_Divergenz_einer_Reihe_beweisen:_Konvergenzkriterien).


​	