from django.shortcuts import render

def Indexa(request):
    return render(request, 'base.html', {
        'Estudiantes': 'Hola',
        'Mensaje': 'Este es un hola'
    })