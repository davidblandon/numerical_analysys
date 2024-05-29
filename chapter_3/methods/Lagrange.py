import numpy as np
import pandas as pd
def method_lagrange(x,y):
    n = len(x)
    polinomios = []

    for i in range(n):
        numerador = 1
        denominador = 1
        for j in range(n):
            if i != j:
                numerador *= (x - x[j])
                denominador *= (x[i] - x[j])
        polinomio_i = numerador / denominador
        polinomios.append(polinomio_i)

    polinomio_interpolacion = 0
    for i in range(n):
        polinomio_interpolacion += y[i] * polinomios[i]

    # Construir representación en cadena de texto del polinomio de interpolación
    polinomio_interpolacion_str = ""
    for i, coef in enumerate(polinomio_interpolacion):
        if i == 0:
            polinomio_interpolacion_str += f"{coef:.2f}"
        else:
            polinomio_interpolacion_str += f" + {coef:.2f}x^{i}"

    # Construir representación en cadena de texto de los polinomios
    polinomios_str = []
    for p in polinomios:
        polinomio_str = ""
        for i, coef in enumerate(p):
            if i == 0:
                polinomio_str += f"{coef:.2f}"
            else:
                polinomio_str += f" + {coef:.2f}x^{i}"
        polinomios_str.append(polinomio_str)

    resultado = pd.DataFrame({
        'x': x,
        'y': y,
        'polinomio Lagrange': [polinomio_interpolacion_str] * n,
        'polinomios': polinomios_str
    })

    # Verificar si la interpolación fue exitosa
    if np.isfinite(polinomio_interpolacion).all():
        mensaje = 'La interpolación de Lagrange se realizó correctamente para los puntos dados.'
    else:
        mensaje = 'La interpolación de Lagrange falló. Por favor, verifica los puntos de entrada.'

    return resultado, mensaje

# Ejemplo de uso
points = {
    'x': np.array([0, 1, 2]),
    'y': np.array([1, 3, 2])
}

#resultado = Lagrange(points)
#print(resultado)
