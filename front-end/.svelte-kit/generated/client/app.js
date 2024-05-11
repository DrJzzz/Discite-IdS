export { matchers } from './matchers.js';

export const nodes = [
	() => import('./nodes/0'),
	() => import('./nodes/1'),
	() => import('./nodes/2'),
	() => import('./nodes/3'),
	() => import('./nodes/4'),
	() => import('./nodes/5'),
	() => import('./nodes/6'),
	() => import('./nodes/7'),
	() => import('./nodes/8'),
	() => import('./nodes/9'),
	() => import('./nodes/10'),
	() => import('./nodes/11'),
	() => import('./nodes/12'),
	() => import('./nodes/13')
];

export const server_loads = [];

export const dictionary = {
		"/": [3],
		"/dashboard": [4,[2]],
		"/dashboard/decks": [5,[2]],
		"/dashboard/decks/[id]": [6,[2]],
		"/dashboard/notes": [7,[2]],
		"/dashboard/notes/[id]": [8,[2]],
		"/dashboard/settings": [9,[2]],
		"/dashboard/user": [10,[2]],
		"/landing": [11],
		"/login": [12],
		"/signIn": [13]
	};

export const hooks = {
	handleError: (({ error }) => { console.error(error) }),

	reroute: (() => {})
};

export { default as root } from '../root.svelte';