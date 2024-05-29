from django.shortcuts import render
from .methods.Lagrange import method_lagrange
from .methods.newton_interpolante import method_newton_interpolante
from numerical_analysys.export.toTxt import create_txt_download
from .methods.vandermonde import method_vandermonde
from .methods.spline_lineal import method_spline_lineal
from .methods.spline_cubico import method_spline_cubico
import numpy as np
import ast

def home(request):
    return render(request, 'home.html')

def lagrange(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            
            answer = request.POST.get('answer')
            message = request.POST.get('message')

            return create_txt_download(answer, message)
        
        print(request.POST.get('x'))
        print(request.POST.get('y'))
        x= np.array(ast.literal_eval(request.POST.get('x')), dtype=float)
        y = np.array(ast.literal_eval(request.POST.get('y')), dtype=float)

        answer, message = method_lagrange(x,y)

        view_data['x'] = x
        view_data['y'] = y    

        if answer.empty:
            view_data['answer'] = 'No se encontró la solución'

        else:

            view_data['answer'] = answer.to_html()
            view_data['answer_raw'] = answer
        view_data['message'] = message


        return render(request, 'lagrange.html', {'view_data': view_data})
    else:

        return render(request, 'lagrange.html', {'view_data': view_data})

def newton_interpolante(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            
            answer = request.POST.get('answer')
            message = request.POST.get('message')

            return create_txt_download(answer, message)
        
        print(request.POST.get('x'))
        print(request.POST.get('y'))
        x= np.array(ast.literal_eval(request.POST.get('x')), dtype=float)
        y = np.array(ast.literal_eval(request.POST.get('y')), dtype=float)

        answer, message = method_newton_interpolante(x,y)

        view_data['x'] = x
        view_data['y'] = y    

        if answer.empty:
            view_data['answer'] = 'No se encontró la solución'

        else:

            view_data['answer'] = answer.to_html()
            view_data['answer_raw'] = answer
        view_data['message'] = message


        return render(request, 'newton_interpolante.html', {'view_data': view_data})
    else:

        return render(request, 'newton_interpolante.html', {'view_data': view_data})

def vandermonde(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            
            answer = request.POST.get('answer')
            message = request.POST.get('message')

            return create_txt_download(answer, message)
        
        print(request.POST.get('x'))
        print(request.POST.get('y'))
        x= np.array(ast.literal_eval(request.POST.get('x')), dtype=float)
        y = np.array(ast.literal_eval(request.POST.get('y')), dtype=float)
        degree = int(request.POST.get('degree'))

        answer, message = method_vandermonde(x,y,degree)

        view_data['x'] = x
        view_data['y'] = y   
        view_data['degree'] = degree   


        if answer.empty:
            view_data['answer'] = 'No se encontró la solución'

        else:

            view_data['answer'] = answer.to_html()
            view_data['answer_raw'] = answer
        view_data['message'] = message


        return render(request, 'vandermonde.html', {'view_data': view_data})
    else:

        return render(request, 'vandermonde.html', {'view_data': view_data})

def spline_lineal(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            
            answer = request.POST.get('answer')
            message = request.POST.get('message')

            return create_txt_download(answer, message)
        
        print(request.POST.get('x'))
        print(request.POST.get('y'))
        x= np.array(ast.literal_eval(request.POST.get('x')), dtype=float)
        y = np.array(ast.literal_eval(request.POST.get('y')), dtype=float)


        answer, message = method_spline_lineal(x,y)

        view_data['x'] = x
        view_data['y'] = y   


        if answer.empty:
            view_data['answer'] = 'No se encontró la solución'

        else:

            view_data['answer'] = answer.to_html()
            view_data['answer_raw'] = answer
        view_data['message'] = message


        return render(request, 'spline_lineal.html', {'view_data': view_data})
    else:

        return render(request, 'spline_lineal.html', {'view_data': view_data})

def spline_cubico(request):
    view_data = {}
    if request.method == 'POST':
        if 'download' in request.POST:
            
            answer = request.POST.get('answer')
            message = request.POST.get('message')

            return create_txt_download(answer, message)
        
        print(request.POST.get('x'))
        print(request.POST.get('y'))
        x= np.array(ast.literal_eval(request.POST.get('x')), dtype=float)
        y = np.array(ast.literal_eval(request.POST.get('y')), dtype=float)


        answer, message = method_spline_cubico(x,y)

        view_data['x'] = x
        view_data['y'] = y   


        if answer.empty:
            view_data['answer'] = 'No se encontró la solución'

        else:

            view_data['answer'] = answer.to_html()
            view_data['answer_raw'] = answer
        view_data['message'] = message


        return render(request, 'spline_cubico.html', {'view_data': view_data})
    else:

        return render(request, 'spline_cubico.html', {'view_data': view_data})
