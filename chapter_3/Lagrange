def Lagrange(points):
    # Verificar si hay duplicados en x o y
    if len(set(points['x'])) != len(points['x']) or len(set(points['y'])) != len(points['y']):
        raise ValueError("No se permiten duplicados en x o y")

    # Inicializar matrices
    polinomios = []
    grado = len(points['x'])

    # Calcular cada polinomio de interpolación
    for k in range(grado):
        numerator = ""
        denominator = ""
        for j in range(grado):
            if j != k:
                if points['x'][j] < 0:
                    numerator += f"(x+{-points['x'][j]})"
                    if points['x'][k] == 0:
                        denominator += f"({points['x'][j]})"
                    else:
                        denominator += f"({points['x'][k]}+{-points['x'][j]})"
                elif points['x'][j] > 0:
                    numerator += f"(x-{points['x'][j]})"
                    if points['x'][k] == 0:
                        denominator += f"({points['x'][j]})"
                    else:
                        denominator += f"({points['x'][k]}-{points['x'][j]})"
                else:
                    numerator += "(x)"
                    if points['x'][k] != 0:
                        denominator += f"({points['x'][k]})"
        polinomios.append(f"({numerator})/({denominator})")

    # Combinar polinomios de interpolación
    polinomio = " + ".join(f"({points['y'][i]}*{pol})" for i, pol in enumerate(polinomios))

    return {'polinomio': polinomio, 'polinomios': polinomios}
