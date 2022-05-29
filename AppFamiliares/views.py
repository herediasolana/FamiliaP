from django.shortcuts import render
from AppFamiliares.models import Familiares


# Create your views here.

def ver_familiares(request):
        familiar=Familiares.objects.all()
        context= {'familiar': familiar}
        return render(request, 'familiares.html', context=context)