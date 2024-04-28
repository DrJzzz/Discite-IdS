<script>
    import {NoteStore} from '../../../../note-store.js'
    import { onMount } from "svelte";
    import SvelteMarkdown from 'svelte-markdown';
    import {Pencil} from "phosphor-svelte";

    export let data;
    /**
	 * @type {{ title: any; content: any; } | null}
	 */
    let note;

    onMount(async function() {
        if ($NoteStore.length) {
            note = $NoteStore.find(film => film.id == data.id)
        } else {
            const endpoint = `http://localhost:8000/notes/notes/${data.id}/`
            let response = await fetch(endpoint)
            if (response.status == 200) {
                note = await response.json()
            } else {
                note = null;
            }
        }
    })

    const title = `# Title:`





    
</script>

{#if note}
    <div class="container-md">
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            <div class="d-flex align-items-center">
                <Pencil/>
                Edit note
            </div>
        </button>
            <div>
                <div class="card bg-secondary mb-3" style="max-width: 900px;max-height: 800px">
                    <div class="card-header">
                        <div class="d-flex align-items-center">
                            <SvelteMarkdown source="{title}" />
                            <SvelteMarkdown source="{note.title}" />
                        </div>

                    </div>
                    <div class="card-body">
                        <SvelteMarkdown source="{note.content}" />
                    </div>
                </div>
            </div>


    </div>
    {:else }
        <h2>No se encontro la nota con id: {data.id}</h2>
    {/if}

