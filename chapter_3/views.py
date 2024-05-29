from django.shortcuts import render
from .methods.Lagrange import method_lagrange
from numerical_analysys.export.toTxt import create_txt_download
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
        

        x= np.array(ast.literal_eval(request.POST.get('x')), dtype=float)
        y = np.array(ast.literal_eval(request.POST.get('y')), dtype=float)

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
