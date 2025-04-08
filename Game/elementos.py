import random

import pygame

import constantes

import os



class Enemigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gemas = random.randint(1,3)

        arbol = os.path.join("recursos", "imagenes", "personajes", "echisera.png")
        self.image = pygame.image.load(arbol).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constantes.ARBOL, constantes.ARBOL))
        self.size = self.image.get_width()

    def draw(self, ventana):
        ventana.blit(self.image, (self.x, self.y))

class Roca:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.roca = 1

        roca_paht = os.path.join("recursos", "imagenes", "personajes", "roca.png")
        self.image = pygame.image.load(roca_paht).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constantes.ARBOL, constantes.ARBOL))
        self.size = self.image.get_width()

    def draw(self, ventana):
        ventana.blit(self.image, (self.x, self.y))


