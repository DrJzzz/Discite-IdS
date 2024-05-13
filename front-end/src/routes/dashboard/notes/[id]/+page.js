/** @type {import('./$types').PageLoad} */
export async function load({ fetch, params }) {
	console.log(params.id)
	const endpoint = `http://localhost:8000/notes/${params.id}/`;
	const res = await fetch(endpoint);
	const note = await res.json();



	// Devuelve las notas cargadas
	return { note };
}