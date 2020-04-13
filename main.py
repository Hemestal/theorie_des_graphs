import os
from array import *
def lire_un_fichier():
    #on ouvre le fichier
    fichier = open("L3_E08_1.txt","r")
    graph=[]#on créer le tableau mémoire
    lignes=fichier.readlines()#on transforme lignes en tableaux de lignes du fichier
    valeur=int(lignes[0])#transforme la premiere ligne en int
    graph.append(valeur)#on rajoute cette valeur au tableau "graph"
    valeur=int(lignes[1])#idem avec la 2eme
    graph.append(valeur)
    compteur_string=0
    compteur_fichier=2
    while len(lignes)!=compteur_fichier:
        separation=lignes[compteur_fichier].split(" ")#
        graph.append([int(separation[0]),int(separation[1]),int(separation[2])])
        compteur_fichier=compteur_fichier+1
    print(graph)
    fichier.close()
lire_un_fichier()