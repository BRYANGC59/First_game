import pygame
import constantes

class Mundo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def draw(self, screen):
        screen.fill(constantes.GREEN)