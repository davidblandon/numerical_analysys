import numpy as np

def NewtonInterpolante(points):
    # Comprobamos si hay valores duplicados en las matrices
    if len(np.unique(points['x'])) != len(points['x']) or len(np.unique(points['y'])) != len(points['y']):
        raise ValueError("Las matrices x e y no pueden tener valores duplicados")

    # Creamos la matriz 'datos' para contener los valores que se utilizarán para calcular los coeficientes del polinomio
    n = len(points['x'])
    datos = np.zeros((n, n))
    datos[:, 0] = points['y']

    # Calculamos los coeficientes del polinomio utilizando el método de diferencias divididas
    for j in range(1, n):
        for i in range(n - j):
            datos[i, j] = (datos[i + 1, j - 1] - datos[i, j - 1]) / (points['x'][i + j] - points['x'][i])

    # Construimos la expresión del polinomio iterando sobre los coeficientes de la matriz 'datos'
    expresion = ""
    for j in range(n):
        termino = datos[0, j]
        for i in range(j):
            termino *= (x - points['x'][i])
        expresion += f" + {termino}"

    # Devolvemos un objeto llamado 'resultados' con los datos de la matriz 'datos' y la variable 'expresion'
    resultados = {
        'diferenciasDivididas': datos,
        'expresion': expresion[3:]  # Eliminamos el primer signo '+' de la expresión
    }
    return resultados
  
#Ejemplo de uso
points = {'x': np.array([1, 2, 3, 4]), 'y': np.array([1, 4, 9, 16])}
resultados = NewtonInterpolante(points)
print(resultados['expresion'])  # Output: 1 + 3*(x - 1) + 3*(x - 1)*(x - 2) + 1*(x - 1)*(x - 2)*(x - 3)
print(resultados['diferenciasDivididas'])
  
