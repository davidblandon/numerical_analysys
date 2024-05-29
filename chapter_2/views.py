from django.shortcuts import render
from .methods.gauss_seidel import method_gauss_seidel
from .methods.jacobi import method_jacobi
from .methods.SOR import method_SOR
from numerical_analysys.export.toTxt import create_txt_download
    
import numpy as np
import sympy as sp
from sympy import symbols
import ast
import matplotlib.pyplot as plt
import re
from ast import literal_eval

def home(request):
    return render(request, 'home.html')

def gauss_seidel(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            
            answer = request.POST.get('answer')
            message = request.POST.get('message')
            print(message)

            return create_txt_download(answer, message)
        
        if 'graph' in request.POST:

            message = request.POST.get('message')
            answer = re.search(r'\[([ -\.\de]+)\]', message).group(1)
            A_str = request.POST.get('a')
            b_str = request.POST.get('b')
            A_str = A_str.replace('[', '').replace(']', '').split()
            dim = int(len(A_str)**0.5)
            A = np.array(A_str, dtype=float).reshape(dim, dim)

            answer = answer.replace('[', '').replace(']', '').split()
            x = np.array(answer, dtype=float)

            b_str = b_str.replace('[', '').replace(']', '').split()
            b = np.array(b_str, dtype=float)

            # Crear la figura y los ejes
            plt.figure(figsize=(8, 8))

            # Graficar los vectores de la matriz A
            for i in range(dim):
                plt.arrow(0, 0, A[i, 0], A[i, 1], head_width=0.5, head_length=0.5, fc='blue', ec='blue', label=f'A[:, {i}]')

            # Graficar el vector b
            plt.arrow(0, 0, b[0], b[1], head_width=0.5, head_length=0.5, fc='green', ec='green', label='b')

            # Resaltar la solución del sistema
            plt.scatter(x[0], x[1], color='red', zorder=5)
            plt.text(x[0], x[1], f'({x[0]:.2f}, {x[1]:.2f})', fontsize=12, verticalalignment='bottom')

            # Configurar los ejes y leyendas
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.grid(color='gray', linestyle='--', linewidth=0.5)
            plt.legend()
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Vectores del sistema Ax = b')
            plt.xlim(-20, 20)
            plt.ylim(-20, 20)

            # Guardar la gráfica en la ruta especificada
            image_path = 'numerical_analysys/static/images/graph.png'
            plt.savefig(image_path)
            plt.close()

            return render(request, 'gauss_seidel.html', {'image_path': image_path})


        a= np.array(ast.literal_eval(request.POST.get('a')), dtype=float)
        b = np.array(ast.literal_eval(request.POST.get('b')), dtype=float)
        x0 = np.array(ast.literal_eval(request.POST.get('x0')),dtype=float)
        tol = float(request.POST.get('tol'))
        iter = int(request.POST.get('iter'))
        answer, message = method_gauss_seidel(a,b ,x0, tol, iter)

        view_data['a'] = a
        view_data['b'] = b    
        view_data['tol'] = tol
        view_data['iter'] = iter
        view_data['x0'] = x0
        if answer.empty:
            view_data['answer'] = 'No se encontró la solución'

        else:

            view_data['answer'] = answer.to_html()
            view_data['answer_raw'] = answer
        view_data['message'] = message


        return render(request, 'gauss_seidel.html', {'view_data': view_data})
    else:

        return render(request, 'gauss_seidel.html', {'view_data': view_data})

def jacobi(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            
            answer = request.POST.get('answer')
            message = request.POST.get('message')

            return create_txt_download(answer, message)
        
        if 'graph' in request.POST:
            message = request.POST.get('message')
            answer = re.search(r'\[([ -\.\de]+)\]', message).group(1)
            A_str = request.POST.get('a')
            b_str = request.POST.get('b')
            A_str = A_str.replace('[', '').replace(']', '').split()
            dim = int(len(A_str)**0.5)
            A = np.array(A_str, dtype=float).reshape(dim, dim)

            answer = answer.replace('[', '').replace(']', '').split()
            x = np.array(answer, dtype=float)

            b_str = b_str.replace('[', '').replace(']', '').split()
            b = np.array(b_str, dtype=float)

            # Crear la figura y los ejes
            plt.figure(figsize=(8, 8))

            # Graficar los vectores de la matriz A
            for i in range(dim):
                plt.arrow(0, 0, A[i, 0], A[i, 1], head_width=0.5, head_length=0.5, fc='blue', ec='blue', label=f'A[:, {i}]')

            # Graficar el vector b
            plt.arrow(0, 0, b[0], b[1], head_width=0.5, head_length=0.5, fc='green', ec='green', label='b')

            # Resaltar la solución del sistema
            plt.scatter(x[0], x[1], color='red', zorder=5)
            plt.text(x[0], x[1], f'({x[0]:.2f}, {x[1]:.2f})', fontsize=12, verticalalignment='bottom')

            # Configurar los ejes y leyendas
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.grid(color='gray', linestyle='--', linewidth=0.5)
            plt.legend()
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Vectores del sistema Ax = b')
            plt.xlim(-20, 20)
            plt.ylim(-20, 20)

            # Guardar la gráfica en la ruta especificada
            image_path = 'numerical_analysys/static/images/graph.png'
            plt.savefig(image_path)
            plt.close()

            return render(request, 'jacobi.html', {'image_path': image_path})

        a= np.array(ast.literal_eval(request.POST.get('a')), dtype=float)
        b = np.array(ast.literal_eval(request.POST.get('b')), dtype=float)
        x0 = np.array(ast.literal_eval(request.POST.get('x0')), dtype=float)
        tol = float(request.POST.get('tol'))
        iter = int(request.POST.get('iter'))
        answer, message = method_jacobi(a,b ,x0, tol, iter)

        view_data['a'] = a
        view_data['b'] = b    
        view_data['tol'] = tol
        view_data['iter'] = iter
        view_data['x0'] = x0
        if answer.empty:
            view_data['answer'] = 'No se encontró la solución'

        else:

            view_data['answer'] = answer.to_html()
            view_data['answer_raw'] = answer
        view_data['message'] = message


        return render(request, 'jacobi.html', {'view_data': view_data})
    else:

        return render(request, 'jacobi.html', {'view_data': view_data})

def sor(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            
            answer = request.POST.get('answer')
            message = request.POST.get('message')

            return create_txt_download(answer, message)
        
        if 'graph' in request.POST:
            message = request.POST.get('message')
            answer = re.search(r'\[([ -\.\de]+)\]', message).group(1)
            A_str = request.POST.get('a')
            b_str = request.POST.get('b')
            A_str = A_str.replace('[', '').replace(']', '').split()
            dim = int(len(A_str)**0.5)
            A = np.array(A_str, dtype=float).reshape(dim, dim)

            answer = answer.replace('[', '').replace(']', '').split()
            x = np.array(answer, dtype=float)

            b_str = b_str.replace('[', '').replace(']', '').split()
            b = np.array(b_str, dtype=float)

            # Crear la figura y los ejes
            plt.figure(figsize=(8, 8))

            # Graficar los vectores de la matriz A
            for i in range(dim):
                plt.arrow(0, 0, A[i, 0], A[i, 1], head_width=0.5, head_length=0.5, fc='blue', ec='blue', label=f'A[:, {i}]')

            # Graficar el vector b
            plt.arrow(0, 0, b[0], b[1], head_width=0.5, head_length=0.5, fc='green', ec='green', label='b')

            # Resaltar la solución del sistema
            plt.scatter(x[0], x[1], color='red', zorder=5)
            plt.text(x[0], x[1], f'({x[0]:.2f}, {x[1]:.2f})', fontsize=12, verticalalignment='bottom')

            # Configurar los ejes y leyendas
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.grid(color='gray', linestyle='--', linewidth=0.5)
            plt.legend()
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Vectores del sistema Ax = b')
            plt.xlim(-20, 20)
            plt.ylim(-20, 20)

            # Guardar la gráfica en la ruta especificada
            image_path = 'numerical_analysys/static/images/graph.png'
            plt.savefig(image_path)
            plt.close()

            return render(request, 'sor.html', {'image_path': image_path})

        a= np.array(ast.literal_eval(request.POST.get('a')), dtype=float)
        b = np.array(ast.literal_eval(request.POST.get('b')), dtype=float)
        x0 = np.array(ast.literal_eval(request.POST.get('x0')), dtype=float)
        tol = float(request.POST.get('tol'))
        iter = int(request.POST.get('iter'))
        w = float(request.POST.get('w'))
        answer, message = method_jacobi(a,b ,x0, tol, iter,w)

        view_data['a'] = a
        view_data['b'] = b    
        view_data['tol'] = tol
        view_data['iter'] = iter
        view_data['x0'] = x0
        view_data['w'] = w
        if answer.empty:
            view_data['answer'] = 'No se encontró la solución'

        else:

            view_data['answer'] = answer.to_html()
            view_data['answer_raw'] = answer
        view_data['message'] = message


        return render(request, 'sor.html', {'view_data': view_data})
    else:

        return render(request, 'sor.html', {'view_data': view_data})
