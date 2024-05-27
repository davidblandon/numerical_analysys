import sympy as sp
import pandas as pd

def raices_multiples(f_expr, x0, m, tol, niter):
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr, 'numpy')
    df = sp.lambdify(x, sp.diff(f_expr, x), 'numpy')

    resultados = pd.DataFrame(columns=['Iteración', 'xn', 'f(xn)', 'df(xn)', 'Error'])

    xn = x0
    iteracion = 0
    error = tol + 1

    while error > tol and iteracion < niter:
        f_xn = f(xn)
        df_xn = df(xn)

        if df_xn == 0:
            mensaje = "Derivada cero en el punto, no se puede continuar."
            return resultados, mensaje
        
        xn_new = xn - m * f_xn / df_xn
        error = abs(xn_new - xn)
        
        resultados.loc[iteracion] = [iteracion, xn_new, f_xn, df_xn, error]
        
        xn = xn_new
        iteracion += 1

    mensaje = f'{xn} es una aproximación de una raíz de f(x) con una tolerancia de {tol}' if error < tol else "Fracasó en alcanzar la convergencia"
    return resultados, mensaje

x = sp.symbols('x')
f_expr = (x - 2)**3 + 1
x0 = 3.0  # Punto inicial
m = 3
tol = 1e-8
niter = 20

resultados, mensaje = raices_multiples(f_expr, x0, m, tol, niter)
print(mensaje)
print(resultados)

