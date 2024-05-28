import numpy as np

def Vandermonde(points):
    # Crear matrices A, B y C
    matrizA = np.vander(points['x'], increasing=True)
    matrizB = np.matrix(points['y']).T
    matrizC = np.array([f"a{i}" for i in range(len(points['x']))])

    # Resolver el sistema de ecuaciones
    coeficientes = np.linalg.solve(matrizA, matrizB)

    # Crear el polinomio resultante
    polinomio_resultante = " + ".join([f"{coef:.2f} * {var}" for coef, var in zip(coeficientes, matrizC)])

    # Crear el objeto resultados
    resultados = {
        "matrizA": matrizA,
        "matrizB": matrizB,
        "matrizC": matrizC,
        "polinomio_resultante": polinomio_resultante,
        "coeficientes": coeficientes
    }

    return resultados
  
  #points = {"x": np.array([1, 2, 3]), "y": np.array([3, 5, 7])}
  #resultados = Vandermonde(points)
  #print(resultados)
