import pygame
import random

import pygame.imageext
class Nave:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 40
        self.alto = 40
        self.velocidad = 30
        self.color = "black"
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        self.imagen = pygame.image.load("Python/Juegos/PYgame/Imagenes/Nave.png")
        self.tamano = pygame.transform.scale(self.imagen,(self.ancho,self.alto))

    def dibujar (self , ventana):
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        pygame.draw.rect(ventana , self.color , self.rect)
        ventana.blit(self.tamano,(self.x,self.y))

