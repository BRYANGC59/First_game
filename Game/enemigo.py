import random

class Enemigo:
    def __init__(self, nombre, vida, daño):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño

    def atacar(self, jugador):
        jugador.recibir_dano(self.daño)

    def soltar_gemas(self):
        if self.gemas > 0:
            self.gemas -= 1
            return True
        return False

class Roca:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.roca = 1

        roca_paht = os.path.join("recursos", "imagenes", "personajes", "roca.png")
        self.image = pygame.image.load(roca_paht).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constantes.ENEMIGO, constantes.ENEMIGO))
        self.size = self.image.get_width()

    def draw(self, ventana):
        ventana.blit(self.image, (self.x, self.y))


