#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import IFrame


# # Differentialgleichungen (Teil 2)
# 
# 
# ## Lernziele
# ```{admonition} Lernziele
# :class: tip
# * Sie können bei einer gegebenen Differentialgleichung entscheiden, ob diese eine **lineare Differentialgleichung** ist oder nicht.
# * Sie können eine **homogene lineare Differentialgleichung 1. Ordnung** lösen.
# * Sie können eine **inhomogene lineare Differentialgleichung 1. Ordnung** lösen.
# * Sie können das Lösungsverfahren **Variation der Konstante** anwenden, um die Lösung einer linearen Differentialgleichung zu bestimmen.
# * Sie können erklären, was ein **System von Differentialgleichungen** ist.
# * Sie können ein **System von Differentialgleichungen 2. Ordnung** lösen.
# ```

# ## Lineare Differentialgleichungen
# 
# Eine Differentialgleichung, die wir in der Form
# 
# $$a_n(x)y^{(n)} + a_{n-1}(x)y^{(n-1)}+ \ldots + a_1(x)y' + a_0(x)y = r(x)$$
# 
# schreiben können, nennen wir eine **lineare DGL**. Die rechte Seite $r(x)$ wird **Störfunktion** genannt.
# 
# Wenn die rechte Seite 0 ist, also die Störfunktion fehlt, wird die lineare DGL **homogen** genannt, ansonsten **inhomogen**. 

# ## Wie wird eine homogene lineare DGL 1. Ordnung gelöst?
# 
# Zuerst betrachten wir eine homogene lineare DGL 1. Ordnung, also
# 
# $$a_1(x)y' + a_0(x)y = 0.$$
# 
# Das ist eine separable DGL und die allgemeine Lösung lautet
# 
# $$y_h(x)=C \cdot e^{-\int \frac{a_0(x)}{a_1(x)}\, dx}.$$
# 
# Beispiel:
# 
# Gegeben ist die homogene lineare DGL 1. Ordnung
# 
# $$y'+3y=0,$$
# 
# also $a_1(x)=1$ und $a_0(x)=3$. Damit ist die allgemeine homogene Lösung der DGL
# 
# $$y_h(x)=C \cdot e^{-\int \frac{3}{1}\, dx} = C\cdot e^{-3x}.$$

# In[2]:


IFrame(width=560, height=315, src="https://www.youtube.com/embed/Sm0Go9IioJ4")


# ## Wie wird eine inhomogene lineare DGL 1. Ordnung gelöst?
# 
# Nun betrachten wir eine inhomogene lineare DGL 1. Ordnung, also
# 
# $$a_1(x)y' + a_0(x) y = r(x).$$
# 
# Als erstes lassen wir die Störfunktion weg und berechnen die homogene Lösung
# 
# $$y_h(x)=C \cdot e^{-\int \frac{a_0(x)}{a_1(x)}\, dx}.$$
# 
# Dann ersetzen wir die Konstante $C$ durch eine Funktion $C(x)$ -- das nennt man **Variation der Konstanten** -- und setzen diese Lösung in die inhomogene DGL ein. Dadurch entsteht eine DGL für die unbekannte Funktion $C(x)$, die wir dann lösen.
# 
# Beispiel:
# 
# Gegeben ist die inhomogene lineare DGL 1. Ordnung
# 
# $$y'+3y=x^2.$$
# 
# Die homogene Lösung ist $y_h(x)=C\cdot e^{-3x}$. Wir variieren die Konstante
# 
# $$y(x)=C(x)\cdot e^{-3x} \quad \Rightarrow \quad y'(x)=C'(x)e^{-3x} -3 C(x) e^{-3x}$$
# 
# und setzen in die DGL ein:
# 
# $$C'(x)e^{-3x} -3 C(x) e^{-3x} + 3C(x)\cdot e^{-3x} = x^2.$$
# 
# Wir vereinfachen
# 
# $$C'(x)e^{-3x} -3 C(x) e^{-3x} + 3C(x)\cdot e^{-3x} = x^2$$
# 
# zu
# 
# $$ C'(x)e^{-3x} = x^2 \quad \Rightarrow \quad C'(x)=x^2\cdot e^{3x}.$$
# 
# Integration auf beiden Seiten:
# 
# \begin{multline*}
# C(x)= \left[x^2\cdot\frac{1}{3}e^{3x}\right] -\int 2x \frac{1}{3}e^{3x}\, dx = \\
# = \left[x^2\cdot\frac{1}{3}e^{3x}\right] - \left[2x\cdot\frac{1}{9}e^{3x}\right] + \int 2\cdot  \frac{1}{3}e^{3x} \, dx = \\
# = \frac{1}{27}e^{3x}(9x^2 - 6x + 2) + C_1
# \end{multline*}
# 
# Allgemeine Lösung der inhomogenen DGL
# 
# $$y(x)= C_1e^{-3x} + \frac{1}{3}x^2 - \frac{1}{9}x + \frac{2}{27}.$$
# 

# In[3]:


IFrame(width=560, height=315, src="https://www.youtube.com/embed/AWdLkNZJZ70")


# ## Was ist ein System von Differentialgleichungen?
# 
# Wir betrachten in dieser Vorlesung nur Systeme von 2 DGL, die homogen, lineaer und von 1. Ordnung sind.
# 
# Ein System von Differentialgleichungen
# \begin{align*}
# y_1' &= a_{11}y_1 + a_{12}y_2 \\ 
# y_2' &= a_{21}y_1 + a_{22}y_2
# \end{align*}
# heißt homogenes System von Differentialgleichungen 1. Ordnung mit konstanten Koeffizienten.
# 
# Es werden also zwei Funktionen $y_1$ und $y_2$ gesucht. Beide gesuchten Funktionen kommen mit der 1. Ableitung vor, in Summe hat das System damit die 2. Ordnung.

# ## Wie wird ein System 2. Ordnung gelöst?
# 
# Bilde die **charakteristische Gleichung**
# 
# $$\det(A-\lambda E) = \begin{vmatrix} a_{11}-\lambda & a_{12} \\ a_{21} & a_{22}-\lambda \end{vmatrix}$$
# 
# und berechne die Nullstellen $\lambda_1$ und $\lambda_2$ (=Eigenwerte).
# 
# Es gibt drei mögliche Lösungen:
# 
# * 2 Nullstellen, d.h. $\lambda_1 \neq \lambda_2$ reell
# * 1 Nullstelle, d.h. $\lambda_1 = \lambda_2$ reell
# * 0 Nullstellen, d.h. $\lambda_1 \neq \lambda_2$ komplex, weil für die komplexen Zahlen eine quadratische Gleichung immer zwei Lösungen hat
# 
# Je nachdem, welcher dieser dieser Fälle eintritt, lauten die Lösungen wie folgt.
# 
# ### 2 Nullstellen
# 
# Es gilt also $\lambda_1 \neq \lambda_2$ reell.
# 
# 1. Lösungsfunktion: $y_1(x)=C_1\cdot e^{\lambda_1 x} + C_2\cdot e^{\lambda_2 x}$ 
# 
# 2. Lösungsfunktion erhalten wir, indem wir die $y_1$ in die 1. DGL einsetzen und dann nach $y_2$ auflösen:
# 
# $$y_2(x)=\frac{1}{a_{12}}(y_1' - a_{11} y_1) $$
# 
# ### 1 Nullstelle 
# 
# Es gilt also $\lambda_1 = \lambda_2 = \alpha$ reell.
# 
# 1. Lösungsfunktion: $y_1(x)=(C_1+C_2 x) \cdot e^{\alpha x} $
# 
# 2. Lösungsfunktion erhalten wir wiederum als
# 
# $$y_2(x)=\frac{1}{a_{12}}(y_1' - a_{11} y_1) $$
# 
# 
# ### 0 Nullstellen
# 
# Es gilt also $\lambda_1 \neq \lambda_2$ komplex, die komplexen Nullstellen können geschrieben werden als $\lambda_{1/2}=\alpha \pm \omega i$. 
# 
# 1. Lösungsfunktion: $y_1(x)=e^{\alpha x}\left(C_1\sin(\omega x) + C_2 \cos(\omega x)\right) $
# 
# 2. Lösungsfunktion erhalten wir wiederum als
# 
# $$y_2(x)=\frac{1}{a_{12}}(y_1' - a_{11} y_1) $$
# 

# In[4]:


IFrame(width=560, height=315, src="https://www.youtube.com/embed/u1Jm4YXF11c")

