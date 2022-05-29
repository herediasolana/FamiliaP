from AppFamiliares.views import ver_familiares
from django.urls import path


urlpatterns = [
    path('', ver_familiares, name='Familiares'),
]