# Modèles numériques du système solaire

## Description

Aujourd'hui, les calculs d'éphémérides pour les planètes du système solaire font appel à des modèles où les équations différentielles résultant de l'application des lois de la physique sont intégrées numériquement. Ces modèles prennent en compte les effets relativistes via une [approximation post-newtonnienne](https://fr.wikipedia.org/wiki/%C3%89quations_d%27Einstein-Infeld-Hoffmann).

Parmi les modèles existants, citons celui de [l’**I**nstitut de **M**écanique **C**éleste et de **C**alcul des **E**phémérides (**IMCCE**)](https://www.imcce.fr/institut/presentation/) : **I**ntégrateur **N**umérique **P**lanétaire de l'**O**bservatoire de **P**aris ([modèle **INPOP**](https://www.imcce.fr/inpop)). Citons aussi celui du [**J**et **P**ropulsion **L**aboratory (**JPL**)](https://www.jpl.nasa.gov/) : **D**eveloppement **E**phemeris ([modèle **DE**](https://ssd.jpl.nasa.gov/)).

Le modèle du JPL étant associé à une [API](https://ssd-api.jpl.nasa.gov/doc/horizons.html) donnant facilement accès aux éphémérides, il sera utilisé ici pour effectuer des comparaisons avec un "modèle Newton", pour illustrer la modélisation par équation d'état et l'intégration numérique des équations différentielles ordinaires.

## Un "modèle Newton" simple

Chacun des $N$ astres inclus dans le modèle a une position $\vec{p_n}$ et une vitesse $\vec{v_n}$ dans le référentiel inertiel [ICRS](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_r%C3%A9f%C3%A9rence_c%C3%A9leste_international).

L'équation d'état qui régit le mouvement de ces astres fait aussi intervenir leur [paramètre gravitationnel standard](https://fr.wikipedia.org/wiki/Param%C3%A8tre_gravitationnel_standard) noté $\mu_k$ :

$$\dfrac{d\vec{p_n}}{dt}=\vec{v_n}$$

$$\dfrac{d\vec{v_n}}{dt}=\sum_{1\leq k \leq N,k \neq n}-\mu_k\dfrac{\vec{p_n}-\vec{p_k}}{\left\lVert\vec{p_n}-\vec{p_k}\right\lVert^3}$$

Ce modèle fait donc appel à la mécanique classique et aux lois de Newton pour la gravitation. Les valeurs des paramètres gravitationnels standards $\mu_k$ sont repris de l'article ["The JPL Planetary and Lunar Ephemerides DE440 and DE441"](https://iopscience.iop.org/article/10.3847/1538-3881/abd414/pdf) (Table 2, page 5).

Le programme de simulation qui résout numériquement l'équation d'état proposée permet de réaliser ensuite des comparaisons avec les [éphémérides fournies par le JPL](https://ssd.jpl.nasa.gov/horizons/app.html#/). Les conditions initiales pour les simulations numériques correspondent à la première ligne des fichiers importés du site du JPL, donc aux positions et vitesses des astres à la date de début choisie. Le pas de calcul pour les simulations numériques est le même que celui choisi pour les fichiers importés, afin de faciliter les comparaisons.

L'objectif est de montrer que la modélisation simplifiée qui est proposée donne cependant des résultats qui restent cohérents avec ces éphémérides très précises du JPL.

## Les programmes Python

### Le "notebook"

Dans le dossier **Notebook**, on trouvera le fichier **Systeme_solaire.ipynb**. Ce fichier est directement utilisable dans **Google Colaboratory**, par exemple. Son exécution génère en effet tous les fichiers de données nécessaires pour effectuer des comparaisons entre les éphémérides délivrées par le JPL et les résultats de simulation du "modèle Newton" proposé.

### Le code

Dans le dossier **Code**, on trouvera le fichier **astro.py** rassemblant toutes les fonctions permettant la récupération des éphémérides du JPL associées au modèle DE, les simulations numériques du "modèle Newton" et les comparaisons entre ces deux modèles.

Dans une console Python, il suffit d'importer le module "astro" avec la ligne ci-dessous.
```
import astro
```

Le fichier **lance_astro.py** donne des exemples d'appel aux différentes fonctions disponibles dans ce module.

### Les données initiales du "modèle Newton"

Le fichier **Planetes.csv** peut être généré "à la main" ou via la fonction **astro.planetes**. Il comprend la liste des planètes prises en compte dans le "modèle Newton". La colonne "id" est un identifiant que l'on peut répurérer avec la fonction **astro.liste_id**.
```
import astro
>>> astro.planetes(Planetes='Planetes.csv')
       Nom            mu      units   id
0   Soleil  1.327124e+11  km^3 s^-2   10
1  Mercure  2.203187e+04  km^3 s^-2    1
2    Venus  3.248586e+05  km^3 s^-2    2
3    Terre  3.986004e+05  km^3 s^-2  399
4     Lune  4.902800e+03  km^3 s^-2  301
5     Mars  4.282838e+04  km^3 s^-2    4
6  Jupiter  1.267128e+08  km^3 s^-2    5
7  Saturne  3.794058e+07  km^3 s^-2    6
8   Uranus  5.794556e+06  km^3 s^-2    7
9  Neptune  6.836527e+06  km^3 s^-2    8
```

