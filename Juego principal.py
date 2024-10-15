import pygame
import random
from Personaje import *
from Puntos import *
from Vidas import *
from Enemigos import *

pygame.init()
#Ventana
if True:
    ANCHO               = 900
    ALTO                = 750
    VENTANA             = pygame.display.set_mode([ANCHO,ALTO])
    FPS                 = 60
    FUENTE              = pygame.font.SysFont("Comic Sans", 40)

#Personajes
if True:
    Jugador             = Nave (ANCHO/2,ALTO/2)
    Enemigos            = []
    Vidas_ext           = []
    Puntos_ext          = []

#Tiempo
if True:
    reloj               = pygame.time.Clock()   #El tiempo esta dado en milisegundos

#Tiempo Enemigos
if True:
    Tiempo_New_enemigo    = 0
    Tiempo_Enemigos       = 1000

#Tiempo Puntos
if True:
    Tiempo_New_Puntos   = 0
    Tiempo_Puntos       = 1000

#Tiempo Nivel
if True:
    Tiempo_New_Nivel    = 0
    Tiempo_Niveles      = 12000

#Vidas, Puntos, Niveles
if True:
    Vidas               = 5 #Infinitas vidas
    Niveles             = 0 #Limite de 8 niveles
    Puntos              = 0 
    Puntos_por_Vida     = 5 #Obtener Puntos para que aparezca una vida

#Teclas
def gestionar_teclas(teclas):
    if teclas[pygame.K_w]:
        Jugador.y -= Jugador.velocidad
    if teclas[pygame.K_s]:
        Jugador.y += Jugador.velocidad
    if teclas[pygame.K_d]:
        Jugador.x += Jugador.velocidad
    if teclas[pygame.K_a]:
        Jugador.x -= Jugador.velocidad

#Juego
Jugando = True
while Jugando and Vidas > 0:
    #Tiempo
    if True:
        Tiempo_New_enemigo    += reloj.tick(FPS)
        Tiempo_New_Nivel    += reloj.tick(FPS)
        Tiempo_New_Puntos      += reloj.tick(FPS)

    #Niveles
    if True:
        if Tiempo_New_Nivel > Tiempo_Niveles:
            if Niveles < 5:
                Tiempo_New_Nivel = 0
                Niveles         += 1
                Tiempo_Enemigos   -= 150
                Tiempo_Puntos   += 1000
            elif Niveles >= 5 and Niveles <=8:
                Tiempo_New_Nivel = 0
                Niveles         += 1
                Tiempo_Enemigos   -= 5
                Tiempo_Puntos   += 1000
            elif Niveles == 9:
                Niveles == "Lvl Max"
                Tiempo_Enemigos -= 35
                Tiempo_Puntos   == 4000

    #Aparicion de enemigos
    if True:
        if Tiempo_New_enemigo > Tiempo_Enemigos:
            Enemigos.append(Enemigo_Down(random.randint(0,ANCHO),ALTO+100))
            Enemigos.append(Enemigo_Up(random.randint(0,ANCHO),1))
            Enemigos.append(Enemigo_izq(1,random.randint(0,ALTO)))
            Enemigos.append(Enemigo_der(ANCHO+100,random.randint(0,ALTO)))
            Tiempo_New_enemigo = 0
    
    #Aparicion de puntos
    if True:
        if Tiempo_New_Puntos > Tiempo_Puntos:
            ubicacion_puntos = random.randint (1,4)
            if ubicacion_puntos == 1:
                Puntos_ext.append(Puntos_izq(1,random.randint(0,ALTO)))
            elif ubicacion_puntos == 2:
                Puntos_ext.append(Puntos_der(ANCHO+100,random.randint(0,ALTO)))
            elif ubicacion_puntos == 3:
                Puntos_ext.append(Puntos_Up(random.randint(0,ANCHO),0))
            elif ubicacion_puntos == 4:
                Puntos_ext.append(Puntos_Down(random.randint(0,ANCHO),ALTO+100))
            Tiempo_New_Puntos = 0

    #Sistema nuevo de obtencion de vidas
    if True:
        if Puntos == Puntos_por_Vida:
            lugar_de_aparicion = random.randint(1,5)
            if lugar_de_aparicion == 1:
                Vidas_ext.append(Vidas_izq(1,random.randint(0,ALTO)))
            elif lugar_de_aparicion == 2:
                Vidas_ext.append(Vidas_der(ANCHO+100,random.randint(0,ALTO)))
            elif lugar_de_aparicion == 3:
                Vidas_ext.append(Vidas_Up(random.randint(0,ANCHO),0))
            elif lugar_de_aparicion == 4:
                Vidas_ext.append(Vidas_Down(random.randint(0,ANCHO),ALTO+100))
            #Evento de vida especial
            elif lugar_de_aparicion == 5:
                exito = random.randint (1,100)
                if exito <=10:
                    Vidas_ext.append(Vidas_izq(1,random.randint(0,ALTO)))
                    Vidas_ext.append(Vidas_der(ANCHO+100,random.randint(0,ALTO)))
                    Vidas_ext.append(Vidas_Up(random.randint(0,ANCHO),0))     
                    Vidas_ext.append(Vidas_Down(random.randint(0,ANCHO),ALTO+100))
            Puntos_por_Vida     += 5
    
    #Teclas y eventos
    if True:
        eventos = pygame.event.get()
        teclas = pygame.key.get_pressed()
        gestionar_teclas(teclas)

    #Crear texto
    if True:
        texto_vida      = FUENTE.render(f"Vida: {Vidas}", True, "red")
        texto_Nivel     = FUENTE.render(f"Nivel: {Niveles}", True, "red")
        texto_puntos    = FUENTE.render(F"Puntos: {Puntos}", True, "red")

    #Cerrar el juego
    if True:
        for evento in eventos:
            if evento.type == pygame.QUIT:
                Jugando = False
    
    #Personaje
    if True:
        VENTANA.fill ("black")
        Jugador.dibujar(VENTANA)
    
    #Enemigos
    if True:
        for enemigo in Enemigos:
            enemigo.dibujar(VENTANA)
            enemigo.movimiento()
            #Sistema de colision y vidas
            if pygame.Rect.colliderect(Jugador.rect,enemigo.rect):
                Vidas -=1
                Enemigos.remove(enemigo)
    
    #Vidas extra
    if True:
        for vida in Vidas_ext:
            vida.dibujar(VENTANA)
            vida.movimiento()
            #Sistema de colision y +vidas
            if pygame.Rect.colliderect(Jugador.rect,vida.rect):
                Vidas +=1
                Vidas_ext.remove(vida)
    
    #Puntos extra
    if True:
        for puntos in Puntos_ext:
            puntos.dibujar(VENTANA)
            puntos.movimiento()
            #Sistema de colision y +puntos
            if pygame.Rect.colliderect(Jugador.rect,puntos.rect):
                Puntos +=1
                Puntos_ext.remove(puntos)
    
    #Aparicion de texto en pantalla
    if True:
        VENTANA.blit(texto_vida,(20,0))
        VENTANA.blit(texto_Nivel,(20,40))
        VENTANA.blit(texto_puntos,(20,80))

    #Actualizacion del juego
    pygame.display.update()

quit()
