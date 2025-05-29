import random

class Enemigo:
    def __init__(self, nombre, vida, daño):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño

    def atacar(self, jugador):
        jugador.recibir_dano(self.daño)

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    def esta_vivo(self):
        return self.vida > 0

class Enemigo_de_fuego(Enemigo):
    def __init__(self):
        super().__init__("Demonio de Fuego", random.randint(30, 50), random.randint(5, 15))


