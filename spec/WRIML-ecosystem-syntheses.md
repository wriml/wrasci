# WRIML Ecosystem — Notes de synthèse

---

## 1. UCP — Universal Color Palette

### Contexte

La couleur est au cœur de toute communication visuelle — qu'il s'agisse d'un document imprimé, d'une interface web, d'une illustration ou d'une vidéo. Or, les systèmes de couleur actuels sont fragmentés par medium : RVB pour les écrans, CMJN pour l'impression offset, Pantone et couleurs spot pour l'impression de précision. Un designer qui travaille pour plusieurs médias doit aujourd'hui gérer plusieurs fichiers, plusieurs exports, plusieurs conversions — avec des risques de dérive chromatique à chaque étape.

### Problème à résoudre

Il n'existe pas de format de définition de couleur **universel, lisible par l'humain et indépendant du medium**. CSS ne parle que RVB. Les fichiers de palettes propriétaires (ASE, ACO, PAL) sont binaires et non portables. Les profils ICC sont opaques et techniques. Aucun de ces systèmes ne permet à un auteur de dire : *"cette couleur, c'est ça — peu importe où tu l'affiches"*.

### Vision et ambition

UCP est une spécification de couleur **déclarative et universelle**. Une couleur y est définie une seule fois, avec toutes ses coordonnées selon les espaces colorimétriques pertinents. Le medium qui consomme le fichier sélectionne la coordonnée qu'il reconnaît. UCP a vocation à devenir la couche couleur partagée de tout l'écosystème WRIML — utilisée par ADML, USIL et SVL.

### Philosophie

> Définir une fois. Rendre partout.

UCP ne convertit pas — il **déclare**. La responsabilité de la conversion appartient au medium, pas au fichier. Cela préserve l'intention de l'auteur et élimine la dérive chromatique inter-medium.

### Approche

Chaque couleur est un bloc nommé contenant ses coordonnées multi-espaces :

```wriml
^couleur id=''bleu-principal'':
  ^rgb r=''30'' g=''100'' b=''200''*
  ^cmjn c=''85'' m=''50'' j=''0'' n=''22''*
  ^pantone ref=''2945C''*
  ^spot nom=''BLUE-001''*
_couleur:
```

Une palette UCP est un fichier `.ucp` autonome, importable dans tout document de l'écosystème WRIML.

---

## 2. ADML — Appearance Description Markup Language

### Contexte

CSS est le langage de mise en forme dominant du web. Il est puissant, largement supporté — mais conçu exclusivement pour les écrans. Il ne parle que RVB. Il ignore l'impression, les couleurs spot, les unités physiques comme le point typographique ou le millimètre. Un designer qui prépare un document destiné à la fois au web et à l'impression doit aujourd'hui maintenir deux systèmes de mise en forme distincts.

### Problème à résoudre

CSS n'est pas un langage d'apparence universel — c'est un langage d'apparence pour navigateurs. Il manque :
- Un support natif des espaces couleur d'impression (CMJN, Pantone, spot)
- Une philosophie medium-agnostique (écran, papier, projection)
- Une lisibilité auteur comparable à WRIML
- Une intégration native avec un système de couleur universel comme UCP

### Vision et ambition

ADML est une alternative à CSS qui décrit l'apparence d'un document de façon **indépendante du medium**. Il consomme UCP pour la couleur, utilise la syntaxe WRIML, et produit un rendu cohérent que le medium soit un navigateur, une imprimante offset ou un écran de projection. ADML ne remplace pas CSS à court terme — il propose une voie alternative pour les auteurs qui travaillent sur plusieurs médias.

### Philosophie

> L'apparence est une intention, pas une instruction technique.

Un auteur ADML décrit ce qu'il veut obtenir visuellement. La traduction en instructions techniques (CSS pour le web, PostScript pour l'impression) est l'affaire du rendu, pas de l'auteur.

### Approche

À définir en détail. Les grandes lignes :
- Syntaxe WRIML native
- Couleurs référencées depuis une palette UCP
- Unités à la fois relatives (%) et physiques (mm, pt)
- Directives medium conditionnelles (`^si medium=''impression''`)

---

## 3. WRISC / WRIMAC — WRIML Schema for Scientific and Academic Writing

*Note : WRISC et WRIMAC désignent le même langage — le nom définitif n'est pas encore arrêté.*

### Contexte

L'écriture scientifique et académique repose sur deux grandes traditions outillées séparément : TEI (Text Encoding Initiative) pour l'annotation textuelle et les humanités, MathML pour les formules mathématiques. Ces deux standards coexistent mal — modèles de contenu incompatibles, namespaces conflictuels, philosophies divergentes. Un document qui mêle annotation linguistique et formules tombe dans un no man's land technique.

Par ailleurs, LaTeX — qui reste le standard de facto du rendu académique — mêle constamment contenu et formatage. Un fichier `.tex` typique est truffé de `\textbf{}`, `\vspace{}`, `\hfill` inline : le contenu et la présentation sont inextricables.

### Problème à résoudre

L'écriture scientifique est morcelée entre des outils incompatibles. TEI ne parle pas MathML. MathML ne parle pas TEI. LaTeX parle les deux mais au prix d'une confusion permanente entre structure et apparence. Il manque un schéma unifié, orienté contenu, qui couvre l'ensemble du spectre de l'écriture savante dans une syntaxe cohérente et lisible.

### Vision et ambition

WRISC est un schéma WRIML pour l'écriture scientifique et académique. Il unifie dans un seul langage ce que TEI et MathML couvrent séparément — annotations textuelles, gloses interlinéaires, formules, citations, données structurées — sans jamais mêler contenu et présentation.

Le rendu repose sur LaTeX : un transpileur traduit le fichier WRISC en `.tex`, et les classes de documents des publishers (Elsevier, Springer, ACM…) font le reste. Pour rester dans l'écosystème WRIML, une surcouche ADML peut se substituer à LaTeX.

### Philosophie

> Contenu et structure uniquement. Le formatage n'a pas sa place ici.

WRISC bannit toute balise de formatage visuel. Pas de gras, pas d'italique décoratif, pas de mise en page inline. Uniquement du contenu sémantique et de la structure logique. La présentation est déléguée — à LaTeX, aux classes publishers, ou à ADML. Cette contrainte est forte et intentionnelle : elle force une séparation stricte que LaTeX prêche en théorie mais viole constamment en pratique.

### Approche

Hérite de la syntaxe WRIML Core. Ajoute un vocabulaire de balises spécialisées :

```wriml
^formule type=''inline'':
  ^frac:^num:a+b_num: ^den:c_den:_frac:
_formule:

^glose:
  ^mb:tral E jE O fa-li O_mb:
  ^gl:habit ^gr''foc'' ^gr''3'' ^gr''sg'' prendre-^gr''pas''.^gr''perf''_gl:
  ^ft:C'est un habit qu'il a pris_ft:
_glose:
```

---

## 4. WRIDAL — WRIters Data Annotation Language

### Contexte

La recherche produit des données — corpus textuels, tableaux, annotations, métadonnées. Ces données sont aujourd'hui stockées dans des formats hétérogènes : CSV pour les tableaux, XML/TEI pour les corpus annotés, JSON pour les métadonnées structurées. Aucun de ces formats n'est conçu pour être **édité directement par un chercheur non-développeur** tout en restant exploitable par une machine.

### Problème à résoudre

Le chercheur en sciences humaines qui veut annoter un corpus linguistique, archiver des données de terrain ou structurer des résultats d'analyse se retrouve face à un choix inconfortable : soit des formats lisibles mais peu structurés (tableurs, notes texte), soit des formats structurés mais illisibles (XML, JSON brut). Il manque un format qui soit les deux.

### Vision et ambition

WRIDAL est un langage d'annotation de données orienté chercheur. Il permet de structurer, annoter et archiver des données de recherche — qu'il s'agisse de données linguistiques, ethnographiques, bibliographiques ou statistiques — dans un format texte lisible, validable et exportable vers d'autres formats (CSV, JSON, TEI).

### Philosophie

> Les données de recherche appartiennent au chercheur, pas au logiciel.

WRIDAL produit des fichiers texte pérennes, indépendants de tout logiciel propriétaire, archivables sur le long terme et lisibles sans outil spécial.

### Approche

À définir en détail. Les grandes lignes :
- Syntaxe WRIML native
- Structures dédiées aux corpus annotés, aux tableaux, aux métadonnées
- Export vers CSV, JSON, TEI
- Compatible avec les standards d'archivage de données de recherche (Dublin Core, DataCite)

---

## 5. USIL — Universal Scalable Image description Language

### Contexte

Les formats d'image raster dominants — JPEG, PNG, WebP — encodent une image comme une matrice de pixels. Cette approche a une limite fondamentale : la résolution est figée au moment de l'enregistrement. Agrandir une image raster, c'est interpoler — et donc perdre en qualité. SVG résout ce problème pour les illustrations géométriques, mais ne peut pas représenter des photographies réalistes.

Par ailleurs, le monde de la couleur est fragmenté entre les écrans (RVB) et l'impression (CMJN, Pantone). Un fichier image aujourd'hui ne contient qu'une version de sa couleur — ce qui oblige à des exports multiples et des conversions risquées.

### Problème à résoudre

Il n'existe pas de format image qui soit à la fois :
- **Scalable** — rendu parfait à toute résolution
- **Universel** — valide pour les écrans et l'impression dans le même fichier
- **Lisible par l'humain** — éditable à la main, versionnable, diffable
- **Capable de représenter des photographies** réalistes, pas seulement des illustrations

### Vision et ambition

USIL est un langage de **description** d'images, pas d'encodage. Une image USIL n'est pas une grille de pixels — c'est un ensemble de zones, de contours, d'ancres de couleur et de descripteurs sémantiques. Un interpréteur reconstruit l'image à la résolution demandée, en sélectionnant l'espace couleur approprié au medium.

USIL réconcilie dans un seul format ce qui était séparé : illustrations et photographies, écran et impression, fichier source et fichier de rendu.

### Philosophie

> Une image est une description, pas un enregistrement.

Cette philosophie s'inspire directement du système visuel humain : l'œil ne capte pas la réalité de façon exhaustive — il échantillonne, et le cerveau comble les lacunes par inférence. USIL fait de même : il stocke les informations essentielles, et l'interpréteur reconstruit le reste.

### Approche

Trois niveaux de description coexistent dans un fichier `.usi` :

**Description géométrique** — formes, dégradés, contours en courbes de Bézier. Rendu déterministe, scalabilité parfaite.

```wriml
^zone id=''ciel'' type=''dégradé'':
  ^couleur ref=''bleu-matin''*
  ^direction de=''haut'' à=''bas''*
  ^stops:
    ^stop position=''0%'' luminosité=''95%''*
    ^stop position=''100%'' luminosité=''70%''*
  _stops:
_zone:
```

**Description par ancres** — points de référence positionnés en pourcentages, avec coordonnées couleur. La précision des pourcentages s'adapte à la complexité locale de l'image : un dixième suffit pour un ciel uniforme, plusieurs décimales pour un détail fin.

```wriml
^zone id=''iris'' complexité=''élevée'':
  ^ancre x=''47.3821%'' y=''31.0094%'' rgb=''82,143,167''*
  ^ancre x=''47.3902%'' y=''31.0187%'' rgb=''79,140,163''*
_zone:
```

**Description sémantique** — métadonnées sur le contenu d'une zone, exploitées par un interpréteur neuronal pour l'inférence des détails.

```wriml
^zone id=''visage'' type=''portrait'':
  ^sémantique:peau, lumière-gauche, ton-chaud_sémantique:
  ^contour type=''bézier'':
    ^bézier p0=''31%,18%'' p1=''45%,15%'' p2=''58%,19%'' p3=''62%,35%''*
  _contour:
_zone:
```

**Couleurs multi-espaces** via UCP — chaque couleur référencée contient ses coordonnées RVB, CMJN et Pantone. Le medium sélectionne ce qu'il comprend.

**Deux modes de génération** :
- *Génération auteur* — fichier lisible, sémantique, éditable à la main
- *Génération machine* — fichier dense, non sémantique, généré automatiquement par un appareil ou un logiciel, mais toujours valide et enrichissable

---

## 6. SVL — Scalable Video description Language

### Contexte

La vidéo numérique est aujourd'hui encodée en frames — des images successives compressées par des algorithmes comme H.264 ou HEVC. Ces formats sont efficaces : ils ne stockent que les différences entre frames consécutives (delta de pixels). Mais leur unité fondamentale reste le pixel. La scalabilité est absente : une vidéo HD n'est pas une vidéo 4K.

### Problème à résoudre

Les formats vidéo actuels partagent les mêmes limites que les formats image raster :
- Résolution figée à l'encodage
- Espaces couleur uniques (RVB pour le web, YUV pour la compression)
- Fichiers binaires, opaques, non éditables à la main
- Aucune séparation entre la description du contenu et les instructions de rendu

### Vision et ambition

SVL est l'extension temporelle de USIL. Une vidéo SVL est une séquence de descriptions d'images USIL dans le temps, enrichie de balises temporelles, de deltas sémantiques et de directives de mouvement. Elle est **scalable** — le même fichier `.svl` rend correctement sur un téléphone, un écran 4K ou un projecteur de cinéma. Elle est **medium-agnostique** — les couleurs sont définies via UCP, le medium sélectionne son espace colorimétrique.

### Philosophie

> Une vidéo est une description de changement dans le temps, pas une suite de photographies.

Si rien ne change dans une zone pendant dix secondes, **rien n'est stocké** pour cette zone pendant dix secondes. Le gain en poids est structurel, pas algorithmique.

### Approche

SVL ajoute à USIL une dimension temporelle fondée sur trois concepts :

**La frame clé** — description complète d'un état visuel à un instant T, identique à un fichier USIL.

**Le delta sémantique** — description de ce qui change entre deux frames clés. Pas un diff pixel, mais une description de transformation :

```wriml
^delta de=''0s'' à=''3.8s'':
  ^stable zones=''ciel,fond''*
  ^mouvement zone=''visage'' type=''rotation'' axe=''y'' amplitude=''12°''*
  ^transition zone=''lumière'' propriété=''luminosité'' de=''72%'' à=''68%''*
_delta:
```

**La directive stable** — déclare qu'une zone est identique sur une durée donnée. Zéro donnée stockée, rendu parfait.

La scalabilité de SVL est totale : puisque chaque frame est décrite géométriquement et sémantiquement, l'interpréteur peut la rendre à n'importe quelle résolution sans re-encoder. Un seul fichier `.svl` pour tous les écrans.
