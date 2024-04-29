<script>
    import {NoteStore} from '../../../note-store.js'
    import {onMount} from 'svelte'
    import { goto } from '$app/navigation';
    import NewNote from "../../../components/Forms/NewNote.svelte";
    import SvelteMarkdown from "svelte-markdown";
    import {Plus} from "phosphor-svelte";

    function navigateToNote(id) {
        goto(`/dashboard/notes/${id}`);
    }

    onMount(async function() {
        const endpoint = 'http://127.0.0.1:8000/notes/'
        const response = await fetch(endpoint)
        const data = await response.json()
        console.log(data)
        console.log(data.results.length)
        NoteStore.set(data.results)

    } )

</script>

<h1> Displaying notes </h1>

<!-- Botón que activa el modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
    <div class="d-flex align-items-center">
        <Plus />
        Add note
    </div>
</button>

<div>
    <h2>Notes List</h2>
    
    <div>
        {#each $NoteStore as note}
       
        <div class="col-12 col-sm-6 col-md-4">
            
            <div class="card w-100 h-100">
            
                <div class="card-body d-flex flex-column justify-content-between gap-4">
					<div>
                        <SvelteMarkdown source="{note.title}"/>
                       
                    </div>
                    <div>
                        <a on:click={() => navigateToNote(note.id)} class="btn btn-primary" >View</a>
					</div>
                </div>
              </div>

        </div>
        {/each}
    </div>
    
</div>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <NewNote/>
        </div>
    </div>
</div>