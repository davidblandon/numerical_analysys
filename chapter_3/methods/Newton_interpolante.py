import numpy as np
import matplotlib.pyplot as plt

def newton_interpolante(x, y):
    n = len(x)
    a = np.zeros((n, n))
    a[:, 0] = y
    
    for i in range(1, n):
        for j in range(i, n):
            a[j, i] = (a[j, i-1] - a[j-1, i-1]) / (x[j] - x[j-i])
    
    polinomio = "P(x) = "
    for i in range(n):
        if i > 0:
            polinomio += " + "
        polinomio += f"{a[i, i]:.2f}"
        for j in range(i):
            polinomio += f"(x - {x[j]:.2f})"
    
    return polinomio

def graficar(x, y, polinomio):
    x_interp = np.linspace(min(x), max(x), 100)
    y_interp = np.interp(x_interp, x, y)
    plt.plot(x, y, 'o', label='Datos')
    plt.plot(x_interp, y_interp, label=polinomio)
    plt.legend()
    plt.show()

def guardar_archivo(x, y, polinomio):
    with open("resultado.txt", "w") as f:
        f.write("Datos:\n")
        for i in range(len(x)):
            f.write(f"({x[i]:.2f}, {y[i]:.2f})\n")
        f.write("\nPolinomio:\n")
        f.write(polinomio + "\n")

def main():
    x = input("Ingrese los valores de x separados por coma: ")
    y = input("Ingrese los valores de y separados por coma: ")
    x = np.array([float(i) for i in x.split(',')])
    y = np.array([float(i) for i in y.split(',')])
    
    polinomio = newton_interpolante(x, y)
    print(polinomio)
    graficar(x, y, polinomio)
    guardar_archivo(x, y, polinomio)

if __name__ == "__main__":
    main()
