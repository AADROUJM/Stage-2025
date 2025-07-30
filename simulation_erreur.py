import numpy as np
import matplotlib.pyplot as plt

# Paramètres
p = 5
eps = 2**(-p)
N = 10**6  # Nombre d'échantillons
ln2 = np.log(2)

# 1. Génération des valeurs x ~ log-uniforme sur [1, 2[
# Pour une loi log-uniforme : log2(x) est uniforme sur [0, 1]
u = np.random.rand(N)   # Uniforme sur [0,1]
x = 2**u                #  log-uniforme sur [1,2[

# 2. Arrondi au plus proche
k = np.round((x - 1)/eps)*eps + 1

# 3. Calcul de l'erreur relative
delta_sim = (k - x)/x

# 4. Histogramme empirique
plt.figure(figsize=(10,6))
plt.hist(delta_sim, bins=200, density=True, alpha=0.6, color='steelblue', edgecolor='black')
plt.xlabel(r"Erreur relative $\delta$")
plt.ylabel("Densité empirique")
plt.title(f"Histogramme empirique de l'erreur relative (mantisse à p={p} bits)")
plt.grid(True)
plt.tight_layout()
plt.show()
