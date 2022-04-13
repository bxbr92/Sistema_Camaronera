
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from app_empresa.app_reg_empresa.models import Piscinas
from app_stock.app_detalle_stock.models import Producto_Stock



# METODO PARA LISTAR LA VENTANA PRINCIPAL DEL SEGUIMIENTO
class listarSeguimientoView(ListView):
    model = Piscinas
    template_name = 'app_segLineal/segLineal_principal.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Producto_Stock.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # defino el dicionario para enviar variables a mi plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Seguimiento Lineal'
        context['seguimiento'] = Piscinas.objects.all()
        context['piscinas'] = Piscinas.objects.all()
        return context


# VENTANA PAR LISTAR EL SEGUIMIENTO POR DETALLES DE BUSQUEDA EJEMPLO: ID
class listarSeguimientoPiscinasView(ListView):
    model = Piscinas
    template_name = 'app_segLineal/segLineal_detalle.html'

    def get_queryset(self):
        return Piscinas.objects.filter(id=self.kwargs['pk'])

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Piscinas.objects.get(id=self.kwargs['pk']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # defino el dicionario para enviar variables a mi plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Kardex Stock Productos PSM'
        context['numero'] = Piscinas.objects.filter(id=self.kwargs['pk'])
        return context