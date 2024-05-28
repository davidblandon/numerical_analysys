import numpy as np
import matplotlib.pyplot as plt

def vandermonde(x, y, degree):
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
    polynomial = np.poly1d(coefficients)
    return vandermonde_matrix, polynomial

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

# Ejemplo de uso
x = np.array([-1, 0, 1, 2, 3])
y = np.array([1, 2, 3, 4, 5])
degree = 3

vandermonde_matrix, polynomial = vandermonde(x, y, degree)
print("Matriz de Vandermonde:")
print(vandermonde_matrix)
print("Polinomio de la solución:")
print(polynomial)

plot_polynomial(x, y, polynomial)
