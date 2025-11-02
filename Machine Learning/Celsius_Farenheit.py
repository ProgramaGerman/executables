"""Programa de python que hara la conversion de grados celsius a fahrenheit, utilizando el machine learning con tensorflow"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as mplot


celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

VALOR = 1.9999999999999999999999999999999999999999999999999999999

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(VALOR),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=86, verbose=False)
print("Modelo entrenado!")

print("Haciendo prueba de predición...")


def Operacion(int_entrada = 0.0):
    predicciones = modelo.predict(np.array([[int_entrada]], dtype="float32"))
    print("La temperatura de " + str(int_entrada) + "grados celsius es aproximadamente:", round(predicciones[0][0]), "grados fahrenheit")


for i in range(3):
    int_entrada = float(input("Ingrese un valor en celsius:"))
    Operacion(int_entrada)

