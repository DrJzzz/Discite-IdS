
/** @type {import('./$types').PageLoad} */
export async function load({parent, fetch, params }) {
    const user = await parent();
    // Verificar si se obtuvo el usuario correctamente
    if (!user) {
        console.error("No se pudo obtener el usuario del UserStore");
        return;
    }
    const endpoint = `http://127.0.0.1:8000/users/${user.user.id}/notebooks/`;
    const res = await fetch(endpoint, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials : 'include',
    });

    const data = await res.json();
    const notebooks = data.notebooks;
    const notes = [];

    // Itera sobre cada cuaderno y carga las notas
    for (const notebook of notebooks) {
        const notesEndpoint = `http://localhost:8000/notebooks/${notebook.id}/notes/`;
        const notesRes = await fetch(notesEndpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials : 'include',
        });

        const notesData = await notesRes.json();
        notes.push(notesData);
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

    // Devuelve las notas cargadas
    return { notes, users };
}
