import {getCookie} from "../../../utils/csrf.js";
import {UserStore} from "../../../stores.js";
/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params }) {
    try {
        const token =typeof localStorage !== 'undefined' ? localStorage.getItem('key') : '';
        const csrftoken = getCookie('csrftoken');
        // Construye la URL del endpoint usando el parámetro de la carta ID
        const endpoint = `http://localhost:8000/rest-auth/user/`;

        // Realiza la solicitud GET para obtener los datos de la carta
        const res = await fetch(endpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`,
                'X-CSRFToken': `${csrftoken}`
            },
            credentials : 'include',
        });


        // Verifica si la solicitud fue exitosa (código de respuesta 200)
        if (res.ok) {
            // Extrae los datos JSON de la respuesta
            const user = await res.json();
            const endpointImg = `http://localhost:8000/users/${user.id}/get_picture/`;
            const resImage = await fetch(endpointImg, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                credentials : 'include',
            });

            const endpointTotal = `http://localhost:8000/users/${user.id}/total/`;
            const resTotal = await fetch(endpointTotal, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                credentials : 'include',
            });
            const total = await resTotal.json();
            const imgJson = await resImage.json();
            console.log(imgJson)
            const img = imgJson.picture;
            UserStore.set(user);
            // Devuelve las cartas cargadas junto con su ID
            return { user , img, total};
        } else {
            // Si la solicitud no fue exitosa, lanza un error con el mensaje de estado
            return {user : [], img : "", total : []}
        }
    } catch (error) {
        // Maneja cualquier error que ocurra durante la carga de la carta
        console.error('Error loading user:', error);

        // Devuelve un objeto vacío en caso de error
        return { user: [], img : '' , total : []};
    }
}
