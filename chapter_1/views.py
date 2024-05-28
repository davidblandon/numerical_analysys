from django.shortcuts import render
from .methods.biseccion import method_biseccion
from .methods.newton import method_newton
from .methods.punto_fijo import method_punto_fijo
from .methods.raices_multiples import method_raices_multiples
from .methods.regla_falsa import method_regla_falsa
from .methods.secante import  method_secante

# Create your views here.

def home(request):
    return render(request, 'home.html')

def biseccion(request):
    view_data = {}
    if request.method == 'POST':

        funcion = request.POST.get('funcion')
        xi = request.POST.get('xi')
        xs = request.POST.get('xs')
        tol = request.POST.get('tol')
        iter = request.POST.get('iter')
        answer = method_biseccion(funcion, xi, xs, tol, iter)

        view_data['funcion'] = funcion
        view_data['xi'] = xi
        view_data['xs'] = xs    
        view_data['tol'] = tol
        view_data['iter'] = iter
        view_data['answer'] = answer

        return render(request, 'biseccion.html', {'view_data': view_data})
    else:

        return render(request, 'biseccion.html', {'view_data': view_data})

def newton(request):
    view_data = {}
    if request.method == 'POST':

        funcion = request.POST.get('funcion')
        x0 = request.POST.get('x0')
        tol = request.POST.get('tol')
        iter = request.POST.get('iter')
        answer = method_newton(funcion, x0, tol, iter)

        view_data['funcion'] = funcion
        view_data['x0'] = x0    
        view_data['tol'] = tol
        view_data['iter'] = iter
        view_data['answer'] = answer

        return render(request, 'newton.html', {'view_data': view_data})
    else:

        return render(request, 'newton.html', {'view_data': view_data})


def punto_fijo(request):
    view_data = {}
    if request.method == 'POST':

        f_func= request.POST.get('f_func')
        g_func = request.POST.get('g_func')
        x0 = request.POST.get('x0')
        tol = request.POST.get('tol')
        iter = request.POST.get('iter')
        answer = method_punto_fijo(f_func,g_func, x0, tol, iter)


        view_data['f_func'] = f_func
        view_data['g_func'] = g_func
        view_data['x0'] = x0    
        view_data['tol'] = tol
        view_data['iter'] = iter
        view_data['answer'] = answer

        return render(request, 'punto_fijo.html', {'view_data': view_data})
    else:

        return render(request, 'punto_fijo.html', {'view_data': view_data})

def raices_multiples(request):
    view_data = {}
    if request.method == 'POST':

        funcion= request.POST.get('funcion')
        x0 = request.POST.get('x0')
        m = request.POST.get('m')
        tol = request.POST.get('tol')
        iter = request.POST.get('iter')
        answer = method_raices_multiples(funcion, x0, m, tol, iter)

        view_data['funcion'] = funcion
        view_data['x0'] = x0    
        view_data['tol'] = tol
        view_data['iter'] = iter
        view_data['m'] = m
        view_data['answer'] = answer

        return render(request, 'raices_multiples.html', {'view_data': view_data})
    else:

        return render(request, 'raices_multiples.html', {'view_data': view_data})

def regla_falsa(request):
    view_data = {}
    if request.method == 'POST':

        funcion= request.POST.get('funcion')
        a = request.POST.get('a')
        b = request.POST.get('b')
        tol = request.POST.get('tol')
        max_iter = request.POST.get('max_iter')
        answer = method_regla_falsa(funcion, a, b, tol, iter)

        view_data['funcion'] = funcion
        view_data['a'] = a    
        view_data['tol'] = tol
        view_data['max_iter'] = max_iter
        view_data['b'] = b
        view_data['answer'] = answer

        return render(request, 'regla_falsa.html', {'view_data': view_data})
    else:

        return render(request, 'regla_falsa.html', {'view_data': view_data})

def secante(request):
    view_data = {}
    if request.method == 'POST':

        funcion= request.POST.get('funcion')
        x0 = request.POST.get('x0')
        x1 = request.POST.get('x1')
        tol = request.POST.get('tol')
        iter = request.POST.get('iter')
        answer = method_secante()

        view_data['funcion'] = funcion
        view_data['x0'] = x0    
        view_data['tol'] = tol
        view_data['iter'] = iter
        view_data['x1'] = x1
        view_data['answer'] = answer

        return render(request, 'secante.html', {'view_data': view_data})
    else:

        return render(request, 'secante.html', {'view_data': view_data})