# WRASCI — WRiting ASCii Ipa

> Version : 1.1 (Kiel 2020 Compliant — Suffixes Géométriques Unifiés)
> Statut : Spécification de Production
> Licence : Apache 2.0
> Organisation : [wriml-org](https://github.com/wriml-org)

WRASCI est un système de transcription phonétique en ASCII pur,
conçu pour la documentation computationnelle des langues en danger.

## Doctrine

**Exclusivité alphanumérique stricte** : seuls `[a-z0-9]` sont autorisés.
Aucun caractère spécial — zéro conflit avec JSON, XML, SQL, regex.

**Séparation par espace** : chaque token est un phonème ou un modificateur.
Le parseur se réduit à `chaine.split(" ")` — complexité O(N).

**Suffixes géométriques** :
- `i` — inversé (miroir horizontal)
- `r` — renversé (miroir vertical)
- `u` — arrondi
- `b` — barré

## Intégration WRIML

```wriml
^t''gb a tl''           (forme courte — quotée)
^wa: gb a tl _wa:       (forme standard)
^wrasci: gb a tl _wrasci:  (forme longue — pour les puristes)
```

## Couverture

- Voyelles (API complète + Kiel 2020)
- Consonnes pulmoniques (occlusives, nasales, fricatives, approximantes)
- Consonnes non-pulmoniques (clics, implosives, co-articulations)
- Modificateurs et diacritiques
- Système de tons africains (5 niveaux + contours)

## Documentation

- [Spécification complète](spec/WRASCI-spec.md)
- [Philosophie de conception](spec/WRASCI-rationale.md)
- [Intégration WRIDAL](integration/wridal.md)
- [Intégration WRIMLIFT](integration/wrimlift.md)
