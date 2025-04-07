import pygame
import constantes
import os


class Personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventario = {"Gemas": 0}
        imagen_path = os.path.join("recursos", "imagenes", "personajes", "caballero.png")
        self.imagen = pygame.image.load(imagen_path).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (constantes.PERSONAJE, constantes.PERSONAJE))
        self.size = self.imagen.get_width()

    def draw(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))

    def movimientos(self, mx, my):
        self.x += mx
        self.y += my
        self.x = max(0, min(self.x, constantes.ANCHO - self.size))
        self.y = max(0, min(self.y, constantes.ALTO - self.size))