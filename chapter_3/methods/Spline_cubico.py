import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def spline_cubico(x, y):
    cs = CubicSpline(x, y, bc_type='natural')
    return cs

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
