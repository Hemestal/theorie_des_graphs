import os
from array import *
def lire_un_fichier():
    #on ouvre le fichier
    fichier = open("graphe12.txt","r")
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
    #prend en parametre terminal,sommet restant, retourne tab de point d'entrée regarde dans terminal si il y a des valeurs qui manque parmis les sommets restants
    point_entre=[]
    supprimer=True
    for i in range (0,len(sommet_reste)):
        supprimer=True
        for j in range (0,len(terminal)):
            if (sommet_reste[i]==terminal[j]):#si la valeur du sommet existe dans le tableau terminal alors on ne le supprime pas
                supprimer=False
        if (supprimer==True):#si supprimer est vrai cad que la condition précédente n'a pas été executé
            point_entre.append(sommet_reste[i])#on ajoute dans le tableau pt entrée
    return point_entre

def suppr_point(pt_entree,initial,terminal):
    #prend en parametre point entrée et le tab initial et terminal, supprime toutes les valeurs qui coincident entre pt entrée et fusion premiere colonne
    compteur=0
    taille_init=len(initial)
    for entree in pt_entree:
        while compteur<len(initial):#tant que le compteur n'a pas parcouru tout le tableau "initial"
            if(entree==initial[compteur]):#si la valeur dans initial est un point d'entrée, on supprime les valeurs qui sont dans la même ligne
                del initial[compteur]
                del terminal[compteur]
            else:
                compteur=compteur+1
        compteur=0
    return initial,terminal

def detect_circuit(initialtab,terminaltab,nbsommet):
    """
    detect si fin algo=>tab point entrer vide et sommet restant taille est 1=>pas circuit
    si tab_entree est vide et sommet restant>1

    1st step: detect les entrées
    2nd step: supprime ces points
    3rd step: on répète
    detection de sortie=>en haut
    """
    sommet_reste=[]
    for i in range(0,nbsommet):
        sommet_reste.append(i)
    while(True):
        print("points d'entrées:\n")
        pt_entree=point_entre(terminaltab,sommet_reste)
        print(pt_entree,"\n")
        for entree in pt_entree:#on supprime les sommets qui sont des points d'entrées dans le tab des sommets restants
            if (entree in sommet_reste):
                sommet_reste.remove(entree)
        print("sommet restant:\n")
        print(sommet_reste)
        initialtab,terminaltab=suppr_point(pt_entree,initialtab,terminaltab)
        if(len(sommet_reste)==1):#condition de sortie
            print("pas circuit")
            return True
            break
        elif(len(pt_entree)==0 and len(sommet_reste)>1):#condition de sortie
            print("c 1 circuit")
            return False
            break

def ordo(initial,terminal,arc,nbsommet,nbarc,graph):
    """
    prend en paramètre initial, terminal, arc
    appel fction pt entrée
    regarde si il y a q'1 seul entrée
    appel pt sortie
    regarde si il y a q'1 seul sortie
    appel dect_circuit->si pas circuit on continue
    appel valeur identique si oui retourne boléen
    appel valeur pt entrée si oui retoune boléen
    appel arc négative et retourne booléen
    """
    sommet=[]
    initialtab=initial
    terminaltab=terminal
    print(initial)
    for i in range(0,nbsommet):
        sommet.append(i)
    pt_entree=point_entre(terminal,sommet)
    if(len(pt_entree)==1):
        print("il y a bien une seule entrée\n")
        pt_sortie=point_sortie(terminal,sommet)
        if(len(pt_sortie)==1):
            print("il y a bien une seule sortie\n")
            if(detect_circuit(initial,terminal,nbsommet)):
                print("il n'y a pas de circuit\n")
                graph=lire_un_fichier()
                initial,terminal,arc,nbsommet,nbarc=separation(graph)
                if(val_identique(initial,arc,nbsommet)):
                    print("valeurs identiques pour tous les arcs incidents vers l’extérieur à un sommet\n")
                    if(val_pt_entree(pt_entree[0],initial,arc)):
                            print("arcs incidents vers l’extérieur au point d’entrée de valeur nulle")
                            if(is_arc_negative(arc)):
                                print("pas d’arcs à valeur négative")
                            else:
                                print("l'ordonnancement n'est pas correct, il y a une valeur négative\n")
                    else:
                            print("l'ordonnancement n'est pas correct, arcs incidents vers l’extérieur au point d’entrée de valeur non nulle\n")
                else:
                        print("l'ordonnancement n'est pas correct, valeurs pas identique pour tous les arcs incidents vers l’extérieur à un sommet\n")
            else:
                print("l'ordonnancement n'est pas correct, le graphe comporte un circuit\n")
        else:
            print("l'ordonnancement n'est pas correct, il y a pas un seul point de sortie\n")
    else:
        print("l'ordonnancement n'est pas correct, il y a pas un seul point d'entrée\n")



def point_sortie(initial,sommet):
    #prend en parametre initial,sommet restant, retourne tab de point de sorties regarde dans initial si il y a des valeurs qui manque parmis les sommets restants
    point_sortie=[]
    supprimer=True
    for i in range (0,len(sommet)):
        supprimer=True
        for j in range (0,len(initial)):
            if (sommet[i]==initial[j]):#si la valeur du sommet existe dans le tableau terminal alors on ne le supprime pas
                supprimer=False
        if (supprimer==True):#si supprimer est vrai cad que la condition précédente n'a pas été executé
            point_sortie.append(sommet[i])#on ajoute dans le tableau pt entrée
    return point_sortie

def val_pt_entree(entree,initial,arc):
    #prend en parametre entree, initial et arc(valeur de l'arc) regarde pour le pt d'entree si la valeur correspondante est bien 0
    for i in range(0,len(initial)):
        if(entree==initial[i] and arc[i]!=0):
                return False
    return True

def val_identique(initial,arc,nbsommet):
    #prend en parametre initial et arc(valeur de l'arc) regarde pour tous les points de la même valeur si la valeur de l'arc est la même
    tab_comparatif=[]
    for i in range(0,nbsommet):
        for j in range(0,len(initial)):
            if(initial[j]==i):
                tab_comparatif.append(arc[j])
        for j in range(0,len(tab_comparatif)):
            if(tab_comparatif[0]!=tab_comparatif[j]):
                return False
        tab_comparatif.clear
    return True

def is_arc_negative(arc):
    #prend en parametre arc(valeur de l'arc) regarde si il y a une valeur négative
    for negative in arc:
        if (negative<0):
            return False
    return True


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


def afficher_tableau(tab):
    for i in tab:
        print(i)
    print("\n")

def rang_(pt_entree, rang, initial, terminal,circuit):
    if circuit == True:
        tableau_rang = [[]]
        for x in range(0,len(pt_entree)):
            tableau_rang[rang].append(pt_entree[x])
        return tableau_rang
    else:
        print("Il n'y a pas de rang pour ce graphe.\n\n")

def main():
    graph=lire_un_fichier()
    initial,terminal,arc,nbsommet,nbarc=separation(graph)
    matrice_adj=matrice_adjacence(initial,terminal,arc,nbsommet,nbarc)
    matrice_val=matrice_valeur(initial,terminal,arc,nbsommet,nbarc)
    #detect_circuit(initial,terminal,nbsommet)
    ordo(initial,terminal,arc,nbsommet,nbarc,graph)
main()
