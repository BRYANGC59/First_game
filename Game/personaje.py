import pygame

import constantes


class Personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20

    def draw(self, screen):
        pygame.draw.rect(screen, constantes.BLUE, (self.x,self.y, self.size, self.size))

    def movimientos(self, mx, my):
        self.x += mx
        self.y += my