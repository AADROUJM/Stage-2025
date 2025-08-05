import numpy as np

def esperance_delta(K, epsilon, delta_min, delta_max):
    """
    Calcule l'espérance E[δ] à partir de la formule finale
    """
    ln2 = np.log(2)
    terme_commun = (delta_max - delta_min) - (np.log(1 + delta_max) - np.log(1 + delta_min))
    
    numerateur = np.log((K + epsilon / 2) / (K - epsilon / 2))
    
    return np.sum((numerateur / (ln2 ** 2)) * terme_commun)


p_values = [4, 6, 8, 10, 12, 16, 24]
    
print("Calcul de l'espérance E[δ] pour différentes précisions (p bits) :\n")
    
for p in p_values:
    epsilon = 2 ** (-p)
    delta_min = -epsilon
    delta_max = epsilon
        
    K = np.arange(1 + epsilon, 2, epsilon)
        
    E_delta = esperance_delta(K, epsilon, delta_min, delta_max)
        
    print(f"p = {p:2d} | ε = {epsilon:.3e} | E[δ] ≈ {E_delta:.6e}")
