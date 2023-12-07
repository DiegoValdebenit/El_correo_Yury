// import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.6.0/firebase-auth.js";
// import { obtenerDatosUsuario } from './firebaseConfig.js'; // Ajusta la ruta según sea necesario

// const auth = getAuth();

// onAuthStateChanged(auth, async (user) => {
//     if (user) {
//         const userData = await obtenerDatosUsuario(user.email);
//         if (!userData) {
//             await signOut(auth);
//             window.location.href = '../index.html';
//             return;
//         }
        
//         // Se obtiene el nombre del archivo de la URL actual
//         const currentPage = window.location.pathname.split('/').pop();
        
//         // Según rol se asigna el acceso
//         const acceso = {
//             "jefe de rr.hh": ["jefe_rrhh_perfil.html", "jefe_rrhh_table.html"],
//             "empleado de la empresa": ["empleado.html"],
//             "empleado de rr.hh": ["empleado_rrhh_form.html", "empleado_rrhh_perfil.html"]
//         };

//         const rolesPermitidos = Object.keys(acceso);
//         for (let rol of rolesPermitidos) {
//             if (userData.cargo.toLowerCase() === rol && acceso[rol].includes(currentPage)) {
//                 return;
//             }
//         }

//         await signOut(auth);
//         window.location.href = '../index.html';
//     } else {
//         window.location.href = '../index.html';
//     }
// });
