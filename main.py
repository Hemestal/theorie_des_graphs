import os
from array import *


print("\n")
print("***** Projet Theorie des Graphes *****")
print("***** TON Steven, HULIN Pauline, PASCO-CASTILLO Marc *****")
print("\n\n")
print("1: G01\n 2: G02\n 3: G03\n 4: G04\n 5: G05\n 6: G06\n 7: G07\n 8: G08\n 9: G09\n10: G10\n11: G11\n12: G12\n13: G13\n14: Exit\n")
print("\n")


c = int(input("Veuillez choisir un nombre entre 1 et 14 pour choisir votre Graphe : "))

while (c < 1 or c > 14): #on ouvre le fichier en fonction du graphe sélectionner
    c = int(input("\nchoisir un nombre entre 1 et 14 seulement : "))
if (c == 1):
    fichier = open("G01.txt","r")
    trace = open("T01.txt", "w")
if (c == 2):
    fichier = open("G02.txt","r")
    trace = open("T02.txt", "w")
if (c == 3):
    fichier = open("G03.txt","r")
    trace = open("T03.txt", "w")
if (c == 4):
    fichier = open("G04.txt","r")
    trace = open("T04.txt", "w")
if (c == 5):
    fichier = open("G05.txt","r")
    trace = open("T05.txt", "w")
if (c == 6):
    fichier = open("G06.txt","r")
    trace = open("T06.txt", "w")
if (c == 7):
    fichier = open("G07.txt","r")
    trace = open("T07.txt", "w")
if (c == 8):
    fichier = open("G08.txt","r")
    trace = open("T08.txt", "w")
if (c == 9):
    fichier = open("G09.txt","r")
    trace = open("T09.txt", "w")
if (c == 10):
    fichier = open("G10.txt","r")
    trace = open("T10.txt", "w")
if (c == 11):
    fichier = open("G11.txt","r")
    trace = open("T11.txt", "w")
if (c == 12):
    fichier = open("G12.txt","r")
    trace = open("T12.txt", "w")
if (c == 13):
    fichier = open("G13.txt","r")
    trace = open("T13.txt", "w")
if (c ==14):
    fichier = exit()

print(fichier,file = trace)

print("\n\n", file = trace)
print("***** Projet Theorie des Graphes *****", file = trace)
print("***** TON Steven, HULIN Pauline, PASCO-CASTILLO Marc *****", file = trace)
print("\n\n", file = trace)
print(" 1: G01\n 2: G02\n 3: G03\n 4: G04\n 5: G05\n 6: G06\n 7: G07\n 8: G08\n 9: G09\n10: G10\n11: G11\n12: G12\n13: G13\n14: Exit\n", file = trace)

print("Le graphe choisi est le :",c, file = trace)
print("\n\n", file = trace)


def lire_un_fichier(): #fonction lire un fichier et transformer les valeurs en entier dans un tableau
    graph = [] #on créer le tableau mémoire
    lignes = fichier.readlines() #on transforme lignes en tableaux de lignes du fichier
    valeur = int(lignes[0]) #on transforme la premiere ligne en int
    graph.append(valeur) #on rajoute cette valeur au tableau "graph"
    valeur = int(lignes[1]) #idem avec la 2eme
    graph.append(valeur)
    compteur_string = 0
    compteur_fichier = 2
    while len(lignes)!=compteur_fichier:
        separation = lignes[compteur_fichier].split(" ") #on sépare le string en plusieurs string avec les espaces
        graph.append([int(separation[0]),int(separation[1]),int(separation[2])]) #on transforme les string en int et on ajoute dans le tab
        compteur_fichier = compteur_fichier+1
    return graph

def matrice_adjacence(initial,terminal,arc,nbsommet,nbarc):
    tab = [['']] #la valeur " " représente la position [0][0] qui devrait etre vide
    compteur = 0
    ajoutage = 0
    #remplissage des index dans le tableau
    for i in range(0,nbsommet):
        tab[0].append(i)
    for j in range(0,nbsommet):
        tab.append([j])
    #remplissage du tableau
    for i in range(1,nbsommet+1): #pour parcourir le tableau "tab"
        for j in range(1,nbsommet+1): #pour parcourir le tableau "tab"
            while compteur!=len(initial): #pour parcourir le tableau initial et arc
                if(initial[compteur] == (i-1) and terminal[compteur]==(j-1)): #si on trouve que les valeurs correspondent alors on ajoute 1
                    tab[i].append(1)
                    ajoutage = 1
                compteur = compteur+1
            if(ajoutage == 0):#sinon on ajoute 0
                tab[i].append(0)
            else:
                ajoutage = 0
            compteur = 0
    return tab

def matrice_valeur(initial,terminal,arc,nbsommet,nbarc):
    tab = [['']] #la valeur " " représente la position [0][0] qui devrait etre vide
    verif = 0
    compteur = 0
    ajoutage = 0
    #remplissage des index dans le tableau
    for i in range(0,nbsommet):
        tab[0].append(i)
    for j in range(0,nbsommet):
        tab.append([j])
    #remplissage du tableau
    for i in range(1,nbsommet+1):
        for j in range(1,nbsommet+1):
            while verif == 0 and compteur!=len(initial): #ici mon met la taille du tab initial mais ca aurait pu etre terminal ou arc
                if(initial[compteur] == (i-1) and terminal[compteur] == (j-1)): #si trouve que les valeurs correspondent alors on ajoute la valeur de l'arc
                    tab[i].append(arc[compteur])
                    ajoutage = 1
                compteur = compteur+1
            if(ajoutage == 0): #sinon on ajoute *
                tab[i].append("*")
            else:
                ajoutage = 0
            compteur = 0
    return tab

def point_entre(terminal,sommet_reste):
    #prend en parametre terminal, sommet restant, retourne tab de point d'entrée regarde dans terminal si il y a des valeurs qui manquent parmis les sommets restants
    point_entre = []
    ajouter = True
    for i in range (0,len(sommet_reste)):
        ajouter = True
        for j in range (0,len(terminal)):
            if (sommet_reste[i] == terminal[j]): #si la valeur du sommet existe dans le tableau terminal alors on ne le supprime pas
                ajouter = False
        if (ajouter == True): #si ajouter est vrai càd que la condition précédente n'a pas été executé
            point_entre.append(sommet_reste[i]) #on ajoute dans le tableau point entrée
    return point_entre

def suppr_point(pt_entree,initial,terminal):
    #prend en parametre point entrée et le tab initial et terminal, supprime toutes les valeurs qui coincident entre point entrée et fusion premiere colonne
    compteur = 0
    taille_init = len(initial)
    for entree in pt_entree:
        while compteur<len(initial): #tant que le compteur n'a pas parcouru tout le tableau "initial"
            if(entree == initial[compteur]): #si la valeur dans initial est un point d'entrée, on supprime les valeurs qui sont sur la même ligne
                del initial[compteur]
                del terminal[compteur]
            else:
                compteur = compteur+1
        compteur = 0
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
    initialtab = initial.copy()
    terminaltab = terminal.copy()
    sommet_reste = []
    for i in range(0,nbsommet): #tableau qui répertorie les sommets
        sommet_reste.append(i)
    while(True):
        if(afficher == True):
            print("points d'entrées:\n")
            print("points d'entrées:\n", file = trace)
        pt_entree = point_entre(terminaltab,sommet_reste) #on repère les points d'entrées
        if(afficher == True):
            print(pt_entree,"\n")
            print(pt_entree, file = trace)
        for entree in pt_entree: #on supprime les sommets qui sont des points d'entrées dans le tab des sommets restants
            if (entree in sommet_reste):
                sommet_reste.remove(entree)
        if(afficher==True):
            print("sommet restant:\n")
            print("sommet restant:\n", file = trace)
            print(sommet_reste)
            print(sommet_reste, file = trace)
        initialtab,terminaltab = suppr_point(pt_entree,initialtab,terminaltab)
        if(len(sommet_reste) == 1): #condition de sortie
            if(afficher == True):
                print("Ce graphe n'a pas de circuit")
                print("Ce graphe n'a pas de circuit", file = trace)
            return True
            break
        elif(len(pt_entree) == 0 and len(sommet_reste)>1): #condition de sortie
            if(afficher == True):
                print("ce graphe comporte un circuit")
                print("ce graphe comporte un circuit", file = trace)
            return False
            break

def ordo(initial,terminal,arc,nbsommet,nbarc,afficher):
    """
    prend en paramètre initial, terminal, arc
    appel fction point entrée
    regarde si il y a q'1 seul entrée
    appel point sortie
    regarde si il y a q'1 seul sortie
    appel dect_circuit->si pas circuit on continue
    appel valeur identique si oui retourne boléen
    appel valeur pt entrée si oui retoune boléen
    appel arc négative et retourne booléen
    """
    sommet = []
    for i in range(0,nbsommet):
        sommet.append(i)
    pt_entree = point_entre(terminal,sommet)
    if(len(pt_entree) == 1):
        if(afficher == True):
            print("il y a bien une seule entrée\n")
            print("il y a bien une seule entrée\n", file = trace)
        pt_sortie = point_sortie(initial,sommet)
        if(len(pt_sortie) == 1):
            if(afficher == True):
                print("il y a bien une seule sortie\n")
                print("il y a bien une seule sortie\n", file = trace)
            if(detect_circuit(initial, terminal, nbsommet, False)):
                if(afficher == True):
                    print("il n'y a pas de circuit\n")
                    print("il n'y a pas de circuit\n", file = trace)
                if(val_identique(initial,arc,nbsommet)):
                    if(afficher == True):
                        print("valeurs identiques pour tous les arcs incidents vers l’extérieur à un sommet\n")
                        print("valeurs identiques pour tous les arcs incidents vers l’extérieur à un sommet\n", file = trace)
                    if(val_pt_entree(pt_entree[0],initial,arc)):
                        if(afficher == True):
                            print("arcs incidents vers l’extérieur au point d’entrée de valeur nulle")
                            print("arcs incidents vers l’extérieur au point d’entrée de valeur nulle", file = trace)
                        if(is_arc_negative(arc)):
                                if(afficher == True):
                                    print("pas d’arc à valeur négative")
                                    print("pas d’arc à valeur négative", file = trace)
                                    print("c'est un ordonnancement correct")
                                    print("c'est un ordonnancement correct", file = trace)
                                return True
                        else:
                            if(afficher == True):
                                    print("l'ordonnancement n'est pas correct, il y a une valeur négative\n")
                                    print("l'ordonnancement n'est pas correct, il y a une valeur négative\n", file = trace)
                            return False
                    else:
                        if(afficher == True):
                            print("l'ordonnancement n'est pas correct, arcs incidents vers l’extérieur au point d’entrée de valeur non nulle\n")
                            print("l'ordonnancement n'est pas correct, arcs incidents vers l’extérieur au point d’entrée de valeur non nulle\n", file = trace)
                        return False
                else:
                    if(afficher == True):
                        print("l'ordonnancement n'est pas correct, valeurs pas identique pour tous les arcs incidents vers l’extérieur à un sommet\n")
                        print("l'ordonnancement n'est pas correct, valeurs pas identique pour tous les arcs incidents vers l’extérieur à un sommet\n", file = trace)
                    return False
            else:
                if(afficher == True):
                    print("l'ordonnancement n'est pas correct, le graphe comporte un circuit\n")
                    print("l'ordonnancement n'est pas correct, le graphe comporte un circuit\n", file = trace)
                return False
        else:
            if(afficher == True):
                print("l'ordonnancement n'est pas correct, il y a pas un seul point de sortie\n")
                print("l'ordonnancement n'est pas correct, il y a pas un seul point de sortie\n", file = trace)
            return False
    else:
        if(afficher == True):
            print("l'ordonnancement n'est pas correct, il y a pas un seul point d'entrée\n")
            print("l'ordonnancement n'est pas correct, il y a pas un seul point d'entrée\n", file = trace)
        return False

def point_sortie(initial,sommet):
    #prend en parametre initial,sommet restant, retourne tab de point de sorties regarde dans initial si il y a des valeurs qui manquent parmis les sommets restants
    point_sortie = []
    supprimer = True
    for i in range (0,len(sommet)):
        supprimer = True
        for j in range (0,len(initial)):
            if (sommet[i] == initial[j]): #si la valeur du sommet existe dans le tableau terminal alors on ne le supprime pas
                supprimer = False
        if (supprimer == True): #si supprimer est vrai càd que la condition précédente n'a pas été executé
            point_sortie.append(sommet[i]) #on ajoute dans le tableau point entrée
    return point_sortie

def val_pt_entree(entree,initial,arc):
    #prend en parametre entree, initial et arc(valeur de l'arc) regarde pour le pt d'entree si la valeur correspondante est bien 0
    for i in range(0,len(initial)):
        if(entree == initial[i] and arc[i]!=0):
                return False
    return True

def val_identique(initial,arc,nbsommet):
    #prend en parametre initial et arc (valeur de l'arc) regarde pour tous les points de la même valeur si la valeur de l'arc est la même
    tab_comparatif = []
    for i in range(0,nbsommet):
        for j in range(0,len(initial)):
            if(initial[j] == i):
                tab_comparatif.append(arc[j])
        for j in range(0,len(tab_comparatif)):
            if(tab_comparatif[0]!=tab_comparatif[j]):
                return False
        tab_comparatif.clear()
    return True

def is_arc_negative(arc):
    #prend en parametre arc (valeur de l'arc) regarde si il y a une valeur négative
    for negative in arc:
        if (negative<0):
            return False
    return True

def separation(graph): #dans cette fonction, on décompose le premier tableau pour que ce soit plus pratique
    nbsommet = graph[0]
    nbarc = graph[1]
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
        print(i, file = trace)
    print("\n")
    print("\n", file = trace)

def rang(initial,terminal,nbsommet,afficher):
    #regarder si le graphe est un circuit ou non
    initialtab = initial.copy()
    terminaltab = terminal.copy()
    rang = 0
    sommet_reste = []
    sommet_tab = []
    rang_tab = []
    sommet_tab.append("sommet")
    rang_tab.append("rang")
    """
    for i in range(1,nbsommet+1): #on insère les sommets dans le tableau
        sommet_tab[i] = (i-1)
    """
    for i in range(0,nbsommet):
        sommet_reste.append(i) #tableau avec tout les sommets non supprimés
    pas_circuit = detect_circuit(initialtab,terminaltab,nbsommet,False)
    nb_entree = point_entre(terminaltab, sommet_reste)
    if pas_circuit == True: #si notre graphe n'est pas un circuit

        if(afficher == True):
            print("Calcul du rang\n Méthode d’élimination des points d’entrée\n")
            print("Calcul du rang\n Méthode d’élimination des points d’entrée\n", file = trace)
        while len(sommet_reste)!=0: #tant qu'il y a des sommets
            if(afficher == True):
                print("rang courant = ",rang,"\n")
                print("rang courant = ",rang,"\n", file = trace)
                print("points d'entrées:\n",nb_entree,"\n")
                print("points d'entrées:\n",nb_entree,"\n", file = trace)
            for entree in nb_entree: #on supprime les sommets qui sont des points d'entrées dans le tab des sommets restants
                if (entree in sommet_reste):
                    sommet_reste.remove(entree)
            """
            for i in range (1,len(rang_tab)):
                for entree in nb_entree:
                    if(sommet_tab[i] == entree):
                        rang_tab[i] = rang
            """
            for i in range (0,len(nb_entree)):
                rang_tab.append(rang)
            for entree in nb_entree:
                sommet_tab.append(entree)
            rang+=1
            initialtab,terminaltab = suppr_point(nb_entree,initialtab,terminaltab)
            nb_entree = point_entre(terminaltab, sommet_reste)
            tab_rang = []
            tab_rang.append(rang_tab)
            tab_rang.append(sommet_tab)
        if(afficher== True):
            afficher_tableau(tab_rang)
        return tab_rang
    else:
        if(afficher == True):
            print("impossible votre graphe comporte un circuit")
            print("impossible votre graphe comporte un circuit", file = trace)

def tacheetsalongueur(tab_rang,initial,arc,nbsommet):
    longueur = []
    calendrier = []
    longueur.append("longueur")
    for i in range (1,len(tab_rang[1])): #parcours le tableau de tabrang pour associer une longueur à un sommet
        for j in range(0,len(initial)):
            if (tab_rang[1][i] == initial[j]):
                longueur.append(arc[j])
                break
    longueur.append(None)
    calendrier.append(tab_rang[0])
    calendrier.append(tab_rang[1])
    calendrier.append(longueur)
    return calendrier

def calendrier_opluto(initial,terminal,arc,nbsommet,nbarc,afficher): #cette fonction appelera seulement les autres fonctions, pour constituer le calendrier
    max_value = 0
    is_correct = ordo(initial,terminal,arc,nbsommet,nbarc,False)
    if(is_correct):
        tab_rang = rang(initial,terminal,nbsommet,False)
        calendrier = tacheetsalongueur(tab_rang,initial,arc,nbsommet)
        calendrier = predecesseurs(calendrier,initial,terminal)
        calendrier = date_par_predecesseurs(calendrier)
        calendrier.append(["date au plus tôt"])
        for date in calendrier[4]:
            if(date!='date par predecesseurs'):
                if ('/' in date):
                    separation = date.split("/")
                    for elements in separation:
                        if (elements!=""):
                            if(int(elements)>max_value):
                                max_value = int(elements)
                    calendrier[5].append(int(max_value))
                    max_value = 0
                else:
                    calendrier[5].append(int(date))
        if(afficher == True):
            afficher_tableau(calendrier)
        date_opluto = calendrier[5][len(calendrier[5])-1]
        calendrier_oplutar(initial,terminal,arc,nbsommet,nbarc,afficher,calendrier,date_opluto)
    else:
        print("Ce graphe comporte un circuit donc on ne peut pas.\n\n")
        print("Ce graphe comporte un circuit donc on ne peut pas.\n\n", file = trace)


def predecesseurs(calendrier,initial,terminal):
    prec_sommet = []
    predecesseurs = []
    string = ""
    predecesseurs.append("predecesseurs")
    for i in range (1,len(calendrier[1])): #pour chaque sommet:
        for j in range(0,len(terminal)): #on parcours le tableau terminal
            if(terminal[j] == calendrier[1][i]): #si les valeurs sont les mêmes
                prec_sommet.append(initial[j]) #on stocke l'extremité initial dans un tableau
        for elements in prec_sommet: #on transforme le tableau en string
            if(len(prec_sommet)>1):
                string+=str(elements)+"/"
            elif(len(prec_sommet) == 1):
                string = str(elements)
        predecesseurs.append(string) #on ajoute dans le calendrier
        prec_sommet.clear()
        string = ""
    calendrier.append(predecesseurs)
    return calendrier

def date_par_predecesseurs(calendrier):
    string = ""
    calendrier.append(["date par predecesseurs"])
    tab_renvoie = [[]]
    val_max = 0
    compteur = 0
    for i in range(1,len(calendrier[3])): #pour toutes les cases de la ligne predecesseur
        if(calendrier[3][i] == '' or calendrier[3][i] == '0'):
            calendrier[4].append('0')
        else:
            if('/' in calendrier[3][i]): #cas ou il y a plusieurs predecesseurs
                separation = calendrier[3][i].split('/')
                for elements in separation:
                    if(elements!=''):
                        tab_renvoie[0].append(int(elements))
                #pour les longueurs
                tab_renvoie.append([]) #on crée une nouvelle ligne dans le tableau
                for pred in tab_renvoie[0]:
                    for j in range(1,len(calendrier[1])):
                        if(pred == calendrier[1][j]): #si le predecesseur est egal au sommet courant
                            tab_renvoie[1].append(calendrier[2][j])
                #pour les dates par prédecesseur
                tab_renvoie.append([]) #on crée une nouvelle ligne dans le tableau
                for pred in tab_renvoie[0]:#pour chaque pred,
                #on cherche la date par predecesseur
                    for j in range (1,len(calendrier[4])): #pour tous les sommets qui ont une date
                        if(pred == calendrier[1][j]): #si on trouve la bonne colonne
                            separe_date = calendrier[4][j].split("/") #on prend toutes les dates
                            for truc in separe_date: #on cherche la valeur la plus grande
                                if(truc!=""):
                                    if(int(truc)>val_max):
                                        val_max = int(truc)
                    tab_renvoie[2].append(val_max)
                    val_max = 0
                if(len(tab_renvoie[0]) == len(tab_renvoie[2])):
                    tab_renvoie = calcul_date(tab_renvoie)
                    for h in tab_renvoie[3]:
                        string+=str(h)+"/"
                    calendrier[4].append(string)
                    string = ""
                    tab_renvoie = [[]]
                    val_max = 0
            else: #cas où il y a 1 seul predecesseur
                tab_renvoie[0].append(int(calendrier[3][i]))
                tab_renvoie.append([]) #on crée une nouvelle ligne
                for j in range(1,len(calendrier[1])): #pour parcourir le tableau
                    if(int(calendrier[3][i]) == calendrier[1][j]): #si le predecesseur est egal au sommet courant
                        tab_renvoie[1].append(calendrier[2][j])
                tab_renvoie.append([]) #on crée une nouvelle ligne dans le tableau
                for j in range(1,len(calendrier[4])):
                    if(int(calendrier[3][i]) == calendrier[1][j]): #si le predecesseur est egal au sommet courant
                        if("/" in calendrier[4][j]): #si le predecesseur a plusieurs dates
                            separe_date = calendrier[4][j].split("/")
                            for truc in separe_date: #on cherche la valeur la plus grande
                                if(truc!=""):
                                    if(int(truc)>val_max):
                                        val_max = int(truc)
                            tab_renvoie[2].append(int(val_max))
                        else:
                            tab_renvoie[2].append(int(calendrier[4][j]))
                if(len(tab_renvoie[0]) == len(tab_renvoie[2])):
                    tab_renvoie = calcul_date(tab_renvoie)
                    calendrier[4].append(str(tab_renvoie[3]))
                    tab_renvoie = [[]]
                    val_max = 0
    return calendrier

def calcul_date(tab_renvoie):
    taille_tab = len(tab_renvoie[0])
    if(taille_tab == 1): #si il y a qu'un seul predecesseur
        value = tab_renvoie[1][0]+tab_renvoie[2][0]
        tab_renvoie.append(value)
    else:
        tab_renvoie.append([])
        for i in range (0,taille_tab): #sinon on fait le meme calcul pour chaque colonne
            value = tab_renvoie[1][i]+tab_renvoie[2][i]
            tab_renvoie[3].append(value)
    return tab_renvoie

def successeur(calendrier,initial,terminal):
    succ_sommet = []
    successeur = []
    string = ""
    for i in range (1,len(calendrier[1])): #pour chaque sommet:
        for j in range(0,len(terminal)): #on parcours le tableau terminal
            if(initial[j] == calendrier[1][i]): #si les valeurs sont les mêmes
                succ_sommet.append(terminal[j]) #on stocke l'extremité initiale dans un tableau
        for elements in succ_sommet: #on transforme le tableau en string
            if(len(succ_sommet)>1):
                string+=str(elements)+"/"
            elif(len(succ_sommet) == 1):
                string = str(elements)
        successeur.append(string) #on ajoute dans le calendrier
        succ_sommet.clear()
        string = ""
    return successeur

def date_par_successeur(calendrier,nbsommet,date_opluto):
    string = ""
    calendrier.append([str(date_opluto)])
    tab_renvoie = [[]]
    val_min = 0
    compteur = 0
    for i in range(0,len(calendrier[3])): #pour toutes les cases de la ligne predecesseur
            if('/' in calendrier[3][i]):
                separation = calendrier[3][i].split('/')
                for elements in separation:
                    if(elements!=''):
                        tab_renvoie[0].append(int(elements))
                #pour les longueurs
                tab_renvoie.append([]) #on crée une nouvelle ligne dans le tableau
                for pred in tab_renvoie[0]:
                    for j in range(0,len(calendrier[1])):
                        if(pred == calendrier[1][j]): #si le predecesseur est egal au sommet courant
                            tab_renvoie[1].append(calendrier[2][i])
                #pour les dates par prédecesseurs
                tab_renvoie.append([]) #on crée une nouvelle ligne dans le tableau
                for pred in tab_renvoie[0]:#pour chaque pred,
                #on cherche la date par predecesseur
                    for j in range (0,len(calendrier[4])): #pour tous les sommets qui ont une date
                        if(pred == calendrier[1][j]): #si on trouve la bonne colonne
                            separe_date = calendrier[4][j].split("/") #on prend toutes les dates
                            for truc in range (0,len(separe_date)): #on cherche la valeur la plus grande
                                if(truc == 0):
                                    val_min = int(separe_date[truc])
                                if(separe_date[truc]!=""):
                                    if(int(separe_date[truc])<val_min):
                                        val_min = int(separe_date[truc])
                    tab_renvoie[2].append(val_min)
                    val_min=0
                if(len(tab_renvoie[0]) == len(tab_renvoie[2])):
                    tab_renvoie = calcul_datesucc(tab_renvoie)
                    for h in tab_renvoie[3]:
                        string+=str(h)+"/"
                    calendrier[4].append(string)
                    string = ""
                    tab_renvoie = [[]]
                    val_min = 0
            else:
                if(calendrier[3][i]!=""):
                    tab_renvoie[0].append(int(calendrier[3][i]))
                    tab_renvoie.append([])
                    for j in range(0,len(calendrier[1])):
                        if(int(calendrier[3][i]) == calendrier[1][j]): #si le predecesseur est egal au sommet courant
                            tab_renvoie[1].append(calendrier[2][i])
                    tab_renvoie.append([]) #on crée une nouvelle ligne dans le tableau
                    for j in range(0,len(calendrier[4])):
                        if(int(calendrier[3][i]) == calendrier[1][j]): #si le successeur est egal au sommet courant
                            if("/" in calendrier[4][j]): #si le predecesseur a plusieurs dates
                                separe_date = calendrier[4][j].split("/")
                                for truc in range (0,len(separe_date)): #on cherche la valeur la plus grande
                                    if(truc == 0):
                                        val_min = separe_date[truc]
                                    if(separe_date[truc]!=""):
                                        if(int(separe_date[truc])<val_min):
                                            val_min = int(separe_date[truc])
                                tab_renvoie[2].append(val_min)
                            else:
                                tab_renvoie[2].append(int(calendrier[4][j]))
                    if(len(tab_renvoie[0]) == len(tab_renvoie[2])):
                        tab_renvoie = calcul_datesucc(tab_renvoie)
                        calendrier[4].append(str(tab_renvoie[3]))
                        tab_renvoie = [[]]
    return calendrier

def calcul_datesucc(tab_renvoie):
    taille_tab = len(tab_renvoie[0])
    if(taille_tab == 1):
        value = tab_renvoie[2][0]-tab_renvoie[1][0]
        tab_renvoie.append(value)
    else:
        tab_renvoie.append([])
        for i in range (0,taille_tab):
            value = tab_renvoie[2][i]-tab_renvoie[1][i]
            tab_renvoie[3].append(value)
    return tab_renvoie

def calendrier_oplutar(initial,terminal,arc,nbsommet,nbarc,afficher,calendrier,date_opluto):
    min_value = 0
    calendriertab = calendrier.copy()
    succ = successeur(calendriertab,initial,terminal)
    reverse = reversetab(calendriertab,succ)
    reverse = date_par_successeur(reverse,nbsommet,date_opluto)
    calendriertab = rereverse(reverse)
    calendriertab.append(["date au plus tard"])
    for date in calendriertab[4]:
            if(date!='date par predecesseurs'):
                if ('/' in date):
                    separation = date.split("/")
                    for elements in range(0,len(separation)):
                        if(elements == 0):
                            min_value = int(separation[0])
                        if (separation[elements]!=""):
                            if(int(separation[elements])<min_value):
                                min_value = int(separation[elements])
                    calendriertab[5].append(int(min_value))
                    max_value=0
                else:
                    if(date!="date par successeur"):
                        calendriertab[5].append(int(date))
    afficher_tableau(calendriertab)
    marge(calendrier[5],calendriertab[5])

def marge(date_oputo,date_oputar):
    marge = []
    marge.append(date_oputo)
    marge.append(date_oputar)
    marge.append(["marge"])
    for i in range(1,len(date_oputo)):
        marge[2].append(date_oputar[i]-date_oputo[i])
    afficher_tableau(marge)

def rereverse(reverse):
    reverse[0].reverse()
    reverse[1].reverse()
    reverse[2].reverse()
    reverse[3].reverse()
    reverse[4].reverse()
    reverse[0].insert(0,"rang")
    reverse[1].insert(0,"sommet")
    reverse[2].insert(0,"longueur")
    reverse[3].insert(0,"successeur")
    reverse[4].insert(0,"date par successeur")
    return reverse

def reversetab(calendrier,successeur):
    del calendrier[3]
    del calendrier[3]
    del calendrier[3]
    for i in range (0,len(calendrier)):
         del calendrier[i][0]
    calendrier.append(successeur)
    calendrier[0].reverse()
    calendrier[1].reverse()
    calendrier[2].reverse()
    calendrier[3].reverse()
    return calendrier

def main():

    graph = lire_un_fichier()
    initial,terminal,arc,nbsommet,nbarc = separation(graph)

    print("Choisissez quelle fonction executer")
    print("Choisissez quelle fonction executer", file = trace)
    print("\n")
    print("\n", file = trace)
    fonction_select = None
    print("\n\n", file = trace)

    while (fonction_select!=8):
        print("1: lire un fichier\n2: matrice adjacence\n3: matrice des valeurs\n4: detection de circuit\n5: calcul du rang\n6: ordonnancement\n7: calendrier au plus tot, au plus tard et marge\n8: exit\n")
        print("1: lire un fichier\n2: matrice adjacence\n3: matrice des valeurs\n4: detection de circuit\n5: calcul du rang\n6: ordonnancement\n7: calendrier au plus tot, au plus tard et marge\n8: exit\n", file = trace)
        print("\n", file = trace)
        print("\n")
        fonction_select = int(input("Choisissez la fonction à executer :\n"))
        print("\n", file = trace)
        print("\n")
        print("Vous executez la fonction :", fonction_select, file = trace)
        print("\n")
        print("\n", file = trace)

        if(fonction_select == 1):
            print("nombre de sommets:",nbsommet,"\n")
            print("nombre d'arcs:",nbarc,"\n")
            for i in range(0,len(initial)):
                print(initial[i],"->",terminal[i],"=",arc[i],"\n")
                #pour le fichier trace
            print("nombre de sommets:",nbsommet,"\n", file = trace)
            print("nombre d'arcs:",nbarc,"\n", file = trace)
            for i in range(0,len(initial)):
                print(initial[i],"->",terminal[i],"=",arc[i],"\n", file = trace)
        if(fonction_select == 2):
            matrice_adj = matrice_adjacence(initial,terminal,arc,nbsommet,nbarc)
            afficher_tableau(matrice_adj)

        if(fonction_select == 3):
            matrice_val = matrice_valeur(initial,terminal,arc,nbsommet,nbarc)
            afficher_tableau(matrice_val)

        if(fonction_select == 4):
            detect_circuit(initial,terminal,nbsommet,True)

        if(fonction_select == 5):
            rang(initial,terminal,nbsommet,True)

        if(fonction_select == 6):
            ordo(initial,terminal,arc,nbsommet,nbarc,True)


        if(fonction_select == 7):
            calendrier_opluto(initial,terminal,arc,nbsommet,nbarc,True)

        if(fonction_select == 8):
            exit()
main()
