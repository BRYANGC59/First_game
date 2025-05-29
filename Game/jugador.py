import pygame
from Extras import constantes
import os



class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.arma = "Espada de madera"
        self.armadura = "Armadura de cuero"
        self.inventario = []
        self.estrellas = 0


    def cargar_archivo_imagen(self, nombre_archivo):
        path = os.path.join('recursos', 'imagenes', 'objetos', nombre_archivo)
        imagen = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(imagen, (40,40))

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
        return (abs(self.x - obj.x) <= max(self.size, obj.size +5 and
                abs(self.y - obj.y) <= max(self.size, obj.size)+5))


    def interactuar(self, mundo):
        for enemigo in mundo.enemigo:
            if self.esta_cerca(enemigo):
                if enemigo.soltar_gemas():
                    self.inventario['GEMAS'] += 1
                    if enemigo.gemas == 0:
                        mundo.enemigo.remove(enemigo)
                return

    def draw_inventario(self, ventana):
        backgrounds = pygame.Surface((constantes.ANCHO, constantes.ALTO), pygame.SRCALPHA)
        backgrounds.fill((0,0,0,128))
        ventana.blit(backgrounds, (0,0))

        font = pygame.font.Font(None, 36)
        titulo = font.render('Inventario', True, constantes.WHITE)
        ventana.blit(titulo, (constantes.ANCHO // 2 - titulo.get_width() // 2, 20))

        item_font = pygame.

