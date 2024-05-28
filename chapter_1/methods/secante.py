import sympy as sp
import pandas as pd
import numpy as np

def method_secante(f_expr, x0, x1, tol, niter):
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr, 'numpy')  # Convertir la expresión simbólica a una función evaluable

    resultados = pd.DataFrame(columns=['Iteración', 'xn', 'f(xn)', 'Error'])
    
    xn_minus1 = x0
    xn = x1
    f_xn_minus1 = f(xn_minus1)
    f_xn = f(xn)
    
    iteracion = 0
    error = abs(xn - xn_minus1)
    
    while error > tol and iteracion < niter:
        if f_xn - f_xn_minus1 == 0:
            mensaje = "División por cero debido a una diferencia nula en f(x) consecutivos."
            return resultados, mensaje

        xn_plus1 = xn - f_xn * (xn - xn_minus1) / (f_xn - f_xn_minus1)
        f_xn_plus1 = f(xn_plus1)
        error = abs(xn_plus1 - xn)

        resultados.loc[iteracion] = [iteracion, xn_plus1, f_xn_plus1, error]

        xn_minus1 = xn
        xn = xn_plus1
        f_xn_minus1 = f_xn
        f_xn = f_xn_plus1
        
        iteracion += 1

    if error < tol:
        mensaje = f'{xn} es una aproximación de una raíz de f(x) con una tolerancia de {tol}'
    else:
        mensaje = 'Fracasó en alcanzar la convergencia en el número máximo de iteraciones'
    
    return resultados, mensaje

# Definición de la función
x = sp.symbols('x')
f_expr = x**2 - 4

# Parámetros iniciales
x0 = 1.0  # Punto inicial cercano a la raíz real
x1 = 2.0  # Punto inicial cercano a la raíz real
tol = 1e-8
niter = 100

# resultados, mensaje = secante(f_expr, x0, x1, tol, niter)
# print(mensaje)
# print(resultados)
