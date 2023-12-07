// login.js

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('login-button').addEventListener('click', login);
});

// Importar funciones necesarias desde firebaseConfig.js
import { signInWithEmailAndPassword } from '../../seguridad/firebaseConfig.js';
import { obtenerDatosUsuario } from '../../seguridad/firebaseConfig.js';


// Definir la función login
export async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        // Autenticar con Firebase
        const userCredential = await signInWithEmailAndPassword(username, password);
        const user = userCredential.user;

        // Obtener datos del usuario desde Firestore
        const userData = await obtenerDatosUsuario(username);

        // Redirigir según el cargo
        if (userData && userData.cargo) {
            switch (userData.cargo.toLowerCase()) {
                case "jefe de rr.hh":
                    window.location.href = "../../pages/jefe_rrhh_table.html";
                    console.log('inicio exitoso como Jefe de RR.HH');
                    break;
                case "empleado de la empresa":
                    window.location.href = "../../pages/empleado_rrhh_form.html";
                    console.log('inicio exitoso como Empleado de la empresa');
                    break;
                case "empleado de rr.hh":
                    window.location.href = "../../pages/empleado.html";
                    console.log('inicio exitoso como Empleado de RR.HH');
                    break;
                default:
                    // Manejar otros casos si es necesario
                    break;
            }
        } else {
            console.error("Error: No se pudo obtener la información del usuario.");
        }
    } catch (error) {
        console.error("Error de autenticación:", error.message);
        // Manejar errores de autenticación, por ejemplo, mostrar un mensaje al usuario
    }
}
