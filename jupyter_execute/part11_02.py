#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import IFrame


# # Lösungen von Differentialgleichungen
# 
# In diesem Abschnitt werden wir uns mit der Lösung einer Differentialgleichung beschäftigen. Wir werden den Unterschied zwischen der allgemeinen Lösung und einer speziellen Lösung der DGL betrachten und uns mit Anfangs- und Randwertproblemen beschäftigen.
# 
# ```{admonition} Lernziele
# :class: tip
# * Sie können den Unterschied zwischen der **allgemeinen Lösung** und einer **speziellen Lösung** einer Differentialgleichung erklären.
# * Sie wissen, was ein **Anfangswertproblem** ist.
# * Sie wissen, was ein **Randwertproblem** ist.
# ```

# ## Die allgemeine Lösung sind unendlich viele Funktionen
# 
# Das Lösen von Differentialgleichungen ist ein eigenes Forschungsgebiet der Mathematik. Wie Sie bereits im vorherigen Abschnitt gesehen haben, gehört dazu die Integration, was ja an sich schon ein schwieriges Thema ist. Und nicht immer existiert überhaupt eine Funktion, die die Differentialgleichung erfüllt. Daher halten wir zunächst einmal fest:
# 
# Eine Funktion, die eingesetzt in die Differentialgleichung dazu führt, dass die linke Seite der Gleichung gleich der rechten Seite ist, heißt **Lösung der Differentialgleichung**.

# Im Abschnitt "[](sec_11_01_a)" haben wir bereits festgestellt, dass es auch unendlich viele Lösungen einer Differentialgleichung geben kann. Beispielsweise lösen alle Funktionen
# 
# $$y(x)=\sin(x)+C_1 x + C_2$$
# 
# die Differentialgleichung $y''(x) = -\sin(x).$ Die beiden Integrationskonstanten $C_1$ und $C_2$ entstehen dadurch, dass die höchste auftretende Ableitung die zweite Ableitung ist. Die DGL hat Ordnung 2 und wir müssen zweimal ingtegrieren, um zu einer Lösung zu gelangen. Und obwohl wir von *der* Lösung der DGL sprechen, meinen wir damit eigentlich unendlich viele Funktionen. 
# 
# ```{admonition} Was ist ... die allgemeine Lösung einer DGL?
# Enthält die Lösungsfunktion der Differentialgleichung noch Integrationskonstanten und ist damit eigentlich eine Schar von unendlich vielen Funktionen, so nennen wir diese Schar von Funktionen
# die **allgemeine Lösung** der Differentialgleichung.
# ```

# ## Mit Zusatzbedingungen wird die Lösung speziell
# 
# Aus der allgemeinen Lösung wählen wir eine sogenannte **spezielle Lösung** aus, indem wir die Integrationskonstanten festlegen. In dem obigen Beispiel bekommen wir durch die Wahl von $C_1=2$ und $C_2 = 3$ die spezielle Lösung
# 
# $$y(x)=\sin(x)+2x+3$$
# 
# der DGL $y''(x)=-\sin(x)$.
# 
# Normalerweise raten wir nicht einfach Integrationskonstanten, sondern legen diese durch zusätzliche Informationen, also weitere Zusatzbedingungen fest. 
# 
# Beispielsweise könnten wir fordern, dass unsere gewünschte spezielle Lösung durch die Punkte $(0,0)$ und $(\pi,1)$ gehen soll. Dann würde die spezielle Lösung mit $C_1=\frac{1}{\pi}$ und $C_2=0$ sowohl die DGL erfüllen als auch die Zusatzbedingungen, denn es gilt
# 
# \begin{align*}
# y(0) &= \sin(0) + \frac{1}{\pi}\cdot 0 + 0 = 0,\\
# y(\pi) &= \sin(\pi) + \frac{1}{\pi} \cdot \pi + 0 = 1.
# \end{align*}
# 
# Sicherheitshalber rechnen wir noch die 2. Ableitung der Funktion $y(x)=\sin(x)+\frac{1}{\pi}x$ aus, aber das ist tatsächlich $y''(x)=-\sin(x)$, so dass die DGL auch erfüllt ist.
# 
# ```{admonition} Was ist ... eine spezielle Lösung einer DGL?
# Die **spezielle Lösung** einer DGL ist eine Funktion, die die Differentialgleichung erfüllt, aber keine Integrationskonstanten mehr enthält. Sie wird meist aus der allgemeinen Lösung berechnet, indem noch Zusatzbedingungen gestellt werden.
# ```

# ## Anfangswerte sind die häufigsten Zusatzbedingungen
# 
# Die Zusatzbedingungen kommen normalerweise aus dem Anwendungskontext. Wir schauen uns ein Beispiel aus der Physik an. Lassen wir einen Körper in der Nähe der Erdoberfläche fallen, so wirkt die Schwerkraft auf ihn ein. Seine Beschleunigung $a$ ist dann gleich der negativen Erdbeschleunigung, also $a = - g = - 9.81 \text{m}/\text{s}^2$. 
# 
# Wir wissen, dass die Beschleunigung $a(t)$ die 1. Ableitung der Geschwindigkeit-Zeit-Funktion $v(t)$ ist, die wiederum die 1. Ableitung der Weg-Zeit-Funktion $s(t)$ ist. Damit ist die Beschleunigung die 2. Ableitung der Weg-Zeit-Funktion $s(t)$. Es gilt die Differentialgleichung
# 
# $$\ddot{s}(t) = -g.$$
# 
# Bemerkung: Da die Weg-Zeit-Funktion eine zeitliche Größe ist, benutzen wir hier die Schreibweise mit der unabhängigen Variable $t$ und den zwei Punkten, um die 2. Anbleitung nach $t$ zu formulieren. Mehr dazu finden Sie im Abschnitt [](sec_11_01_b).

# Wir integrieren die Differentialgleichung zunächst unbestimmt, um die Geschwindigkeit-Zeit-Funktion $v(t)=\dot{s}(t)$ zu erhalten:
# 
# $$
# \int \ddot{s}(t)\, dt = \int -g \, dt \quad  \Rightarrow \quad v(t)=\dot{s}(t) = -gt + C_1.$$
# 
# Dann integrieren wir ein zweites Mal unbestimmt, um die Weg-Zeit-Funktion $s(t)$ zu bekommen:
# 
# 
# $$\int \dot{s}(t) \, dt = \int -gt + C_1 \, dt \quad \Rightarrow \quad s(t) = -\frac{1}{2}gt^2 + C_1 t + C_2. $$
# 
# Wie zu erwarten war, entstehen durch die zweimalige Integration zwei Integrationskonstanten. Wir brauchen Zusatzbedingungen, um aus der allgemeinen Lösung eine spezielle Lösung auszuwählen. Dazu betrachten wir den Anwendungskontext etwas näher.
# 
# Die Zeitmessung beginnt, sobald der Körper anfängt zu fallen. Daher ist es besonders geschickt, die Zusatzinformationen zu Beginn des Prozesses $t=0$ zu messen und daraus die beiden Integrationskonstanten zu bestimmen. Zu Beginn des freien Falls können wir die Höhe messen, aus der der Körper fällt. Wir bezeichnen die Anfangshöhe mit $s_0$. Es muss nicht sein, dass der Körper aus der Ruhe beginnt zu fallen. Die Anfangsgeschwindigkeit zum Zeitpunkt $t=0$ bezeichnen wir mit $v_0$. Es gilt also
# 
# $$s(0)=s_0 \quad \text{ und } \quad v(0)=v_0.$$
# 
# Wenn wir nun die allgemeine Lösung $s(t) = -\frac{1}{2}gt^2 + C_1 t + C_2$ zum Zeitpunkt $t=0$ betrachten, so gilt
# 
# $$s(0)=-\frac{1}{2}g\cdot0^2 + C_1\cdot 0 + C_2 = C_2.$$
# 
# Daraus können wir sofort ablesen, dass die Integrationskonstante $C_2$ der Anfangshöhe $s_0$ entsprechen muss.
# 
# Als nächstes betrachten wir die 1. Ableitung der allgemeinen Lösung zum Zeitpunkt $t=0$, also die Geschwindigkeit-Zeit-Funktion $v(t)$
# 
# $$\dot{s}(0)=-g\cdot 0 + C_1 = C_1.$$
# 
# Damit erhalten wir die spezielle Lösung
# 
# $$s(t)=\frac{1}{2}gt^2 + v_0 t + s_0$$
# 
# passend zu den Anfangsbedingungen $s(0)=s_0$ und $v(0)=v_0$.

# ```{admonition} Was ist ... ein Anfangswertproblem?
# Sind zusätzlich zu einer Differentialgleichung noch weitere Bedingungen für die Funktion und ihre Ableitungen an einer *einzigen* Stelle gegeben, so nennen wir beides zusammen **Anfangswertproblem**.
# 
# Hat die Differentialgleichung die Ordnung $n$, dann brauchen wir $n$ Anfangsbedingungen, um aus der allgemeinen Lösung eine spezielle Lösung auszuwählen.
# ```

# ## Randwertprobleme sind seltener und schwierig
# 
# Bei den Anfangswertproblemen werden alle Zusatzbedingungen an derselben Stelle gefordert. Sehr oft ist diese Stelle der Anfang eines zeitlichen Prozesses, aber das muss nicht sein. Wenn jedoch die Zusatzbedingungen an verschiedenen Stellen gestellt werden, dann sprechen wir von einem Randwertproblem.
# 
# ```{admonition} Was ist ... ein Randwertproblem?
# Sind zusätzlich zu einer Differentialgleichung noch weitere Bedingungen für die Funktion und ihre Ableitungen an *mehreren* Stellen gegeben, so nennen wir beides zusammen **Randwertproblem**.
# 
# Für eine Differentialgleichung der Ordnung $n$ brauchen wir $n$ Randwerte, um aus der allgemeinen Lösung eine spezielle Lösung auszuwählen.
# ```
# 
# 

# Wir betrachten als nächstes ein klassisches Beispiel eines Randwertproblems aus der Technischen Mechanik. Ein Balken wird auf zwei Stützen gelagert und gleichmäßig belastet. Für die Biegelinie $y(x)$, die die Auslenkung des Balkens an jeder Position $x$ beschreibt, gilt die folgende Differentialgleichung:
# 
# $$y'' = -\frac{M_b}{EI}.$$
# 
# Die physikalischen Größen sind dabei das Biegemoment $M_b$, der Elastizitätsmodul $E$ und das Flächenmoment $I$ des Balkenquerschnitts. Wirkt eine konstante Streckenlast $q$ auf den Balken, so ist das Biegemoment
# 
# $$M_b(x) = \frac{1}{2}q(lx-x^2).$$
# 
# abhängig von der Position $x$ und die Differentialgleichung lautet
# 
# $$y'' = - \frac{q}{2EI}(lx-x^2).$$
# 
# Dabei sind wir davon ausgegangen, dass die linke Stütze die Position $x=0$ und die rechte Stütze die Position $x=l$ hat. An beiden Randpunkten ist die Auslenkung 0, also haben wir die zusätzlichen Randwerte 
# 
# $$y(0)=0 \quad \text{und} \quad y(l)=0$$
# 
# als zusätzliche Bedingung. Als erstes bestimmen wir die allgemeine Lösung des Randwertproblems. Dazu integrieren wir zweimal unbestimmt und erhalten zwei Integrationskonstanten:
# 
# \begin{align*}
# \int y''(x)\, dx = -\frac{q}{2EI} \int lx - x^2 \, dx \quad &\Rightarrow \quad
# y'(x) = - \frac{q}{2EI}\left(\frac{1}{2}lx^2 - \frac{1}{3}x^3 + C_1\right) \\ 
# \int y'(x) \, dx = - \frac{q}{2EI} \int \frac{1}{2}lx^2 - \frac{1}{3}x^3 + C_1 \, dx \quad &\Rightarrow \quad y(x) = - \frac{q}{2EI} \left(\frac{1}{6}lx^3 -\frac{1}{12} x^4 + C_1x + C_2\right)  
# \end{align*}

# Um jetzt aus der allgemeinen Lösung mit den zwei Integrationskonstanten die spezielle Lösung zu berechnen, die das Randwertproblem löst, setzen wir die beiden Randwerte in die allgemeine Lösung ein: 
# 
# \begin{align*}
# y(0) &= -\frac{q}{2EI} C_2, \\
# y(l) &= -\frac{q}{2EI} \left(\frac{1}{6}l^4  - \frac{1}{12} l^4 + C_1\cdot l + C_2\right). 
# \end{align*}
# 
# Da die Durchbiegung an der linken und rechten Stütze jeweils 0 ist, setzen wir $y(0)=y(l)=0$. Wir können sofort auf beiden Seiten durch den Term $-\frac{q}{2EI}$ teilen, da dieser aus physikalischen Gründen selbst ungleich 0 sein muss. Damit erhalten wir sofort $y(0)=C_2=0$. Das setzen wir in die zweite Gleichung ein und erhalten
# 
# $$y(l)=\frac{1}{6}l^4  - \frac{1}{12} l^4 + C_1\cdot l=0.$$
# 
# Durch $l$ geteilt und nach $C_1$ aufgelöst erhalten wir $C_1 = -\frac{1}{12}l^3$. Damit lautet die spezielle Lösung der Differentialgleichung für die Biegelinie
# 
# $$y(x)=\frac{q}{24 EI}\left(x^4 -2lx^3 + l^3x\right).$$

# In[2]:


IFrame(src="https://www.geogebra.org/calculator/xuzuerpf?embed", width=800, height=600)


# In[ ]:




