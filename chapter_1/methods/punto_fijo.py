import sympy as sp
import pandas as pd

def method_punto_fijo(f_expr, g_expr, x0, tol, niter):
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr, 'numpy')  # Convertir la expresión simbólica de f a una función evaluable
    g = sp.lambdify(x, g_expr, 'numpy')  # Convertir la expresión simbólica de g a una función evaluable

    resultados = pd.DataFrame(columns=['Iteración', 'xn', 'f(xn)', 'Error'])
    xn = x0
    error = tol + 1  # Iniciar error mayor que la tolerancia para entrar al bucle
    
    iteracion = 0
    while error > tol and iteracion < niter:
        xn_new = g(xn)
        f_xn_new = f(xn_new)
        error = abs(xn_new - xn)
        
        resultados.loc[iteracion] = [iteracion, xn_new, f_xn_new, error]
        
        if f_xn_new == 0:
            mensaje = f'{xn_new} es raíz de f(x)'
            return resultados, mensaje
        
        xn = xn_new
        iteracion += 1
    
    if error < tol:
        mensaje = f'{xn} es una aproximación de una raíz de f(x) con una tolerancia= {tol}'
    else:
        mensaje = f'Fracasó en {niter} iteraciones'
    
    return resultados, mensaje

# Ejemplo de uso de la función
# x = sp.symbols('x')
# f_expr = sp.exp(x)/x + 3  # Esta es la función f
# g_expr = -sp.exp(x)/3  # Esta es la función g que transforma x
# x0 = -1
# tol = 0.001
# niter = 1000

# resultados, mensaje = punto_fijo(f_expr, g_expr, x0, tol, niter)
# print(mensaje)
# print(resultados)
