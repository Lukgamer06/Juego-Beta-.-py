import pygame
import random

class Enemigo_izq:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 100
        self.alto = 50
        self.velocidad = random.randint(10,15)
        self.color = "black"
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        self.imagen = pygame.image.load("Python/Juegos/PYgame/Imagenes/Enemigo_Derecha.png")
        self.tamano = pygame.transform.scale(self.imagen,(self.ancho,self.alto))

    def dibujar(self , ventana):
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        pygame.draw.rect(ventana , self.color , self.rect)
        ventana.blit(self.tamano,(self.x,self.y))

    def movimiento(self):
        self.x += self.velocidad

class Enemigo_der:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 100
        self.alto = 50
        self.velocidad = random.randint(10,15)
        self.color = "black"
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        self.imagen = pygame.image.load("Python/Juegos/PYgame/Imagenes/Enemigo_Izquierda.png")
        self.tamano = pygame.transform.scale(self.imagen,(self.ancho,self.alto))
    
    def dibujar(self , ventana):
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        pygame.draw.rect(ventana , self.color , self.rect)
        ventana.blit(self.tamano,(self.x,self.y))

    def movimiento(self):
        self.x -= self.velocidad

class Enemigo_Up:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 100
        self.velocidad = random.randint(10,15)
        self.color = "black"
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        self.imagen = pygame.image.load("Python/Juegos/PYgame/Imagenes/Enemigo_Abajo.png")
        self.tamano = pygame.transform.scale(self.imagen,(self.ancho,self.alto))
    
    def dibujar(self , ventana):
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        pygame.draw.rect(ventana , self.color , self.rect)
        ventana.blit(self.tamano,(self.x,self.y))

    def movimiento(self):
        self.y += self.velocidad

class Enemigo_Down:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 100
        self.velocidad = random.randint(10,15)
        self.color = "black"
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        self.imagen = pygame.image.load("Python/Juegos/PYgame/Imagenes/Enemigo_Arriba.png")
        self.tamano = pygame.transform.scale(self.imagen,(self.ancho,self.alto))
    
    def dibujar(self , ventana):
        self.rect = pygame.Rect (self.x , self.y , self.ancho , self.alto)
        pygame.draw.rect(ventana , self.color , self.rect)
        ventana.blit(self.tamano,(self.x,self.y))

    def movimiento(self):
        self.y -= self.velocidad
