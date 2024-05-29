import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re


def method_lagrange(x, y):
    n = len(x)
    polinomios = []

    for i in range(n):
        numerador = np.poly1d([1.])
        denominador = 1.
        for j in range(n):
            if i != j:
                numerador *= np.poly1d([1., -x[j]])
                denominador *= x[i] - x[j]
        polinomio_i = numerador / denominador
        polinomios.append(polinomio_i)

    polinomio_interpolacion = np.poly1d([0.])
    for i in range(n):
        polinomio_interpolacion += y[i] * polinomios[i]

    # Crear un rango de valores x para la gráfica
    x_range = np.linspace(min(x), max(x), 100)

    # Evaluar el polinomio de interpolación en el rango de x
    y_range = np.polyval(polinomio_interpolacion, x_range)

    # Graficar la función de interpolación y los puntos de entrada
    plt.plot(x_range, y_range, label='Interpolación de Lagrange')
    plt.scatter(x, y, color='red', label='Puntos de entrada')

    # Ajustar los límites de los ejes para que la gráfica se vea desde más lejos
    x_margin = 0.1 * (max(x) - min(x))
    y_margin = 0.1 * (max(y) - min(y))
    plt.xlim(min(x) - x_margin, max(x) + x_margin)
    plt.ylim(min(y) - y_margin, max(y) + y_margin)

    plt.legend()
    plt.show()

    # Construir representación en cadena de texto del polinomio de interpolación
    polinomio_interpolacion_str = " + ".join([f"{coef:.2f}x^{i}" for i, coef in enumerate(polinomio_interpolacion.coeffs[::-1])])

    # Construir representación en cadena de texto de los polinomios
    polinomios_str = [" + ".join([f"{coef:.2f}x^{i}" for i, coef in enumerate(p.coeffs[::-1])]) for p in polinomios]

    resultado = pd.DataFrame({
        'x': x,
        'y': y,
        'polinomio Lagrange': [polinomio_interpolacion_str] * n,
        'polinomios': polinomios_str
    })

    # Verificar si la interpolación fue exitosa
    if np.isfinite(polinomio_interpolacion).all():
        mensaje = 'La interpolación de Lagrange se realizó correctamente para los puntos dados.'
    else:
        mensaje = 'La interpolación de Lagrange falló. Por favor, verifica los puntos de entrada.'

    return resultado, mensaje





# Ejemplo de uso
points = {
    'x': np.array([0, 1, 2]),
    'y': np.array([1, 3, 2])
}

#resultado = Lagrange(points)
#print(resultado)

#polinomio_interpolacion, mensaje = method_lagrange(x, y)
#print(mensaje)

# Crear un rango de valores x para la gráfica
