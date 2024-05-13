
/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params }) {
    const endpoint = 'http://127.0.0.1:8000/users/2/notebooks/';
    const res = await fetch(endpoint);
    const data = await res.json();
    const notebooks = data.notebooks;
    const notes = [];

    // Itera sobre cada cuaderno y carga las notas
    for (const notebook of notebooks) {
        const notesEndpoint = `http://localhost:8000/notebooks/${notebook.id}/notes/`;
        const notesRes = await fetch(notesEndpoint);
        const notesData = await notesRes.json();
        notes.push(notesData);
    }

    // Devuelve las notas cargadas
    return { notes };
}
