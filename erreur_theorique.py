import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Paramètres principaux
# -----------------------------
p = 6                               # Nombre de bits de la mantisse (exemple : 6)
eps = 2 ** (-p)                     # Taille d'un pas de quantification
ln2 = np.log(2)                     # Logarithme naturel de 2 (pour la normalisation)

# -----------------------------
# Grille des valeurs de delta (erreur relative) pour le tracé
# -----------------------------
delta_vals = np.linspace(-eps, eps, 2000)  # De -epsilon à +epsilon
f_delta_vals = np.zeros_like(delta_vals)   # Tableau pour stocker la densité théorique

# -----------------------------
# Ensemble des mantisses k dans [1, 2[
# -----------------------------
K = np.arange(1, 2, eps)

# -----------------------------
# Calcul de la densité théorique par morceaux
# -----------------------------
for k in K:
    # Déterminer l'intervalle de delta influencé par ce k
    delta_min = (k / (k + eps / 2)) - 1
    delta_max = (k / (k - eps / 2)) - 1

    # Constante pour ce palier basée sur la loi log-uniforme
    coeff = np.log((k + eps / 2) / (k - eps / 2)) / (ln2 ** 2)

    # Masque pour savoir quelles valeurs de delta appartiennent à cet intervalle
    mask = (delta_vals >= delta_min) & (delta_vals < delta_max)

    # Ajouter la contribution de ce palier à la densité théorique
    f_delta_vals[mask] += coeff / (1 + delta_vals[mask])

# -----------------------------
# Tracé du résultat
# -----------------------------
plt.figure(figsize=(10, 6))
plt.plot(delta_vals, f_delta_vals, 'r-', lw=2, label="Théorique $f_\\delta(\\delta)$")
plt.xlabel(r"Erreur relative $\delta$")
plt.ylabel(r"Densité $f_\delta(\delta)$")
plt.title(f"Densité théorique de l'erreur relative (mantisse {p} bits)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
