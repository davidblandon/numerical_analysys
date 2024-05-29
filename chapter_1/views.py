from django.shortcuts import render
from .methods.biseccion import method_biseccion
from .methods.newton import method_newton
from .methods.punto_fijo import method_punto_fijo
from .methods.raices_multiples import method_raices_multiples
from .methods.regla_falsa import method_regla_falsa
from .methods.secante import  method_secante
from numerical_analysys.export.toTxt import create_txt_download
import numpy as np
import sympy as sp
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import re

# Create your views here.

def home(request):
    return render(request, 'home.html')

def biseccion(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            answer = request.POST.get('answer')
            message = request.POST.get('message')
            return create_txt_download(answer, message)
        if 'graph' in request.POST:
            x = sp.symbols('x')
            message = request.POST.get('message')
            numero_float = float(message.split(" es una aproximación")[0])
            xi = float(request.POST.get('xi'))
            xs = float(request.POST.get('xs'))
            print(numero_float, xi, xs)
            funcion_str = request.POST.get('funcion')
            funcion = sp.sympify(funcion_str.replace('sympy.', ''), locals={'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 'pi': sp.pi})
            x_test = np.linspace(xi, xs, 1000)
            y_test = np.array([funcion.subs(x, val).evalf() for val in x_test])
            min_index = np.argmin(np.abs(y_test - numero_float))
            x_numero_float = x_test[min_index]  # Este es el x que buscamos

            # Evaluar la función en los puntos relevantes
            y_xi = funcion.subs(x, xi).evalf()
            y_xs = funcion.subs(x, xs).evalf()
            y_numero_float = numero_float  # Ya lo conocemos

            # Crear un rango de valores de x para evaluar la función
            x_vals = np.linspace(min(xi, xs, x_numero_float) - 1, max(xi, xs, x_numero_float) + 1, 400)
            y_vals = [funcion.subs(x, val).evalf() for val in x_vals]

            # Crear la figura para la gráfica
            plt.figure()
            plt.plot(x_vals, y_vals, label=f'f(x) = {funcion}')
            plt.scatter([xi, xs, x_numero_float], [y_xi, y_xs, y_numero_float], color='red')
            plt.title("Gráfica de la función")
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.legend()

            # Añadir anotaciones para cada punto
            plt.annotate(f'xi ({xi}, {y_xi:.2f})', (xi, y_xi), textcoords="offset points", xytext=(0,10), ha='center')
            plt.annotate(f'xs ({xs}, {y_xs:.2f})', (xs, y_xs), textcoords="offset points", xytext=(0,10), ha='center')
            plt.annotate(f'Punto aproximado ({x_numero_float:.2f}, {y_numero_float:.2f})', (x_numero_float, y_numero_float), textcoords="offset points", xytext=(0,10), ha='center')

            # Guardar la gráfica como una imagen
            image_path = 'numerical_analysys/static/images/graph.png'
            plt.savefig(image_path)
            plt.close()

            # Pasar la ruta de la imagen a la plantilla
            return render(request, 'biseccion.html', {'image_path': image_path})
        else:

            funcion = request.POST.get('funcion')
            xi = float(request.POST.get('xi'))
            xs = float(request.POST.get('xs'))
            tol = float(request.POST.get('tol'))
            iter = int(request.POST.get('iter'))
            answer,message = method_biseccion(funcion, xi, xs, tol, iter)

            view_data['funcion'] = funcion
            view_data['xi'] = xi
            view_data['xs'] = xs    
            view_data['tol'] = tol
            view_data['iter'] = iter
            if answer.empty:
                view_data['answer'] = 'No se encontró la solución'

            else:

                view_data['answer'] = answer.to_html()
                view_data['answer_raw'] = answer
                view_data['message'] = message

            return render(request, 'biseccion.html', {'view_data': view_data})
    else:

        return render(request, 'biseccion.html', {'view_data': view_data})

def newton(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            
            answer = request.POST.get('answer')
            message = request.POST.get('message')

            return create_txt_download(answer, message)
        
        if 'graph' in request.POST:
            x = sp.symbols('x')
            message = request.POST.get('message')
            numero_float = float(message.split(" es una aproximación")[0])
            x0 = float(request.POST.get('x0'))
            funcion_str = request.POST.get('funcion')

            funcion = sp.sympify(funcion_str, locals={'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 'pi': sp.pi, 'exp': sp.exp, 'log': sp.log, 'sqrt': sp.sqrt})

            xi = x0 - 5
            xs = x0 + 5

            # Crea un rango de valores de x para evaluar la función
            x_vals = np.linspace(xi, xs, 400)
            y_vals = [funcion.subs(x, val).evalf() for val in x_vals]

            # Valor de la función en x0
            y0 = funcion.subs(x, x0).evalf()

            # Crear la figura para la gráfica
            plt.figure()
            plt.plot(x_vals, y_vals, label=f'f(x) = {funcion}')
            plt.scatter([x0], [y0], color='red')  # Marcar el punto x0
            plt.scatter([x0], [numero_float], color='blue')  # Marcar el valor de numero_float en y
            plt.title("Gráfica de la función")
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.legend()

            # Añadir anotaciones para los puntos
            plt.annotate(f'x0 ({x0}, {y0:.2f})', (x0, y0), textcoords="offset points", xytext=(0,10), ha='center')
            plt.annotate(f'Número aproximado y ({x0}, {numero_float:.2f})', (x0, numero_float), textcoords="offset points", xytext=(0,-20), ha='center')

            # Guardar la gráfica como una imagen en el directorio adecuado
            image_path = 'numerical_analysys/static/images/graph.png'
            plt.savefig(image_path)
            plt.close()
        
            # Pasar la ruta de la imagen a la plantilla
            return render(request, 'biseccion.html', {'image_path': image_path})

        funcion = request.POST.get('funcion')
        x0 = float(request.POST.get('x0'))
        tol = float(request.POST.get('tol'))
        iter = int(request.POST.get('iter'))
        answer,message = method_newton(funcion, x0, tol, iter)

        view_data['funcion'] = funcion
        view_data['x0'] = x0    
        view_data['tol'] = tol
        view_data['iter'] = iter
        if answer.empty:
            view_data['answer'] = 'No se encontró la solución'

        else:

            view_data['answer'] = answer.to_html()
            view_data['answer_raw'] = answer
        view_data['message'] = message

        return render(request, 'newton.html', {'view_data': view_data})
    else:

        return render(request, 'newton.html', {'view_data': view_data})


def punto_fijo(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            
            answer = request.POST.get('answer')
            message = request.POST.get('message')

            return create_txt_download(answer, message)

        if 'graph' in request.POST:
            x = sp.symbols('x')
            message = request.POST.get('message')
            numero_float = float(message.split(" es una aproximación")[0])
            x0 = float(request.POST.get('x0'))
            f_funcion_str = request.POST.get('f_funcion')
            g_funcion_str = request.POST.get('g_funcion')

            print(f_funcion_str, g_funcion_str)

            f_funcion = sp.sympify(f_funcion_str, locals={'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 'pi': sp.pi, 'exp': sp.exp, 'log': sp.log, 'sqrt': sp.sqrt})
            g_funcion = sp.sympify(g_funcion_str, locals={'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 'pi': sp.pi, 'exp': sp.exp, 'log': sp.log, 'sqrt': sp.sqrt})

            # Establecer los límites alrededor de x0
            xi = x0 - 5
            xs = x0 + 5

            # Crear un rango de valores de x para evaluar las funciones
            x_vals = np.linspace(xi, xs, 400)
            f_y_vals = [f_funcion.subs(x, val).evalf() for val in x_vals]
            g_y_vals = [g_funcion.subs(x, val).evalf() for val in x_vals]

            # Crear la figura para la gráfica
            plt.figure()
            plt.plot(x_vals, f_y_vals, label=f'f(x) = {f_funcion}', color='blue')
            plt.plot(x_vals, g_y_vals, label=f'g(x) = {g_funcion}', color='green')
            plt.scatter([x0], [numero_float], color='red', zorder=5)  # Marcar el valor de numero_float en y, asumiendo que pertenece a f o g en x0
            plt.title("Gráfica de las funciones f y g")
            plt.xlabel('x')
            plt.ylabel('y')
            plt.legend()

            # Añadir anotaciones para el punto
            plt.annotate(f'Punto ({x0}, {numero_float:.2f})', (x0, numero_float), textcoords="offset points", xytext=(0,10), ha='center')

            # Guardar la gráfica como una imagen en el directorio adecuado
            image_path = 'numerical_analysys/static/images/graph.png'
            plt.savefig(image_path)
            plt.close()

            return render(request, 'punto_fijo.html', {'image_path': image_path})

        f_func= request.POST.get('f_func')
        g_func = request.POST.get('g_func')
        x0 = float(request.POST.get('x0'))
        tol = float(request.POST.get('tol'))
        iter = int(request.POST.get('iter'))
        answer, message = method_punto_fijo(f_func,g_func, x0, tol, iter)


        view_data['f_func'] = f_func
        view_data['g_func'] = g_func
        view_data['x0'] = x0    
        view_data['tol'] = tol
        view_data['iter'] = iter
        if answer.empty:
            view_data['answer'] = 'No se encontró la solución'

        else:

            view_data['answer'] = answer.to_html()
            view_data['answer_raw'] = answer
        view_data['message'] = message

        return render(request, 'punto_fijo.html', {'view_data': view_data})
    else:

        return render(request, 'punto_fijo.html', {'view_data': view_data})

def raices_multiples(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            
            answer = request.POST.get('answer')
            message = request.POST.get('message')

            return create_txt_download(answer, message)

        if 'graph' in request.POST:
            x = sp.symbols('x')
            message = request.POST.get('message')
            numero_float = float(message.split(" es una aproximación")[0])
            x0 = float(request.POST.get('x0'))
            funcion_str = request.POST.get('funcion')

            funcion = sp.sympify(funcion_str, locals={'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 'pi': sp.pi, 'exp': sp.exp, 'log': sp.log, 'sqrt': sp.sqrt})

            xi = x0 - 5
            xs = x0 + 5

            # Crea un rango de valores de x para evaluar la función
            x_vals = np.linspace(xi, xs, 400)
            y_vals = [funcion.subs(x, val).evalf() for val in x_vals]

            # Valor de la función en x0
            y0 = funcion.subs(x, x0).evalf()

            # Crear la figura para la gráfica
            plt.figure()
            plt.plot(x_vals, y_vals, label=f'f(x) = {funcion}')
            plt.scatter([x0], [y0], color='red')  # Marcar el punto x0
            plt.scatter([x0], [numero_float], color='blue')  # Marcar el valor de numero_float en y
            plt.title("Gráfica de la función")
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.legend()

            # Añadir anotaciones para los puntos
            plt.annotate(f'x0 ({x0}, {y0:.2f})', (x0, y0), textcoords="offset points", xytext=(0,10), ha='center')
            plt.annotate(f'Número aproximado y ({x0}, {numero_float:.2f})', (x0, numero_float), textcoords="offset points", xytext=(0,-20), ha='center')

            # Guardar la gráfica como una imagen en el directorio adecuado
            image_path = 'numerical_analysys/static/images/graph.png'
            plt.savefig(image_path)
            plt.close()
        
            # Pasar la ruta de la imagen a la plantilla
            return render(request, 'raices_multiples.html', {'image_path': image_path})
        
        funcion= request.POST.get('funcion')
        x0 = float(request.POST.get('x0'))
        m = float(request.POST.get('m'))
        tol = float(request.POST.get('tol'))
        niter = int(request.POST.get('iter'))
        answer, message = method_raices_multiples(funcion, x0, m, tol, niter)

        view_data['funcion'] = funcion
        view_data['x0'] = x0    
        view_data['tol'] = tol
        view_data['iter'] = niter
        view_data['m'] = m
        if answer.empty:
            view_data['answer'] = 'No se encontró la solución'

        else:

            view_data['answer'] = answer.to_html()
            view_data['answer_raw'] = answer
        view_data['message'] = message

        return render(request, 'raices_multiples.html', {'view_data': view_data})
    else:

        return render(request, 'raices_multiples.html', {'view_data': view_data})

def regla_falsa(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            
            answer = request.POST.get('answer')
            message = request.POST.get('message')

            return create_txt_download(answer, message)

        if 'graph' in request.POST:
            x = sp.symbols('x')
            message = request.POST.get('message')
            numero_float = float(re.search(r"c = ([\d\.]+)", "Convergencia alcanzada en la iteración 85: c = 1.3247156522332095").group(1))
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            funcion_str = request.POST.get('funcion')

            funcion = sp.sympify(funcion_str, locals={'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 'pi': sp.pi, 'exp': sp.exp, 'log': sp.log, 'sqrt': sp.sqrt})

            xi = min(a, b) - 5
            xs = max(a, b) + 5

            x_vals = np.linspace(xi, xs, 400)
            y_vals = [funcion.subs(x, val).evalf() for val in x_vals]

            # Evaluar la función en a, b y numero_float
            y_a = funcion.subs(x, a).evalf()
            y_b = funcion.subs(x, b).evalf()
            y_numero_float = funcion.subs(x, numero_float).evalf()

            # Crear la figura para la gráfica
            plt.figure()
            plt.plot(x_vals, y_vals, label=f'f(x) = {funcion}', color='blue')
            plt.scatter([a, b, numero_float], [y_a, y_b, y_numero_float], color='red')  # Marca los puntos a, b, y numero_float
            plt.title("Gráfica de la función f(x)")
            plt.xlabel('x')
            plt.ylabel('y')
            plt.legend()

            # Añadir anotaciones para los puntos
            plt.annotate(f'Punto a ({a}, {y_a:.2f})', (a, y_a), textcoords="offset points", xytext=(0,10), ha='center')
            plt.annotate(f'Punto b ({b}, {y_b:.2f})', (b, y_b), textcoords="offset points", xytext=(0,10), ha='center')
            plt.annotate(f'Punto ({numero_float}, {y_numero_float:.2f})', (numero_float, y_numero_float), textcoords="offset points", xytext=(0,-20), ha='center')

            # Guardar la gráfica como una imagen en el directorio adecuado
            image_path = 'numerical_analysys/static/images/graph.png'
            plt.savefig(image_path)
            plt.close()


            # Pasar la ruta de la imagen a la plantilla
            return render(request, 'regla_falsa.html', {'image_path': image_path})
        
        funcion= request.POST.get('funcion')
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        tol = float(request.POST.get('tol'))
        max_iter = int(request.POST.get('max_iter'))
        answer, message = method_regla_falsa(funcion, a, b, tol, max_iter)

        view_data['funcion'] = funcion
        view_data['a'] = a    
        view_data['tol'] = tol
        view_data['max_iter'] = max_iter
        view_data['b'] = b
        if answer.empty:
            view_data['answer'] = 'No se encontró la solución'

        else:

            view_data['answer'] = answer.to_html()
            view_data['answer_raw'] = answer
        view_data['message'] = message

        return render(request, 'regla_falsa.html', {'view_data': view_data})
    else:

        return render(request, 'regla_falsa.html', {'view_data': view_data})

def secante(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            
            answer = request.POST.get('answer')
            message = request.POST.get('message')

            return create_txt_download(answer, message)

        if 'graph' in request.POST:
            x = sp.symbols('x')
            message = request.POST.get('message')
            numero_float = float(message.split(" es una aproximación")[0])
            x0 = float(request.POST.get('x0'))
            x1 = float(request.POST.get('x1'))
            funcion_str = request.POST.get('funcion')

            funcion = sp.sympify(funcion_str, locals={'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 'pi': sp.pi, 'exp': sp.exp, 'log': sp.log, 'sqrt': sp.sqrt})

            # Definir los límites de la gráfica para incluir x0, x1
            xi = min(x0, x1) - 5
            xs = max(x0, x1) + 5

            # Crear un rango de valores de x para evaluar la función
            x_vals = np.linspace(xi, xs, 400)
            y_vals = [funcion.subs(x, val).evalf() for val in x_vals]

            # Evaluar la función en x0 y x1
            y_x0 = funcion.subs(x, x0).evalf()
            y_x1 = funcion.subs(x, x1).evalf()

            # Intentar encontrar un x tal que f(x) sea igual a numero_float
            # Usaremos np.linspace para explorar un rango más amplio y buscar un x que satisfaga f(x) = numero_float
            x_range = np.linspace(xi, xs, 1000)
            x_soluciones = []
            for x_val in x_range:
                if abs(funcion.subs(x, x_val).evalf() - numero_float) < 0.01:  # Umbral de tolerancia
                    x_soluciones.append(x_val)

            # Crear la figura para la gráfica
            plt.figure()
            plt.plot(x_vals, y_vals, label=f'f(x) = {funcion}', color='blue')
            plt.scatter([x0, x1], [y_x0, y_x1], color='red')  # Marca los puntos x0 y x1
            for x_sol in x_soluciones:
                plt.scatter([x_sol], [numero_float], color='orange')  # Marca los puntos donde f(x) = numero_float

            plt.title("Gráfica de la función f(x)")
            plt.xlabel('x')
            plt.ylabel('y')
            plt.legend()

            # Añadir anotaciones para los puntos
            plt.annotate(f'x0 ({x0}, {y_x0:.2f})', (x0, y_x0), textcoords="offset points", xytext=(0,10), ha='center')
            plt.annotate(f'x1 ({x1}, {y_x1:.2f})', (x1, y_x1), textcoords="offset points", xytext=(0,10), ha='center')
            for x_sol in x_soluciones:
                plt.annotate(f'x para f(x)={numero_float:.2f} ({x_sol:.2f}, {numero_float:.2f})', (x_sol, numero_float), textcoords="offset points", xytext=(0,-20), ha='center')

            # Guardar la gráfica como una imagen en el directorio adecuado
            image_path = 'numerical_analysys/static/images/graph.png'
            plt.savefig(image_path)
            plt.close()

            return render(request, 'secante.html', {'image_path': image_path})

        funcion= request.POST.get('funcion')
        x0 = float(request.POST.get('x0'))
        x1 = float(request.POST.get('x1'))
        tol = float(request.POST.get('tol'))
        iter = int(request.POST.get('iter'))
        answer, message = method_secante(funcion, x0, x1, tol, iter)

        view_data['funcion'] = funcion
        view_data['x0'] = x0    
        view_data['tol'] = tol
        view_data['iter'] = iter
        view_data['x1'] = x1
        if answer.empty:
            view_data['answer'] = 'No se encontró la solución'

        else:

            view_data['answer'] = answer.to_html()
            view_data['answer_raw'] = answer
        view_data['message'] = message

        return render(request, 'secante.html', {'view_data': view_data})
    else:

        return render(request, 'secante.html', {'view_data': view_data})