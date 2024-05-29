import sympy as sp
import pandas as pd

def method_newton(f_expr, x0, tol, niter):
    x = sp.symbols('x')
    f_expr = sp.sympify(f_expr)  # Convert the string into a sympy expression
    f = sp.lambdify(x, f_expr, 'numpy')  # Convert the sympy expression f into an evaluable function
    df = sp.lambdify(x, sp.diff(f_expr, x), 'numpy')  # Convert the derivative of f

    resultados = pd.DataFrame(columns=['Iteración', 'xn', 'f(xn)', 'df(xn)', 'Error'])
    xn = x0
    error = tol + 1  # Iniciar error mayor que la tolerancia para entrar al bucle

    iteracion = 0
    while error > tol and iteracion < niter:
        f_xn = f(xn)
        df_xn = df(xn)

        if df_xn == 0:
            mensaje = f'La derivada se hizo cero en x = {xn}. No se puede continuar.'
            return resultados, mensaje
        
        xn_new = xn - f_xn / df_xn
        error = abs(xn_new - xn)

        resultados.loc[iteracion] = [iteracion, xn_new, f_xn, df_xn, error]
        
        if f_xn == 0:
            mensaje = f'{xn_new} es raíz de f(x)'
            return resultados, mensaje
        
        xn = xn_new
        iteracion += 1

    if error < tol:
        mensaje = f'{xn} es una aproximación de una raíz de f(x) con una tolerancia de {tol}'
    else:
        mensaje = f'Fracasó en {niter} iteraciones'

    return resultados, mensaje

# Ejemplo de uso de la función
# x = sp.symbols('x')
# f_expr = (sp.exp(x)/x) + 3  # Esta es la función f
# x0 = -1
# tol = 1e-8
# niter = 100

# resultados, mensaje = newton(f_expr, x0, tol, niter)
# print(mensaje)
# print(resultados)
