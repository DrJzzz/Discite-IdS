<script>
    import {CardStore} from "../../../card-store.js"
    import {onMount} from "svelte";
    import {NoteStore} from "../../../note-store.js";
    import NewCard from "../../../components/Forms/NewCard.svelte";


    onMount(async function() {
        const endpoint = 'http://127.0.0.1:8000/cards/'
        const response = await fetch(endpoint)
        const data = await response.json()
        CardStore.set(data.results)
    });


</script>


<div>
    <!-- Botón que activa el modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
        Agregar carta
    </button>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <NewCard/>
            </div>
        </div>
    </div>
</div>