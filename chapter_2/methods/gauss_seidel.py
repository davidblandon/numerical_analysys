import numpy as np
import pandas as pd

def method_gauss_seidel(A, b, x0, tol, niter):
    n = len(A)
    x = x0.copy()
    resultados = pd.DataFrame(columns=['Iteración', 'x', 'Error'])
    
    iteracion = 0
    error = tol + 1  # Inicializar error para asegurar la entrada al bucle

    while error > tol and iteracion < niter:
        x_old = x.copy()
        for i in range(n):
            suma = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - suma) / A[i, i]
        
        error = np.linalg.norm(x - x_old, np.inf) / np.linalg.norm(x, np.inf)
        resultados.loc[iteracion] = [iteracion, x.copy(), error]
        
        iteracion += 1
    
    mensaje = f'La solución convergió a {x} en {iteracion} iteraciones con una tolerancia de {tol}.' if error < tol else 'Fracasó en alcanzar la convergencia dentro del número máximo de iteraciones permitidas.'
    
    return resultados, mensaje

# Ejemplo de uso:

