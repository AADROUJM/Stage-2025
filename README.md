# Modélisation stochastique de l'erreur de calcul

Ce projet s'inscrit dans le cadre d'un stage de recherche au laboratoire LI-PaRAD.  
L'objectif est d'étudier et de modéliser **l'erreur d'arrondi en arithmétique flottante**.  

---

## Contexte

En arithmétique flottante, chaque opération d’addition ou de multiplication est affectée d’une petite erreur relative d’arrondi, notée :

$$
\mathrm{fl}(a \circ b) = (a \circ b)(1 + \delta), \quad |\delta| \leq u
$$

où $u$ est la précision machine (epsilon).  
L'étude de la distribution de $\delta$ est essentielle pour mieux comprendre la stabilité numérique des algorithmes.

---

## Contenu du dépôt

### 1. `simulation_delta.py`
- **But** : Générer des échantillons suivant une loi log-uniforme sur [1,2[, appliquer un arrondi flottant, et tracer l’**histogramme empirique** de l’erreur relative $\delta$.
- **Concepts illustrés** :
  - Distribution empirique de $\delta$

---

### 2. `densite_theorique.py`
- **But** : Calculer et tracer la **densité théorique** de l’erreur relative $\delta$, dérivée analytiquement.  
- **Idée clé** : la densité s’exprime comme une combinaison de morceaux dépendant des points de discrétisation $k$.
- **Sortie** : courbe représentant la loi théorique.

---

### 3. `esperance_delta.py`
- **But** : Calculer l’**espérance** de l’erreur relative $E[\delta]$ pour différentes précisions $p$ (nombre de bits de mantisse).
- **Résultat attendu** :  
  - Le biais moyen $E[\delta]$ décroît très rapidement avec $p$.  
  - Pour les formats IEEE (simple ou double précision), le biais est négligeable.

---

### 4. `correlation_deltas.py`
- **But** : Étudier la **corrélation entre deux erreurs successives** $(\delta_k, \delta_{k+1})$ lors de l’accumulation de sommes.
- **Méthode** :
  - Génération de nombres uniformes
  - Comparaison entre la somme flottante et la somme exacte (via `Decimal`)
  - Calcul du coefficient de corrélation de Pearson
  - Tracé du nuage de points
- **Intérêt** : vérifier si les erreurs peuvent être considérées comme indépendantes.

---

## Résultats principaux

- L’erreur relative $\delta$ a une distribution **presque symétrique** autour de zéro, avec espérance très proche de 0.
- Le biais $E[\delta]$ est en $O(\varepsilon^2)$ et devient insignifiant en pratique.
- Les corrélations entre erreurs successives sont faibles, confirmant l’**hypothèse d’indépendance** souvent utilisée en analyse probabiliste des erreurs numériques.

---

