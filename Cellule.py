import Window as wind
import pygame
from random import *


class Cellule(wind.Window):
    # cette classe nous permet de créer une liste de tuples de coordonnées x et y représentant les cellules, de calculer le nombre de voisins d'une cellules
    # vivante puis de créer une nouvelle liste en fonctions du nombre de voisins de chaque cellule qui sera affcher à la prochaine itération du programme
    def __init__(self,x = 1200,y = 700):
        super().__init__(x,y)
        self.width = 900
        self.height = 700
        self.taille_cell = 10
        self.liste_cellules = self.random_generation(500)


    def compte_voisin(self):
        """
        Objectif de la méthode: nous permet de compter le nombre de voisin que possède une cellules afin de créer une nouvelle liste avec les 
        coordonnée x et y des nouvelles cellules sous forme de tuples 
        préconditions: elle prend en paramètre les objets de la classe 
        postconditions: elle renvoie la nouvelle liste contenant les nouveaux emplacemet des cellules
        """

        new_cells = []

        for x in range(int(self.width/self.taille_cell)):
            for y in range(int(self.height/self.taille_cell)):
                Neighbours = 0
                if (x+1, y) in self.liste_cellules:
                    Neighbours += 1
                if (x-1, y) in self.liste_cellules:
                    Neighbours += 1
                if (x, y+1) in self.liste_cellules:
                    Neighbours += 1
                if (x, y-1) in self.liste_cellules:
                    Neighbours += 1
                if (x+1, y+1) in self.liste_cellules:
                    Neighbours += 1
                if (x-1, y-1) in self.liste_cellules:
                    Neighbours += 1
                if (x+1, y-1) in self.liste_cellules:
                    Neighbours += 1
                if (x-1, y+1) in self.liste_cellules:
                    Neighbours += 1
                
                if (x,y) in self.liste_cellules:
                    if Neighbours == 3:
                        new_cells.append((x,y)) 
                    elif Neighbours == 2:
                        new_cells.append((x,y))
                else:
                    if Neighbours == 3:
                        new_cells.append((x,y))

        return new_cells

    def random_generation(self,nombre_cellule):
        """
        Objectif de la méthode: nous permet de générer aléatoirement une liste de tuples représentant les coordonnées des cellules générées
        préconditions: elle prend en paramètre les objets de la classe et le nomnbre de cellules qu'il faut généré "nombre_cellule".
        postconditions: elle renvoie une liste de coordonnées "seed"
        """

        seed = []

        compteur = 0

        maxX = self.width/self.taille_cell
        maxY = self.height/self.taille_cell

        while compteur <= nombre_cellule:

            x = randint(0, maxX)
            y = randint(0, maxY)

            seed.append((x,y))

            compteur +=1

        return seed

    def create_cell(self):
        """
        objectif de la méthode: nous permet de créer les cellules sur l'interface pygame
        préconditions: elle prend en paramètre les objets de la classe.
        postconditions: elle ne renvoie rien. 
        """

        for x in range(int(self.width/self.taille_cell)):
            for y in range(int(self.height/self.taille_cell)):
                if (x,y) in self.liste_cellules:
                    alive_cell = pygame.Rect(x*self.taille_cell, y*self.taille_cell, 
                        self.taille_cell, self.taille_cell)
                    pygame.draw.rect(self.w, self.black, alive_cell)
        

    def delete_cell(self):
        """
        objectif de la méthode: nous permet de supprimer les cellules sur l'interface pygame lorsqu'il n'y a pas de quadrillage uniquement.
        préconditions: elle prend en paramètre les objets de la classe.
        postconditions: elle ne renvoie rien. 
        """
        
        for x in range(int(self.width/self.taille_cell)):
            for y in range(int(self.height/self.taille_cell)):
                if (x,y) in self.liste_cellules:
                    dead_cell = pygame.Rect(x*self.taille_cell, y*self.taille_cell, 
                        self.taille_cell, self.taille_cell)
                    pygame.draw.rect(self.w, self.white, dead_cell)


    
