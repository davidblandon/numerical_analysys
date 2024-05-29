import numpy as np

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

    resultado = {
        'polinomio': str(polinomio_interpolacion),
        'polinomios': [str(p) for p in polinomios]
    }

    return resultado

# Ejemplo de uso
points = {
    'x': np.array([0, 1, 2]),
    'y': np.array([1, 3, 2])
}

#resultado = Lagrange(points)
#print(resultado)
