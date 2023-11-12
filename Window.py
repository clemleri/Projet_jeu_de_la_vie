import pygame
from random import *

class Window():
    # cette classe nous permet de définir les variables que nous utiliserons dans les autres classes ainsi que de faire un quadrillage sur l'interface 
    # et de le supprimer 
    def __init__(self,x=1200,y=700):
        self.x = x
        self.y = y
        self.w =  pygame.display.set_mode((self.x, self.y))
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.grey = (200,200,200)
        self.Hover_button= (170,170,170)

    def quadrillage(self):
        """
        Objectif de la méthode: cette méthode nous permet de créer un quadrillage dans l'interface pygame 
        préconditions: elle prend en paramètre les objets de la classe 
        postconditions:  elle ne renvoie rien
        """
        self.x = 0
        self.y = 0
        while self.x < 910:
            pygame.draw.line(self.w,self.black,(self.x,0),(self.x,700))
            if self.y < 700:
                pygame.draw.line(self.w,self.black,(0,self.y),(900,self.y))
            self.x+=10
            self.y+=10

    def delete_quad(self):
        """
        Objectif de la méthode: cette méthode nous permet de supprimer le quarillage dans l'interface pygame 
        préconditions: elle prend en paramètre les objets de la classe 
        postconditions:  elle ne renvoie rien
        """
        self.x = 0
        self.y = 0
        while self.x < 910:
            pygame.draw.line(self.w,(255,255,255),(self.x,0),(self.x,700))
            if self.y < 700:
                pygame.draw.line(self.w,(255,255,255),(0,self.y),(900,self.y))
            self.x+=10
            self.y+=10
