# TIPE - Modélisation Fractale des Villes

Ce TIPE (Travaux d'Initiatives Personnelles encadrées) réalisé durant les années en Classe Préparatoire Scientifique au
lycée Champollion (Grenoble) de 2022 à 2023.

Le thème de cette année était : **la Ville**.

Ce TIPE se place dans le cadre de l'étude des villes et de leur développement à l'aide de modèles mathématiques. La
modélisation choisie ici est celle d'une fractale afin de répondre à la problématique suivante : **_Comment les fractales
peuvent-elles nous renseigner sur l'évolution de nos villes ?_**

NB : Les Informations suivantes pourront être modifiées


## Objectif

L'objectif est ici d'appliquer le modèle mathématique des fractales à une ville (ici Grenoble) et sa périphérie afin 
d'en extraire des informations telles que la dimension de Hausdorff associée (en dimension 2) grâce à la méthode dite 
"*Box Counting Method*" implémentée à l'aide du langage de programmation Python.

Une fois une telle information obtenue, elle sera utilisée pour caractériser la compacité de la ville. Le processus sera
répété à plusieurs reprises mais à des périodes historiques différentes afin d'être capable de commenter l'évolution de
l'indice de compacité au cours du temps, et si possible d'en trouver les raisons socio-économiques.

Une telle étude sera menée à l'aide de cartes d'occupation des sols issues de l'analyse d'image-satellites. Pour des
époques plus anciennes, des cartes historiques seront numériquement traitées afin de les rendre utilisables.

## Bibliographie

* A Study on the Curves of Scaling Behaviour of Fractal Cities
* Fractal carthography of Urbans Areas
* Hausdorff Dimension, its Properties and its Surprises
* The Box Counting Method for Evaluate the Fractal Dimension

## Source des données utilisées

* [IGN Remonter le temps](https://remonterletemps.ign.fr) : Carte de l'État-Major (1866)
* [GeoPortail](https://www.geoportail.gouv.fr/) : Carte IGN (1950)
* [Theia](https://www.theia-land.fr/) : Carte d'occupation des sols (2009, 2010, 2011, 2014, 2016, 2017, 2018)
* [CORINE Land Cover](https://land.copernicus.eu/pan-european/corine-land-cover) : Carte d'occupation des sols (1990, 2000, 2006, 2012, 2018)
