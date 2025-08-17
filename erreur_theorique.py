import numpy as np
import matplotlib.pyplot as plt


p = 6                               # Nombre de bits de la mantisse (exemple : 6)
eps = 2 ** (-p)                     # Taille d'un pas de quantification
ln2 = np.log(2)                     # Logarithme naturel de 2 (pour la normalisation)

delta_vals = np.linspace(-eps, eps, 2000)  # De -epsilon à +epsilon
f_delta_vals = np.zeros_like(delta_vals)   # Tableau pour stocker la densité théorique


K = np.arange(1, 2, eps)


for k in K:
    delta_min = (k / (k + eps / 2)) - 1
    delta_max = (k / (k - eps / 2)) - 1

    coeff = np.log((k + eps / 2) / (k - eps / 2)) / (ln2 ** 2)

    mask = (delta_vals >= delta_min) & (delta_vals < delta_max)

    f_delta_vals[mask] += coeff / (1 + delta_vals[mask])


plt.figure(figsize=(10, 6))
plt.plot(delta_vals, f_delta_vals, 'r-', lw=2, label="Théorique $f_\\delta(\\delta)$")
plt.xlabel(r"Erreur relative $\delta$")
plt.ylabel(r"Densité $f_\delta(\delta)$")
plt.title(f"Densité théorique de l'erreur relative (mantisse {p} bits)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
