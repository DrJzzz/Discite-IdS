import {UserStore} from "../../user-store.js";
import {getCookie} from "../../utils/csrf.js";

/** @type {import('./$types').LayoutLoad} */
export async function load({ fetch }) {
    try {
        // Construye la URL del endpoint usando el parámetro de la carta ID
        const token =typeof localStorage !== 'undefined' ? localStorage.getItem('key') : '';
        const csrftoken = getCookie('csrftoken');
        const endpoint = `http://localhost:8000/rest-auth/user/`;

        // Realiza la solicitud GET para obtener los datos de la carta
        const res = await fetch(endpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`,
                'X-CSRFToken': `${csrftoken}`
            },
            credentials : 'include'
        });


        // Verifica si la solicitud fue exitosa (código de respuesta 200)
        if (res.ok) {
            // Extrae los datos JSON de la respuesta
            const user = await res.json();
            UserStore.set(user);
            // Devuelve las cartas cargadas junto con su ID
            return { user };
        } else {
            // Si la solicitud no fue exitosa, lanza un error con el mensaje de estado
            throw new Error(`Failed to fetch user: ${res.status} ${res.statusText}`);
        }
    } catch (error) {
        // Maneja cualquier error que ocurra durante la carga de la carta
        console.error('Error loading user:', error);

        // Devuelve un objeto vacío en caso de error
        return { user: null };
    }
}
