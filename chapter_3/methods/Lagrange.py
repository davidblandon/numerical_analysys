import numpy as np
import matplotlib.pyplot as plt

def lagrange(x, y):
    n = len(x)
    polinomio = ""
    for i in range(n):
        numerador = 1
        denominador = 1
        for j in range(n):
            if i != j:
                numerador *= f"(x - {x[j]:.2f})"
                denominador *= (x[i] - x[j])
        polinomio += f"({y[i]:.2f} * {numerador}) / {denominador} + "
    polinomio = polinomio[:-3]  # Eliminar el "+ " extra al final
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
    
    polinomio = lagrange(x, y)
    print(polinomio)
    graficar(x, y, polinomio)
    guardar_archivo(x, y, polinomio)

if __name__ == "__main__":
    main()
