/** @type {import('./$types').PageLoad} */
export async function load({ parent, fetch, params }) {
    try {
        const user = await parent();

        if (!user) {
            console.error("No se pudo obtener el usuario del UserStore");
            return;
        }

        const csrftoken = getCookie('csrftoken');

        const endpoint = `http://127.0.0.1:8000/users/${user.user.id}/notebooks/`;
        const res = await fetch(endpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
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
                    'X-CSRFToken': csrftoken
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
                'X-CSRFToken': csrftoken
            },
            credentials: 'include'
        });

        const usersJSON = await usersRes.json();
        const users = usersJSON.users;

        return { notes, users };
    } catch (error) {
        console.error("Error fetching data:", error);
        return { notes: [], users: [] };
    }
}
// Función para obtener el token CSRF desde las cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
