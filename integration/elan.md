# WRASCI — Intégration ELAN

WRASCI peut être utilisé comme valeur de tier dans ELAN,
directement dans le champ texte d'une annotation.

## Workflow recommandé

1. Annoter dans ELAN avec WRASCI dans un tier dédié
   (`phonetic-wrasci@L001`)
2. Importer dans WRIDAL-corpus via `^corpus.tier`
3. Le tier WRASCI est préservé tel quel — aucune conversion
   nécessaire à l'import

## Exemple

```
Tier : phonetic-wrasci@L001
Annotation : gb a tl
```

Devient dans WRIDAL :

```wriml
^corpus.tier id="phonetic-wrasci@L001"
             type="alignable" speaker="L001":
    ^corpus.ann id="a001" ts-start="ts001" ts-end="ts002":
        ^wa: gb a tl _wa:
    _corpus.ann:
_corpus.tier:
```
