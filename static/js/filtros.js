document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('filter-button').addEventListener('click', function () {
        // Obtener valores seleccionados
        var sexo = document.getElementById('filter-sexo').value;
        var cargo = document.getElementById('filter-cargo').value;
        // Obtener valores seleccionados para área y departamento

        // Realizar la solicitud al servidor
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                // Actualizar la tabla con los datos filtrados
                document.getElementById('employeesTableBody').innerHTML = xhr.responseText;
            }
        };
        xhr.open('GET', '/ruta-de-filtrado/?sexo=' + sexo + '&cargo=' + cargo, true);
        // Agrega parámetros de área y departamento a la URL

        xhr.send();
    });
});