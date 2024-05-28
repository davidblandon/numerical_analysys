import sympy as sp
import pandas as pd

def method_regla_falsa(f_expr, a, b, tol, max_iter):
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr, 'numpy')
    
    resultados = pd.DataFrame(columns=['Iteración', 'a', 'b', 'c', 'f(c)', 'Error'])
    fa = f(a)
    fb = f(b)
    
    if fa == 0:
        return resultados, f'{a} es raíz exacta de f(x)'
    if fb == 0:
        return resultados, f'{b} es raíz exacta de f(x)'
    if fa * fb > 0:
        return resultados, "El intervalo no cumple la condición de cambio de signo."
    
    iteraciones = 0
    while iteraciones < max_iter:
        denominador = (fb - fa)
        if denominador == 0:
            return resultados, "División por cero en el cálculo de c"
        c = (a * fb - b * fa) / denominador
        fc = f(c)
        
        resultados.loc[iteraciones] = [iteraciones, a, b, c, fc, abs(fc)]
        
        if abs(fc) < tol:
            return resultados, f'Convergencia alcanzada en la iteración {iteraciones}: c = {c}'
        
        if sp.sign(fc) == sp.sign(fa):
            a = c
            fa = fc
        else:
            b = c
            fb = fc
        
        iteraciones += 1
        
    return resultados, f'Convergencia no alcanzada en {max_iter} iteraciones. Mejor aproximación: {c}'

# Ejemplo de uso
# x = sp.symbols('x')
# f_expr = x**3 - x - 1
# a = 1
# b = 5
# tol = 1e-5
# max_iter = 100

# resultados, mensaje = regla_falsa(f_expr, a, b, tol, max_iter)
# print(mensaje)
# print(resultados)
