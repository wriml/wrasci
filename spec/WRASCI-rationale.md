# WRASCI — Philosophie de conception

## Pourquoi un nouveau système ?

X-SAMPA et Kirshenbaum ont résolu le problème de 1990 :
transcrire l'IPA sur un terminal ASCII 7-bit. En 2026, le
problème est différent : intégrer la phonétique dans des
pipelines de traitement de données modernes (JSON, XML, SQL,
regex, bases de données NoSQL) sans conflits de syntaxe.

Les caractères spéciaux de X-SAMPA (`\`, `_`, `~`, `!`, `^`)
sont des métacaractères dans la quasi-totalité de ces contextes.
WRASCI supprime le problème à la racine.

## Le système de suffixes géométriques

La charte IPA est visuellement cohérente : les symboles dérivés
sont des transformations géométriques des symboles de base.
WRASCI exploite cette cohérence plutôt que d'inventer des
abréviations articulatoires ad hoc.

```
i  (inversé)   ɘ = ei     ɛ = 3i     ɥ = wy
r  (renversé)  ɐ = ar     ʌ = vr
u  (arrondi)   ø = eu     ɞ = 3u     ɒ = aou
b  (barré)     ɨ = ib     ʉ = ub     ɵ = ob
```

Ce système est appris une fois et appliqué partout — pas une
liste à mémoriser, une règle.

## Le double espace

L'espace simple sépare les tokens phonétiques. Le double
espace insère un espace orthographique dans la transcription.
Convention stricte, documentée explicitement, signalée par
le parseur.

## Relation avec WRIML

WRASCI vit dans des balises WRIML dédiées — il ne "pollue"
pas la syntaxe WRIML principale. Les caractères réservés de
WRIML (`^`, `_`, `:`) ne peuvent pas apparaître dans une
chaîne WRASCI par construction (doctrine alphanumérique).
