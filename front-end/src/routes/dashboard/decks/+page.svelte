<script>
    import {CardStore} from "../../../card-store.js"
    import {onMount} from "svelte";
    import {NoteStore} from "../../../note-store.js";
    import NewCard from "../../../components/Forms/NewCard.svelte";
    import SvelteMarkdown from "svelte-markdown";
    import {goto} from "$app/navigation";
    import {Plus} from "phosphor-svelte";
    import {S} from "../../../../.svelte-kit/output/client/_app/immutable/chunks/index.BBeg5s6H.js";
    function navigateToCard(id) {
        goto(`/dashboard/decks/${id}`);
    }

    const id = "5";

    let decks;

    onMount(async function() {

        

        const endpoint = 'http://127.0.0.1:8000/decks/1/cards/'
        const response = await fetch(endpoint)
        decks = await response.json()
        CardStore.set(decks.results)
    });





</script>

<style>
    .card-view{
        cursor: pointer;
    }
</style>


<div>
    <!-- Botón que activa el modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
        <div class="d-flex align-items-center">
            <Plus />
            Add card
        </div>
    </button>

    {#if decks}
        <div class="accordion" id="accordionPanelsStayOpenExample">
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseOne" aria-expanded="true" aria-controls="panelsStayOpen-collapseOne">
                        {decks.deck.name}
                    </button>
                </h2>
                <div id="panelsStayOpen-collapseOne" class="accordion-collapse collapse show">
                    <div class="accordion-body">
                        <div class="list-group">
                            {#each decks.cards as card}
                                <a on:click={() => navigateToCard(card.id)}    class="list-group-item list-group-item-action active card-view" aria-current="true">
                                    <div class="d-flex w-100 justify-content-between">
                                        <SvelteMarkdown source="{card.front}"/>
                                        <small class="text-light">{card.modified}</small>
                                    </div>
                                </a>
                            {/each}
                        </div>
                    </div>
                </div>
            </div>
        </div>

    {/if}
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <NewCard/>
            </div>
        </div>
    </div>


</div>

