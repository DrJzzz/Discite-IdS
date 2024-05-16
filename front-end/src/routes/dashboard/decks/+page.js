
/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params }) {
    const endpoint = 'http://127.0.0.1:8000/users/1/decks/';
    const res = await fetch(endpoint, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials : 'include',
    });

    const data = await res.json();
    const decks = data.decks;
    const cards = [];

    // Itera sobre cada cuaderno y carga las notas
    for (const deck of decks) {
        const cardsEndpoint = `http://localhost:8000/decks/${deck.id}/cards/`;
        const cardsRes = await fetch(cardsEndpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials : 'include',
        });

        const cardsData = await cardsRes.json();
        console.log(cardsData)
        cards.push(cardsData);
    }

    // Devuelve las notas cargadas
    return { cards };
}
