import numpy as np

def method_spline(x,y, cubic=False):
    x = points['x']
    y = points['y']
    n = len(x)

    if cubic:
        # Calcular los coeficientes para un spline cúbico
        A = np.zeros((n*4, n*4))
        B = np.zeros(n*4)
        for i in range(n-1):
            A[i, i*4:i*4+4] = x[i]**3, x[i]**2, x[i], 1
            A[i+n, i*4:i*4+4] = x[i+1]**3, x[i+1]**2, x[i+1], 1
            A[i+2*n, i*4:i*4+4] = 3*x[i]**2, 2*x[i], 1, 0
            A[i+3*n, i*4:i*4+4] = 3*x[i+1]**2, 2*x[i+1], 1, 0
            B[i] = y[i]
            B[i+n] = y[i+1]
        coeficientes = np.linalg.solve(A, B)
    else:
        # Calcular los coeficientes para un spline lineal
        A = np.zeros((n*2, n*2))
        B = np.zeros(n*2)
        for i in range(n-1):
            A[i, i*2:i*2+2] = x[i], 1
            A[i+n, i*2:i*2+2] = x[i+1], 1
            B[i] = y[i]
            B[i+n] = y[i+1]
        coeficientes = np.linalg.solve(A, B)

    return coeficientes

# Ejemplo de uso
#points = {"x": np.array([1, 2, 3]), "y": np.array([3, 5, 7])}
#coeficientes = method_spline(points, cubic=True)
#print("Coeficientes:")
#print(coeficientes)