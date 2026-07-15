# WRASCI — Intégration WRIDAL

## Balises disponibles

```wriml
^t''a tl''*                       (forme quotée — inline)

^wa: gb a tl _wa:                 (forme standard)

^wrasci: gb a tl _wrasci:         (forme longue)
```

## Dans un corpus WRIDAL

```wriml
^corpus.tok id="tok-001":
    ^corpus.tx: gbà _corpus.tx:
    ^wa: gb a tl _wa:
    ^corpus.gl: boire _corpus.gl:
_corpus.tok:
```

## Dans une annotation acoustique

```wriml
^corpus.interval xmin="0.195" xmax="0.450"
                 label="a" id="ph-003":
    ^wa: a th _wa:
_corpus.interval:
```
