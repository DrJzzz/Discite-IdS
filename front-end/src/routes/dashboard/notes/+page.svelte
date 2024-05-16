<script>
    import {NoteStore} from '../../../note-store.js'
    import {onMount} from 'svelte'
    import { goto } from '$app/navigation';
    import { writable } from "svelte/store";
    import NewNote from "../../../components/Forms/NewNote.svelte";
    import SvelteMarkdown from "svelte-markdown";
    import {Plus} from "phosphor-svelte";
    import NewNotebook from "../../../components/Forms/NewNotebook.svelte";

    /** @type {import('./$types').PageData} */
    export let data;
    function navigateToNote(id) {
        goto(`/dashboard/notes/${id}`);
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
{#if data}
    <div class="accordion" id="accordionPanelsStayOpenExample">
        {#each data.notes as info}
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse{info.notebook.id}" aria-expanded="true" aria-controls="panelsStayOpen-collapse{info.notebook.id}">
                        {info.notebook.name}
                    </button>
                </h2>
                <div id="panelsStayOpen-collapse{info.notebook.id}" class="accordion-collapse collapse">
                    <div class="accordion-body">
                        <div class="list-group">
                            {#each info.notes as note}
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