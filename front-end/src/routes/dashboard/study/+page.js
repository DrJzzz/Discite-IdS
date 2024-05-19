/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params }) {
    try {
        // Construye la URL del endpoint usando el parámetro de la carta ID
        const endpoint = `http://localhost:8000/decks/1/to_review/`;

        // Realiza la solicitud GET para obtener los datos de la carta
        const res = await fetch(endpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials : 'include',
        });


        // Verifica si la solicitud fue exitosa (código de respuesta 200)
        if (res.ok) {
            // Extrae los datos JSON de la respuesta
            const data = await res.json();
            console.log(data)
            const values = data.values;

            const cards = [];

            // Itera sobre cada cuaderno y carga las notas
            for (const value of values) {
                if (value.count == 0){
                    continue;
                }
                for (const cardtemp of value.cards){
                    const cardsEndpoint = `http://localhost:8000/cards/${cardtemp.id}/`;
                    const cardsRes = await fetch(cardsEndpoint, {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        credentials : 'include',
                    });

                    const cardsData = await cardsRes.json();
                    cards.push(cardsData);
                }
            }



            // Devuelve las cartas cargadas junto con su ID
            return { cards };
        } else {
            // Si la solicitud no fue exitosa, lanza un error con el mensaje de estado
            throw new Error(`Failed to fetch card: ${res.status} ${res.statusText}`);
        }
    } catch (error) {
        // Maneja cualquier error que ocurra durante la carga de la carta
        console.error('Error loading cards list:', error);

        // Devuelve un objeto vacío en caso de error
        return { cards: null };
    }
}
