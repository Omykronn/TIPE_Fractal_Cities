# TIPE - Modélisation Fractale des Villes

Ce TIPE (Travaux d'Initiatives Personnelles encadrées) réalisé durant les années en Classe Préparatoire Scientifique au
lycée Champollion (Grenoble) de 2022 à 2023.

Le thème de cette année était : **la Ville**.

Ce TIPE se place dans le cadre de l'étude des villes et de leur développement à l'aide de modèles mathématiques. La
modélisation choisie ici est celle d'une fractale afin de répondre à la problématique suivante : **_Comment les fractales
peuvent-elles nous renseigner sur l'évolution de nos villes ?_**

NB : Les informations suivantes pourront être modifiées


## Objectif

L'objectif est ici d'appliquer le modèle mathématique des fractales à une ville (ici Grenoble) et sa périphérie afin 
d'en extraire des informations telles que la dimension de Hausdorff associée (en dimension 2) grâce à la méthode dite 
"*Box Counting Method*" implémentée à l'aide du langage de programmation Python.

Une fois une telle information obtenue, elle sera utilisée pour caractériser la compacité de la ville. Le processus sera
répété à plusieurs reprises mais à des périodes historiques différentes afin d'être capable de commenter l'évolution de
l'indice de compacité au cours du temps, et si possible d'en trouver les raisons socio-économiques.

Une telle étude sera menée à l'aide de cartes d'occupation des sols issues de l'analyse d'image-satellites. Pour des
époques plus anciennes, des cartes historiques seront numériquement traitées afin de les rendre utilisables.


## Premiers Résultats

Après avoir divisé la périphérie de Grenoble en 400 carrés de 2.5km de côté, on applique la méthode dite *Box Counting
Method* à chacune d'entre elles afin d'en déduire la dimension fractale (ou de Hausdorff) de chacune. Dans le cas de la
ville de Grenoble en 2018, on obtient la répartition suivante : 

![Analyse Fractale de Grenoble en 2018](results/Grenoble_2018.png)

Tout d'abord, on retrouve l'organisation générale de la ville de Grenoble avec son hypercentre (au centre en bleu) où
les bâtiments sont répartis plus densément et sa périphérie en forme d'étoile à trois branches imposée par les montagnes.

Toutefois, on observe des zones de dimensions fractales négatives, ce qui est impossible. Après étude des zones concernées,
on découvre que ce sont des zones quasiment vides, dont la répartition des bâtiments se rapproche du point. Cela devrait 
alors être associé à une dimension fractale proche de 0. 

On pourrait alors songer à simplement forcer l'algorithme à affecter la valeur zéro dans le cas d'une dimension trouvée 
négative. Pourtant, il semble plus intéressant d'affecter le complément à 2 de la dimension trouvée puisque qu'on pourrait
interpréter le résultat trouvé comme la dimension de Hausdorff de l'ensemble formée par les zones sans bâtiments.

## Bibliographie

* A Study on the Curves of Scaling Behaviour of Fractal Cities
* Fractal carthography of Urbans Areas
* Hausdorff Dimension, its Properties and its Surprises
* The Box Counting Method for Evaluate the Fractal Dimension

## Source des données utilisées

[CORINE Land Cover](https://land.copernicus.eu/pan-european/corine-land-cover) : Carte d'occupation des sols (1990, 2006, 2018)
