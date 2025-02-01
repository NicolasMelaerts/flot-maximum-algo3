# Projet INFO-F310 - Algorithmique et Recherche Opérationnelle

## Description du Projet

Ce projet consiste à résoudre le problème de flot maximum en utilisant deux méthodes différentes :
1. **Programmation Linéaire** : Formuler le problème sous forme de programme linéaire et le résoudre à l'aide du solver `glpk`.
2. **Méthode des Chemins Augmentants** : Implémenter cette méthode en Python pour trouver le flot maximum.

Le projet comprend la génération de modèles, la résolution des instances, et la comparaison des performances des deux méthodes.

## Fichiers à Remettre

1. **Script de Génération de Modèle** : `generate_model.py`
   - Prend en entrée un fichier d'instance `inst-n-p.txt` et génère un fichier `.lp` au format CPLEX LP.
   - Exemple d'utilisation :
     ```bash
     python3 generate_model.py inst-300-0.3.txt
     ```

2. **Fichier de Programme Linéaire** : `model-300-0.3.lp`
   - Fichier généré par le script `generate_model.py`.

3. **Fichier de Solution du Programme Linéaire** : `model-300-0.3.sol`
   - Contient la solution optimale obtenue avec `glpk`.

4. **Script de la Méthode des Chemins Augmentants** : `chemin_augmentant.py`
   - Prend en entrée un fichier d'instance `inst-n-p.txt` et génère un fichier `.path` contenant la solution.
   - Exemple d'utilisation :
     ```bash
     python3 chemin_augmentant.py inst-300-0.3.txt
     ```

5. **Rapport** : Un rapport au format PDF contenant :
   - Les noms, prénoms et matricules des membres du groupe.
   - Le système d'exploitation utilisé pour les tests.
   - La formulation du problème et la description des méthodes utilisées.
   - Une analyse des résultats et des performances des deux méthodes.

## Consignes de Remise

- Le projet est à réaliser en binôme.
- Les fichiers doivent être organisés dans un répertoire nommé `NOM1_NOM2`.
- Le répertoire doit être compressé en un fichier `.zip` et soumis sur l'UV avant le **22 mai à 14h**.
