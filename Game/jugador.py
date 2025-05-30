class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.arma = "Espada de madera"
        self.armadura = "Armadura de cuero"
        self.inventario = []
        self.estrellas = 0

    def atacar(self, enemigo):
        danos = {
            "Espada de madera": 10,
            "Espada de hierro": 20,
            "Hacha": 25,
            "Lanza": 30
        }
        dano = danos.get(self.arma, 10)
        enemigo.recibir_dano(dano)

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    def recoger_mejora(self, mejora):
        if mejora.tipo == "arma":
            self.arma = mejora.valor
        elif mejora.tipo == "armadura":
            self.armadura = mejora.valor
        elif mejora.tipo == "habilidad":
            self.inventario.append(mejora.valor)

    def esta_vivo(self):
        return self.vida > 0

    def reiniciar(self):
        self.vida = 100
        self.arma = "Espada de madera"
        self.armadura = "Armadura de cuero"
        self.inventario = []
        self.estrellas = 0


