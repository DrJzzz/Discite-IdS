<script>
    import {CardStore} from "../../../card-store.js"
    import {DeckStore} from "../../../deck-store.js";
    import { writable } from "svelte/store";
    import {onMount} from "svelte";
    import NewCard from "../../../components/Forms/NewCard.svelte";
    import SvelteMarkdown from "svelte-markdown";
    import {goto} from "$app/navigation";
    import {Plus} from "phosphor-svelte";
    import NewDeck from "../../../components/Forms/NewDeck.svelte";
    function navigateToCard(id) {
        goto(`/dashboard/decks/${id}`);
    }
    let isMounted = writable(false);
    let decks;

    onMount(async function() {
        const endpoint = 'http://localhost:8000/users/1/decks/'
        const response = await fetch(endpoint)
        const data = await response.json()
        if (data.decks.length > $DeckStore.length){
            DeckStore.set([]);
            CardStore.set([]);

            decks = data.decks
            DeckStore.set(decks)
            Object.keys($DeckStore).forEach(key => {
                card($DeckStore[key].id)
            })
        }
        isMounted.set(true);
    });


    async function card(id) {
        const endpointCard = `http://localhost:8000/decks/${id}/cards/`
        const response = await fetch(endpointCard)
        const data = await response.json()
        $CardStore.push(data)
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
    {#if $isMounted}
            <div class="accordion" id="accordionPanelsStayOpenExample">
            {#each $CardStore as data}
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse{data.deck.id}" aria-expanded="true" aria-controls="panelsStayOpen-collapse{data.deck.id}">
                            {data.deck.name}
                        </button>
                    </h2>
                    <div id="panelsStayOpen-collapse{data.deck.id}" class="accordion-collapse collapse">
                        <div class="accordion-body">
                            <div class="list-group">
                                {#each data.cards as card}
                                    <a on:click={() => navigateToCard(card.id)}    class="list-group-item list-group-item-action active card-view" aria-current="true">
                                        <div class="d-flex w-100 justify-content-between">
                                            <!--
                                            <SvelteMarkdown source="{card.front}"/>
                                            <small class="text-light">{card.modified}</small>
                                            -->
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
