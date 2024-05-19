/** @type {import('./$types').PageLoad} */
export async function load({ parent, fetch, params }) {
    try {
        const user = await parent();

        // Verificar si se obtuvo el usuario correctamente
        if (!user || !user.user || !user.user.id) {
            console.error("No se pudo obtener el usuario del UserStore");
            return { notes: [], users: [] }; // Retorna valores por defecto
        }

        const userId = user.user.id;

        // URLs de los endpoints
        const notebooksEndpoint = `http://127.0.0.1:8000/users/${userId}/notebooks/`;
        const usersEndpoint = 'http://127.0.0.1:8000/users/list_all/';

        // Fetch requests paralelas
        const [notebooksRes, usersRes] = await Promise.all([
            fetch(notebooksEndpoint, {
                method: 'GET',
                headers: { 'Content-Type': 'application/json' },
                credentials: 'include'
            }),
            fetch(usersEndpoint, {
                method: 'GET',
                headers: { 'Content-Type': 'application/json' },
                credentials: 'include'
            })
        ]);

        const notebooksData = await notebooksRes.json();
        const usersData = await usersRes.json();
        console.log(usersData)

        const notebooks = notebooksData.notebooks || [];
        const users = usersData.users || [];

        // Fetch de notas en paralelo
        const notesPromises = notebooks.map(async (notebook) => {
            const notesEndpoint = `http://localhost:8000/notebooks/${notebook.id}/notes/`;
            const notesRes = await fetch(notesEndpoint, {
                method: 'GET',
                headers: { 'Content-Type': 'application/json' },
                credentials: 'include',
            });
            const notesData = await notesRes.json();
            return notesData;
        });

        const notes = await Promise.all(notesPromises);

        // Devuelve las notas y usuarios cargados
        return { notes, users };

    } catch (error) {
        console.error("Error al cargar los datos:", error);
        return { notes: [], users: [] }; // Retorna valores por defecto en caso de error
    }
}

