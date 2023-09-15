---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  main_language: python
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
---

# 1.1 Ableitungen

```{warning}
Dieser Abschnitt wird gerade überarbeitet.
```

## Lernziele

```{admonition} Lernziele
:class: important
* Sie wissen, was die **mittlere Änderungsrate** einer zeitabhängigen Größe ist
  und können diese berechnen.
* Sie können den **Differenzenquotienten** einer Funktion berechnen.
* Sie können den Differenzenquotient als **Steigung der Sekante** geometrisch
  interpretieren.
```


## Die mittlere Änderungsrate oder der Differenzenquotient

2018 hat Italien ein neues System zur Geschwindigkeitsmessung in Betrieb
genommen (siehe
[https://www.verkehrsrundschau.de](https://www.verkehrsrundschau.de/nachrichten/transport-logistik/italien-neues-system-zur-geschwindigkeitsmessung-in-betrieb-2985039)).
Das System funktioniert nach dem Prinzip
[Abschnittskontrolle](https://de.wikipedia.org/wiki/Abschnittskontrolle), das
wie folgt funktioniert. Entlang der Strecke befinden sich mehrere
Kontrollpunkte. Wenn ein Auto den ersten Kontrollpunkt passiert, wird es
fotografiert und sein Kennzeichen ermittelt. Wird das Auto dann beim nächsten
Kontrollpunkt erneut per Kamera identifiziert, kann aus der Strecke zwischen den
Kontrollpunkten und der verstrichenen Zeit zwischen den beiden Aufnahmen die
Durchschnittsgeschwindigkeit berechnet werden. Ist die
Durchschnittsgeschwindigkeit höher als die erlaubte Geschwindigkeit, wird
automatisch ein Bußgeldverfahren eingeleitet.

Ein deutscher Tourist ist mit seinem Pkw auf der Autobahn unterwegs. Nachdem er
auf die Autobahn aufgefahren ist, protokolliert sein Fahrtenschreiber dreimal
pro Minute die zurückgelegte Strecke. Die Höchstgeschwindigkeit auf
italienischen Autobahnen ist 130 km/h. Wird er einen Bußgeldbescheid bekommen?

```{code-cell} ipython3
:tags: [remove-input]
import numpy as np
import plotly.express as px

t = np.linspace(10, 40, 91)
v = np.array([126.15338352, 126.49564866, 124.35022414, 125.87816443, 126.20696608,
 124.95444079, 128.44578754, 126.94806568, 126.26024726, 127.23297097,
 125.19978525, 127.69765993, 126.24715084, 124.97870157, 126.58576195,
 125.16482471, 126.81436067, 125.43389495, 125.4693086 , 123.75087393,
 125.91089725, 128.97207015, 125.36010679, 127.02841208, 124.17665284,
 127.58666025, 124.32453023, 127.8072856 , 127.18899723, 125.23975044,
 124.17863936, 126.91204387, 128.71914545, 129.1362791 , 130.907928,
 133.55471212, 135.53258782, 134.41012697, 135.16891874, 134.24454479,
 134.4576227 , 135.69746795, 136.46782703, 134.88242462, 132.25486494,
 135.43951289, 131.73502969, 133.85094214, 135.25239654, 133.61209273,
 135.34498774, 136.02784544, 136.68294526, 135.08131722, 135.56567131,
 133.82665751, 133.67007453, 134.36904437, 134.85722446, 136.24814849,
 136.98381544, 131.29044508, 131.64834418, 130.25264147, 127.4859585,
 127.95614561, 124.77370291, 124.75191859, 123.05482126, 121.75950736,
 122.23326904, 119.47659862, 120.47929885, 121.75958698, 119.97401422,
 118.69556004, 130.4820603 , 130.92546842, 129.16566364, 131.39161811,
 129.9079236 , 129.95842169, 127.29467381, 130.69431831, 130.34639392,
 130.28881128, 129.60258212, 129.05129734, 129.54145907, 128.70977913,
 130.81804945,])
s_km = np.cumsum(v * 10 / 36 * 20) / 1000 
fig = px.scatter(x = t, y = s_km,
                 labels = {'x': 'Zeit [min]', 'y': 'Strecke seit Autobahnauffahrt [km]'},
                 title='Protokoll des Fahrtenschreibers')
fig.show()
```

```{admonition} Mini-Übung
:class: tip
Wenn Sie mit dem Mauszeiger über die Punkte des Diagramms fahren, werden Zeit und zurückgelegte Strecke eingeblendet. 

1. Berechnen Sie die Durchschnittgesgeschwindigkeit im Zeitraum [10 min, 40 min]. 
2. Berechnen Sie die Durchschnittgesgeschwindigkeit im Zeitraum [15 min, 20 min]. 
3. Berechnen Sie die Durchschnittgesgeschwindigkeit im Zeitraum [20 min, 30 min]. 
```
```{admonition} Lösung
:class: tip, toggle
1. Die Strecke zum Zeitpunkt t<sub>1</sub> = 10 min ist s<sub>1</sub> = 0.7008521 km. Zum Zeitpunkt t<sub>2</sub> = 40 min wurden s<sub>2</sub> = 65.23726 km zurückgelegt. Damit ist die Durchschnittsgeschwindigkeit im Zeitraum [10 min, 40 min]

$$\frac{65.23726 \text{ km} - 0.7008521 \text{ km}}{40 \text{ min} - 10 \text{ min}} = 
\frac{64.5364079 \text{ km}}{30 \text{ min}} = \frac{64.5364079 \text{ km}}{0.5 \text{ h}} \approx 129.07 \text{ km/h}.$$

2. Die Strecke zum Zeitpunkt t<sub>1</sub> = 15 min ist s<sub>1</sub> = 11.21555 km. Zum Zeitpunkt t<sub>2</sub> = 20 min wurden s<sub>2</sub> = 21.71135 km zurückgelegt. Damit ist die Durchschnittsgeschwindigkeit im Zeitraum [15 min, 20 min]

$$\frac{21.71135 \text{ km} - 11.21555 \text{ km}}{20 \text{ min} - 15 \text{ min}} = 
\frac{10.4958 \text{ km}}{5 \text{ min}} = \frac{10.49795 \text{ km}}{1/12 \text{ h}} \approx 125.95 \text{ km/h}.$$

3. Die Strecke zum Zeitpunkt t<sub>1</sub> = 20 min ist s<sub>1</sub> = 21.71135 km. Zum Zeitpunkt t<sub>2</sub> = 30 min wurden s<sub>2</sub> = 44.04965 km zurückgelegt. Damit ist die Durchschnittsgeschwindigkeit im Zeitraum [20 min, 30 min]

$$\frac{44.04965 \text{ km} - 21.71135 \text{ km}}{30 \text{ min} - 20 \text{ min}} = 
\frac{22.3383 \text{ km}}{10 \text{ min}} = \frac{22.3383 \text{ km}}{1/6 \text{ h}} \approx 134.03 \text{ km/h}.$$

Je nachdem, wo das Auto die Kontrollpunkte passiert hat, droht ein Bußgeld.
```

Die obige Vorgehensweise zur Ermittlung der Durchschnittsgeschwindigkeit kann
auf andere zeitabhängige Größen verallgemeinert werden. Ist auf der x-Achse die
Zeit $t$ aufgetragen und auf der y-Achse die zeitabhängige Größe $f(t)$, so gibt
der Quotient

\begin{equation*} 
\frac{f(t_2) - f(t_1)}{t_2 - t_1} 
\end{equation*}

die sogenannte **mittlere Änderungsrate** der zeitabhängigen Größe $f(t)$ an.

```{admonition} Was ist ... die mittlere Änderungsrate?
:class: note
Die mittlere Änderungsrate einer zeitabhängigen Größe gibt an, wie sich die
zeitabhängige Größe durchschnittlich zwischen zwei Zeitpunkten verändert. 
Sie wird folgendermaßen berechnet:
\begin{equation*} 
\text{mittlere Änderungsrate} = \frac{f(t_2) - f(t_1)}{t_2 - t_1}.
\end{equation*}
Dabei stehen $t_1$ und $t_2$ für die beiden Zeitpunkte und $f(t_1)$ und $f(t_2)$
jeweils für den Wert der zeitabhängigen Größe zu diesen Zeitpunkten.
```

Allgemeiner betrachtet, kann jeder funktionale Zusammenhang, bei dem auf der
x-Achse die Ursache und auf der y-Achse die Wirkung dargestellt sind, auf diese
Weise analysiert werden. Die abhängige Größe (Wirkung) bezeichnen wir mit $f$,
die Ursache mit $x$. Betrachten wir zwei Messungen zur Ursache $x_1$ und zur
Ursache $x_2$, dann wird der Quotient

\begin{equation*} 
\frac{f(x_2) - f(x_1)}{x_2 - x_1} 
\end{equation*}

ganz allgemein **Differenzenquotient** genannt. Im Zähler steht eine Differenz,
im Nennen steht eine Differenz, der Term ist also ein Quotient von Differenzen
oder kurz ausgedrückt, ein Differenzenquotient. Er gibt an, wie sich
durchschnittlich die Wirkung verändert, wenn sich deren Ursache verändert.

```{admonition} Was ist ... der Differenzenquotient?
:class: note
Für eine reellwertige Funktion $f$, bei der das Intervall $[x_1, x_2]$ zur
Definitionsmenge gehört, bezeichnen wir den Term
\begin{equation*} 
\frac{f(x_2) - f(x_1)}{x_2 - x_1} 
\end{equation*}
als Differenzenquotient von $f$ im Intervall $[x_1, x_2]$.
```

+++

## Der Differenzenquotient geometrisch interpretiert

Bisher haben wir zwei verschiedene Kontrollpunkte auf der Autobahn oder
allgemein zwei verschiedene Ursachen $x_1$ und $x_2$ betrachtet. Betrachten wir
die Punkte $(x_1, f(x_1))$ und $(x_2, f(x_2))$ rein geometrisch, also mit ihren
Koordinaten $(x_1,y_1)$ und $(x_2,y_2)$, so lautet der Differenzenquotient

\begin{equation*} 
\frac{f(x_2) - f(x_1)}{x_2 - x_1} = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}.
\end{equation*}

Verbinden wir die beiden Punkte $(x_1,y_1)$ und $(x_2,y_2)$ durch eine Gerade,
dann ist der Differenzenquotient die Steigung dieser Gerade. Diese spezielle
Gerade, die zwei Punkte eines Funktionsgraphens miteinander verbindet, wird
**Sekante** genannt. Der Differenzenquotient ist also die Steigung der Sekante.

