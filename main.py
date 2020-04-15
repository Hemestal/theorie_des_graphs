import os
from array import *
def lire_un_fichier():
    #on ouvre le fichier
    fichier = open("graphe2.txt","r")
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

def point_entre(terminal,sommet_reste):
    #prend en parametre fusion,sommet restant, retourne tab de point d'entrée regarde dans fusion colonne 2 si il y a des valeurs qui manque parmis les sommets restants
    point_entre=[]
    supprimer=True
    for i in range (0,len(sommet_reste)):
        supprimer=True
        for j in range (0,len(terminal)):
            if (sommet_reste[i]==terminal[j]):
                supprimer=False
        if (supprimer==True):
            point_entre.append(sommet_reste[i])
    return point_entre

def suppr_point(pt_entree,initial,terminal):
    #prend en parametre point entrée et le graph fusion, supprime toutes les valeurs qui coincident entre pt entrée et fusion premiere colonne
    compteur=0
    taille_init=len(initial)
    for entree in pt_entree:
        while compteur<len(initial):
            if(entree==initial[compteur]):
                del initial[compteur]
                del terminal[compteur]
            else:
                compteur=compteur+1
        compteur=0
    #print("tableau init:",initial)
    #print("tableau term:",terminal)
    return initial,terminal

def detect_circuit(initial,terminal,nbsommet):
    """
    detect si fin algo=>tab point entrer vide et sommet restant taille est 1=>pas circuit
    si tab_entree est vide et sommet restant>1

    1st step: detect les entrées
    2nd step: supprime ces points
    3rd step: on répète
    detection de sortie=>en haut
    """
    #pt_entree=[]
    sommet_reste=[]
    for i in range(0,nbsommet):
        sommet_reste.append(i)
    while(True):
        print("points d'entrées:\n")
        pt_entree=point_entre(terminal,sommet_reste)
        print(pt_entree,"\n")
        for entree in pt_entree:#on supprime les sommets qui sont des points d'entrées dans le tab des sommets restants
            if (entree in sommet_reste):
                sommet_reste.remove(entree)
        print("sommet restant:\n")
        print(sommet_reste)
        initial,terminal=suppr_point(pt_entree,initial,terminal)
        if(len(sommet_reste)==1):#condition de sortie
            print("pas circuit")
            break
        elif(len(pt_entree)==0 and len(sommet_reste)>1):#condition de sortie
            print("c 1 circuit")
            break


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
    detect_circuit(initial,terminal,nbsommet)
main()
