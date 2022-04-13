var tblProducts;
var tblSearchProducts;
var vents = {
    items: {
        producto_empresa: '',
        cantidad_usar: '',
        cantidad_ingreso: '',
        fecha_ingreso: '',
        numero_guia: '',
        responsable_ingreso: '',
        products: []
    },
    get_ids: function () {
        var ids = [];
        $.each(this.items.products, function (key, value) {
            ids.push(value.id);
        });
        return ids;
    },
    calculate_invoice: function () {
        // var subtotal = 0.00;
        // var iva = $('input[name="iva"]').val();
        $.each(this.items.products, function (pos, dict) {
            // dict.pos = pos;
            // dict.subtotal = dict.cant * parseFloat(dict.pvp);
            // subtotal += dict.subtotal;
            // dict.cantidad_ingreso = dict.cantidad_usar;
            console.log('POS : ' + pos)
            console.log('dict : ' + dict)
        });
        // this.items.subtotal = subtotal;
        // this.items.iva = this.items.subtotal * iva;
        // this.items.total = this.items.subtotal + this.items.iva;
        //
        // $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        // $('input[name="ivacalc"]').val(this.items.iva.toFixed(2));
        // $('input[name="total"]').val(this.items.total.toFixed(2));
    },
    add: function (item) {
        this.items.products.push(item);
        this.list();
    },
    list: function () {
        // this.calculate_invoice()
        tblProducts = $('#tblProducts').DataTable({
            language: {
                "oPaginate": {
                    "sFirst": "Primero",
                    "sLast": "Último",
                    "sNext": "Siguiente",
                    "sPrevious": "Anterior"
                },
                "zeroRecords": "Ningun dato disponible en esta tabla",
                "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
                "infoEmpty": "Tabla vacia por favor inserte datos",
                "lengthMenu": "Listando _MENU_ registros",
                "sSearch": "Buscar:",
                "infoFiltered": "(filtrado de _MAX_ registros totales)"
            },
            //responsive: true,
            bPaginate: false,
            responsive: true,
            autoWidth: false,
            scrollY: "500px",
            destroy: true,
            data: this.items.products,
            columns: [
                {"data": "id"},
                {"data": "nombre_prod.nombre"},
                {"data": "nombre_prod.presentacion"},
                {"data": "nombre_empresa.siglas"},
                {"data": "stock"},
                {"data": "id"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat" style="color: white;"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
                {
                    targets: [-5],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        console.log(data)
                        return data;
                    }
                },
                {
                    targets: [-4],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        console.log(data)
                        return data;
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        console.log(data)
                        return data;
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cantidad_usar" class="form-control text-center" autocomplete="off" value="' + row.cantidad_usar + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<b>' + parseFloat(row.cantidad_ingreso).toFixed(2) + '<b>';
                    }
                }
            ],
            initComplete: function (settings, json) {

            }
        });
        console.clear();
        console.log(this.items);
        console.log(this.get_ids());
    },
};

$(function () {

    $('#btnBuscarPsm').on('click', function () {
        tblSearchProducts = $('#tblSearchProducts').DataTable({
            language: {
                "oPaginate": {
                    "sFirst": "Primero",
                    "sLast": "Último",
                    "sNext": "Siguiente",
                    "sPrevious": "Anterior"
                },
                "zeroRecords": "Ningun dato disponible en esta tabla",
                "sInfo": "Registros del _START_ al _END_ de un total de _TOTAL_ registros",
                "infoEmpty": "Tabla vacia por favor inserte datos",
                "lengthMenu": "Listando _MENU_ registros",
                "sSearch": "Buscar:",
                "infoFiltered": "(filtrado de _MAX_ registros totales)"
            },
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'ids': JSON.stringify(vents.get_ids()),
                    'empresa': 'PSM'
                },
                dataSrc: ""
            },
            columns: [
                {"data": "nombre_prod.nombre"},
                {"data": "nombre_empresa.nombre"},
                {"data": "id"},
            ],
            columnDefs: [
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return data;
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return data;
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a rel="add" class="btn btn-success btn-xs btn-flat" style="color: white;"><i class="fas fa-plus"></i></a> ';
                        return buttons;
                    }
                },
            ],
            initComplete: function (settings, json) {

            }
        });
        $('#myModalSearchProducts').modal('show');
    });


    $('#btnBuscarBio').on('click', function () {
        tblSearchProducts = $('#tblSearchProducts').DataTable({
            language: {
                "oPaginate": {
                    "sFirst": "Primero",
                    "sLast": "Último",
                    "sNext": "Siguiente",
                    "sPrevious": "Anterior"
                },
                "zeroRecords": "Ningun dato disponible en esta tabla",
                "sInfo": "Registros del _START_ al _END_ de un total de _TOTAL_ registros",
                "infoEmpty": "Tabla vacia por favor inserte datos",
                "lengthMenu": "Listando _MENU_ registros",
                "sSearch": "Buscar:",
                "infoFiltered": "(filtrado de _MAX_ registros totales)"
            },
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'ids': JSON.stringify(vents.get_ids()),
                    'empresa': 'BIO'
                    // 'term': $('select[name="search"]').val()
                },
                dataSrc: ""
            },
            columns: [
                {"data": "nombre_prod.nombre"},
                {"data": "nombre_empresa.nombre"},
                {"data": "id"},
            ],
            columnDefs: [
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return data;
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return data;
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a rel="add" class="btn btn-success btn-xs btn-flat" style="color: white;"><i class="fas fa-plus"></i></a> ';
                        return buttons;
                    }
                },
            ],
            initComplete: function (settings, json) {

            }
        });
        $('#myModalSearchProducts').modal('show');
    });


    $('#tblSearchProducts tbody').on('click', 'a[rel="add"]', function () {
        var tr = tblSearchProducts.cell($(this).closest('td, li')).index();
        var product = tblSearchProducts.row(tr.row).data();
        vents.add(product);
        tblSearchProducts.row($(this).parents('tr')).remove().draw();
    });


    $('#tblProducts tbody')
        .on('click', 'a[rel="remove"]', function () {
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            // alert('¿Estas seguro de eliminar el producto de tu detalle?');
            vents.items.products.splice(tr.row, 1);
            vents.list();
        })

        .on('change', 'input[name="cantidad_usar"]', function () {
            // console.clear();
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            var data = tblProducts.row(tr.row).data();
            console.log(data);
            data.cantidad_usar = parseInt($(this).val());
            if (data.nombre_prod.presentacion === 'CANECA') {
                data.cantidad_ingreso = data.cantidad_usar * data.nombre_prod.valor_aplicacion * 1;
            } else if (data.nombre_prod.nombre === 'PRO W') {
                data.cantidad_ingreso = data.cantidad_usar * data.nombre_prod.peso_presentacion;
            } else {
                data.cantidad_ingreso = data.cantidad_usar * data.nombre_prod.peso_presentacion * data.nombre_prod.valor_aplicacion;
            }
            $('td:eq(-1)', tblProducts.row(tr.row).node()).html('<b>' + data.cantidad_ingreso.toFixed(0) + '</b>');
        });


    $('.btnSave').on('click', function (event) {
        event.preventDefault();
        var items = tblProducts.rows().data().toArray();
        if ($.isEmptyObject(items)) {
            alerta_error('Debe ingresar al menos un item');
            return false;
        }
        $.ajax({
            url: window.location.pathname,
            data: {
                'action': $('input[name="action"]').val(),
                'fecha_ingreso': $('input[name="fecha_ingreso"]').val(),
                'numero_guia': $('input[name="numero_guia"]').val(),
                'responsable_ingreso': $('input[name="responsable_ingreso"]').val(),
                'items': JSON.stringify(items)
            },
            type: 'POST',
            dataType: 'json',
            success: function (request) {
                if (!request.hasOwnProperty('error')) {
                    //alert('Ingresado correctamente');
                    location.href = '/factura/listar';
                    return false;
                }
                alert(request.error);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert(errorThrown + ' ' + textStatus);
            }
        });
    });

    // Esto se puso aqui para que funcione bien el editar y calcule bien los valores del iva.
    // sino tomaría el valor del iva de la base debe
    // coger el que pusimos al inicializarlo.
    vents.list();

});