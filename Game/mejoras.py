class Mejora:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def obtener_mejora_aleatoria(self):
        import random
        opciones = [
            Mejora("arma", "Espada de fuego"),
            Mejora("arma", "Hacha pesada"),
            Mejora("armadura", "Armadura de hierro"),
            Mejora("armadura", "Armadura de sombras"),
            Mejora("habilidad", "Velocidad extra"),
            Mejora("habilidad", "Regeneración de vida")
        ]
        return random.choice(opciones)