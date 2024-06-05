import {getCookie} from "../../../utils/csrf.js";
import {SharedDeckStore} from '../../../stores.js';
import {SharedNotebookStore} from '../../../stores.js';
import {TagStore} from "../../../stores.js";
import { get } from 'svelte/store';
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
        SharedDeckStore.set(cards);
        SharedNotebookStore.set(notes);
        replaceTagIdsWithNamesNotebooks()
        replaceTagIdsWithNamesDecks()
        // Devuelve las notas cargadas
        return { cards, notes };
    }catch (error){
        return {cards : null, notes : null}
    }

}

// Función para reemplazar ids por nombres en CardStore
function replaceTagIdsWithNamesNotebooks() {
    let tags = get(TagStore);
    let notesData = get(SharedNotebookStore);
    let tagDict = {};
    tags.forEach(tag => {
        tagDict[tag.id] = tag.name;
    });
    notesData.forEach(notebook => {
        notebook.notes.forEach(note => {
            note.tags = note.tags.map(tagId => tagDict[tagId]);
        });
    });
    SharedNotebookStore.set(notesData);
}

// Función para reemplazar ids por nombres en CardStore
function replaceTagIdsWithNamesDecks() {
    let tags = get(TagStore);
    let cardsData = get(SharedDeckStore);
    let tagDict = {};
    tags.forEach(tag => {
        tagDict[tag.id] = tag.name;
    });
    cardsData.forEach(deck => {
        deck.cards.forEach(card => {
            card.tags = card.tags.map(tagId => tagDict[tagId]);
        });
    });
    SharedDeckStore.set(cardsData);
}


