<script>
    import {NoteStore} from '../../../note-store.js'
    import {onMount} from 'svelte'
    import { goto } from '$app/navigation';
    import { writable } from "svelte/store";
    import NewNote from "../../../components/Forms/NewNote.svelte";
    import SvelteMarkdown from "svelte-markdown";
    import {Plus} from "phosphor-svelte";
    import NewNotebook from "../../../components/Forms/NewNotebook.svelte";
    import {CardStore} from "../../../card-store.js";

    let isMounted = writable(false);
    function navigateToNote(id) {
        goto(`/dashboard/notes/${id}`);
    }

    onMount(async function() {
        const endpoint = 'http://127.0.0.1:8000/users/1/notebooks/'
        const response = await fetch(endpoint)
        const data = await response.json()
        if (data.notebooks.length > $NoteStore.length){
            NoteStore.set([]);

            const notebooks = data.notebooks;
            console.log(data)
            Object.keys(notebooks).forEach(key => {
                note(notebooks[key].id)
            })
        }
        isMounted.set(true);
    } )

    async function note(id) {
        const endpointCard = `http://localhost:8000/notebooks/${id}/notes/`
        const response = await fetch(endpointCard)
        const data = await response.json()
        console.log(data)
        $NoteStore.push(data)
    }

</script>
<style>
    .card-view{
        cursor: pointer;
    }
</style>
<!-- Botón que activa el modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
    <div class="d-flex align-items-center">
        <Plus />
        Add note
    </div>
</button>
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#notebookModal">
    <div class="d-flex align-items-center">
        <Plus />
        Add notebook
    </div>
</button>
{#if $isMounted}
    <div class="accordion" id="accordionPanelsStayOpenExample">
        {#each $NoteStore as data}
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse{data.notebook.id}" aria-expanded="true" aria-controls="panelsStayOpen-collapse{data.notebook.id}">
                        {data.notebook.name}
                    </button>
                </h2>
                <div id="panelsStayOpen-collapse{data.notebook.id}" class="accordion-collapse collapse">
                    <div class="accordion-body">
                        <div class="list-group">
                            {#each data.notes as note}
                                <a on:click={() => navigateToNote(note.id)}    class="list-group-item list-group-item-action active card-view" aria-current="true">
                                    <div class="d-flex w-100 justify-content-between">
                                        <SvelteMarkdown source="{note.title}"/>
                                    </div>
                                </a>
                            {/each}
                        </div>
                    </div>
                </div>
            </div>
        {/each}
    </div>
{:else }
    <div>
        <h3>Cargando..</h3>
    </div>
{/if}

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <NewNote/>
        </div>
    </div>
</div>

<div class="modal fade" id="notebookModal" tabindex="-1" aria-labelledby="notebookModal" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <NewNotebook/>
        </div>
    </div>
</div>