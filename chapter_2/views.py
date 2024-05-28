from django.shortcuts import render
from .methods.gauss_seidel import method_gauss_seidel
from .methods.jacobi import method_jacobi
from .methods.SOR import method_SOR

def home(request):
    return render(request, 'home.html')

def gauss_seidel(request):
    view_data = {}
    if request.method == 'POST':

        a= request.POST.get('a')
        b = request.POST.get('b')
        x0 = request.POST.get('x0')
        tol = request.POST.get('tol')
        iter = request.POST.get('iter')
        answer = method_gauss_seidel(a,b ,x0, tol, iter)

        view_data['a'] = a
        view_data['b'] = b    
        view_data['tol'] = tol
        view_data['iter'] = iter
        view_data['x0'] = x0
        view_data['answer'] = answer

        return render(request, 'gauss_seidel.html', {'view_data': view_data})
    else:

        return render(request, 'gauss_seidel.html', {'view_data': view_data})

def jacobi(request):
    view_data = {}
    if request.method == 'POST':

        a= request.POST.get('a')
        b = request.POST.get('b')
        x0 = request.POST.get('x0')
        tol = request.POST.get('tol')
        iter = request.POST.get('iter')
        answer = method_jacobi(a,b ,x0, tol, iter)

        view_data['a'] = a
        view_data['b'] = b    
        view_data['tol'] = tol
        view_data['iter'] = iter
        view_data['x0'] = x0
        view_data['answer'] = answer

        return render(request, 'jacobi.html', {'view_data': view_data})
    else:

        return render(request, 'jacobi.html', {'view_data': view_data})

def sor(request):
    view_data = {}
    if request.method == 'POST':

        a= request.POST.get('a')
        b = request.POST.get('b')
        x0 = request.POST.get('x0')
        tol = request.POST.get('tol')
        iter = request.POST.get('iter')
        w = request.POST.get('w')
        answer = method_jacobi(a,b ,x0, tol, iter,w)

        view_data['a'] = a
        view_data['b'] = b    
        view_data['tol'] = tol
        view_data['iter'] = iter
        view_data['x0'] = x0
        view_data['w'] = w
        view_data['answer'] = answer

        return render(request, 'sor.html', {'view_data': view_data})
    else:

        return render(request, 'sor.html', {'view_data': view_data})
