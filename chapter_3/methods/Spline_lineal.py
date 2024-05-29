import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import InterpolatedUnivariateSpline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

def method_spline_lineal(x, y):
    spl = InterpolatedUnivariateSpline(x, y, k=1)

    # Generar una lista de valores y de los polinomios evaluados en esos valores
    x_values = np.linspace(min(x), max(x), num=100)
    y_values = spl(x_values)

    # Graficar la función de interpolación y los puntos de entrada
    plt.plot(x_values, y_values, label='Interpolación de spline lineal')
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
        mensaje = 'La interpolación de spline lineal se realizó correctamente para los puntos dados.'
    else:
        mensaje = 'La interpolación de spline lineal falló. Por favor, verifica los puntos de entrada.'

    return resultado, mensaje
def graficar(x, y, spl):
    x_new = np.linspace(min(x), max(x), 100)
    y_new = spl(x_new)
    plt.plot(x, y, 'o', label='Datos')
    plt.plot(x_new, y_new, label='Spline lineal')
    plt.legend()
    plt.show()

def guardar_archivo(x, y, spl):
    with open("resultado_lineal.txt", "w") as f:
        f.write("Datos:\n")
        for i in range(len(x)):
            f.write(f"({x[i]:.2f}, {y[i]:.2f})\n")
        f.write("\nPolinomio:\n")
        f.write(str(spl) + "\n")

def main():
    x = input("Ingrese los valores de x separados por coma: ")
    y = input("Ingrese los valores de y separados por coma: ")
    x = np.array([float(i) for i in x.split(',')])
    y = np.array([float(i) for i in y.split(',')])
    
    spl = spline_lineal(x, y)
    print(spl)
    graficar(x, y, spl)
    guardar_archivo(x, y, spl)

if __name__ == "__main__":
    main()
