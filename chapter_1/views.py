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
            message = request.POST.get('messaje')

            return create_txt_download(answer, message)
        

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