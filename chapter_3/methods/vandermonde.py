import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def method_vandermonde(x, y, degree):
    """
    Calcula la matriz de Vandermonde y el polinomio de la solución.

    Parámetros:
    x (array): Valores de x
    y (array): Valores de y
    degree (int): Grado del polinomio

    Retorna:
    vandermonde_matrix (array): Matriz de Vandermonde
    polynomial (array): Coeficientes del polinomio
    """
    vandermonde_matrix = np.vander(x, degree + 1, increasing=True)
    coefficients, _, _, _ = np.linalg.lstsq(vandermonde_matrix, y, rcond=None)
    polynomial = np.poly1d(coefficients[::-1])

    # Crear un rango de valores x para la gráfica
    x_range = np.linspace(min(x), max(x), 100)

    # Evaluar el polinomio de interpolación en el rango de x
    y_range = np.polyval(polynomial, x_range)

    # Graficar la función de interpolación y los puntos de entrada
    plt.plot(x_range, y_range, label='Interpolación de Vandermonde')
    plt.scatter(x, y, color='red', label='Puntos de entrada')

    # Ajustar los límites de los ejes para que la gráfica se vea desde más lejos
    x_margin = 0.1 * (max(x) - min(x))
    y_margin = 0.1 * (max(y) - min(y))
    plt.xlim(min(x) - x_margin, max(x) + x_margin)
    plt.ylim(min(y) - y_margin, max(y) + y_margin)

    plt.legend()
    plt.show()

    # Construir representación en cadena de texto del polinomio
    polynomial_str = str(polynomial)

    resultado = pd.DataFrame({
        'x': x,
        'y': y,
        'polinomio Vandermonde': [polynomial_str] * len(x)
    })

    # Verificar si la interpolación fue exitosa
    if np.isfinite(polynomial).all():
        mensaje = 'La interpolación de Vandermonde se realizó correctamente para los puntos dados.'
    else:
        mensaje = 'La interpolación de Vandermonde falló. Por favor, verifica los puntos de entrada.'

    return resultado, mensaje

def plot_polynomial(x, y, polynomial):
    """
    Grafica el polinomio.

    Parámetros:
    x (array): Valores de x
    y (array): Valores de y
    polynomial (array): Coeficientes del polinomio
    """
    x_plot = np.linspace(x.min(), x.max(), 400)
    y_plot = polynomial(x_plot)
    plt.plot(x, y, 'o', label='Datos')
    plt.plot(x_plot, y_plot, label='Polinomio')
    plt.legend()
    plt.show()

def save_to_file(vandermonde_matrix, polynomial, x, y):
    """
    Guarda la información en un archivo txt.

    Parámetros:
    vandermonde_matrix (array): Matriz de Vandermonde
    polynomial (array): Coeficientes del polinomio
    x (array): Valores de x
    y (array): Valores de y
    """
    with open('vandermonde_output.txt', 'w') as f:
        f.write('Matriz de Vandermonde:\n')
        f.write(str(vandermonde_matrix) + '\n\n')
        f.write('Polinomio de la solución:\n')
        f.write(str(polynomial) + '\n\n')
        f.write('Valores de x:\n')
        f.write(str(x) + '\n\n')
        f.write('Valores de y:\n')
        f.write(str(y) + '\n\n')

# Ejemplo de uso
x = np.array([-1, 0, 1, 2, 3])
y = np.array([1, 2, 3, 4, 5])
degree = 3

#vandermonde_matrix, polynomial = vandermonde(x, y, degree)
#print("Matriz de Vandermonde:")
#print(vandermonde_matrix)
#print("Polinomio de la solución:")
#print(polynomial)

#plot_polynomial(x, y, polynomial)

#save_to_file(vandermonde_matrix, polynomial, x, y)
