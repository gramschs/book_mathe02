# Übungen

```{admonition} Übung A
:class: miniexercise
Gehen Sie auf die Trainingsseite [Mathebattle: Ableitung ganzrationale Funktionen](https://mathebattle.de/edu_randomtasks/training_show/129) und lösen Sie solange die dortigen Ableitungsaufgaben, bis Sie drei hintereinander richtig gelöst haben.
```

```{admonition} Übung B
:class: miniexercise
Gehen Sie auf die Trainingsseite [Mathebattle: Ableiten mit x im Nenner](https://mathebattle.de/edu_randomtasks/training_show/727) und lösen Sie solange die dortigen Ableitungsaufgaben, bis Sie drei hintereinander richtig gelöst haben.
```

```{admonition} Übung C
:class: miniexercise
Gehen Sie auf die Trainingsseite [Mathebattle: Ableiten mit Wurzel](https://mathebattle.de/edu_randomtasks/training_show/726) und lösen Sie solange die dortigen Ableitungsaufgaben, bis Sie drei hintereinander richtig gelöst haben.
```

```{admonition} Übung D
:class: miniexercise
Gehen Sie auf die Trainingsseite [Mathebattle: Kettenregel](https://mathebattle.de/edu_randomtasks/training_show/714) und lösen Sie solange die dortigen Ableitungsaufgaben, bis Sie drei hintereinander richtig gelöst haben.
```

```{admonition} Übung E
:class: miniexercise
Gehen Sie auf die Trainingsseite [Mathebattle: Produktregel](https://mathebattle.de/edu_randomtasks/training_show/131) und lösen Sie solange die dortigen Ableitungsaufgaben, bis Sie drei hintereinander richtig gelöst haben.
```

```{admonition} Übung F
:class: miniexercise
Gehen Sie auf die Trainingsseite [Mathebattle: Ketten- und Produktregel](https://mathebattle.de/edu_randomtasks/training_show/724) und lösen Sie solange die dortigen Ableitungsaufgaben, bis Sie drei hintereinander richtig gelöst haben.
```

```{admonition} Übung G
:class: miniexercise
Gehen Sie auf die Trainingsseite [Mathebattle: alles zusammen](https://mathebattle.de/edu_randomtasks/training_show/466) und lösen Sie solange die dortigen Ableitungsaufgaben, bis Sie drei hintereinander richtig gelöst haben.
```

```{admonition} Übung H
:class: miniexercise
Gehen Sie auf die Trainingsseite [Mathebattle: Extrempunkte](https://mathebattle.de/edu_randomtasks/training_show/398) und lösen Sie solange die dortigen Ableitungsaufgaben, bis Sie drei hintereinander richtig gelöst haben.
```

```{admonition} Übung I
:class: miniexercise
Ein Rechteckt hat seine obere Seite unter der Parabel $f(x) = 16 - x^2$ und
seine untere Seite auf der x-Achse. Die beiden vertikalen Seiten des Rechtecks
sind parallel zur y-Achse. Bestimmen Sie die Abmessungen des Rechtecks, so dass
sein Flächeninhalt maximal ist.

Fertigen Sie dazu eine Skizze an.
```

```{admonition} Lösung
:class: miniexercise, toggle
Die Parabel $f(x) = -x^2 + 16$ ist symmetrisch zur y-Achse, daher ist auch das
Rechteck symmetrisch zur y-Achse. Daher genügt es, nur die rechte Hälfte des
Rechtecks zu betrachten und $x>0$ zu fordern.

Die Hauptbedingung lautet

$$A = x\cdot y.$$

Die Nebenbedingung lautet

$$y = -x^2 + 16.$$

Daraus wird die Zielfunktion

$$A(x) = x \cdot (-x^2 + 16),$$

die maximiert werden soll. Wir vereinfachen die Zielfunktion und erhalten

$$\Rightarrow A(x) = -x^3 + 16x.$$

Wir bilden die 1. Ableitung:

$$A'(x) = -3x^2+16.$$

Notwendige Bedingung für Extremwerte ist, dass $A'(x)=0$ erfüllt ist. Daher lösen
wir die Gleichung

$$-3x^2+16 = 0$$ 

und erhalten als Lösung $x_1 = \sqrt{\frac{16}{3}} = \frac{4}{3}\sqrt{3}$ und $x_2 =
-\sqrt{\frac{16}{3}}$. Die negative Stelle $x_2$ wird nicht weiter betrachtet,
da wir nur die rechte Seite des Rechtecks betrachten und daher $x>0$
vorausgesetzt haben. Als nächstes überprüfen wir mit der 2. Ableitung, ob ein
Extremwert vorliegt (hinreichende Bedingung).

$$A''(x) = -6x \quad \Rightarrow A''(x_1) = -6\cdot \frac{4}{3}\sqrt{3} =
-8\sqrt{3} < 0.$$

Da die 2. Ableitung an der Stelle $x_1$ negativ ist, liegt ein Maximum vor. Für
das entsprechende $y_1$ gilt dann

$$y_2 = f(x_1) = 16 - x_1^2 = 16 - \left(  \sqrt{\frac{16}{3}}\right)^2 =
\frac{32}{3}.$$

Antwort: Somit ist die linke Seite des gesuchten kompletten Rechtecks an der
Stelle $x = -\frac{4}{3}\sqrt{3}$ (was $x_2$ entspricht) und die rechte Seite
an der Stelle $x = \frac{4}{3}\sqrt{3}$. Die obere Seite liegt bei $y = \frac{32}{3}$.
Der Flächeninhalt des kompletten gesuchten Rechtecke ist

$$A_{\text{gesamt}} = 2 \cdot  \frac{4}{3}\sqrt{3} \cdot \frac{32}{3} =
\frac{256}{9}\sqrt{3}.$$
```

```{admonition} Übung J
:class: miniexercise
Ein senkrechter Zylinder wird in eine Kugel mit dem Radius 1 m eingesetzt, so
dass beide Mittelpunkte übereinstimmen. Bestimmen Sie Radius $r$, Höhe $h$ und
Volumen $V$ des Zylinders, wenn der Zylinder das maximale Volumen haben soll.

Fertigen Sie dazu eine Skizze des Querschnitts an.
```

```{admonition} Lösung
:class: miniexercise, toggle
Die Hauptbedingung (Volumen des Zylinders) lautet

$$V = \pi r^2 \cdot h.$$

Die Nebenbedingung lautet (erkenntlich aus Skizze des Querschnitts)

$$r^2 + \left(\frac{h}{2}\right)^2 = 1.$$

Aufgelöst nach der Höhe $h$ lautet die Nebenbedingung

$$h = 2\sqrt{1-r^2}.$$

Eingesetzt in die Hauptbedingung erhalten wir die Zielfunktion

$$V(r) = 2\pi r^2 \cdot \sqrt{1-r^2},$$

die maximiert werden soll. Dazu berechnen wir die 1. Ableitung als

$$V'(r) = \frac{4\pi r - 6\pi r^3}{\sqrt{1-r^2}}.$$

Um die möglichen Extremwertstellen zu berechnen (notwendige Bedingung), setzen
wir die 1. Ableitung gleich Null:

$$V'(r) = 0  \quad \Rightarrow \frac{4\pi r - 6\pi r^3}{\sqrt{1-r^2}} = 0.$$

Wir multiplizieren die Gleichung auf beiden Seiten mit $\sqrt{1-r^2}$ und
klammern $r$ aus:

$$\Rightarrow r\cdot \left(4\pi - 6 \pi r^2\right) = 0.$$

Die erste Lösung dieser Gleichung $r_1 = 0$ verwerfen wir, denn ein Zylinder mit
Radius 0 ist nicht existent. Aus $4\pi - 6 \pi r^2 = 0$ folgen die beiden
Lösungen $r_2 = \sqrt{\frac{2}{3}}$ und $r_3 = -\sqrt{\frac{2}{3}}$. Die dritte
Lösung verwerfen wir ebenfalls, da ein Zylinder keinen negativen Radius haben
kann. Wir betrachten nur noch die Stelle $r_2 = \sqrt{\frac{2}{3}}$.

Um zu überprüfen, ob die Stelle $r_2 = \sqrt{\frac{2}{3}} = \frac{1}{3}\sqrt{6}$
einen Extremwert hat (hinreichende Bedingung), bilden wir die 2. Ableitung und
erhalten nach einigen Umformungen:

$$V''(r) = \frac{2\pi (6r^4 - 9r^2 + 2)}{(1-r^2)^{\frac{3}{2}}}.$$

Setzen wir nun $r_2 = \frac{1}{3}\sqrt{6}$ in die 2. Ableitung ein, erhalten wir

$$V''\left(\sqrt{\frac{2}{3}}\right) = -8\pi\sqrt{3} < 0.$$

Somit hat die Zielfunktion $V(r)$ an der Stelle $r_2 = \frac{1}{3}\sqrt{6}$ ein
Maximum. Die dazugehörige Höhe ist

$$h_2 = 2 \sqrt{1- r_2^2} = \frac{2}{3}\sqrt{3}$$

und das maximale Volumen

$$V = \pi r_2^2 \cdot h_2 = \frac{4}{9}\sqrt{3}\pi.$$
```
