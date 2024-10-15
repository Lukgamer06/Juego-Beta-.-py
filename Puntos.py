import pygame
import random

class Puntos_izq:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 20
        self.color = "black"
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        self.imagen = pygame.image.load("Python/Juegos/PYgame/Imagenes/Puntos.png")
        self.tamano = pygame.transform.scale(self.imagen,(self.ancho,self.alto))

    def dibujar(self , ventana):
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        pygame.draw.rect(ventana , self.color , self.rect)
        ventana.blit(self.tamano,(self.x,self.y))

    def movimiento(self):
        self.x += self.velocidad

class Puntos_der:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 20
        self.color = "black"
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        self.imagen = pygame.image.load("Python/Juegos/PYgame/Imagenes/Puntos.png")
        self.tamano = pygame.transform.scale(self.imagen,(self.ancho,self.alto))

    def dibujar(self , ventana):
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        pygame.draw.rect(ventana , self.color , self.rect)
        ventana.blit(self.tamano,(self.x,self.y))

    def movimiento(self):
        self.x -= self.velocidad

class Puntos_Up:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 20
        self.color = "black"
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        self.imagen = pygame.image.load("Python/Juegos/PYgame/Imagenes/Puntos.png")
        self.tamano = pygame.transform.scale(self.imagen,(self.ancho,self.alto))

    def dibujar(self , ventana):
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        pygame.draw.rect(ventana , self.color , self.rect)
        ventana.blit(self.tamano,(self.x,self.y))

    def movimiento(self):
        self.y += self.velocidad

class Puntos_Down:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 20
        self.color = "black"
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        self.imagen = pygame.image.load("Python/Juegos/PYgame/Imagenes/Puntos.png")
        self.tamano = pygame.transform.scale(self.imagen,(self.ancho,self.alto))

    def dibujar(self , ventana):
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        pygame.draw.rect(ventana , self.color , self.rect)
        ventana.blit(self.tamano,(self.x,self.y))
        
    def movimiento(self):
        self.y -= self.velocidad
