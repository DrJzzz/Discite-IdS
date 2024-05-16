<script>

    import NewCard from "../../../components/Forms/NewCard.svelte";
    import SvelteMarkdown from "svelte-markdown";
    import {goto} from "$app/navigation";
    import {Plus} from "phosphor-svelte";
    import NewDeck from "../../../components/Forms/NewDeck.svelte";

    /** @type {import('./$types').PageData} */
    export let data;
    function navigateToCard(id) {
        goto(`/dashboard/decks/${id}`);
    }


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
    <!-- Botón que activa el modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#deckModal">
        <div class="d-flex align-items-center">
            <Plus />
            Add deck
        </div>
    </button>
    {#if data}
            <div class="accordion" id="accordionPanelsStayOpenExample">
            {#each data.cards as info}
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse{info.deck.id}" aria-expanded="true" aria-controls="panelsStayOpen-collapse{info.deck.id}">
                            {info.deck.name}
                        </button>
                    </h2>
                    <div id="panelsStayOpen-collapse{info.deck.id}" class="accordion-collapse collapse">
                        <div class="accordion-body">
                            <div class="list-group">
                                {#each info.cards as card}
                                    <a on:click={() => navigateToCard(card.id)}    class="list-group-item list-group-item-action active card-view" aria-current="true">
                                        <div class="d-flex w-100 justify-content-between">
                                            <p>Card {card.id}</p>
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
                <NewCard/>
            </div>
        </div>
    </div>
    <div class="modal fade" id="deckModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <NewDeck/>
            </div>
        </div>
    </div>
</div>
