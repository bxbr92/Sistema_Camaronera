
from django.urls import path
from .views.factura import *


app_name = 'app_factura'


urlpatterns = [

    path('listar', listarFacturaView.as_view(), name='listar_factura'),
    path('crear', crearFacturaView.as_view(), name='crear_factura'),
    path('editar/<int:pk>/', editarFacturaView.as_view(), name='editar_factura'),
    path('reporte/pdf/<int:pk>/', SaleInvoicePdfView.as_view(), name='factuta_pdf'),


]
