import os
from array import *
import numpy
def lire_un_fichier():
    #on ouvre le fichier
    print("\n")
    print("*****Projet Theorie des Graphes*****")
    print("***** TON Steven, HULIN Pauline, PASCO-CASTILLO Marc *****")
    print("\n\n")
    print(" 1: G01\n 2: G02\n 3: G03\n 4: G04\n 5: G05\n 6: G06\n 7: G07\n 8: G08\n 9: G09\n10: G10\n11: G11\n12: G12\n13: G13\n14: Exit\n")
    c =int(input("Vueillez choisir un nombre entre 1 et 14 pour choisir votre Graphes : "))
    while (c < 1 or c > 14):
        c = int(input("\nchoisir un nombre entre 1 et 14 seulement : "))
    if (c == 1):
        fichier = open("G01.txt","r")
    if (c == 2):
        fichier = open("G02.txt","r")
    if (c == 3):
        fichier = open("G03.txt","r")
    if (c == 4):
        fichier = open("G04.txt","r")
    if (c == 5):
        fichier = open("G05.txt","r")
    if (c == 6):
        fichier = open("G06.txt","r")
    if (c == 7):
        fichier = open("G07.txt","r")
    if (c == 8):
        fichier = open("G08.txt","r")
    if (c == 9):
        fichier = open("G09.txt","r")
    if (c == 10):
        fichier = open("G010.txt","r")
    if (c == 11):
        fichier = open("G11.txt","r")
    if (c == 12):
        fichier = open("G12.txt","r")
    if (c == 13):
        fichier = open("G013.txt","r")
    if (c ==14):
        fichier = exit()
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


def detect_circuit(initial,terminal,nbsommet,afficher):
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
        if(afficher==True):
            print("points d'entrées:\n")
        pt_entree=point_entre(terminal,sommet_reste)
        if(afficher==True):
            print(pt_entree,"\n")
        for entree in pt_entree:#on supprime les sommets qui sont des points d'entrées dans le tab des sommets restants
            if (entree in sommet_reste):
                sommet_reste.remove(entree)
        if(afficher==True):
            print("sommet restant:\n")
            print(sommet_reste)
        initial,terminal=suppr_point(pt_entree,initial,terminal)
        if(len(sommet_reste)==1):#condition de sortie
            if(afficher==True):
                print("pas circuit")
            return True
            break
        elif(len(pt_entree)==0 and len(sommet_reste)>1):#condition de sortie
            if(afficher==True):
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
    for i in range(0,nbsommet):
        sommet.append(i)
    pt_entree=point_entre(terminal,sommet)
    if(len(pt_entree)==1):
        print("il y a bien une seule entrée\n")
        pt_sortie=point_sortie(terminal,sommet)
        if(len(pt_sortie)==1):
            print("il y a bien une seule sortie\n")
            if(detect_circuit(initial,terminal,nbsommet,False)):
                print("il n'y a pas de circuit\n")
                graph=lire_un_fichier()
                initial,terminal,arc,nbsommet,nbarc=separation(graph)
                if(val_identique(initial,arc,nbsommet)):
                    print("valeurs identiques pour tous les arcs incidents vers l’extérieur à un sommet\n")
                    if(val_pt_entree(pt_entree[0],initial,arc)):
                            print("arcs incidents vers l’extérieur au point d’entrée de valeur nulle")
                            if(is_arc_negative(arc)):
                                print("pas d’arc à valeur négative")
                                print("c'est un ordonnancement correct")
                                return True
                            else:
                                print("l'ordonnancement n'est pas correct, il y a une valeur négative\n")
                                return False
                    else:
                            print("l'ordonnancement n'est pas correct, arcs incidents vers l’extérieur au point d’entrée de valeur non nulle\n")
                            return False
                else:
                        print("l'ordonnancement n'est pas correct, valeurs pas identique pour tous les arcs incidents vers l’extérieur à un sommet\n")
                        return False
            else:
                print("l'ordonnancement n'est pas correct, le graphe comporte un circuit\n")
                return False
        else:
            print("l'ordonnancement n'est pas correct, il y a pas un seul point de sortie\n")
            return False
    else:
        print("l'ordonnancement n'est pas correct, il y a pas un seul point d'entrée\n")
        return False



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
        tab_comparatif.clear()
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


def rang(initial, terminal,nbsommet,afficher):
    ##regarder si le graphe est un circuit ou non
    rang=0
    sommet_reste=[]
    sommet_tab=[None]*(nbsommet+1)#on crée la longueur du tableau
    rang_tab=[None]*(nbsommet+1)#on crée la longueur du tableau
    sommet_tab[0]="Sommet"
    rang_tab[0]="Rang"
    print(rang_tab)
    for i in range(1,nbsommet+1):#on insère les sommets dans le tableau
        sommet_tab[i]=(i-1)
    for i in range(0,nbsommet):
        sommet_reste.append(i)#tableau avec tout les sommets non supprimé
    pas_circuit=detect_circuit(initial,terminal,nbsommet,False)
    graph=lire_un_fichier()
    initial,terminal,arc,nbsommet,nbarc=separation(graph)
    nb_entree=point_entre(terminal, sommet_reste)
    if pas_circuit==True:#Si notre graphe n'est pas un circuit

        if(afficher==True):
            print("Calcul du rang\n Méthode d’élimination des points d’entrée\n")

        while len(sommet_reste)!=0:#tant qu'il y a des sommets
            if(afficher==True):
                print("rang courant = ",rang,"\n")
                print("points d'entrée:\n",nb_entree,"\n")
            for entree in nb_entree:#on supprime les sommets qui sont des points d'entrées dans le tab des sommets restants
                if (entree in sommet_reste):
                    sommet_reste.remove(entree)
            for i in range (1,len(rang_tab)):
                for entree in nb_entree:
                    if(sommet_tab[i]==entree):
                        rang_tab[i]=rang
            rang+=1
            initial,terminal=suppr_point(nb_entree,initial,terminal)
            nb_entree=point_entre(terminal, sommet_reste)
            tab_rang=[]
            tab_rang.append([sommet_tab])
            tab_rang.append([rang_tab])
        if(afficher==True):
            afficher_tableau(tab_rang)
    else:
        if(afficher==True):
            print("impossible votre graphe comporte un circuit")

def

def main():
    graph=lire_un_fichier()
    initial,terminal,arc,nbsommet,nbarc=separation(graph)
    #matrice_adj=matrice_adjacence(initial,terminal,arc,nbsommet,nbarc)
    #matrice_val=matrice_valeur(initial,terminal,arc,nbsommet,nbarc)
    #detect_circuit(initial,terminal,nbsommet,True)
    #ordo(initial,terminal,arc,nbsommet,nbarc,graph)
    rang(initial, terminal,nbsommet,True)


main()
