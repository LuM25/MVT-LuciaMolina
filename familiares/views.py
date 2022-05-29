from django.shortcuts import render
from familiares.models import Relative



# Create your views here.
def relatives(request):
    relative_1 = Relative.objects.create(name ='Mariano', age = 25 , ocupation = 'Ing.', relationship = 'hermano' )
    relative_2 = Relative.objects.create(name ='Barbara', age = 29 , ocupation = 'Psicologa', relationship = 'prima' )
    relative_3 = Relative.objects.create(name ='Maida', age = 76 , ocupation = 'jubilada', relationship = 'abuela' )
    context = {'relative_1': relative_1, 'relative_2':relative_2, 'relative_3': relative_3 }
    return render (request, 'familiares.html', context = context)

