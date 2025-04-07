import pygame

import constantes


class Personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.inventario = {"Gemas": 0}

    def draw(self, screen):
        pygame.draw.rect(screen, constantes.WHITE, (self.x,self.y, self.size, self.size))

    def movimientos(self, mx, my):
        self.x += mx
        self.y += my
        self.x = max(0, min(self.x, constantes.ANCHO - self.size))
        self.y = max(0, min(self.y, constantes.ALTO - self.size))