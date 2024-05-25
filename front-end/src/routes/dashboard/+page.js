/** @type {import('./$types').PageLoad} */
export async function load({ parent, fetch, params  }) {

    try {
        const user = await parent();

        // Verificar si se obtuvo el usuario correctamente
        if (!user) {
            console.error("No se pudo obtener el usuario del UserStore");
            return;
        }
        const token = localStorage.getItem('key');
        const csrftoken = getCookie('csrftoken');
        const endpoint = `http://127.0.0.1:8000/users/${user.user.id}/decks/`;
        const res = await fetch(endpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': `${csrftoken}`
            },
            credentials : 'include',
        });

        if (res.ok){
            const data = await res.json();
            const decks = data.decks;

            const endpointUsers = `http://127.0.0.1:8000/users/user_public_preview/`;
            const resUsers = await fetch(endpointUsers, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                credentials : 'include'
            });

            if (resUsers.ok){
                const users = await resUsers.json()
                return {decks, users}
            }

            return { decks, users : []};
        }





        // Devuelve las notas cargadas
        return {decks: [], users: []}
    }catch (error){
        return {decks: [], users: []}
    }

}

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