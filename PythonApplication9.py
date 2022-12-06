import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt

data = pd.read_csv("uber.csv")
# premier etape comprendre les donnes 
print(data.head()) # lire les titres pour comprendre les donnees 
print(data.tail()) #  on a 250 ligne 
print(data.shape) # le nombre des lignes est compatible avec la numeration 
print(data.describe()) # la description des donnes montre que les colonnes numeriques, counte les elements , moyennes ecart type(std)
print(data.columns) # affichage des listes des noms des colones et leurs types 
print(data.nunique()) # affichage combien on a chaque colonnes des valeurs uniques 
print(data["Open"].head().unique()) #affichage des uniques valeurs dans le colonnes Open ici colone.head() pour affiche les 5 premiers
# EDA cleaning les donnees 
print(data.isnull().sum()) # premiere choses des cherches les valeurs null dans les donnees utilisant la fonction isnull
# 2eme etape de releve les colonnes inutille par cree une unouvelle base des donnes 
#data2 = data.drop(["les noms des colonnes a leve"], axis = 1)
#dans notre cas, on est besoin de tt les colonnes qu'on a 
#3 eme etape de verifier les valeurs aberrantes, 
#3 : analyse les relation 
corelation = data.corr()
print(corelation)
sns.heatmap(corelation , xticklabels = corelation.columns, yticklabels=corelation.columns , annot = True) #visualisation des corelations
plt.show()
sns.pairplot(data) #verifier la relation entre chaque deux variable des colonnes dans la base des donnnees
plt.show() # un nuage des points est un type des donnees affichees qui montre la entre deux variable obient un trace
sns.relplot( x = 'Open', y = 'High', hue='Date', data = data) # affichage dans plot de parametre open high avec chnagement de DAte sure le data
plt.show()
sns.distplot(data["Open"])# la affichage de la distrubition durant l open 
plt.show()
sns.catplot(x = 'Open', kind = 'box', data= data)
plt.show()
