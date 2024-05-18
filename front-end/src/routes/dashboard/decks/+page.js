import {UserStore} from "../../../user-store.js";
/** @type {import('./$types').PageLoad} */
export async function load({ parent, fetch, params  }) {

    try {
        const user = await parent();
        // Verificar si se obtuvo el usuario correctamente
        if (!user) {
            console.error("No se pudo obtener el usuario del UserStore");
            return;
        }

        const endpoint = `http://127.0.0.1:8000/users/${user.user.id}/decks/`;
        const res = await fetch(endpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials : 'include',
        });

        const data = await res.json();
        const decks = data.decks;
        const cards = [];

        // Itera sobre cada cuaderno y carga las notas
        for (const deck of decks) {
            const cardsEndpoint = `http://localhost:8000/decks/${deck.id}/cards/`;
            const cardsRes = await fetch(cardsEndpoint, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                },
                credentials : 'include',
            });

            const cardsData = await cardsRes.json();
            cards.push(cardsData);
        }

        const usersEndpoint = 'http://127.0.0.1:8000/users/list_all/';
        const usersRes = await fetch(usersEndpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials : 'include'
        });

        const usersJSON = await usersRes.json();
        const users = usersJSON.users;
        console.log(users)

        // Devuelve las notas cargadas
        return { cards , users };
    }catch (error){
        return {cards : null, users: null}
    }

}
