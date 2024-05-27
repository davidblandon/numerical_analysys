import numpy as np
import pandas as pd

def SOR(A, b, x0, tol, niter, w):
    if w <= 0 or w >= 2:
        raise ValueError("El factor de relajación w debe estar entre 0 y 2.")
    
    n = len(A)
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    
    resultados = pd.DataFrame(columns=['Iteración', 'x', 'Error'])
    error = tol + 1  # Inicializar el error para asegurar la entrada al bucle
    
    iteracion = 0
    while error > tol and iteracion < niter:
        T = np.dot(np.linalg.inv(D - w * L), (1 - w) * D + w * U)
        C = w * np.dot(np.linalg.inv(D - w * L), b)
        x = np.dot(T, x0) + C
        
        error = np.linalg.norm(x - x0, np.inf)
        resultados.loc[iteracion] = [iteracion, x.copy(), error]
        
        x0 = x.copy()
        iteracion += 1
    
    mensaje = f'La solución convergió a {x} en {iteracion} iteraciones con una tolerancia de {tol}.' if error < tol else 'Fracasó en alcanzar la convergencia dentro del número máximo de iteraciones permitidas.'
    
    return resultados, mensaje

# Ejemplo de uso:
A = np.array([[4, -1, 0, 0],
              [-1, 4, -1, 0],
              [0, -1, 4, -1],
              [0, 0, -1, 3]], dtype=float)

b = np.array([15, 10, 10, 10], dtype=float)
x0 = np.zeros(len(b))  # Condiciones iniciales
tol = 1e-5  # Tolerancia
niter = 100  # Número máximo de iteraciones
w = 1.25  # Factor de relajación

resultados, mensaje_final = SOR(A, b, x0, tol, niter, w)
print(mensaje_final)
print(resultados)
