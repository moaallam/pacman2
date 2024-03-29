import pygame
from event import *
from fonction_annexe import *
from time import sleep
from time import time
from random import randint


pacMan = initialise_pacMan()

fantomes = []
initialise_fantomes(fantomes)   
            
# cerise = { "x":10 , "y":10 , "image" : './image/pacman_droite.png' }


points = []#initialise_point()
superPoints = []#initialise_superPoint()
cerises = []#initialise_cerise()
murs = [] #initialise_murs()
            
terrain = { "TAILLE_LARGEUR" : 560 , "TAILLE_LARGEUR" : 620, "TAILLE_CASE_HAUTEUR":30, "TAILLE_CASE_LARGEUR":30 ,"murs":murs}


initialiseJeu(pacMan,fantomes,points,superPoints,cerises)
cree_fenetre(terrain["TAILLE_LARGEUR" ],terrain["TAILLE_LARGEUR"])

while gameOver(pacMan):

    # affichage des objets

    efface_tout()
    afficheJeu(terrain,pacMan,fantomes,points,superPoints,cerises)
    mise_a_jour()
    
    # gestion des événements
    evenement = donne_ev()
    type = type_ev(evenement)
    
    if type == 'Quitte':
        break
        
    elif type == 'Touche':
        change_direction_pac_man(pacMan, touche(evenement)) # direction
       
    #deplacement
    deplace_personnages(pacMan,fantomes,murs)
    teleportation(pacMan,terrain["TAILLE_LARGEUR" ],terrain["TAILLE_LARGEUR"])
    collision(pacMan,fantomes,points,superPoints,cerises)
    
    # attente avant rafraîchissement
    sleep(1/pacMan["vitesse"])
    
ferme_fenetre()
