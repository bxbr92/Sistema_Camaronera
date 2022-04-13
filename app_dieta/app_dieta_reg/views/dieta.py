# Create your views here.
import json
from django.db import transaction
import datetime
import decimal
from django.db import transaction
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, View, UpdateView, DeleteView
from weasyprint import HTML
from app_dieta.app_dieta_reg.forms import AnioDietaForm, RegistroDiaDietaForm, DiaDietaForm, DescripcionDietaForm
from app_dieta.app_dieta_reg.models import MesDieta, AnioDieta, DiaDietaRegistro, DetalleDiaDieta, DescripcionDieta
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
# Para crear las Dietas
from app_empresa.app_reg_empresa.models import Empresa, Piscinas
from app_inventario.app_categoria.models import Producto
from app_reportes.utils import render_to_pdf
from app_stock.app_detalle_stock.models import Producto_Stock, Total_Stock


class crearAnioDietaView(CreateView):
    model = AnioDieta
    form_class = AnioDietaForm
    template_name = 'app_dieta/dieta_principal_anio_crear.html'
    success_url = reverse_lazy('app_dieta:principal_anio')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Dieta'
        return context


class crearMesDietaView(CreateView):
    model = MesDieta
    template_name = 'app_dieta/dieta_principal_mes_crear.html'
    success_url = reverse_lazy('app_dieta:principal_mes')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Dieta'
        return context


def modificarDietas(request):
    print(request)
    if request.POST:
        id_dieta = int(request.POST.get('id'))
        dieta_registro = DetalleDiaDieta.objects.get(id=id_dieta)
        # dieta_registro.dieta_id=request.POST.get('dieta')
        # dieta_registro.piscinas_id = request.POST.get('piscinas')

        id_balanceado = int(request.POST.get('balanceado'))
        cantidad = decimal.Decimal(request.POST.get('cantidad').replace(",", "."))
        if id_balanceado != dieta_registro.balanceado.pk or cantidad != dieta_registro.cantidad:
            if id_balanceado > 0:
                # Realizo el rollback (se suma el stock del producto que se actualizó)
                ps = Total_Stock.objects.get(nombre_empresa_id=dieta_registro.piscinas.empresa.pk,
                                             nombre_prod_id=dieta_registro.balanceado.pk)
                ps.stock = ps.stock + dieta_registro.cantidad
                ps.save()

                producto = Producto_Stock.objects.filter(piscinas=dieta_registro.piscinas.numero,
                                                         producto_empresa_id=ps.pk)
                producto.delete()

                dieta_registro.balanceado_id = id_balanceado
                dieta_registro.cantidad = cantidad

        insumo1 = int(request.POST.get('insumo1'))
        gramaje1 = decimal.Decimal(request.POST.get('gramaje1'))
        if insumo1 != dieta_registro.insumo1 or gramaje1 != dieta_registro.gramaje1:
            if insumo1 > 0:
                # Realizo el rollback (se suma el stock del producto que se actualizó)
                ps = Total_Stock.objects.get(nombre_empresa_id=dieta_registro.piscinas.empresa.pk,
                                             nombre_prod_id=dieta_registro.insumo1)
                ps.stock = ps.stock + dieta_registro.gramaje1
                ps.save()

                producto = Producto_Stock.objects.filter(piscinas=dieta_registro.piscinas.numero,
                                                         producto_empresa_id=ps.pk)
                producto.delete()

                dieta_registro.insumo1 = insumo1
                dieta_registro.gramaje1 = gramaje1

        insumo2 = int(request.POST.get('insumo2'))
        gramaje2 = decimal.Decimal(request.POST.get('gramaje2'))
        if insumo2 != dieta_registro.insumo2 or gramaje2 != dieta_registro.gramaje2:
            if insumo2 > 0:
                # Realizo el rollback (se suma el stock del producto que se actualizó)
                ps = Total_Stock.objects.get(nombre_empresa_id=dieta_registro.piscinas.empresa.pk,
                                             nombre_prod_id=dieta_registro.insumo2)
                ps.stock = ps.stock + dieta_registro.gramaje2
                ps.save()

                producto = Producto_Stock.objects.filter(piscinas=dieta_registro.piscinas.numero,
                                                         producto_empresa_id=ps.pk)
                producto.delete()

                dieta_registro.insumo2 = insumo2
                dieta_registro.gramaje2 = gramaje2

        insumo3 = int(request.POST.get('insumo3'))
        gramaje3 = decimal.Decimal(request.POST.get('gramaje3'))
        if insumo3 != dieta_registro.insumo3 or gramaje3 != dieta_registro.gramaje3:
            if insumo3 > 0:
                # Realizo el rollback (se suma el stock del producto que se actualizó)
                ps = Total_Stock.objects.get(nombre_empresa_id=dieta_registro.piscinas.empresa.pk,
                                             nombre_prod_id=dieta_registro.insumo3)
                ps.stock = ps.stock + dieta_registro.gramaje3
                ps.save()

                producto = Producto_Stock.objects.filter(piscinas=dieta_registro.piscinas.numero,
                                                         producto_empresa_id=ps.pk)
                producto.delete()

                dieta_registro.insumo3 = insumo3
                dieta_registro.gramaje3 = gramaje3

        insumo4 = int(request.POST.get('insumo4'))
        gramaje4 = decimal.Decimal(request.POST.get('gramaje4'))
        if insumo4 != dieta_registro.insumo4 or gramaje4 != dieta_registro.gramaje4:
            if insumo4 > 0:
                # Realizo el rollback (se suma el stock del producto que se actualizó)
                ps = Total_Stock.objects.get(nombre_empresa_id=dieta_registro.piscinas.empresa.pk,
                                             nombre_prod_id=dieta_registro.insumo4)
                ps.stock = ps.stock + dieta_registro.gramaje4
                ps.save()

                producto = Producto_Stock.objects.filter(piscinas=dieta_registro.piscinas.numero,
                                                         producto_empresa_id=ps.pk)
                producto.delete()

                dieta_registro.insumo4 = insumo4
                dieta_registro.gramaje4 = gramaje4
        dieta_registro.save()
        return HttpResponse("Se registro MODIFICAR DIETA..!")


# def modificarDietas(request):
#     if request.POST:
#         dieta_registro=DetalleDiaDieta.objects.get(id=request.POST.get('id'))
#         dieta_registro.dieta_id=request.POST.get('dieta')
#         dieta_registro.piscinas_id = request.POST.get('piscinas')
#         if int(request.POST.get('balanceado'))>0:
#             dieta_registro.balanceado_id = request.POST.get('balanceado')
#             dieta_registro.cantidad = request.POST.get('cantidad').replace(",",".")
#         if int(request.POST.get('insumo1'))>0:
#             dieta_registro.insumo1 = request.POST.get('insumo1')
#             dieta_registro.gramaje1 = request.POST.get('gramaje1')
#         if int(request.POST.get('insumo2')) > 0:
#             dieta_registro.insumo2 = request.POST.get('insumo2')
#             dieta_registro.gramaje2 = request.POST.get('gramaje2')
#         if int(request.POST.get('insumo3')) > 0:
#             dieta_registro.insumo3 = request.POST.get('insumo3')
#             dieta_registro.gramaje3 = request.POST.get('gramaje3')
#         if int(request.POST.get('insumo4')) > 0:
#             dieta_registro.insumo4 = request.POST.get('insumo4')
#             dieta_registro.gramaje4 = request.POST.get('gramaje4')
#         dieta_registro.save()
#         return HttpResponse("Se registro MODIFICAR DIETA..!")


def crearDiaDieta(request, pk):
    productos = Producto.objects.all()
    if request.POST:
        dieta_registro = DetalleDiaDieta()
        dieta_registro.dieta_id = request.POST.get('dieta')
        dieta_registro.piscinas_id = request.POST.get('piscinas')
        with transaction.atomic():
            if int(request.POST.get('balanceado')) > 0:
                dieta_registro.balanceado_id = request.POST.get('balanceado')
                dieta_registro.cantidad = request.POST.get('cantidad')
            if int(request.POST.get('insumo1')) > 0:
                dieta_registro.insumo1 = request.POST.get('insumo1')
                dieta_registro.gramaje1 = request.POST.get('gramaje1')
            if int(request.POST.get('insumo2')) > 0:
                dieta_registro.insumo2 = request.POST.get('insumo2')
                dieta_registro.gramaje2 = request.POST.get('gramaje2')
            if int(request.POST.get('insumo3')) > 0:
                dieta_registro.insumo3 = request.POST.get('insumo3')
                dieta_registro.gramaje3 = request.POST.get('gramaje3')
            if int(request.POST.get('insumo4')) > 0:
                dieta_registro.insumo4 = request.POST.get('insumo4')
                dieta_registro.gramaje4 = request.POST.get('gramaje4')
            dieta_registro.save()
            return HttpResponse("Se registro CREAR DIETA..!")
    contexto = {
        'nombre': 'Dia de Dieta',
        'piscinas': Piscinas.objects.all(),
        'balanceados': productos.filter(categoria__nombre__icontains='BALANCEADOS'),
        'insumos': productos.filter(categoria__nombre__icontains='INSUMOS'),
        'dieta_registros': DetalleDiaDieta.objects.filter(dieta_id=pk),
        'mes': DiaDietaRegistro.objects.get(id=pk).mes_dieta,
        'pk': pk,
    }
    return render(request, 'app_dieta/app_dias_dietas/frm_dieta_dia_crear.html', contexto)


class crearDiaDietaView(CreateView):
    model = DetalleDiaDieta
    form_class = DiaDietaForm
    template_name = 'app_dieta/app_dias_dietas/frm_dieta_dia_version2.html'
    success_url = reverse_lazy('app_dieta:principal_dia')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_piscinas':
                data = []
                empresa = request.POST['empresa']
                queryset = Piscinas.objects.all()
                ids_exclude = json.loads(request.POST['ids'])
                queryset = queryset.filter(empresa__siglas=empresa).exclude(id__in=ids_exclude)
                for i in queryset:
                    item = i.toJSON()
                    data.append(item)
            elif action == 'search_balanceado':
                print('llego aqui a buscar balanceado')
                data = []
                queryset = Producto.objects.all()
                for i in queryset:
                    item = i.toJSON()
                    data.append(item)
            elif action == 'create':
                with transaction.atomic():
                    items = json.loads(request.POST['items'])
                    print(items)
                    factura = DiaDietaRegistro.objects.get(id=self.kwargs['pk'])
                    factura.mes_dieta_id = factura.mes_dieta.pk
                    factura.fecha = request.POST['fecha']
                    factura.save()
                    for i in items:
                        inv = DetalleDiaDieta()
                        inv.dieta_id = factura.pk
                        inv.piscinas_id = int(i['id']) if i.get('id') else None
                        inv.balanceado_id = int(i['balanceado']) if i.get('balanceado') else None
                        inv.cantidad = decimal.Decimal(i['cantidad']) if i.get('cantidad') else 0
                        inv.insumo1 = int(i['insumo1']) if i.get('insumo1') else 0
                        inv.gramaje1 = decimal.Decimal(i['gramaje1']) if i.get('gramaje1') else 0
                        inv.insumo2 = int(i['insumo2']) if i.get('insumo2') else 0
                        inv.gramaje2 = decimal.Decimal(i['gramaje2']) if i.get('gramaje2') else 0
                        inv.insumo3 = int(i['insumo3']) if i.get('insumo3') else 0
                        inv.gramaje3 = decimal.Decimal(i['gramaje3']) if i.get('gramaje3') else 0
                        inv.insumo4 = int(i['insumo4']) if i.get('insumo4') else 0
                        inv.gramaje4 = decimal.Decimal(i['gramaje4']) if i.get('gramaje4') else 0
                        inv.save()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = 'el error es : ' + str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dieta = DiaDietaRegistro.objects.get(id=self.kwargs['pk']).mes_dieta
        context['nombre'] = 'Dia de Dieta - %s %s' % (dieta.mes_dieta, dieta.anio.anio_dieta)
        context['entity'] = 'Registro de Dieta'
        context['list_url'] = self.success_url
        context['action'] = 'create'
        context['piscinas'] = Piscinas.objects.all()
        context['balanceados'] = Producto.objects.filter(categoria__nombre__icontains='BALANCEADOS')
        context['insumos'] = Producto.objects.filter(categoria__nombre__icontains='INSUMOS')
        context['dieta2'] = DetalleDiaDieta.objects.filter(dieta_id=self.kwargs['pk'])
        context['dieta_registros'] = DetalleDiaDieta.objects.filter(dieta_id=self.kwargs['pk'])
        context['mes'] = dieta.mes_dieta
        context['prin_dia'] = dieta.id
        context['pk'] = self.kwargs['pk']
        context['det'] = []
        return context


class editarDiaDietaView(UpdateView):
    model = DetalleDiaDieta
    form_class = DiaDietaForm
    template_name = 'app_dieta/app_dias_dietas/frm_dieta_dia_version2.html'
    success_url = reverse_lazy('app_dieta:principal_dia')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        #self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_piscinas':
                data = []
                empresa = request.POST['empresa']
                queryset = Piscinas.objects.all()
                ids_exclude = json.loads(request.POST['ids'])
                queryset = queryset.filter(empresa__siglas=empresa).exclude(id__in=ids_exclude)
                for i in queryset:
                    item = i.toJSON()
                    data.append(item)
            elif action == 'search_balanceado':
                print('llego aqui a buscar balanceado')
                data = []
                queryset = Producto.objects.all()
                for i in queryset:
                    item = i.toJSON()
                    data.append(item)
            elif action == 'edit':
                with transaction.atomic():
                    items = json.loads(request.POST['items'])
                    factura = DiaDietaRegistro.objects.get(mes_dieta_id = self.kwargs['pk'])
                    factura.mes_dieta_id = factura.mes_dieta.pk
                    factura.fecha = request.POST['fecha']
                    factura.save()
                    # for s in factura.detallediadieta_set.all():
                    #     s.producto_empresa.stock = float(s.producto_empresa.stock) + float(s.cantidad)
                    #     s.producto_empresa.stock = float(s.producto_empresa.stock) + float(s.gramaje1)
                    #     s.producto_empresa.stock = float(s.producto_empresa.stock) + float(s.gramaje2)
                    #     s.producto_empresa.stock = float(s.producto_empresa.stock) + float(s.gramaje3)
                    #     s.producto_empresa.stock = float(s.producto_empresa.stock) + float(s.gramaje4)
                    #     s.producto_empresa.save()
                    #     s.delete()
                    for i in items:
                        inv = DetalleDiaDieta()
                        inv.dieta_id = factura.pk
                        inv.piscinas_id = int(i['id']) if i.get('id') else None
                        inv.balanceado_id = int(i['balanceado']) if i.get('balanceado') else None
                        inv.cantidad = decimal.Decimal(i['cantidad']) if i.get('cantidad') else 0
                        inv.insumo1 = int(i['insumo1']) if i.get('insumo1') else 0
                        inv.gramaje1 = decimal.Decimal(i['gramaje1']) if i.get('gramaje1') else 0
                        inv.insumo2 = int(i['insumo2']) if i.get('insumo2') else 0
                        inv.gramaje2 = decimal.Decimal(i['gramaje2']) if i.get('gramaje2') else 0
                        inv.insumo3 = int(i['insumo3']) if i.get('insumo3') else 0
                        inv.gramaje3 = decimal.Decimal(i['gramaje3']) if i.get('gramaje3') else 0
                        inv.insumo4 = int(i['insumo4']) if i.get('insumo4') else 0
                        inv.gramaje4 = decimal.Decimal(i['gramaje4']) if i.get('gramaje4') else 0
                        inv.save()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_detalle(self):
        data = []
        for i in DetalleDiaDieta.objects.filter(dieta_id=self.kwargs['pk']):
            item = i.piscinas.toJSON()
            item['balanceado'] = i.balanceado
            item['cantidad'] = i.cantidad
            item['insumo1'] = i.insumo1
            item['gramaje1'] = i.gramaje1
            item['insumo2'] = i.insumo2
            item['gramaje2'] = i.gramaje2
            item['insumo3'] = i.insumo3
            item['gramaje3'] = i.gramaje3
            item['insumo4'] = i.insumo4
            item['gramaje4'] = i.gramaje4
            data.append(i.toJSON())
        return json.dumps(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dieta = DiaDietaRegistro.objects.get(id=self.kwargs['pk']).mes_dieta
        context['nombre'] = 'Dia de Dieta - %s %s' % (dieta.mes_dieta, dieta.anio.anio_dieta)
        context['entity'] = 'Registro de Dieta'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['piscinas'] = Piscinas.objects.all()
        context['balanceados'] = Producto.objects.filter(categoria__nombre__icontains='BALANCEADOS')
        context['insumos'] = Producto.objects.filter(categoria__nombre__icontains='INSUMOS')
        context['dieta2'] = DetalleDiaDieta.objects.filter(dieta_id=self.kwargs['pk'])
        context['dieta_registros'] = DetalleDiaDieta.objects.filter(dieta_id=self.kwargs['pk'])
        context['mes'] = dieta.mes_dieta
        context['prin_dia'] = dieta.id
        pk = self.kwargs['pk']
        context['det'] = self.get_detalle()
        # # context['frmClient'] = ClientForm()
        return context


# Para listar las Dietas Año
class listarDietaAnioPrincipalView(ListView):
    model = AnioDieta
    template_name = 'app_dieta/dieta_principal_anio.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = AnioDieta.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # defino el dicionario para enviar variables a mi plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Ventana Principal Dieta Año'
        context['dieta'] = AnioDieta.objects.all()
        return context


# dietas del mes, crea, lista y modifica
def listaDietas(request, anio):
    contexto = {
        'nombre': 'Ventana Principal Dieta Mes',
        'meses': MesDieta.objects.filter(anio_id=anio),
        'anio': AnioDieta.objects.get(id=anio)
    }
    if request.POST:
        if request.GET.get('nuevo'):
            mes = MesDieta(anio_id=anio, mes_dieta=request.POST.get('mes_dieta'),
                           descripcion=request.POST.get('descripcion'))
        else:
            mes = MesDieta.objects.get(id=request.GET.get('mes'))
            mes.descripcion = request.POST.get('descripcion')
        mes.save()
    return render(request, 'app_dieta/dieta_principal_mes.html', contexto)


# Para listar las Dietas Dia
def listarDias(request, pk):
    dietas = DiaDietaRegistro.objects.filter(mes_dieta_id=pk)
    mes = MesDieta.objects.get(id=pk)
    if request.POST:
        dietasR = DiaDietaRegistro(mes_dieta_id=pk)
        dietasR.save()
        return redirect(reverse('app_dieta:crear_dia_dieta', kwargs={'pk': dietasR.pk}))
    contexto = {
        'anio_id': mes.anio.id,
        'mes': mes,
        'fecha': datetime.datetime.now(),
        'dietas': dietas,
        'nombre': 'Ventana Principal Dieta Dia',
    }
    return render(request, 'app_dieta/app_dias_dietas/frm_dieta_dia_principal.html', contexto)


# CON XHTML2PDF
class ListarDietaPDF(View):
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            dieta = DetalleDiaDieta.objects.filter(dieta_id=kwargs['pk']).order_by('piscinas__orden')
            fecha_dieta = ''

            if dieta:
                fecha_dieta = dieta[0].dieta.fecha

            # Empresa PSM
            balanceado = {}
            insumo = {}

            for b in dieta.filter(piscinas__empresa__siglas='PSM'):
                if b.balanceado:
                    nombre_b = b.balanceado.nombre

                    if nombre_b not in balanceado:
                        balanceado[nombre_b] = b.cantidad
                    else:
                        balanceado[nombre_b] = balanceado[nombre_b] + b.cantidad

                nombre_i = b.insumo1
                if nombre_i:
                    nombre_i = Producto.objects.get(id=nombre_i).nombre
                    if nombre_i not in insumo:
                        insumo[nombre_i] = b.gramaje1
                    else:
                        insumo[nombre_i] = insumo[nombre_i] + b.gramaje1

                nombre_i = b.insumo2
                if nombre_i:
                    nombre_i = Producto.objects.get(id=nombre_i).nombre
                    if nombre_i not in insumo:
                        insumo[nombre_i] = b.gramaje2
                    else:
                        insumo[nombre_i] = insumo[nombre_i] + b.gramaje2

                nombre_i = b.insumo3
                if nombre_i:
                    nombre_i = Producto.objects.get(id=nombre_i).nombre
                    if nombre_i not in insumo:
                        insumo[nombre_i] = b.gramaje3
                    else:
                        insumo[nombre_i] = insumo[nombre_i] + b.gramaje3

                nombre_i = b.insumo4
                if nombre_i:
                    nombre_i = Producto.objects.get(id=nombre_i).nombre
                    if nombre_i not in insumo:
                        insumo[nombre_i] = b.gramaje4
                    else:
                        insumo[nombre_i] = insumo[nombre_i] + b.gramaje4

            resumen_totales = {
                'psm': {'balanceado': balanceado, 'insumo': insumo}
            }

            # Empresa BIO
            balanceado = {}
            insumo = {}

            for b in dieta.filter(piscinas__empresa__siglas='BIO'):
                if b.balanceado:
                    nombre_b = b.balanceado.nombre

                    if nombre_b not in balanceado:
                        balanceado[nombre_b] = b.cantidad
                    else:
                        balanceado[nombre_b] = balanceado[nombre_b] + b.cantidad

                nombre_i = b.insumo1
                if nombre_i:
                    nombre_i = Producto.objects.get(id=nombre_i).nombre
                    if nombre_i not in insumo:
                        insumo[nombre_i] = b.gramaje1
                    else:
                        insumo[nombre_i] = insumo[nombre_i] + b.gramaje1

                nombre_i = b.insumo2
                if nombre_i:
                    nombre_i = Producto.objects.get(id=nombre_i).nombre
                    if nombre_i not in insumo:
                        insumo[nombre_i] = b.gramaje2
                    else:
                        insumo[nombre_i] = insumo[nombre_i] + b.gramaje2

                nombre_i = b.insumo3
                if nombre_i:
                    nombre_i = Producto.objects.get(id=nombre_i).nombre
                    if nombre_i not in insumo:
                        insumo[nombre_i] = b.gramaje3
                    else:
                        insumo[nombre_i] = insumo[nombre_i] + b.gramaje3

                nombre_i = b.insumo4
                if nombre_i:
                    nombre_i = Producto.objects.get(id=nombre_i).nombre
                    if nombre_i not in insumo:
                        insumo[nombre_i] = b.gramaje4
                    else:
                        insumo[nombre_i] = insumo[nombre_i] + b.gramaje4

            resumen_totales['bio'] = {'balanceado': balanceado, 'insumo': insumo}

            data = {
                'insumos': Producto.objects.filter(categoria__nombre__icontains='INSUMOS'),
                'dieta_registros': dieta, 'fecha_dieta': fecha_dieta, 'resumen_totales': resumen_totales
            }
            pdf = render_to_pdf('app_reportes/printDieta.html', data)
            return HttpResponse(pdf, content_type='application/pdf')


# CON WEASYPRINT
class printDieta(View):

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            dieta = DetalleDiaDieta.objects.filter(dieta_id=kwargs['pk']).order_by('piscinas__orden')
            data = {
                'insumos': Producto.objects.filter(categoria__nombre__icontains='INSUMOS'),
                'dieta_registros': dieta,
            }
            template = get_template("app_reportes/printDieta.html")
            html_template = template.render(data)
            HTML(string=html_template).write_pdf(target="dieta.pdf")


class listarDescripcionDietaView(ListView):
    model = DescripcionDieta
    template_name = 'app_dieta/app_descripcion/listar_descripcion.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = DescripcionDieta.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # defino el dicionario para enviar variables a mi plantilla
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Descripción de Escaneo de Dietas'
        context['descripcion_dieta'] = DescripcionDieta.objects.all()
        return context


class crearDescripcionDietaView(CreateView):
    model = DescripcionDieta
    form_class = DescripcionDietaForm
    template_name = 'app_dieta/app_descripcion/crear_descripcion.html'
    success_url = reverse_lazy('app_dieta:listar_descripcion_dieta')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Descripción de Dieta'
        return context


class actualizarDescripcionDietaView(UpdateView):
    model = DescripcionDieta
    form_class = DescripcionDietaForm
    template_name = 'app_dieta/app_descripcion/crear_descripcion.html'
    success_url = reverse_lazy('app_dieta:listar_descripcion_dieta')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Descripción de Dieta'
        context['action'] = 'crear'
        return context


class eliminarDescripcionDietaView(DeleteView):
    model = DescripcionDieta
    form_class = DescripcionDietaForm
    template_name = 'app_dieta/app_descripcion/eliminar_descripcion.html'
    success_url = reverse_lazy('app_dieta:listar_descripcion_dieta')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Descripción de Dieta'
        context['action'] = 'crear'
        return context
