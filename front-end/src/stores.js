import { writable } from "svelte/store";

export let StudyCards = writable([]);

export let CardStore = writable([]);
export let DeckStore = writable([]);
export let HistoryStore = writable([]);

export let HomeStore = writable([]);

export let ImagesStore = writable([]);

export let NoteStore = writable([]);

export let NotebookStore = writable([]);

export let SharedDeckStore = writable([]);

export let SharedNotebookStore = writable([]);

export let SingleCardStore = writable([]);

export let SingleNoteStore = writable([]);

export let TagStore = writable([]);

export let UserStore = writable([]);

export const UsersStore = writable([]);