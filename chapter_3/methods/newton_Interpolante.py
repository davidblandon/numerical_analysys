import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def method_newton_interpolante(x, y):
    n = len(x)
    a = np.zeros((n, n))
    a[:, 0] = y
    
    for i in range(1, n):
        for j in range(i, n):
            a[j, i] = (a[j, i-1] - a[j-1, i-1]) / (x[j] - x[j-i])
    
    polinomio = np.zeros(n)
    for i in range(n):
        temp = a[i, i]
        for j in range(i):
            temp = np.polymul(temp, np.poly1d([1., -x[j]]))
        polinomio = np.polyadd(polinomio, temp)

    # Crear un rango de valores x para la gráfica
    x_range = np.linspace(min(x), max(x), 100)

    # Evaluar el polinomio de interpolación en el rango de x
    y_range = np.polyval(polinomio, x_range)

    # Graficar la función de interpolación y los puntos de entrada
    plt.plot(x_range, y_range, label='Interpolación de Newton')
    plt.scatter(x, y, color='red', label='Puntos de entrada')

    # Ajustar los límites de los ejes para que la gráfica se vea desde más lejos
    x_margin = 0.1 * (max(x) - min(x))
    y_margin = 0.1 * (max(y) - min(y))
    plt.xlim(min(x) - x_margin, max(x) + x_margin)
    plt.ylim(min(y) - y_margin, max(y) + y_margin)

    plt.legend()
    plt.show()

    # Construir representación en cadena de texto del polinomio de interpolación
    polinomio_str = " + ".join([f"{coef:.2f}x^{i}" for i, coef in enumerate(polinomio[::-1])])

    resultado = pd.DataFrame({
        'x': x,
        'y': y,
        'polinomio Newton': [polinomio_str] * n
    })

    # Verificar si la interpolación fue exitosa
    if np.isfinite(polinomio).all():
        mensaje = 'La interpolación de Newton se realizó correctamente para los puntos dados.'
    else:
        mensaje = 'La interpolación de Newton falló. Por favor, verifica los puntos de entrada.'

    return resultado, mensaje

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
