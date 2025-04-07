import sys

import pygame
import constantes
from mundo import Mundo
from personaje import Personaje

#Inicializar el juego
pygame.init()

ventana = pygame.display.set.mode((constantes.ANCHO, constantes.ALTO))
pygame.display.set_caption("First Game")

def main():
    clock = pygame.time.Clock()
    mundo = Mundo(constantes.ANCHO, constantes.ALTO)
    personaje =