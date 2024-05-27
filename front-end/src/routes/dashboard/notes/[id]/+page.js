import {getCookie} from "../../../../utils/csrf.js";
import {SingleNoteStore} from "../../../../single-note-store.js";
import {HistoryStore} from "../../../../history-store.js";

/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params }) {

	try{
		const endpoint = `http://localhost:8000/notes/${params.id}/`;
		const csrftoken = getCookie('csrftoken');
		const token = localStorage.getItem('key');
		const res = await fetch(endpoint, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				'X-CSRFToken': `${csrftoken}`,
				'Authorization': `Token ${token}`
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
					'X-CSRFToken': `${csrftoken}`,
					'Authorization': `Token ${token}`
				},
				credentials: 'include'
			});

			if (resHistory.ok) {
				const history = await resHistory.json()
				// Devuelve las cartas cargadas junto con su ID
				SingleNoteStore.set(note);
				HistoryStore.set(history.history);

				return {note, id: params.id, history};
			} else {
				SingleNoteStore.set(note);
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
