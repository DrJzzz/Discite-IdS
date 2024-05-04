/** @type {import('../../../../../.svelte-kit/types/src/routes').PageLoad} */
export function load({ params }) {
	return {
		id : params.id
	};
}