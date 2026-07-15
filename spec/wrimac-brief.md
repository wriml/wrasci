# WRIMAC — Synthèse de conception (état actuel)

## 1. Définition générale

WRIMAC (WRIming Markup Language for Academia) est un dialecte de WRIML orienté vers l’écriture académique.

Il ne constitue pas un format de fichier indépendant :
- tous les documents restent en `.wriml`
- WRIMAC est un ensemble de conventions sémantiques et de schémas

---

## 2. Philosophie centrale

### 2.1 Content-only (sans mise en forme)

WRIMAC interdit toute balise de formatage.

Il ne décrit pas :
- italique
- gras
- taille
- couleur
- disposition

Il décrit uniquement :
- la nature logique et scientifique des contenus

Exemples de catégories :
- `gl` (glose)
- `data`
- `theorem`
- `proof`
- `example`
- `citation`

---

### 2.2 Orientation auteur

WRIMAC est conçu pour :
- minimiser la charge cognitive
- maximiser la vitesse d’écriture
- éviter l’apprentissage de multiples syntaxes concurrentes

---

## 3. Architecture générale (relation avec WRIML)

WRIMAC est un **ensemble de schémas** utilisés dans WRIML.

Donc :
- WRIML = langage hôte
- WRIMAC = vocabulaire académique structuré

---

## 4. Organisation des schémas (répertoires)

### 4.1 Répertoires officiels

Un seul schéma canonique par domaine :

- `wrimac-core`
- `wrimac-ling`
- `wrimac-math`
- `wrimac-stats`
- etc.

Objectif :
- éviter fragmentation (problème LaTeX packages concurrents)
- garantir uniformité syntaxique

---

### 4.2 Gouvernance

- Contributions via dépôt officiel (GitHub)
- Validation par comité d’administrateurs
- Intégration uniquement après validation stricte
- Pas de duplication de schémas pour un même besoin

---

### 4.3 Extensions de revues

- Autorisées mais déconseillées
- Doivent être archivées avec l’article
- Risque de divergence → fortement limité

---

## 5. Namespace et résolution

### 5.1 Namespace implicite via schéma

Activation d’un schéma :

```wriml
^article wrimac-schema=''linguistics'':
```

Toutes les balises non qualifiées héritent de ce schéma.


---

5.2 Surcharge locale

Une structure interne peut changer de schéma :
```wriml
^section wrimac-schema=''statistics'':
```

---

5.3 Règle de résolution

La priorité est ascendante :

1. schéma local du nœud


2. schéma du parent


3. etc.


4. fallback core




---

6. Mécanisme de contexte (optionnel conceptuel)

Alternative ou complément :

```wriml
^synisland schema=''linguistics'' :
...
_contexte:
```
Usage :

changer temporairement de cadre interprétatif

signaler une zone disciplinaire homogène



---

7. Modèle recommandé (actuel)

7.1 Modèle principal retenu

WRIMAC repose sur :

schéma déclaré au niveau structurel

héritage de schéma

override local


Exemple :

```wriml
^article wrimac-schema=''linguistics'':

    ^section:
        ^data:
        ...
        _data:
    _section:

    ^section wrimac-schema=''statistics'':
        ^data:
        ...
        _data:
    _section:

_article:
```

---

8. Rétrocompatibilité (principe fondamental)

8.1 Principe de base

Toute extension officielle doit garantir :

validité syntaxique des anciens documents

validité sémantique des anciens usages

absence de rupture de lecture



---

8.2 Conséquence majeure

les balises existantes ne sont jamais supprimées

les significations ne sont jamais modifiées

seules des extensions sont ajoutées



---

8.3 Impact

stabilité cognitive pour les auteurs

réduction de la charge d’apprentissage

durabilité du standard



---

9. Modèle de modularité

WRIMAC privilégie :

répertoires centralisés

schémas disciplinaires uniques

namespaces implicites

héritage de contexte

surcharge locale contrôlée



---

10. Distribution des schémas

Modèle retenu (hybride recommandé)

dépôt central WRIMAC

cache local du parseur

téléchargement automatique si nécessaire

verrouillage optionnel pour reproductibilité stricte



---

11. Objectif global du système

WRIMAC vise à créer :

> un langage d’écriture académique stable, lisible, non fragmenté, et orienté auteur




---

12. Problèmes explicitement résolus

fragmentation des packages (type LaTeX)

ambiguïtés interdisciplinaires

surcharge cognitive des auteurs

dépendances syntaxiques multiples

instabilité des conventions académiques



---

13. Direction architecturale actuelle

WRIMAC converge vers :

standardisation forte par domaine

compatibilité rétroactive stricte

héritage contextuel de schéma

absence de multiplication des syntaxes concurrentes


---