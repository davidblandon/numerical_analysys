import numpy as np
import sympy as sp
import pandas as pd

def method_biseccion(f_expr, xi, xs, tol, niter):
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr, modules={'numpy': np, 'sympy': sp})  # Convertir la expresión a una función evaluable
    fi = f(xi)
    fs = f(xs)

    resultados = pd.DataFrame(columns=['Iteración', 'xi', 'xs', 'xm', 'f(xm)', 'Error'])

    if fi == 0:
        mensaje = f'{xi} es raíz de f(x)'
        return resultados, mensaje
    elif fs == 0:
        mensaje = f'{xs} es raíz de f(x)'
        return resultados, mensaje
    elif fs * fi < 0:
        c = 0
        xm = (xi + xs) / 2
        fe = f(xm)
        error = tol + 1

        while error > tol and fe != 0 and c < niter:
            resultados.loc[c] = [c, xi, xs, xm, fe, error]
            if fi * fe < 0:
                xs = xm
                fs = f(xs)
            else:
                xi = xm
                fi = f(xi)
                
            xa = xm
            xm = (xi + xs) / 2
            fe = f(xm)
            error = abs(xm - xa)
            c += 1
        
        resultados.loc[c] = [c, xi, xs, xm, fe, error]  # Asegúrese de registrar la última iteración

        if fe == 0:
            mensaje = f'{xm} es raíz de f(x)'
        elif error < tol:
            mensaje = f'{xm} es una aproximación a una raíz de f(x) con una tolerancia = {tol}'
        else:
            mensaje = f'Fracasó en {niter} iteraciones'
        return resultados, mensaje
    else:
        mensaje = 'El intervalo es inadecuado'
        return resultados, mensaje

# Ejemplo de uso de la función
# Ejemplo de uso de la función
# x = sp.symbols('x')
# xi = -4
# xs = -0.1
# tol = 0.0001
# niter = 100
# funcion = x**2 - 5*x + 6*sp.sin(x)

# resultados, mensaje = method_biseccion(funcion, xi, xs, tol, niter)

# print(mensaje)
# print(resultados)