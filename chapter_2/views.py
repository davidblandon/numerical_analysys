from django.shortcuts import render
from .methods.gauss_seidel import method_gauss_seidel
from .methods.jacobi import method_jacobi
from .methods.SOR import method_SOR
from numerical_analysys.export.toTxt import create_txt_download
    
import numpy as np
import ast

def home(request):
    return render(request, 'home.html')

def gauss_seidel(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            
            answer = request.POST.get('answer')
            message = request.POST.get('message')

            return create_txt_download(answer, message)
        

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
