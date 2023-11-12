# Clémnent Lerouley
# Alban Gautier


import pygame
from random import *
from time import *
from Cellule import Cellule
from Window import Window 
from Bouton import Bouton


pygame.init()

if __name__ == '__main__' :

    running = True 

    wind = Window()
    bout = Bouton()
    tableau = Cellule()

    background_colour = wind.white
    pygame.display.set_caption('Jeu_de_la_vie')
    wind.w.fill(background_colour)

    clock = pygame.time.Clock()
    FPS = 60  

    while running:
        clock.tick(FPS) 

        bout.mouse_pos= pygame.mouse.get_pos()

        bout.bouton_pause()
        bout.bouton_quad()
        bout.bouton_generation()
        bout.bouton_reinitialiser()

        if bout.click_quad == False:
            if bout.click_pause == False: 
                tableau.delete_cell()
            wind.delete_quad()
        else:
            if bout.click_pause == False: 
                pygame.draw.rect(wind.w,wind.white,(0,0,910,700))
            wind.quadrillage()


        if bout.bouton_reinitialiser() == True:
            if bout.click_quad == False:
                tableau.delete_cell()
            else:
                pygame.draw.rect(wind.w,wind.white,(0,0,910,700))
                wind.quadrillage() 
            tableau.liste_cellules = []

        if bout.bouton_generation() == True and tableau.liste_cellules == []:
            tableau.liste_cellules = tableau.random_generation(500)
            tableau.create_cell()

        if bout.click_pause == False:
            cellule_suivante = tableau.compte_voisin()
            tableau.liste_cellules = cellule_suivante
            tableau.create_cell()


        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False