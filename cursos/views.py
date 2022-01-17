from django.shortcuts import render
from django.shortcuts import redirect
from .models import Cursos, Aulas



def home(request):
    if request.session.get('usuario'):
        cursos = Cursos.objects.all()
        request_usuario = request.session.get('usuario')
        return render(request, 'home.html', {'cursos': cursos, 'request_usuario': request_usuario})
    else:
        return redirect('/auth/login/?status=2')

def curso(request, id):
    if request.session.get('usuario'):
        v_curso = Cursos.objects.get(id = id)
        aulas = Aulas.objects.filter(curso = v_curso)
        return render(request, 'curso.html', {'aulas': aulas})
    else:
        return redirect('/auth/login/?status=2')
    

def aula(request, id):
    if request.session.get('usuario'):
        aula = Aulas.objects.get(id = id)
        return render(request, 'aula.html', {'aula': aula})
    else:
        return redirect('/auth/login/?status=2')
