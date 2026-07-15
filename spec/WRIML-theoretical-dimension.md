# La dimension théorique de WRIML
## Vers une théorie documentaire orientée auteur

---

# 1. Introduction

WRIML n’est pas seulement un langage de balisage ni une simple alternative syntaxique à XML ou Markdown. À travers son noyau et ses projets dérivés, il tend progressivement vers une vision plus large :

> une théorie documentaire centrée sur l’intention humaine, la pérennité des données et la séparation stricte entre contenu et rendu.

Cette dimension théorique n’a pas été construite d’un seul bloc. Elle émerge naturellement des problèmes concrets rencontrés dans :
- l’écriture scientifique,
- l’annotation linguistique,
- l’archivage de données,
- la publication multi-support,
- la représentation de la couleur,
- et plus largement la tension permanente entre structure et rendu dans les systèmes numériques modernes.

WRIML cherche moins à “remplacer XML” qu’à proposer un paradigme documentaire différent :
- orienté auteur,
- lisible,
- pérenne,
- déclaratif,
- indépendant des mediums techniques.

---

# 2. Le principe fondamental de WRIML

Le principe central de l’écosystème peut être formulé ainsi :

> Le fichier source doit préserver l’intention humaine de haut niveau, et non l’état technique d’un medium particulier.

Cette idée traverse tout l’écosystème WRIML.

Le document source ne doit pas être :
- une suite d’instructions techniques,
- un état de rendu figé,
- ni une dépendance à un dispositif particulier.

Il doit être :
- une description sémantique,
- lisible par l’humain,
- stable dans le temps,
- interprétable par différents moteurs de rendu.

---

# 3. Une opposition implicite au paradigme “device-first”

La plupart des formats modernes sont construits autour du medium de rendu.

## Exemples

### CSS
CSS décrit principalement :
- le comportement d’un navigateur,
- dans un environnement écran,
- basé sur RGB.

### JPEG / PNG
Les formats raster décrivent :
- une matrice de pixels,
- figée à une résolution donnée.

### LaTeX
LaTeX mélange :
- structure,
- rendu,
- mise en page,
- commandes typographiques.

### Vidéo moderne
Les codecs vidéo actuels stockent :
- des différences de pixels,
- dépendantes d’une résolution donnée,
- dans des formats binaires opaques.

---

WRIML tend vers une approche opposée :

# paradigme author-first

Le document y est pensé comme :
- une intention structurée,
- indépendante du medium,
- durable,
- réinterprétable.

---

# 4. La séparation structure / rendu

La séparation entre :
- contenu,
- structure,
- apparence,
- implémentation technique,

constitue l’un des piliers théoriques majeurs de WRIML.

---

## 4.1 Le contenu

Le contenu correspond à ce que l’auteur veut exprimer.

Exemples :
- une citation,
- une formule,
- une glose linguistique,
- une section,
- une couleur,
- une zone visuelle.

---

## 4.2 Le rendu

Le rendu correspond à la traduction technique de cette intention :
- HTML,
- CSS,
- PDF,
- PostScript,
- moteur typographique,
- écran,
- impression,
- codec vidéo,
- etc.

---

## 4.3 Le principe WRIML

WRIML considère que :

> le rendu appartient au moteur d’interprétation, pas au document source.

Cette idée se retrouve dans tous les sous-projets de l’écosystème.

---

# 5. Implémentation de cette philosophie dans les sous-projets

---

# 5.1 WRIML Core

WRIML Core constitue la couche syntaxique fondamentale de l’écosystème.

Son objectif n’est pas seulement de baliser des données, mais de fournir :
- une syntaxe lisible,
- éditable directement,
- expressive,
- stable,
- adaptée aux humains autant qu’aux machines.

---

## Philosophie du noyau

WRIML Core tente d’équilibrer :
- rigueur structurelle,
- confort de saisie,
- lisibilité,
- expressivité documentaire.

Il hérite de la tradition SGML/XML tout en cherchant à réduire :
- la verbosité,
- le bruit syntaxique,
- la fatigue visuelle,
- la surcharge de fermeture.

---

## Position théorique implicite

WRIML Core considère qu’un format documentaire doit être :
- humainement éditable,
- durable,
- diffable,
- versionnable,
- indépendant des logiciels propriétaires.

Le texte brut redevient :
- une source primaire,
- et non un artefact technique secondaire.

---

# 5.2 WRISC
## Le manuscrit scientifique comme structure sémantique

WRISC applique les principes de WRIML à l’écriture scientifique.

---

## Position théorique

WRISC considère que :

> un manuscrit scientifique est une structure intellectuelle, pas une mise en page.

Ainsi :
- le gras,
- les espacements,
- les artifices typographiques,
- les ajustements visuels inline,

n’appartiennent pas au document source.

---

## Opposition implicite à LaTeX traditionnel

WRISC réagit à une tension historique :

LaTeX défend théoriquement la séparation structure/rendu, mais en pratique :
- mélange constamment contenu et présentation,
- pousse les auteurs à écrire des commandes typographiques inline.

WRISC pousse cette séparation beaucoup plus loin.

---

## Conséquence

Le fichier WRISC devient :
- une représentation logique du manuscrit,
- indépendante :
  - du PDF,
  - du template éditeur,
  - du medium final.

Le rendu est ensuite délégué :
- à LaTeX,
- à Pandoc,
- à HTML,
- à d’autres moteurs futurs.

---

## Théorie implicite du manuscrit

WRISC considère qu’un article scientifique est avant tout :
- une structure argumentative,
- un ensemble de données intellectuelles,
- une organisation logique du savoir.

La mise en page n’est qu’une projection secondaire.

---

# 5.3 WRIDAL
## La donnée de recherche comme patrimoine documentaire

WRIDAL applique les principes WRIML à l’annotation et à l’archivage des données de recherche.

---

## Position théorique

WRIDAL considère que :

> les données de recherche appartiennent au chercheur, pas au logiciel.

Ainsi :
- les données doivent rester lisibles,
- archivables,
- indépendantes des outils,
- pérennes.

---

## Opposition implicite

WRIDAL réagit contre :
- les formats propriétaires,
- les structures opaques,
- les systèmes dépendants d’applications spécifiques.

---

## La donnée comme document durable

Dans WRIDAL :
- un corpus,
- une annotation,
- une métadonnée,
- un tableau,

deviennent des objets documentaires lisibles directement.

---

## Dimension archivistique

WRIDAL s’inscrit implicitement dans une logique de :
- préservation,
- interopérabilité,
- documentation scientifique,
- archivage long terme.

Cette orientation le rapproche :
- des humanités numériques,
- des archives linguistiques,
- des infrastructures documentaires de recherche.

---

# 5.4 UCP
## La couleur comme entité documentaire

UCP applique la philosophie WRIML au problème de la couleur.

---

## Problème fondamental

Les systèmes actuels définissent les couleurs selon :
- un medium,
- un espace colorimétrique,
- un dispositif de rendu.

Exemples :
- RGB,
- CMYK,
- Pantone,
- couleurs spot.

---

## Position théorique de UCP

UCP considère que :

> une couleur possède une identité documentaire indépendante du medium.

Les différentes coordonnées colorimétriques ne sont alors que :
- des projections techniques,
- d’une même entité abstraite.

---

## Conséquence

Le fichier source :
- ne convertit pas,
- ne privilégie pas un medium,
- ne fixe pas un rendu unique.

Il déclare :
- l’identité de la couleur,
- et laisse le medium sélectionner sa représentation.

---

## Théorie implicite de la couleur

UCP traite la couleur comme :
- une donnée sémantique,
- et non un simple paramètre technique.

Cette approche rapproche la couleur :
- du document,
- de l’édition,
- et de la conservation d’intention auteur.

---

# 5.5 ADML
## L’apparence comme intention

ADML applique cette philosophie au rendu visuel.

---

## Position théorique

ADML considère que :

> l’apparence est une intention, pas une implémentation technique.

L’auteur décrit :
- une hiérarchie visuelle,
- une dominance,
- une relation spatiale,
- une logique de présentation.

Le moteur traduit ensuite :
- vers CSS,
- PostScript,
- PDF,
- ou d’autres systèmes.

---

## Opposition implicite à CSS

CSS reste fortement :
- écran-centrique,
- navigateur-centrique,
- RGB-centrique.

ADML cherche une approche :
- medium-agnostique,
- multi-support,
- typographiquement plus universelle.

---

# 5.6 USIL
## L’image comme description

USIL pousse la logique WRIML vers la représentation visuelle.

---

## Position théorique

USIL considère que :

> une image n’est pas un enregistrement mais une description.

Ainsi :
- l’image n’est plus une grille de pixels,
- mais un ensemble :
  - de formes,
  - de zones,
  - d’ancres,
  - de relations,
  - de descriptions sémantiques.

---

## Inspiration implicite

Cette approche se rapproche :
- de la perception humaine,
- de la représentation continue,
- de la reconstruction,
- de la description plutôt que de l’échantillonnage brut.

---

## Conséquence

Le rendu devient :
- scalable,
- réinterprétable,
- adaptable au medium.

---

# 5.7 SVL
## La vidéo comme transformation décrite

SVL étend cette logique à la temporalité.

---

## Position théorique

SVL considère que :

> une vidéo est une description de changement dans le temps, pas une suite d’images.

---

## Conséquence

Le système décrit :
- des états,
- des transformations,
- des zones stables,
- des mouvements,
- des transitions.

Le medium reconstruit ensuite le rendu.

---

# 6. La cohérence profonde de l’écosystème

Malgré leurs domaines différents, tous les projets WRIML partagent les mêmes invariants :

| Principe | Manifestation |
|---|---|
| Primauté de l’intention | Tous les projets |
| Séparation structure/rendu | WRISC, ADML, UCP |
| Medium-agnosticisme | UCP, ADML, USIL, SVL |
| Lisibilité humaine | WRIML Core, WRIDAL |
| Pérennité documentaire | WRIDAL, WRISC |
| Description plutôt qu’encodage | USIL, SVL |
| Déclaration plutôt qu’instruction | UCP, ADML |
| Auteur-first | Ensemble de l’écosystème |

---

# 7. Conclusion

WRIML ne constitue pas seulement une famille de langages.

L’écosystème tend progressivement vers :
- une théorie documentaire,
- une théorie du rendu,
- et une philosophie de la représentation numérique.

Son idée centrale peut être résumée ainsi :

> préserver l’intention humaine indépendamment des technologies de rendu.

Dans cette vision :
- le document précède le medium,
- la structure précède l’implémentation,
- la description précède l’encodage,
- et le fichier source redevient un objet humainement intelligible.