#!/usr/bin/env python
# coding: utf-8

# # Fourier-Reihen
# 
# Periodische Vorgänge gibt es sowohl in der Natur als auch in der Technik. In der Technik gehören insbesondere Drehbewegungen dazu. Es ist nicht sinnvoll, periodische Funktionen durch Potenzreihen bzw. Taylorpolynome zu approximieren. Stattdessen werden wir periodische Funktionen als Überlagerung von Sinus- und Kosinus-Funktionen approximieren, also sogenannte **Fourier-Reihen**.

# ## Lernziele Fourier-Reihen
# 
# ```{admonition} Lernziele
# :class: tip
# * Sie können erklären, was eine **periodische Funktion** ist.
# * Sie können von einer periodischen Funktion die **Periode** bestimmen.
# * Sie kennen die Kriterien, wann eine Funktion in eine **Fourier-Reihe** entwickelt werden darf.
# * Sie können eine periodische Funktion in eine Fourier-Reihe umschreiben.
# * Sie können die **Fourier-Koeffizienten** berechnen. 
# ```

# In[1]:


from IPython.display import IFrame


# ## Periodische Funktionen - was ist das?
# 
# Bei einer periodischen Funktion wiederholen sich in regelmäßigen Abständen die Funktionswerte wieder. Der Abstand, nachdem sich die Funktionswerte beginnen zu wiederholen, heißt **Periodendauer**.

# In[2]:


IFrame(width=560, height=315, src="https://www.youtube.com/embed/e3lpwsKp75Y")


# ## Wie findet man zu einer periodischen Funktion die passende Überlagerung von Sinus- und Kosinus-Funktionen?
# 
# Kochrezept zur Bestimmung der **Fourier-Reihe**:
# 1. Bestimme $T$, also die Periode der Funktion $f(t)$.
# 2. Berechne daraus die Kreisfrequenz der Grundschwingung $\omega_0 = \frac{2\pi}{T}$.
# 3. Berechne die Fourier-Koeffizienten $a_0$, $a_n$ und $b_n$ entweder allgemein für beliebiges $n$ oder bis zum geforderten Grad $n=1, 2, 3, \ldots.$
# Die Fourier-Koeffizienten werden mit folgenden Formeln berechnet:
# 
# \begin{align*}
# a_0 &= \frac{2}{T}\cdot \int_{T} f(t)\, dt \\
# a_n &= \frac{2}{T}\cdot \int_{T} f(t) \cdot \cos(n\,\omega_0 \,t) \, dt \\
# b_n &= \frac{2}{T}\cdot \int_{T} f(t) \cdot \sin(n\,\omega_0 \,t) \, dt
# \end{align*}
# 4. Setze alles in die Formel für die Fourier-Reihe ein:
# \begin{align*}f(t) = \frac{a_0}{2} &+ a_1\cdot \cos(1\,\omega_0\, t) + b_1\cdot\sin(1\,\omega_0\, t) + \\
# &+ a_2\cdot \cos(2\,\omega_0\, t) + b_2\cdot\sin(2\,\omega_0\, t) +  \\
# &+ a_3\cdot \cos(3\,\omega_0\, t) + b_3\cdot\sin(3\,\omega_0\, t) + \quad \ldots \\
# \end{align*}
