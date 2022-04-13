
from django.urls import path
from .views.dieta import *

app_name = 'app_dieta'

urlpatterns = [

    path('listar/anio/', listarDietaAnioPrincipalView.as_view(), name='principal_anio'),
    path('crear/anio/', crearAnioDietaView.as_view(), name='crear_anio_dieta'),

    #path('listar/mes/', listarDietaMesPrincipalView.as_view(), name='principal_mes'),
    path('listar/mes/<int:anio>/', listaDietas, name='principal_mes'),
    path('dieta/crear/mes/', crearMesDietaView.as_view(), name='crear_mes_dieta'),

    #path('listar/dia/<int:pk>/', listarDietaDiaPrincipalView.as_view(), name='principal_dia'),
    path('listar/dia/<int:pk>/', listarDias, name='principal_dia'),
    #path('crear/dia/<int:pk>/', crearDiaDieta, name='crear_dia_dieta'),
    path('crear/dia/<int:pk>/', crearDiaDietaView.as_view(), name='crear_dia_dieta'),
    #path('crear/dia/edit/', modificarDietas, name='modificar_dieta'),
    path('editar/dia/<int:pk>/', editarDiaDietaView.as_view(), name='modificar_dieta'),

    #path('dieta/crear/dia/registro/', crearRegistroDiaDietaView.as_view(), name='crear_registro_dia'),
    path('reporte_dieta/<int:pk>/', ListarDietaPDF.as_view(), name='reporte_dieta'),

    # PARA LAS DESCIPCIONES DE LAS DIETAS
    path('listar_desc_dieta/', listarDescripcionDietaView.as_view(), name='listar_descripcion_dieta'),
    path('crear_desc_dieta/', crearDescripcionDietaView.as_view(), name='crear_descripcion_dieta'),
    path('editar_desc_dieta/<int:pk>/', actualizarDescripcionDietaView.as_view(), name='editar_descripcion_dieta'),
    path('eliminar_desc_dieta/<int:pk>/', eliminarDescripcionDietaView.as_view(), name='eliminar_descripcion_dieta'),

]