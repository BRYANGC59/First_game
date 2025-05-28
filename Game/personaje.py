import pygame

import constantes

import os

from Game.elementos import Enemigo


class Personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventario = {"GEMAS": 0}
        imagen_path = os.path.join("recursos", "imagenes", "personajes", "caballero.png")
        self.imagen = pygame.image.load(imagen_path).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (constantes.PERSONAJE, constantes.PERSONAJE))
        self.size = self.imagen.get_width()

    def draw(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))

    def movimientos(self, dx, dy, mundo):
        new_x = self.x + dx
        new_y = self.y + dy

        for enemigo in mundo.enemigo:
            if self.comprobar_colision(new_x, new_y, enemigo):
                return

        self.x = new_x
        self.y = new_y
        self.x = max(0, min(self.x, constantes.ANCHO - self.size))
        self.y = max(0, min(self.y, constantes.ALTO - self.size))


    def comprobar_colision(self, x, y, objeto):
        return (x < objeto.x + objeto.size and x + self.size > objeto.x and y < objeto.y + objeto.size and
                y + self.size > objeto.y)

    def esta_cerca(self, obj):
        return (abs(self.x - obj.x) <= max(self.size, obj.size) and
                abs(self.y - obj.y) <= max(self.size, obj.size))


    def interactuar(self, mundo):
        for enemigo in mundo.enemigo:
            if self.esta_cerca(enemigo):
                if enemigo.soltar_gemas():
                    self.inventario['GEMAS'] += 1
                    if enemigo.gemas == 0:
                        mundo.enemigo.remove(enemigo)
                return





