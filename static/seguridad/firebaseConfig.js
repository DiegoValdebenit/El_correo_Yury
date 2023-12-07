//firebaseConfig.js


import { initializeApp } from "https://www.gstatic.com/firebasejs/10.6.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.6.0/firebase-analytics.js";
import { getFirestore, collection, addDoc, getDocs, where } from "https://www.gstatic.com/firebasejs/10.6.0/firebase-firestore.js";
import { getAuth, signInWithEmailAndPassword as firebaseSignInWithEmailAndPassword} from "https://www.gstatic.com/firebasejs/10.6.0/firebase-auth.js";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyANcfreCvFAh2ROAbfQ0ZfRpHJDs8eDnG8",
  authDomain: "el-correo-de-yury-cc45d.firebaseapp.com",
  projectId: "el-correo-de-yury-cc45d",
  storageBucket: "el-correo-de-yury-cc45d.appspot.com",
  messagingSenderId: "71030149395",
  appId: "1:71030149395:web:b038f419967f7386ba8ae6",
  measurementId: "G-P1ELMJDN3S"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const db = getFirestore();



// registrar datos personales
export const registrarDatos = async (datosPersonales) => {
  // almacenar en coleccion empleados
  const datosPersonalesRef = collection(db, 'empleados');
  await addDoc(datosPersonalesRef, datosPersonales);

};

//obtener datos de firestore
export const obtenerDatos = async () => {
  const querySnapshot = await getDocs(collection(db, 'empleados'));
  return querySnapshot.docs.map((doc) => doc.data());
};


// Obtener la instancia de autenticación de Firebase
export const auth = getAuth();

// Función para autenticar con correo y contraseña
export const signInWithEmailAndPassword = async (email, password) => {
  return await firebaseSignInWithEmailAndPassword(auth, email, password);
};

// Función para obtener datos de usuario desde Firestore
export const obtenerDatosUsuario = async (email) => {
  const querySnapshot = await getDocs(collection(db, 'empleados'), where('correo', '==', email));
  if (querySnapshot.docs.length > 0) {
    return querySnapshot.docs[0].data();
  }
  return null;
};