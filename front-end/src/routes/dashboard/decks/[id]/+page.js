/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params }) {
	try {
		// Construye la URL del endpoint usando el parámetro de la carta ID
		const endpoint = `http://localhost:8000/fcards/${params.id}/`;

		// Realiza la solicitud GET para obtener los datos de la carta
		const res = await fetch(endpoint);

		// Verifica si la solicitud fue exitosa (código de respuesta 200)
		if (res.ok) {
			// Extrae los datos JSON de la respuesta
			const card = await res.json();

			// Devuelve las cartas cargadas junto con su ID
			return { card, id: params.id };
		} else {
			// Si la solicitud no fue exitosa, lanza un error con el mensaje de estado
			throw new Error(`Failed to fetch card: ${res.status} ${res.statusText}`);
		}
	} catch (error) {
		// Maneja cualquier error que ocurra durante la carga de la carta
		console.error('Error loading card:', error);

		// Devuelve un objeto vacío en caso de error
		return { card: null, id: params.id };
	}
}
