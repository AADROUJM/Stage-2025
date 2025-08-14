import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

# Précision élevée pour calculer la somme exacte
getcontext().prec = 80

np.random.seed(0)
n = 200
# Génération des x_k uniformes
x = np.random.uniform(-1, 1, size=n).astype(np.float64)

s_float = float(x[0])
deltas = []
for k in range(1, n):
    a = s_float
    b = float(x[k])
    fl_sum = a + b  
    exact = Decimal(a) + Decimal(b)  # somme "exacte" avec Decimal
    if exact != 0:
        delta = float(Decimal(fl_sum) / exact - Decimal(1))
    else:
        delta = 0.0
    deltas.append(delta)
    s_float = fl_sum

deltas = np.array(deltas)

# Décalage pour créer les paires
a = deltas[:-1]  
b = deltas[1:]   

# Tracé du nuage de points
plt.figure(figsize=(5,5))
plt.scatter(a, b, alpha=0.5)
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.plot([a.min(), a.max()], [a.min(), a.max()], 'r--', label='$y = x$')
plt.xlabel(r'$\delta_k$')
plt.ylabel(r'$\delta_{k+1}$')
plt.title('Nuage de points $(\delta_k, \delta_{k+1})$ - Modèle DR')
plt.legend()
plt.show()
