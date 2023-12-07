// Importar las funciones necesarias de Firebase
import { getAuth, signOut, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.6.0/firebase-auth.js";

// Obtener la instancia de autenticación de Firebase
const auth = getAuth();

// Añadir event listener para cerrar sesión
document.addEventListener('DOMContentLoaded', () => {
    const logoutButton = document.getElementById('logout-button');
    if (logoutButton) {
        logoutButton.addEventListener('click', async () => {
            try {
                await signOut(auth);
                window.location.href = '../../index.html';
            } catch (error) {
                console.error('Error al cerrar sesión:', error);
            }
        });
    }
});

// Verificar el estado de autenticación
onAuthStateChanged(auth, user => {
    if (!user) {
        // Si no hay usuario autenticado, redirigir al index.html
        window.location.href = '../../index.html';
    }
});
