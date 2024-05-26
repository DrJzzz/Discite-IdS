import { getCookie } from '../../../utils/csrf';
import {NoteStore} from "../../../note-store.js";
import {UsersStore} from "../../../users-store.js";
import {NotebookStore} from "../../../notebook-store.js";
import {TagStore} from "../../../tag-store.js";

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
        const endpoint = `http://127.0.0.1:8000/users/${user.user.id}/notebooks/`;
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
        const notebooks = data.notebooks;
        const notes = [];

        for (const notebook of notebooks) {
            const notesEndpoint = `http://localhost:8000/notebooks/${notebook.id}/notes/`;
            const notesRes = await fetch(notesEndpoint, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': `${csrftoken}`,
                    'Authorization': `Token ${token}`
                },
                credentials: 'include'
            });

            const notesData = await notesRes.json();
            notes.push(notesData);
        }

        const usersEndpoint = 'http://127.0.0.1:8000/users/list_all/';

        const usersRes = await fetch(usersEndpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': `${csrftoken}`,
                'Authorization': `Token ${token}`,
            },
            credentials: 'include'
        });

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

        const usersJSON = await usersRes.json();
        const users = usersJSON.users;
        const tagsJSON = await tagsRes.json();
        const tags = tagsJSON.results;
        console.log(tags);
        TagStore.set(tags);
        NoteStore.set(notes);
        UsersStore.set(users);
        NotebookStore.set(notebooks);
        return { notes, users };
    } catch (error) {
        console.error("Error fetching data:", error);
        return { notes: [], users: [] };
    }
}
