import math


class ConversorAngulo:

    def __init__(self, angulo):
        self.angulo = angulo

    def radianes_a_grados(self):
        return round(self.angulo * (180 / math.pi), 4)

    def grados_a_radianes(self):
        return round(self.angulo * (math.pi / 180), 4)

    def imprimir_angulo(self):
        print(f"Si el angulo {self.angulo} es en grados, son ",
              self.grados_a_radianes(), "radianes")
        print(f"Si el angulo {self.angulo} es en radianes, son ",
              self.radianes_a_grados(), "grados")
