import {getCookie} from "../../../utils/csrf.js";
import {SharedDeckStore} from '../../../shared-deck-store.js';
import {SharedNotebookStore} from '../../../shared-notebook-store.js';
/** @type {import('./$types').PageLoad} */
export async function load({ parent, fetch, params  }) {

    try {
        const token = localStorage.getItem('key');
        const csrftoken = getCookie('csrftoken');
        const endpoint = `http://localhost:8000/shared/shared_with_me/`;
        const res = await fetch(endpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`,
                'X-CSRFToken': `${csrftoken}`
            },
            credentials : 'include'
        });

        const data = await res.json();
        const values = data.values;
        const cards = [];
        const notes = [];
        // Itera sobre cada cuaderno y carga las notas
        for (const value of values) {

            if(value.type == 1){
                const cardsEndpoint = `http://localhost:8000/decks/${value.id}/cards/`;
                const cardsRes = await fetch(cardsEndpoint, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Token ${token}`,
                        'X-CSRFToken': `${csrftoken}`
                    },
                    credentials : 'include'
                });

                const cardsData = await cardsRes.json();
                cards.push(cardsData);
            }else {
                const notesEndpoint = `http://localhost:8000/notebooks/${value.id}/notes/`;
                const notesRes = await fetch(notesEndpoint, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Token ${token}`,
                        'X-CSRFToken': `${csrftoken}`
                    },
                    credentials : 'include'
                });

                const notesData = await notesRes.json();
                notes.push(notesData);
            }

        }

        SharedDeckStore.set(cards);
        SharedNotebookStore.set(notes);
        // Devuelve las notas cargadas
        return { cards, notes };
    }catch (error){
        return {cards : null, notes : null}
    }

}

