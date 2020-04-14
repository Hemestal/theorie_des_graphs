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
        separation=lignes[compteur_fichier].split(" ")#on sépare le string en plusieurs string avec les espaces
        graph.append([int(separation[0]),int(separation[1]),int(separation[2])])#on transforme les strings en int et on ajoute dans le tab
        compteur_fichier=compteur_fichier+1
    #print(graph)
    fichier.close()
    return graph



def matrice_adjacence(initial,terminal,arc,nbsommet,nbarc):
    tab=[['']]#la valeur " " représente la position [0][0] qui devrait etre vide
    compteur=0
    ajoutage=0
    #remplissage des index dans le tableau
    for i in range(0,nbsommet):
        tab[0].append(i)
    for j in range(0,nbsommet):
        tab.append([j])
    #remplissage du tableau
    for i in range(1,nbsommet+1):
        for j in range(1,nbsommet+1):
            while compteur!=len(initial):#ici mon met la taille du tab initial mais ca peux etre terminal ou arc
                if(initial[compteur]==(i-1) and terminal[compteur]==(j-1)):#si trouve que les valeurs correspondent alors on ajoute 1
                    tab[i].append(1)
                    ajoutage=1
                compteur=compteur+1
            if(ajoutage==0):#sinon on ajoute 0
                tab[i].append(0)
            else:
                ajoutage=0
            compteur=0
    return tab


def matrice_valeur(initial,terminal,arc,nbsommet,nbarc):
    tab=[['']]#la valeur " " représente la position [0][0] qui devrait etre vide
    verif=0
    compteur=0
    ajoutage=0
    #remplissage des index dans le tableau
    for i in range(0,nbsommet):
        tab[0].append(i)
    for j in range(0,nbsommet):
        tab.append([j])
    #remplissage du tableau
    for i in range(1,nbsommet+1):
        for j in range(1,nbsommet+1):
            while verif==0 and compteur!=len(initial):#ici mon met la taille du tab initial mais ca peux etre terminal ou arc
                if(initial[compteur]==(i-1) and terminal[compteur]==(j-1)):#si trouve que les valeurs correspondent alors on ajoute la valeur de l'arc
                    tab[i].append(arc[compteur])
                    ajoutage=1
                compteur=compteur+1
            if(ajoutage==0):#sinon on ajoute *
                tab[i].append("*")
            else:
                ajoutage=0
            compteur=0
    return tab
"""
def detection_circuit(initial,terminal,arc,nbsommet,nbarc):
    print("detection de cicruit\n")
    print("Méthode d’élimination des points d’entrée\n")
    pas_entree=False
    entree_suppr=[]
    while(pas_entree != True or len(terminal)==0):
        for i in range(0,nbsommet):
            if(i not in terminal):
                for y in range(0,len(terminal)-1):
                    print("\npoint d'entrée:\n")
                    if(initial[y]==i):
                        print(y)
                        initial.pop(y)
                        terminal.pop(y)
            else:
                print("aucun\n")
                pas_entree=True
    if(pas_entree==False):
        print("le graphe contient au moins un circuit")
    elif(pas_entree==True):
        print("il n'y a pas de circuits")
"""

def separation(graph):#dans cette fonction, on décompose le premier tableau pour que ce soit plus pratique
    nbsommet=graph[0]
    nbarc=graph[1]
    initial = []
    for i in range(2,nbarc+2):
        initial.append(graph[i][0])
    terminal = []
    for i in range(2,nbarc+2):
        terminal.append(graph[i][1])
    arc = []
    for i in range(2,nbarc+2):
        arc.append(graph[i][2])
    return initial,terminal,arc,nbsommet,nbarc


def afficher_tableau(tab=[]):
    for i in tab:
        print(i)
    print("\n")

def main():
    graph=lire_un_fichier()
    initial,terminal,arc,nbsommet,nbarc=separation(graph)
    matrice_adj=matrice_adjacence(initial,terminal,arc,nbsommet,nbarc)
    matrice_val=matrice_valeur(initial,terminal,arc,nbsommet,nbarc)
    afficher_tableau(matrice_adj)
main()
