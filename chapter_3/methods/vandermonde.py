import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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
