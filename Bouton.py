import Window as wind
import Cellule as tableau
import pygame
from time import *

class Bouton(wind.Window):
    # cette classe nous permet de créer les boutons de l'interface pygame et de les faire fonctionner 
    def __init__(self):
        super().__init__()

        self.mouse_pos = (0,0) 
        self.click_quad = False
        self.click_quad_press = False 
        self.click_pause = False 
        self.click_pause_press = False

    def bouton_pause(self):
        """
        Objectif de la méthode: cette méthode nous sert à créer un bouton sur l'interface ainsi que modifier un objet pour qu'en fonction de celui-ci le programme se mette ne pause ou non.
        préconditions: elle prend en paramètre les objets de la classe.
        postconditions: elle ne renvoie rien. 
        """

        if pygame.mouse.get_pressed()[0] == 0:
            self.click_pause_press = False 


        pygame.draw.rect(self.w,self.grey,(1000,70,100,40))

        if 1000 <= self.mouse_pos[0] <= 1100 and 70 <= self.mouse_pos[1] <= 110:
            pygame.draw.rect(self.w,(170,170,170),(1000,70,100,40))
            if pygame.mouse.get_pressed()[0] == 1 and self.click_pause_press == False:
                self.click_pause_press = True
                print(self.click_pause_press)
                if self.click_pause == False:
                    sleep(1)
                self.click_pause = not self.click_pause
                
                   
        text = pygame.font.SysFont('Corbel',24).render('Pause',True,self.black)
        self.w.blit(text,(1020,80))

    def bouton_quad(self):
        """
        Objectif de la méthode: cette méthode nous sert créer un bouton dans l'interface pygame qui nous permettra de choisir
        de choisir d'afficher ou ne pas afficher le quadrillage. 
        préconditions: elle prend en paramètre les objets de la classe.
        postconditions: elle ne renvoie rien. 
        """

        if pygame.mouse.get_pressed()[0] == 0:
            self.click_quad_press = False 

        pygame.draw.rect(self.w,self.grey,(1000,170,110,40))

        if 1000 <= self.mouse_pos[0] <= 1100 and 170 <= self.mouse_pos[1] <= 210:
            pygame.draw.rect(self.w,(170,170,170),(1000,170,110,40))
            if pygame.mouse.get_pressed()[0] == 1 and self.click_quad_press == False:
                self.click_quad_press = True
                self.click_quad = not self.click_quad
                
                
        text = pygame.font.SysFont('Corbel',24).render('Quadrillage',True,self.black)
        self.w.blit(text,(1000,180))

    def bouton_generation(self):
        """
        Objectif de la méthode: cette méthode nous sert à créer un bouton sur l'interface pygame qui nous permet de générer une nouvelle liste de cellules seulement
        si la liste précédente à été réinitialiser
        préconditions: elle prend en paramètre les objets de la classe.
        postconditions: elle renvoie False lorsque le bouton n'est pas pressé et True seulement lorsque le bouton est pressé.
        """

        pygame.draw.rect(self.w,self.grey,(1000,270,110,40))

        
        self.rect_color = self.grey 
       
        if 1000 <= self.mouse_pos[0] <= 1100 and 270 <= self.mouse_pos[1] <= 310:
            pygame.draw.rect(self.w,(170,170,170),(1000,270,110,40))
            if pygame.mouse.get_pressed()[0] == 1:
                return True

        text = pygame.font.SysFont('Corbel',24).render('Génération',True,self.black)
        self.w.blit(text,(1000,280))

        return False

    def bouton_reinitialiser(self):
        """
        Objectif de la méthode: cette méthode nous sert à créer un bouton sur l'interface pygame qui nous permet de réinitialiser la liste de coordonnées de cellules
        préconditions: elle prend en paramètre les objets de la classe.
        postconditions: elle renvoie False lorsque le bouton n'est pas pressé et True seulement lorsque le bouton est pressé.
        """

        pygame.draw.rect(self.w,self.grey,(1000,370,110,40))
        
        self.rect_color = self.grey 
    
        if 1000 <= self.mouse_pos[0] <= 1100 and 370 <= self.mouse_pos[1] <= 410:
            pygame.draw.rect(self.w,(170,170,170),(1000,370,110,40))
            if pygame.mouse.get_pressed()[0] == 1:
                return True

        text = pygame.font.SysFont('Corbel',24).render('Réinitialiser',True,self.black)
        self.w.blit(text,(1000,380))

        return False