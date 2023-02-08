#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import IFrame


# # Differentialgleichungen: grundlegende Begriffe und separable Differentialgleichungen
# 
# 
# ## Lernziele
# ```{admonition} Lernziele
# :class: tip
# * Sie können erklären, was eine **gewöhnliche Differentialgleichung** und was eine **partielle Differentialgleichung** ist.
# * Sie können die **Ordnung einer Differentialgleichung** ablesen.
# * Sie können den Unterschied zwischen den Fachbegriffen **allgemeine Lösung einer Differentialgleichung** und **spezielle Lösung einer Differentialgleichung** erklären.
# * Sie können unterscheiden, ob eine Differentialgleichung in der **expliziten Form** oder der **impliziten Form** formuliert wurde.
# * Sie können eine **separable Differentialgleichung** lösen. 
# * Sie können das **Verfahren zur Trennung der Variablen** anwenden.
# ```

# ## Grundlegende Begriffe zu Differentialgleichungen
# 
# Wir betrachten ein Beispiel aus der Technischen Mechanik. Die Seilkraft variiert mit dem Winkel $\varphi$ und genügt der Differentialgleichung
# 
# $$\frac{dS(\varphi)}{d\varphi}=\mu_0 \cdot S(\varphi) \quad\text{ bzw. kurz }\quad \frac{dS}{d\varphi}=\mu_0 S.$$
# 
# Damit haben wir also eine Gleichung, bei der eine Funktion gesucht wird. Außerdem kommt in der Gleichung noch die 1. Ableitung der gesuchten Funktion vor. 
# 
# ````{prf:definition}
# :label: def:11:01
# Eine Gleichung, bei der eine Funktion gesucht wird und ihre Ableitungen vorkommen, nennen wir **Differentialgleichung**.
# ````
# 
# 

# Eine Funktion heißt **Lösung der Differentialgleichung**, wenn sie eingesetzt in die Gleichung diese Gleichung erfüllt. Dabei können mehrere Funktionen die Differentialgleichung lösen.
# 
# Beispiel:
# 
# $$f''(x) + 4\cdot f(x) = 0$$
# 
# Mögliche Lösungen:
# 
# * $f_1(x)=\sin(2x) \Rightarrow f_1'(x) = 2\cos(2x)\text{ und } f_1''(x)=-4\sin(2x)$  <br>
# eingesetzt $\Rightarrow -4\sin(2x) + 4\cdot \sin(2x)=0$ 
# 
# * $f_2(x)=\cos(2x) \Rightarrow f_2'(x) = -2\sin(2x)\text{ und } f_2''(x)=-4\cos(2x)$ <br>
# eingesetzt $\Rightarrow -4\cos(2x) + 4\cdot \cos(2x)=0$ 
# 
# Leider gibt es nicht für alle Differentialgleichungen ein Lösungsverfahren, um die gesuchte Funktion zu berechnen. Nur für einige Typen von Differentialgleichungen gibt es Lösungsverfahren, die sich aber je nach Art der Differentialgleichung unterscheiden.
# 
# Klassifikation von Differentialgleichungen:
# 
# * gewöhnlich oder partiell:
#     * gewöhnliche DGL: nur Ableitungen nach einer Variablen
#     * partielle DGL: Ableitungen nach mehreren Variablen
# * Ordnung: höchste vorkommene Ableitung
# * explizit oder implizit
#     * explizit: die höchste Ableitung steht auf einer Seite der Gleichung, alle anderen Terme auf der anderen Seite
#     * implizit: Gegenteil von explizit
# 
# 

# Alle Lösungsfunktionen einer Differentialgleichung nennt man die **allgemeine Lösung der Differentialgleichung**.
# 
# Eine Differentialgleichung der Ordnung $n$ hat noch $n$ Parameter, die sogenannten Integrationskonstanten. 
# 
# Beispiel Seilkraft:
# 
# $$\frac{dS(\varphi)}{d\varphi}=\mu_0 \cdot S(\varphi).$$
# 
# Die allgemeine Lösung dieser DGL 1. Ordnung ist
# 
# $$S(\varphi)=C e^{\mu_0\varphi}$$
# 
# mit einem Parameter $C$, wie wir durch Nachrechnen überprüfen: 
# 
# $$S'(\varphi)=\mu_0\cdot Ce^{\mu_0\varphi} \quad\Rightarrow\quad \mu_0 \cdot C e^{\mu_0 \varphi} = \mu_0 \cdot C e^{\mu_0 \varphi}.$$

# Um ein konkretes Problem aus der Technik zu lösen, müssen die Parameter (Integrationskonstanten) noch spezifiziert werden. Dazu brauchen wir mehr Informationen über das Problem, das mit der Differentialgleichung gelöst werden soll. Es kommen noch
# 
# * Anfangsbedingungen und/oder
# * Randwerte
# 
# dazu. Die Lösung einer DGL für diese Anfangsbedingungen und/oder Randwerte wird dann **spezielle Lösung der DGL** genannt.

# Beispiel Seilkraft: Die DGL
# 
# $$\frac{dS(\varphi)}{d\varphi}=\mu_0 \cdot S(\varphi)$$
# 
# hat die allgemeine Lösung 
# 
# $$S(\varphi)=C e^{\mu_0\varphi}.$$
# 
# Wir fordern, dass für einen Umlaufwinkel von $\varphi=0$ die Seilkraft genau $F_0$ entspricht (= Anfangsbedingung), also
# 
# $$S(0) =C e^{\mu_0 \cdot 0} \overset{!}{=} F_0 \quad \Rightarrow C = F_0.$$
# 
# Spezielle Lösung für die Seilkraft: $S(\varphi)=F_0 e^{\mu_0\varphi}$

# In[2]:


IFrame(src="https://frankfurt-university.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=04438dac-a6b8-4983-b265-ad5500f3ef3a&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all", height=405, width=720)


# ## Separable Diffenrentialgleichungen (Trennung der Variablen)
# 
# Damit eine Differentialgleichung \emph{separabel} ist, müssen zwei Bedigungen erfüllt sein.
# 
# 1. Die DGL muss von 1. Ordnung sein.
# 2.  Die rechte Seite (vorausgesetzt die 1. Ableitung der gesuchten Funktion steht links) lässt sich als ein Produkt von zwei Funktionen schreiben, wobei eine Funktion nur von der Variablen $x$ abhängt und die andere Funktion nur von der gesuchten Funktion $y$ selbst, also
# 
# $$y' = f(x)\cdot g(y).$$
# 

# Die DGL der Seilkraft $S'(\varphi)=\mu_0 \cdot S(\varphi)$ ist separabel.
# 
# 1. Sie ist von 1. Ordnung, da die höchste vorkommene Ableitung eine 1. Ableitung ist.
# 2. Die rechte Seite ist ein Produkt $\mu_0 \cdot S(\varphi)$, wo eine Funktion nur eine Konstante ist (nämlich $\mu_0$) und die andere Funktion hängt nur von der gesuchten Funktion $S$ ab (denn es ist die gesuchte Funktion $S(\varphi)$ selbst).
# 
# Kochrezept zur Lösung separabler DGL (= Verfahrung zur Trennung der Variablen)
# 
# Eine separable DGL
# 
# $$y'  = \frac{dy}{dx} = f(x)\cdot g(y)$$
# 
# lässt sich schrittweise wie folgt lösen:
# 
# 1. Trennnung der beiden Variablen (alles mit y nach links, alles mit x nach rechts)
# 2. Integration auf beiden Seiten
# 3. Auflösen nach y (falls möglich)

# Lösung der DGL Seilkraft:
# 
# $$S'(\varphi)=\frac{dS(\varphi)}{d\varphi}=\mu_0 \cdot S(\varphi)$$
# 
# Schritt 1: Trennung der Variablen, alles mit $S$ nach links, alles mit $\varphi$ nach rechts:
# 
# $$\frac{1}{S}ds = \mu_0 d\varphi $$
# 
# Schritt 2: Integration auf beiden Seiten:
# 
# $$\int \frac{1}{S}ds = \int \mu_0 d\varphi \quad \Rightarrow \quad \ln(S) = \mu_0 \varphi + C_1$$
# 
# Schritt 3: Auflösen nach $S$:
# 
# $$S = e^{\mu_0\varphi + C_1} = C\cdot e^{\mu_0\varphi} \quad \text{ mit } C = e^{C_1}.$$

# In[3]:


IFrame(src="https://frankfurt-university.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=bc52e263-cf13-4313-8f1f-ad53009d2b3c&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all", height=405, width=720)

