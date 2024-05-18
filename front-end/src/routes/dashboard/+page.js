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



        // Devuelve las notas cargadas
        return { decks};
    }catch (error){
        return {decks: null}
    }

}