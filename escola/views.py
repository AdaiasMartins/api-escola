from django.http import JsonResponse

def estudantes(request):
    if request.method == 'GET':
        estudante = {
            'id': 1,
            'nome': 'João',
            'idade': 20,
            'curso': 'Engenharia de Software'
        }
        return JsonResponse(estudante)
