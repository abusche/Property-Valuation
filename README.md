# Property valuation

## Project description :  

Objectives:  
- Estimate the price of a property according to its characteristics and the current offer on the Strasbourg market based on the KNN algorithm.
- Propose a list of ads available on the internet according to desired characteristics in the Strasbourg area  
- Create a database of properties currently on the market in Strasbourg  

## Description of files :
1) `Basics_estimations_functions.py`: Group of functions used to scrap and process data from real estate sites: Get HTML, get links from ads, import data,...
2) `orpi_fonctions.py` : Grouping of functions to obtain the various characteristics of the residences of the advertisements of the Orpi site
3) `nexity_fonctions.py` : Grouping of functions to obtain the different characteristics of the properties in the ads on the Nexity site
4) `lefigaro_fonctions.py` : Grouping of functions to obtain the different characteristics of homes in ads on the Lefigaro immobilier website
5) `estimation_immobilier_fonctions.py` : Grouping of functions `estimation()` and `annonces()`.

## Libraries needed :  
- requests
- pandas  
- numpy  
- bs4
- scikit-learn
- scipy 

## User guide :  

1) Estimate the price of a property according to its characteristics

```
import estimation_immobilier_fonctions as immobilier
immobilier.estimation()
```

2) Obtain a list of ads available on the internet

```
import estimation_immobilier_fonctions as immobilier
immobilier.annonces()
```
