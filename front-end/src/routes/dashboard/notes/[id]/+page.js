/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params }) {

	try{
		const endpoint = `http://localhost:8000/notes/${params.id}/`;
		const csrftoken = getCookie('csrftoken');
		const res = await fetch(endpoint, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				'X-CSRFToken': `${csrftoken}`
			},
			credentials : 'include'
		});
		if (res.ok) {
			const note = await res.json();
			const endpointHistory = `http://localhost:8000/notes/${params.id}/get_history/`;
			// Realiza la solicitud GET para obtener los datos deñ historu
			const resHistory = await fetch(endpointHistory, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': `${csrftoken}`
				},
				credentials: 'include'
			});

			if (resHistory.ok) {
				const history = await resHistory.json()
				// Devuelve las cartas cargadas junto con su ID
				return {note, id: params.id, history};
			} else {
				return {note, id: params.id, history: []};
			}

		} else {
			// Si la solicitud no fue exitosa, lanza un error con el mensaje de estado
			throw new Error(`Failed to fetch card: ${res.status} ${res.statusText}`);
		}


	}catch (error){
		// Maneja cualquier error que ocurra durante la carga de la carta
		console.error('Error loading note:', error);

		// Devuelve un objeto vacío en caso de error
		return { card: [], id: params.id, history : [] };
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
