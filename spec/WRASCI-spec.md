# WRASCI — WRiting ASCii Ipa
## Spécification Technique

**Version :** 1.1 (Kiel 2020 Compliant — Suffixes Géométriques Unifiés)
**Statut :** Spécification de Production

---

## 1. Origine et Philosophie

Le standard **WRASCI** (*WRiting ASCii Ipa*) apporte une solution
moderne au traitement computationnel de l'Alphabet Phonétique
International (API). Contrairement à X-SAMPA ou Kirshenbaum, qui
s'appuient sur des caractères spéciaux (`\`, `_`, `~`, `!`, `^`)
provoquant des conflits lors du parsing (JSON, XML, SQL), WRASCI
repose sur une doctrine stricte :

1. **Exclusivité Alphanumérique** : seuls `[a-z0-9]` autorisés.
2. **Sémantique Espacée** : chaîne segmentée par espaces simples.
   Phonèmes co-articulés et affriquées concaténés (`kp`, `gb`, `tsh`).
   Modificateurs placés *après* le phonème de base.
3. **Double espace** = espace orthographique ordinaire.
4. **Moteur de Suffixes Géométriques** :

| Suffixe | Transformation | Description |
|---|---|---|
| `i` | Miroir horizontal (gauche-droite) | Inversé |
| `r` | Miroir vertical (haut-bas) | Renversé |
| `u` | Arrondissement | Arrondi |
| `b` | Trait de partition | Barré |

---

## 2. Intégration WRIML

```wriml
^t''gb a tl''                   (forme courte — quotée)
^wa: gb a tl _wa:               (forme standard)
^wrasci: gb a tl _wrasci:       (forme longue — puristes)
```

Parseur : `tokens = chaine.split(" ")` — complexité O(N).

---

## 3. Table complète d'équivalence API / X-SAMPA / WRASCI

### 3.1 Voyelles

| API | Description | WRASCI | X-SAMPA | Logique |
|---|---|---|---|---|
| i | Fermée antérieure non arrondie | `i` | `i` | Base |
| y | Fermée antérieure arrondie | `y` | `y` | Base |
| ɨ | Fermée centrale non arrondie | `ib` | `1` | i barré |
| ʉ | Fermée centrale arrondie | `ub` | `}` | u barré |
| ɯ | Fermée postérieure non arrondie | `um` | `M` | u modifié |
| u | Fermée postérieure arrondie | `u` | `u` | Base |
| ɪ | Quasi-fermée quasi-ant. non arrondie | `ic` | `I` | i capital/lax |
| ʏ | Quasi-fermée quasi-ant. arrondie | `yc` | `Y` | y capital/lax |
| ʊ | Quasi-fermée quasi-post. arrondie | `uc` | `U` | u capital/lax |
| e | Mi-fermée antérieure non arrondie | `e` | `e` | Base |
| ø | Mi-fermée antérieure arrondie | `eu` | `2` | e arrondi |
| ɘ | Mi-fermée centrale non arrondie | `ei` | `@\` | e inversé |
| ɵ | Mi-fermée centrale arrondie | `ob` | `8` | o barré |
| ɤ | Mi-fermée postérieure non arrondie | `eo` | `7` | e ouvert |
| o | Mi-fermée postérieure arrondie | `o` | `o` | Base |
| ə | Mi-centrale (Schwa) | `shwa` | `@` | Nom usuel |
| ɛ | Mi-ouverte antérieure non arrondie | `3i` | `E` | 3 inversé |
| œ | Mi-ouverte antérieure arrondie | `oe` | `9` | Ligature OE |
| ɜ | Mi-ouverte centrale non arrondie | `3` | `3` | Visuel direct |
| ɞ | Mi-ouverte centrale arrondie | `3u` | `3\` | 3 arrondi |
| ʌ | Mi-ouverte postérieure non arrondie | `vr` | `V` | v renversé |
| ɔ | Mi-ouverte postérieure arrondie | `oo` | `O` | o ouvert |
| æ | Pré-ouverte antérieure non arrondie | `ae` | `{` | Ligature AE |
| ɐ | Pré-ouverte centrale | `ar` | `6` | a renversé |
| a | Ouverte antérieure non arrondie | `a` | `a` | Base |
| ɶ | Ouverte antérieure arrondie | `aoe` | `&` | a + ligature OE |
| ɑ | Ouverte postérieure non arrondie | `ao` | `A` | a ouvert |
| ɒ | Ouverte postérieure arrondie | `aou` | `Q` | ao arrondi |

### 3.2 Consonnes Pulmoniques — Occlusives et Nasales

| API | Description | WRASCI | X-SAMPA | Logique |
|---|---|---|---|---|
| p / b | Occlusives bilabiales | `p` / `b` | `p` / `b` | Base |
| t / d | Occlusives alvéolaires | `t` / `d` | `t` / `d` | Base |
| ʈ / ɖ | Occlusives rétroflexes | `ttr` / `dtr` | `t\`` / `d\`` | +tr rétroflexe |
| c | Occlusive palatale sourde | `c` | `c` | Base |
| ɟ | Occlusive palatale voisée | `cj` | `J\` | c voisé |
| k / g | Occlusives vélaires | `k` / `g` | `k` / `g` | Base |
| q | Occlusive uvulaire sourde | `q` | `q` | Base |
| ɢ | Occlusive uvulaire voisée | `gq` | `G\` | g uvulaire |
| ʔ | Occlusive glottale | `glot` | `?` | glottal stop |
| m / ɱ | Nasales bilabiale / labiodentale | `m` / `mv` | `m` / `M` | base / +v |
| n / ɳ | Nasales alvéolaire / rétroflexe | `n` / `ntr` | `n` / `n\`` | base / +tr |
| ɲ | Nasale palatale | `ny` | `J` | digraphe naturel |
| ŋ / ɴ | Nasales vélaire / uvulaire | `ng` / `ngq` | `N` / `N\` | digraphe / +q |

### 3.3 Consonnes Pulmoniques — Fricatives

| API | Description | WRASCI | X-SAMPA | Logique |
|---|---|---|---|---|
| ɸ / β | Bilabiales sourde / voisée | `ph` / `bh` | `p\` / `B` | phi / beta |
| f / v | Labiodentales | `f` / `v` | `f` / `v` | Base |
| θ / ð | Dentales sourde / voisée | `tht` / `dht` | `T` / `D` | theta / delta |
| s / z | Alvéolaires | `s` / `z` | `s` / `z` | Base |
| ʃ / ʒ | Post-alvéolaires | `sh` / `zh` | `S` / `Z` | digraphes |
| ʂ / ʐ | Rétroflexes sourde / voisée | `str` / `ztr` | `s\`` / `z\`` | +tr |
| ç / ʝ | Palatales sourde / voisée | `cc` / `jc` | `C` / `j\` | palatales |
| x / ɣ | Vélaires sourde / voisée | `x` / `gh` | `x` / `G` | base / g fricatif |
| χ | Uvulaire sourde | `ch` | `X` | ach-laut |
| ʁ | Uvulaire voisée | `rfr` | `R\` | r français |
| ħ / ʕ | Pharyngales sourde / voisée | `hph` / `phv` | `X\` / `?\` | pharyngales |
| h / ɦ | Glottales sourde / voisée | `h` / `hv` | `h` / `H\` | base / voisée |

### 3.4 Consonnes Pulmoniques — Approximantes et Latérales

| API | Description | WRASCI | X-SAMPA | Logique |
|---|---|---|---|---|
| r | Vibrante alvéolaire | `r` | `r` | Base |
| ʀ | Vibrante uvulaire | `rq` | `R` | r uvulaire |
| ɾ | Battue alvéolaire | `r1` | `4` | r 1 battement |
| ɽ | Battue rétroflexe | `r1tr` | `r\`` | r1 +tr |
| ʋ | Approximante labiodentale | `vh` | `v\` | v spirant |
| ɹ | Approximante alvéolaire | `ra` | `r\` | r approximant |
| ɻ | Approximante rétroflexe | `ratr` | `r\`` | ra +tr |
| j | Approximante palatale (yod) | `j` | `j` | Base |
| w | Approximante labio-vélaire | `w` | `w` | Base |
| l / ɭ | Latérales alvéolaire / rétroflexe | `l` / `ltr` | `l` / `l\`` | base / +tr |
| ʎ | Latérale palatale | `ly` | `L` | l mouillé |
| ʟ | Approximante latérale vélaire | `lk` | `L\` | l vélaire |
| ɬ / ɮ | Fricatives latérales sourde / voisée | `ls` / `lv` | `t\` / `d\` | l sourde/voisée |

### 3.5 Consonnes Non-Pulmoniques et Co-articulations

| API | Description | WRASCI | X-SAMPA | Logique |
|---|---|---|---|---|
| ʘ | Clic bilabial | `clb` | `O\` | clic bilabial |
| ǀ | Clic dental | `cld` | `|\` | clic dental |
| ǃ | Clic alvéolaire | `cla` | `!\` | clic alvéolaire |
| ǂ | Clic palatal | `clp` | `=\` | clic palatal |
| ǁ | Clic latéral | `cll` | `s\` | clic latéral |
| ɓ / ɗ | Implosives bilabiale / alvéolaire | `bimp` / `dimp` | `b_<` / `d_<` | +imp |
| ʄ / ɠ | Implosives palatale / vélaire | `jimp` / `gimp` | `J\_<` / `g_<` | +imp |
| ʛ | Implosive uvulaire | `qimp` | `G\_<` | +imp |
| k͡p / g͡b | Occlusives labio-vélaires | `kp` / `gb` | `kp` / `gb` | concaténation |
| t͡s / d͡z | Affriquées alvéolaires | `ts` / `dz` | `ts` / `dz` | concaténation |
| t͡ʃ / d͡ʒ | Affriquées post-alvéolaires | `tsh` / `dzh` | `tS` / `dZ` | concaténation |

### 3.6 Autres Symboles (Kiel 2020)

| API | Description | WRASCI | X-SAMPA | Logique |
|---|---|---|---|---|
| ʍ | Fricative labio-vélaire sourde | `wsh` | `W` | w sourd |
| ɥ | Approximante labio-palatale voisée | `wy` | `H` | w+y |
| ʜ / ʢ | Fricatives épiglottales | `hch` / `rgh` | `H\` / `<\` | épiglottales |
| ʡ | Occlusive épiglottale | `epl` | `>\` | epiglottal plosive |
| ɕ / ʑ | Fricatives alvéolo-palatales | `csh` / `jzh` | `c` / `z\` | palatales |
| ɺ | Battue latérale alvéolaire | `l1` | `l\` | l 1 battement |
| ɧ | Fricative simultanée ʃ+x | `shx` | `x\` | concaténation |

### 3.7 Modificateurs, Diacritiques et Tons

| API | Description | WRASCI | X-SAMPA | Logique |
|---|---|---|---|---|
| ː | Allongement | `lg` | `:` | long |
| ˑ | Semi-allongement | `slg` | `:\` | semi-long |
| ̃ | Nasalisation | `nas` | `~` | nasalisation |
| ʰ | Aspiration | `asp` | `_h` | aspiration |
| ʼ | Éjective | `ej` | `_>` | éjective |
| ʷ | Labialisation | `lab` | `_w` | labialisation |
| ʲ | Palatalisation | `pal` | `_j` | palatalisation |
| ̥ | Dévoisement | `nvx` | `_0` | non-voix |
| ̬ | Voisement | `vx` | `_v` | voix |
| ◌̘ / ◌̙ | ATR / RTR | `atr` / `rtr` | `_A` / `_q` | acronymes intl |
| ꜛ / ꜜ | Upstep / Downstep | `ustp` / `dstp` | `^` / `!` | pas tonal |
| ↗ / ↘ | Intonation montante / descendante | `glr` / `glf` | N/A | global |

#### Tons africains

| API | Description | WRASCI | X-SAMPA |
|---|---|---|---|
| ◌̋ | Ton Très Haut | `thh` | `_T` |
| ◌́ | Ton Haut | `th` | `_H` |
| ◌̄ | Ton Moyen | `tm` | `_M` |
| ◌̀ | Ton Bas | `tl` | `_L` |
| ◌̏ | Ton Très Bas | `tll` | `_B` |
| ◌̌ | Contour Montant | `tlh` | `_R` |
| ◌̂ | Contour Descendant | `thl` | `_F` |
| ◌᷄ | Contour Mi-Haut Montant | `tmh` | N/A |
| ◌᷅ | Contour Mi-Bas Descendant | `tml` | N/A |
| ◌᷈ | Contour Montant-Descendant | `tlhl` | N/A |

---

## 4. Exemples

```
^wa: gb a tl _wa:               [g͡bà]  — langue Ega (Côte d'Ivoire)
^wa: i nas th _wa:              [ĩ́]    — voyelle nasale tonème haut
^wa: t sh i tl  i tl _wa:      [tʃì ì] — deux mots séparés
^wa: atr e th _wa:              [é̘]   — voyelle ATR haute
```
