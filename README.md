# Fractal Modelisaton of Cities

This TIPE was done during my years in Scientific Preparatory Classes at the Lycée Champollion (Grenoble, France) from 2022 to 2023.

The theme of the year was : **the City**.

>A TIPE ("*Travaux d'Initiatives Personnells encadrées*", literally *Supervised Personal Initiative Work*)) is a project lead during the cursus in Preparatory Class for the competitive exams to access to engineering schools.

This TIPE is about the study of cities and their evolution with mathematical models. Here, I modelised the city of Grenoble with fractals, in order to answer the following problematic :

**In what extend do fractals help us to understand the evolution of our cities ?**

## Objective

In this document I will apply the mathematical model of fractal to cities and their outskirts. It will help me to extract pieces of infomations such as the associated Hausdorff dimension (also called Fractal Dimension) thanks to the *Box-Counting Method*. Moreover, the Hausdorff dimension is correlated with the density of buildings. So, the goal is to evaluate the evolution of urbanization thanks to the Hausdorff dimension, and to explain the socia-economic reasons of the transformations.

 For this, I will use the programming language Python, and repeat the processus for multiple years.

## Data sources

* [CORINE Land Cover](https://land.copernicus.eu/pan-european/corine-land-cover) : Ground Occupation Map (1990, 2006, 2018)

## Results

Fractal Analysis of Grenoble and its outskirt in 1990, 2006 and 2018. Each cell is 1km-sided.

>![Fractal Analysis of Grenoble (1990, 2006, 2018)](results/timelapse_v3.png)

## Approach

First, I divided the maps of Grenoble into 2.5km-sided cells. Then I applied the *Box-Counting Method* to each cell to determine their Hausdorff Dimension. With the first algorithm I used, I obtain the following plots :

>![First Fractal Analysis of Grenoble](results/timelapse_v1.png)

To begin with, we can observe that the global organization of the city is respected : the outksirt is shaped like a 3-branches star because of mountains. The downtown of Grenoble has a Hausdorff Dimension of about 2 which is correct because the builing are near of each other. 

However, some cells have a negative dimension : that's impossible. Indeed, these cells are almost empty. Their dimensions should be about 0 because the organization of buildings is similar to a point.

In order to verify if the algorithm works correctly, I execute it on the [Sierpiński Carpet](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_carpet). The found Hausdorff dimension is 1.60 which is false : it should be 1.89.

So, I decided to change the algorithm to a simpler version of the *Box-Counting Method*, which seems to work better :

>![Second Fractal Analysis of Grenoble](results/timelapse_v2.png)

> The cells are now 1km-sided.

Nevertheless, some packed cells (such as Grenoble's Downtown) don't have a dimension near to 2, but about 1,5 which is illogical.

To solve this problem, I had to artificially increase the side of subdivions to enable the use of larger boxes by the *Box-Counting Method*. I get a more correct dimension (~1.95).

On an other hand, a *try: catch:* block was deleted in the function *fractal_analysis.box_counting* because I thought it was useless. But at the next execution, a log(0) poped in the calcul where the block was took back.

After some investigations, I found an error in the function *fractal_dimension.is_in* : the reset of j was missing. Especially, it means that some low-urbanized areas were associated to a null dimension, even if it shouldn't be the case.

After those two main corrections, I obtained :

>![Third Fractal Analysis of Grenoble](results/timelapse_v3.png)

## Hardware

These analysis were done in 43min, 47min and 49min respectively with the following hardware :

* Processor : Intel Core i5 vPro (2,30GHz)
* RAM : 8GB
* Memory : 512GB SSD
* Programming Language : Python 3.9.2

## Bibliography

* Dierk Schleicher : [*Hausdorff Dimension, its Properties, and its Surprises*](https://arxiv.org/abs/math/0505099) (Sections 1 to 4)

* Mark McClure : [*Chaos and Fractals*](https://www.marksmath.org/classes/Fall2021ChaosAndFractals/chaos_and_fractals_2021/contents.html) (Section 4) 

* Ivana Konatar, Natasa Popovic & Tomo Popovic : [*Box-Counting Method in Python for Fractal Analysis of Biomedical Images*](https://www.semanticscholar.org/paper/Box-Counting-Method-in-Python-for-Fractal-Analysis-Konatar-Popovic/2d7d5f1e1468a30db49e48969abd8a46da32c20c)

* Khaled Harrar & Latifa Hamami : [*The box counting method for evaluate the fractal Dimension in radiographic images*](https://www.researchgate.net/publication/254455405_The_Box_Counting_Method_for_Evaluate_the_Fractal_Dimension_in_Radiographic_Images)

* Sara Encarnação, Marcos Gaudiano, Francisco C. Santos, José A. Tenedório, & Jorge M Pacheco : [*Fractal Carthography of urban area*](https://www.nature.com/articles/srep00527)
