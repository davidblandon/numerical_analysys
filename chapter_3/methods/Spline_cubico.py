import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import CubicSpline

from scipy.interpolate import CubicSpline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def method_spline_cubico(x, y):
    cs = CubicSpline(x, y, bc_type='natural')

    # Generar una lista de valores y de los polinomios evaluados en esos valores
    x_values = np.linspace(min(x), max(x), num=100)
    y_values = cs(x_values)

    # Graficar la función de interpolación y los puntos de entrada
    plt.plot(x_values, y_values, label='Interpolación de spline cúbico')
    plt.scatter(x, y, color='red', label='Puntos de entrada')

    # Ajustar los límites de los ejes para que la gráfica se vea desde más lejos
    x_margin = 0.1 * (max(x) - min(x))
    y_margin = 0.1 * (max(y) - min(y))
    plt.xlim(min(x) - x_margin, max(x) + x_margin)
    plt.ylim(min(y) - y_margin, max(y) + y_margin)

    plt.legend()
    plt.show()

    resultado = pd.DataFrame({
        'x': x_values,
        'y': y_values,
    })

    # Verificar si la interpolación fue exitosa
    if np.isfinite(y_values).all():
        mensaje = 'La interpolación de spline cúbico se realizó correctamente para los puntos dados.'
    else:
        mensaje = 'La interpolación de spline cúbico falló. Por favor, verifica los puntos de entrada.'

    return resultado, mensaje

def graficar(x, y, cs):
    x_new = np.linspace(min(x), max(x), 100)
    y_new = cs(x_new)
    plt.plot(x, y, 'o', label='Datos')
    plt.plot(x_new, y_new, label='Spline cúbico')
    plt.legend()
    plt.show()

def guardar_archivo(x, y, cs):
    with open("resultado_cubico.txt", "w") as f:
        f.write("Datos:\n")
        for i in range(len(x)):
            f.write(f"({x[i]:.2f}, {y[i]:.2f})\n")
        f.write("\nPolinomio:\n")
        f.write(str(cs) + "\n")

def main():
    x = input("Ingrese los valores de x separados por coma: ")
    y = input("Ingrese los valores de y separados por coma: ")
    x = np.array([float(i) for i in x.split(',')])
    y = np.array([float(i) for i in y.split(',')])
    
    cs = spline_cubico(x, y)
    print(cs)
    graficar(x, y, cs)
    guardar_archivo(x, y, cs)

if __name__ == "__main__":
    main()
