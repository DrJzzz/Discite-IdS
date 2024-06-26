import { getCookie } from '../../utils/csrf';
import {HomeStore} from "../../stores.js";
import {TagStore} from "../../stores.js";

/** @type {import('./$types').PageLoad} */
export async function load({ parent, fetch, params  }) {

    try {
        const user = await parent();

        // Verificar si se obtuvo el usuario correctamente
        if (!user) {
            console.error("No se pudo obtener el usuario del UserStore");
            return;
        }
        const token =typeof localStorage !== 'undefined' ? localStorage.getItem('key') : '';
        const csrftoken = getCookie('csrftoken');
        const endpoint = `http://127.0.0.1:8000/users/${user.user.id}/decks/`;
        const res = await fetch(endpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': `${csrftoken}`,
                'Authorization': `Token ${token}`,
            },
            credentials : 'include',
        });

        if (res.ok){
            const data = await res.json();
            const decks = data.decks;

            const endpointUsers = `http://127.0.0.1:8000/users/user_public_preview/`;
            const resUsers = await fetch(endpointUsers, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                credentials : 'include'
            });

            if (resUsers.ok){
                const users = await resUsers.json();
                HomeStore.set(users);
                const tagsEndpoint = 'http://localhost:8000/tags/';
                const tagsRes = await fetch(tagsEndpoint, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': `${csrftoken}`,
                        'Authorization': `Token ${token}`,
                    },
                    credentials: 'include'
                });
                const tagsJSON = await tagsRes.json();
                const tags = tagsJSON.results;
                TagStore.set(tags);
                return {decks, users}

            }
            HomeStore.set([]);
            return { decks, users : []};
        }
        // Devuelve las notas cargadas
        return {decks: [], users: []}
    }catch (error){
        return {decks: [], users: []}
    }

}

