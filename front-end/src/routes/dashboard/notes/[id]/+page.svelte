<script>
    import {NoteStore} from '../../../../note-store.js'
    import { onMount } from "svelte";
    import SvelteMarkdown from 'svelte-markdown';
    import {Pencil} from "phosphor-svelte";
    import NewNote from "../../../../components/Forms/NewNote.svelte";

    export let data;
    /**
	 * @type {{ title: any; content: any; } | null}
	 */


    console.log(data)


    const note = data.note;


    async function handleSubmit() {
        console.log(JSON.stringify(note))
        try {
            const response = await fetch(`http://127.0.0.1:8000/notes/${note.id}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(note)
            });

            if (response.ok) {
                console.log('Form submitted successfully!');
            } else {
                console.error('Failed to submit form');
            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
        }
    }

    const title = `# Title:`





    
</script>

{#if note}
    <div class="container-md" >
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            <div class="d-flex align-items-center">
                <Pencil/>
                Edit note
            </div>
        </button>
            <div>
                <div class="card bg-secondary mb-3" style="max-width: 900px;max-height: 800px;min-width: 720px;min-height: 400px;">
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

        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Add note</h5>
                    </div>
                    <form on:submit|preventDefault={handleSubmit}>
                        <div class="modal-body">

                            <div class="mb-3">
                                <label for="title" class="form-label">Title</label>
                                <input type="text" bind:value={note.title} style="color:black"  class="form-control" id="title"  placeholder="Type in Markdown">
                            </div>
                            <div class="mb-3">
                                <label for="content" class="form-label">Content</label>
                                <textarea bind:value={note.content} style="color:black" class="form-control" id="content" rows="10" placeholder="Type in Markdown"></textarea>
                            </div>

                        </div>

                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                            <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>


    </div>
    {:else }
        <h2>No se encontro la nota con id: {data.id}</h2>
    {/if}

