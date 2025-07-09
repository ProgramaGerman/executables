#Principio de Sustitucion de Liskov

"""
ejercicio 1
"""

#Manera Incorrecta
class Aves:
    def volar(self):
        return "Volando"

class Pollo(Aves):
    def volar(self):
        raise Exception("Los Pollos No vuelan")

#pajaro = Aves()
#pajaro.volar()

#pollo = Pollo()
#pollo.volar()


#Manera Correcta
class Ave:
    def moverse(self):
        return "Moviendo"

class Pollo(Ave):
    def moverse(self):
        return "Caminando"



"""
Ejercicio 2
"""


class Vehiculo:
    def __init__(self,velocidad):
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 1
        print(f"Velocidad del Vehiculo {self.velocidad}")

    def frenar(self):
        self.velocidad -= 1
        print(f"Velocidad del vehiculo {self.velocidad}")


