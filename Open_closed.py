#Principio abierto/cerrado
from abc import ABC, abstractmethod

#Ejercicio

#Incorrecta

from typing import override


class Forma:
    def dibujar_cuadrado(self):
        pass

    def dibujar_circulo(self):
        pass

class Forma:
    def dibujar(self):
        pass


class Cuadrado(Forma):
    def dibujar(self):
        print("Dibujar un Cuadrado")


class Circulo(Forma):
    def dibujar(self):
        print("Dibujar un Circulo")

class Triangulo(Forma):
    def dibujar(self):
        print("Dibujar un Triangulo")


'''
ejercicio Numero 2 OCP
'''


class Opeacion(ABC):
    @abstractmethod
    def Execute(self, A, B):
        pass

class Suma(Opeacion):
    @override
    def Execute(self, A, B):
        return A + B

class Resta(Opeacion):
    @override
    def Execute(self, A, B):
        return A - B

class Multiplicacion(Opeacion):
    @override
    def Execute(self, A, B):
        return A * B

class Division(Opeacion):
    @override
    def Execute(self, A, B):
        return A / B

class Potencia(Opeacion):
    @override
    def Execute(self, A, B):
        return A ** B


class Calculadora:
    def __init__(self):
        self.opeacion = {}

    def agregar_operacion(self, nombre, operacion):
        self.opeacion[nombre] = operacion
    
    def calcular(self, nombre, A, B):
        if nombre not in self.opeacion:
            raise ValueError(f"Operacion con el nombre {nombre} no existe o no es soportada")
        return self.opeacion[nombre].Execute(A, B)
    

calculadora = Calculadora()
calculadora.agregar_operacion("suma", Suma())
calculadora.agregar_operacion("resta", Resta())
calculadora.agregar_operacion("multiplicacion", Multiplicacion())
calculadora.agregar_operacion("division", Division())
calculadora.agregar_operacion("potencia", Potencia())

print(calculadora.calcular("suma", 1, 2))
print(calculadora.calcular("resta", 1, 2))
print(calculadora.calcular("multiplicacion", 1, 2))
print(calculadora.calcular("division", 1, 2))
print(calculadora.calcular("potencia", 4, 5))

