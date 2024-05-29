import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

def spline_lineal(x, y):
    spl = InterpolatedUnivariateSpline(x, y, k=1)
    return spl

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
