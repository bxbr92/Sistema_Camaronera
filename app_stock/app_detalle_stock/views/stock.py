
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView
from app_empresa.app_reg_empresa.models import Empresa
from app_inventario.app_categoria.models import Producto
from app_stock.app_detalle_stock.forms import ProdStockForm, ProdStockTotalForm
from app_stock.app_detalle_stock.models import Producto_Stock, Total_Stock, InvoiceStock
import decimal

# EMPRESA PRESQUERA SAN MIGUEL
class crearStockPSMView(CreateView):
    model = Producto_Stock
    form_class = ProdStockForm
    template_name = 'app_stock/stock_crear_psm.html'
    success_url = reverse_lazy('app_stock:listar_stock_psm')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Stock Productos PSM'
        context['id_producto_empresa'] = self.kwargs['pk']
        producto = Total_Stock.objects.get(pk=self.kwargs['pk'])
        context['producto'] = producto

        unidad_aplicacion = producto.nombre_prod.unid_aplicacion  # LB   KG
        if unidad_aplicacion == 'GR':
            aplicacion = 1000
        elif unidad_aplicacion == 'KG':
            aplicacion = 2.2
        elif unidad_aplicacion == 'LB':
            aplicacion = 1
        else:
            aplicacion = 1000

        context['total'] = decimal.Decimal(aplicacion) * producto.nombre_prod.peso_presentacion

        return context

# class actualizarStockPSMView(UpdateView):
#     model = Producto_Stock
#     form_class = ProdStockForm
#     template_name = 'app_stock/stock_crear_psm.html'
#     success_url = reverse_lazy('app_stock:listar_stock_psm')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['nombre'] = 'Stock Productos PSM'
#         context['id_producto_empresa'] = self.kwargs['pk']
#         producto = Total_Stock.objects.get(pk=self.kwargs['pk'])
#         context['producto'] = producto
#
#         unidad_aplicacion = producto.nombre_prod.unid_aplicacion  # LB   KG
#         if unidad_aplicacion == 'GR':
#             aplicacion = 1000
#         elif unidad_aplicacion == 'KG':
#             aplicacion = 2.2
#         elif unidad_aplicacion == 'LB':
#             aplicacion = 1
#         else:
#             aplicacion = 1000
#
#         context['total'] = decimal.Decimal(aplicacion) * producto.nombre_prod.peso_presentacion
#
#         return context


class listarStockPSMView(ListView):
    model = Total_Stock
    template_name = 'app_stock/stock_psm_listar.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Total_Stock.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # defino el dicionario para enviar variables a mi plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Stock Productos PSM'
        context['sotck'] = Total_Stock.objects.all()
        context['balanceados'] = Total_Stock.objects.filter(nombre_prod__categoria__nombre__icontains='BALANCEADOS', nombre_empresa__siglas='PSM')
        context['insumos'] = Total_Stock.objects.filter(nombre_prod__categoria__nombre__icontains='INSUMOS', nombre_empresa__siglas='PSM')
        return context


class listarStockUnicoPSMView(ListView):
    model = Producto_Stock
    template_name = 'app_stock/app_control/stock_unico_listar_psm.html'

    def get_queryset(self):
        return Producto_Stock.objects.filter(producto_empresa_id=self.kwargs['pk'])

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Producto_Stock.objects.get(producto_empresa_id=self.kwargs['pk']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # defino el dicionario para enviar variables a mi plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Kardex Stock Productos PSM'
        return context


# EMPRESA BIO CASCAJAL
class crearStockBIOView(CreateView):
    model = Producto_Stock
    form_class = ProdStockForm
    template_name = 'app_stock/stock_crear_bio.html'
    success_url = reverse_lazy('app_stock:listar_stock_bio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Stock Productos BIO'
        context['id_producto_empresa'] = self.kwargs['pk']
        producto = Total_Stock.objects.get(pk=self.kwargs['pk'])
        context['producto'] = producto

        unidad_aplicacion = producto.nombre_prod.unid_aplicacion  # LB   KG
        if unidad_aplicacion == 'GR':
            aplicacion = 1000
        elif unidad_aplicacion == 'KG':
            aplicacion = 2.2
        elif unidad_aplicacion == 'LB':
            aplicacion = 1
        else:
            aplicacion = 1000

        context['total'] = decimal.Decimal(aplicacion) * producto.nombre_prod.peso_presentacion

        return context

class listarStockBIOView(ListView):
    model = Total_Stock
    template_name = 'app_stock/stock_bio_listar.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Total_Stock.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # defino el dicionario para enviar variables a mi plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Stock Productos BIO'
        context['sotck'] = Total_Stock.objects.all()
        context['balanceados'] = Total_Stock.objects.filter(nombre_prod__categoria__nombre__icontains='BALANCEADOS', nombre_empresa__siglas='BIO')
        context['insumos'] = Total_Stock.objects.filter(nombre_prod__categoria__nombre__icontains='INSUMOS', nombre_empresa__siglas='BIO')
        return context

class listarStockUnicoBIOView(ListView):
    model = Producto_Stock
    template_name = 'app_stock/app_control/stock_unico_listar_bio.html'

    def get_queryset(self):
        return Producto_Stock.objects.filter(producto_empresa_id=self.kwargs['pk'])

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Producto_Stock.objects.get(producto_empresa_id=self.kwargs['pk']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # defino el dicionario para enviar variables a mi plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Kardex Stock Productos BIO'
        return context