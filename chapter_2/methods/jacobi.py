import numpy as np
import pandas as pd

def method_jacobi(A, b, x0, tol, niter):
    n = len(A)
    x1 = np.zeros(n)
    resultados = pd.DataFrame(columns=['Iteración', 'x', 'Error'])
    
    iteracion = 0
    error = tol + 1  # Inicializar error para asegurar la entrada al bucle
    
    while error > tol and iteracion < niter:
        for i in range(n):
            suma = sum(A[i, j] * x0[j] for j in range(n) if j != i)
            x1[i] = (b[i] - suma) / A[i, i]
        
        error = np.linalg.norm(x1 - x0, np.inf) / np.linalg.norm(x1, np.inf)
        resultados.loc[iteracion] = [iteracion, x1.copy(), error]
        
        x0 = x1.copy()
        iteracion += 1
    
    if error < tol:
        mensaje = f'La solución convergió a {x1} en {iteracion} iteraciones con una tolerancia de {tol}.'
    else:
        mensaje = 'Fracasó en alcanzar la convergencia dentro del número máximo de iteraciones permitidas.'
    
    return resultados, mensaje

# Ejemplo de uso:
A = np.array([[10, -1, 2, 0],
              [-1, 11, -1, 3],
              [2, -1, 10, -1],
              [0, 3, -1, 8]], dtype=float)

b = np.array([6, 25, -11, 15], dtype=float)
x0 = np.zeros(len(b))  # Condiciones iniciales
tol = 1e-5  # Tolerancia
niter = 100  # Número máximo de iteraciones

#resultados, mensaje_final = jacobi(A, b, x0, tol, niter)
#print(mensaje_final)
#print(resultados)


