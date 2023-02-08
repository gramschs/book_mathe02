#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import IFrame


# # Doppelintegral in Polarkoordinaten und Dreifachintegral
# 
# Im letzten Kapitel haben wir nicht thematisiert, dass das Doppelintegral in kartesischen Koordinaten berechnet wurde. In diesem Kapitel verwenden wir Polarkoordinaten und betrachten zusätzlich Dreifachintegrale.

# ## Lernziele
# 
# ```{admonition} Lernziele
# :class: tip
# * Sie können **Polarkoordinaten** in **kartesische Koordinaten** umrechnen.
# * Sie können ein Doppelintegral in kartesischen Koordinaten in ein Doppelintegral in Polarkoordinaten umrechnen, d.h.
# 
# $$\iint_{A}f(x,y)\, dA = \int_{\varphi=\varphi_1}^{\varphi_2} \int_{r=r_i(\varphi)}^{r_a(\varphi)}f(r\cos(\varphi), r\sin(\varphi)) \cdot r\, dr\, d\varphi.$$
# 
# Die Integration erfolgt dabei in zwei Schritten, zuerst kommt die innere Integration über $r$, danach die äußere Integration über $\varphi$.
# 
# * Sie können ein **Dreifachintegral** (in kartesischen Koordinaten) berechnen.
# * Sie können mit einem Dreifachintegral das Volumen $V$ eines Körpers berechnen
# 
# $$V=\iiint_{V}1\,dV.$$
# 
# * Sie können mit drei Dreifachintegralen den Schwerpunkt $S(x_S,y_S,z_S)$ eines Körpers berechnen:
# 
# $$x_S = \frac{1}{V}\iiint_{V}x\, dV, \qquad y_S = \frac{1}{V}\iiint_{V}y\, dV \qquad \text{und} \quad z_S = \frac{1}{V}\iiint_{V}z\, dV.$$
# ```

# ## Polarkoordinaten
# 
# Die Umrechnung von Polarkoordinaten in kartesische Koordinaten erfolgt mit den Formeln:
# \begin{align*}
# x &= r\cdot \cos(\varphi) \\ 
# y &= r\cdot \sin(\varphi)
# \end{align*}
# 
# Zur Erinnerung folgt hier eine Einführung in Polarkoordinaten:

# In[2]:


IFrame(width=560, height=315, src="https://www.youtube.com/embed/l8ZF4m0fPxM")


# In dem folgenden Video wird gezeigt, wie eine Funktion mit Variablen in kartesischen Koordinaten in eine Funktion mit Variablen in Polarkoordinaten umgerechnet werden kann:

# In[3]:


IFrame(width="560", height="315", src="https://www.youtube.com/embed/MCRDcJKeR20")


# In dem folgenden

# In[ ]:





# ## Doppelintegral in Polarkoordinaten
# 
# Um ein Doppelintegral in Polarkoordinaten zu berechnen, muss das Flächenelement $dA$ umgerechnet werden:
# 
# $$dA = r \, dr \, d\varphi.$$
# 
# In dem folgenden Video wird sehr ausführlich der Flächeninhalt eines Halbkreises sowohl mit einem Doppelintegral in kartesischen Koordinaten als auch einem Doppelintegral in Polarkoordinaten erklärt. Nicht verwirren lassen, in dem Video wird das Doppelintegral Bereichsintegral genannt.
# 

# In[4]:


IFrame(width=560, height=315, src="https://www.youtube.com/embed/CghdXlwr5aY")


# ## Dreifachintegral
# 
# Ein Dreifachintegral wird durch drei Integrationen berechnet:
# 
# $$\iiint_{V}f(x,y,z)\, dV = \int_{x=a}^{x=b} \int_{y=g_{u}(x)}^{y=g_{o}(x)} \int_{z = F_{u}(x,y)}^{z = F_{o}(x,y)} f(x,y,z)\, dz \, dy \, dx.$$
# 
# Dabei bedeuten die Bezeichnungen:
# 
# * $F_{o}(x,y)$: obere Fläche 
# * $F_{u}(x,y)$: untere Fläche
# * $g_{o}(x)$: obere Grenzkurve 
# * $g_{u}(x)$: untere Grenzkurve
# 
# wie man auch der folgenden Abbildung entnehmen kann:
# 
# ```{figure} pics/part10_skizze_dreifachintegral.svg
# ---
# width: 600px
# name: part10_skizze_dreifachintegral
# ---
# Skizze Dreifachintegral
# ```
# 
# In dem folgenden Video wird der Unterschied Doppelintegral zu Dreifachintegral erklärt.

# In[5]:


IFrame(width=560, height=315, src="https://www.youtube.com/embed/Ec6xuobv8Mk")


# Hier wird ein Dreifachintegral ausgerechnet, indem die drei Integrationen nacheinander durchgeführt werden:

# In[6]:


IFrame(width=560, height=315, src="https://www.youtube.com/embed/HZRAUqbVKeQ")

