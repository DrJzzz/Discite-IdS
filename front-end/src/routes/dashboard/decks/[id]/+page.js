import {getCookie} from "../../../../utils/csrf.js";
import {SingleCardStore} from "../../../../stores.js";
import {HistoryStore} from "../../../../stores.js";
import {TagStore} from "../../../../stores.js";

/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params }) {
	try {
		// Construye la URL del endpoint usando el parámetro de la carta ID
		const endpoint = `http://localhost:8000/fcards/${params.id}/`;
		const token = localStorage.getItem('key');
		const csrftoken = getCookie('csrftoken');
		// Realiza la solicitud GET para obtener los datos de la carta
		const res = await fetch(endpoint, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				'X-CSRFToken': `${csrftoken}`,
				'Authorization': `Token ${token}`
			},
			credentials : 'include',
		});

		// Verifica si la solicitud fue exitosa (código de respuesta 200)
		if (res.ok) {
			// Extrae los datos JSON de la respuesta
			const card = await res.json();

			const endpointHistory = `http://localhost:8000/cards/${params.id}/get_history/`;

			// Realiza la solicitud GET para obtener los datos de la carta
			const resHistory = await fetch(endpointHistory, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': `${csrftoken}`,
					'Authorization': `Token ${token}`
				},
				credentials : 'include',
			});

			if (resHistory.ok){
				const history = await resHistory.json()
				SingleCardStore.set(card);
				HistoryStore.set(history.history);
				// Devuelve las cartas cargadas junto con su ID
				const tagsEndpoint = 'http://localhost:8000/tags/';
				const tagsRes = await fetch(tagsEndpoint, {
					method: 'GET',
					headers: {
						'Content-Type': 'application/json',
						'X-CSRFToken': `${csrftoken}`,
						'Authorization': `Token ${token}`,
					},
					credentials: 'include'
				});

				if (tagsRes.ok){
					const tagsJSON = await tagsRes.json();
					const tags = tagsJSON.results;
					TagStore.set(tags);
				}

				return { card, id: params.id, history };
			}else {
				SingleCardStore.set(card);
				return { card, id: params.id, history : [] };
			}

		} else {
			// Si la solicitud no fue exitosa, lanza un error con el mensaje de estado
			throw new Error(`Failed to fetch card: ${res.status} ${res.statusText}`);
		}
	} catch (error) {
		// Maneja cualquier error que ocurra durante la carga de la carta
		console.error('Error loading card:', error);

		// Devuelve un objeto vacío en caso de error
		return { card: [], id: params.id, history : [] };
	}
}
