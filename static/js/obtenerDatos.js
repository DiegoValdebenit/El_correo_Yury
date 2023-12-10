import { obtenerDatos } from "../seguridad/firebaseConfig.js";

// Mostrar datos almacenados en Firestore
window.addEventListener('DOMContentLoaded', async () => {
    const datos = await obtenerDatos();

    const tbody = document.getElementById('employeesTableBody');

    datos.forEach(doc => {

        const data = doc; 
        const tr = document.createElement('tr');

        // Agrega cada dato a una celda de la fila
        const keysToShow = ['nombres', 'apellidos', 'rut', 'sexo', 'cargo', 'area', 'departamento'];
        keysToShow.forEach(key => {
            const td = document.createElement('td');
            td.textContent = key in data ? data[key] : ''; //verificar clave antes de asignar
            tr.appendChild(td);
        });

        tbody.appendChild(tr);
    });
});
