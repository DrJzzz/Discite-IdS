import {getCookie} from "../../../utils/csrf.js";
import {CardStore} from "../../../card-store.js";
import {UsersStore} from "../../../users-store.js";

/** @type {import('./$types').PageLoad} */
export async function load({ parent, fetch, params }) {
    try {
        const user = await parent();

        if (!user) {
            console.error("No se pudo obtener el usuario del UserStore");
            return;
        }

        const csrftoken = getCookie('csrftoken');
        const token = localStorage.getItem('key');
        const endpoint = `http://127.0.0.1:8000/users/${user.user.id}/decks/`;
        const res = await fetch(endpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': `${csrftoken}`,
                'Authorization': `Token ${token}`
            },
            credentials: 'include'
        });

        const data = await res.json();
        const decks = data.decks;
        const cards = [];

        for (const deck of decks) {
            const cardsEndpoint = `http://localhost:8000/decks/${deck.id}/cards/`;
            const cardsRes = await fetch(cardsEndpoint, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': `${csrftoken}`,
                    'Authorization': `Token ${token}`
                },
                credentials: 'include'
            });

            const cardsData = await cardsRes.json();
            cards.push(cardsData);
        }

        const usersEndpoint = 'http://127.0.0.1:8000/users/list_all/';
        const usersRes = await fetch(usersEndpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': `${csrftoken}`,
                'Authorization': `Token ${token}`
            },
            credentials: 'include'
        });

        const usersJSON = await usersRes.json();
        const users = usersJSON.users;
        CardStore.set(cards);
        UsersStore.set(users);
        return { cards, users };
    } catch (error) {
        console.error("Error fetching data:", error);
        return { cards: [], users: [] };
    }
}
