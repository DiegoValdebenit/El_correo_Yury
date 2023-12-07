import { registrarDatos } from '../seguridad/firebaseConfig';

// Variable para almacenar temporalmente los datos de contactos y cargas familiares
let contactosTemp = [];
let cargasTemp = [];

// Recibe los datos del formulario
const formDatos = document.getElementById('form');

// agregar contactos de emergencia
const agregarContactoTemp = () => {
    const contactoNombres = formDatos.querySelector('#contacto-nombres').value;
    const contactoApellidos = formDatos.querySelector('#contacto-apellidos').value;
    const relacion = formDatos.querySelector('#relacion').value;
    const contactoTelefono = formDatos.querySelector('#contacto-telefono').value;

    contactosTemp.push({
        nombres: contactoNombres,
        apellidos: contactoApellidos,
        relacion: relacion,
        telefono: contactoTelefono,
    });

    // Limpiar campos
    formDatos.querySelector('#contacto-nombres').value = '';
    formDatos.querySelector('#contacto-apellidos').value = '';
    formDatos.querySelector('#relacion').value = '';
    formDatos.querySelector('#contacto-telefono').value = '';
};

// agregar cargas familiares temporales
const agregarCargaTemp = () => {
    const cargasNombres = formDatos.querySelector('#carga-nombres').value;
    const cargasApellidos = formDatos.querySelector('#carga-apellidos').value;
    const cargasSexo = formDatos.querySelector('input[name="carga-sexo"]:checked').value;
    const cargasRut = formDatos.querySelector('#carga-rut').value;
    const parentesco = formDatos.querySelector('#parentesco').value;

    cargasTemp.push({
        nombres: cargasNombres,
        apellidos: cargasApellidos,
        sexo: cargasSexo,
        rut: cargasRut,
        parentesco: parentesco, // Corregido el nombre del campo
    });

    // Limpiar campos
    formDatos.querySelector('#carga-nombres').value = '';
    formDatos.querySelector('#carga-apellidos').value = '';
    formDatos.querySelector('input[name="carga-sexo"]:checked').checked = false;
    formDatos.querySelector('#carga-rut').value = '';
    formDatos.querySelector('#parentesco').value = '';
};

// Evento para agregar contactos de emergencia
formDatos.querySelector('#btn-agregar-uno').addEventListener('click', () => {
    agregarContactoTemp();
});

// Evento para agregar cargas familiares
formDatos.querySelector('#btn-agregar-dos').addEventListener('click', () => {
    agregarCargaTemp();
});

// Evento para registrar los datos en firestore
formDatos.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Recolecta los datos personales del formulario
    const nombres = formDatos.querySelector('#nombres').value;
    const apellidos = formDatos.querySelector('#apellidos').value;
    const sexo = formDatos.querySelector('input[name="sexo"]:checked').value;
    const rut = formDatos.querySelector('#rut').value;
    const direccion = formDatos.querySelector('#direccion').value;
    const telefono = formDatos.querySelector('#telefono').value;
    const cargo = formDatos.querySelector('input[name="user"]:checked').value;
    const fechaIngreso = formDatos.querySelector('#fecha-ingreso').value;
    const area = formDatos.querySelector('#area').value;
    const departamento = formDatos.querySelector('#departamento').value;
    const email = formDatos.querySelector('#email').value;

    // Objeto con datos personales, contactos de emergencia y cargas familiares
    const datosPersonales = {
        nombres,
        apellidos,
        sexo,
        rut,
        direccion,
        telefono,
        cargo,
        fechaIngreso,
        area,
        departamento,
        email,
        contactos: contactosTemp,
        cargas: cargasTemp,
    };

    // Registrar datos en Firestore
    try {
        await registrarDatos(datosPersonales);

        // Limpiar campos
        //formDatos.reset();
    } catch (error) {
        console.error('Error al registrar datos:', error);
    }
});
