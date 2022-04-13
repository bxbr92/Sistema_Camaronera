$(document).ready(function () {
    // Create DataTable
    var table = $('#tb_seguimiento').DataTable({
        "language": {
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Último",
                "sNext": "Siguiente",
                "sPrevious": "Anterior"
            },
            "zeroRecords": "No se encontró nada, lo siento",
            "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "infoEmpty": "Tabla vacia por favor inserte datos",
            "sSearch": "Buscar:",
            "infoFiltered": "(filtrado de _MAX_ registros totales)"
        },
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                text: '<i class="fas fa-file-excel"></i> ',
                titleAttr: 'Exportar a Excel',
                className: 'btn btn-success'
            },
            {
                extend: 'pdfHtml5',
                text: '<i class="fas fa-file-pdf"></i> ',
                titleAttr: 'Exportar a PDF',
                className: 'btn btn-danger'
            },
            {
                extend: 'print',
                text: '<i class="fa fa-print"></i> ',
                titleAttr: 'Imprimir',
                className: 'btn btn-info'
            },
            {
                extend: 'csvHtml5',
                text: '<i class="fas fa-file-csv"></i> ',
                titleAttr: 'Exportar a CSV',
                className: 'btn btn-success'
            },
        ]
    });

    // Crea la figura con los datos iniciales
    var container = $('<div/>').insertBefore(table.table().container());

    var chart = Highcharts.chart(container[0], {
        chart: {
            type: 'pie',
        },
        title: {
            text: 'DESARROLLO PORCENTUAL POR PISCINAS INDUSTRIAS PSM & BIO',
        },
        series: [
            {
                data: chartData(table),
            },
        ],
    });

    // En cada sorteo, actualice los datos en el gráfico
    table.on('draw', function () {
        chart.series[0].setData(chartData(table));
    });
});

function chartData(table) {
    var counts = {};
    // Cuenta el número de entradas para cada puesto
    table
        .column(0, {search: 'applied'})
        .data()
        .each(function (val) {
            if (counts[val]) {
                counts[val] += 1;
            } else {
                counts[val] = 1;
            }
        });

    // Y mapearlo al formato que usa en gráficos altos
    return $.map(counts, function (val, key) {
        return {
            name: key,
            y: val,
        };
    });
};