
from django.urls import path
from .views.segLineal import *


app_name = 'app_seguimiento'


urlpatterns = [

    path('listar', listarSeguimientoView.as_view(), name='listar_seguimiento'),
    path('listar/det_piscina/<int:pk>/', listarSeguimientoPiscinasView.as_view(), name='listar_seguimiento_det_piscina'),


]
