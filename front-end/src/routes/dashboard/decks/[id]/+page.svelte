<script>
    import { onMount } from "svelte";
    import {page} from "$app/stores";
    import SvelteMarkdown from "svelte-markdown";
    import NewCard from "../../../../components/Forms/NewCard.svelte";
    import {Pencil, ClockCounterClockwise} from "phosphor-svelte";
    import {HistoryStore} from "../../../../history-store.js";
    import {CardStore} from "../../../../card-store.js";

    /** @type {import('./$types').PageData} */
    export let data;

    let card;
    let decks = [];

    let id_deck = "";

    let id_history = 0;

    let history = {id : 0 , front : '' , back : '', history_date : ""} ;

    onMount(()=>{
        CardStore.set(data.card);
        HistoryStore.set(data.history.history);

        history = $HistoryStore[id_history];
        console.log(history)
    })
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


    async function handleSubmit() {

        console.log(JSON.stringify($CardStore))
        try {
            const csrftoken = getCookie('csrftoken');
            const response = await fetch(`http://127.0.0.1:8000/fcards/${data.id}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                credentials : 'include',
                body: JSON.stringify($CardStore)
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

    // Lista de botones de ejemplo
    let buttons = [
        { id: 1, label: 'Button 1' },
        { id: 2, label: 'Button 2' },
        { id: 3, label: 'Button 3' },
        { id: 4, label: 'Button 4' },
        { id: 5, label: 'Button 5' }

        // Añade más botones si es necesario
    ];

    function changeIdHistory(id){
        id_history = id;
        history = $HistoryStore[id_history-1];
    }
</script>
<style>
    /* Hacer que la primera columna sea scrollable */
    .scrollable-column {
        height: 100%;
        max-height: 500px; /* Ajusta según sea necesario */
        overflow-y: auto;
    }

    .card-width{
        width: 30rem;
        margin-left: 20%;
        min-height: 300px;
    }
</style>
{#if CardStore}
    <div>
        <!-- Botón que activa el modal edit-->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            <div class="d-flex align-items-center">
                <Pencil/>
                Edit card
            </div>

        </button>
        <!-- Botón que activa el modal history-->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
            <div class="d-flex align-items-center">
                <ClockCounterClockwise/>
                See history
            </div>

        </button>
        <div class="row">
            <div class="container-sm col">
                <div class="text-center mb-3"><p>Front</p></div>
                <div class="card bg-secondary mb-3 card-width" >
                    <div class="card-body">
                        <SvelteMarkdown source="{$CardStore.front}"/>
                    </div>
                </div>
            </div>
            <div class="container-sm col">
                <div class="text-center mb-3"><p>Back</p></div>
                <div class="card bg-secondary mb-3 card-width" >
                    <div class="card-body">
                        <SvelteMarkdown source="{$CardStore.back}"/>
                    </div>
                </div>
            </div>
        </div>
        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog ">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Edit card</h5>
                    </div>
                    <form on:submit|preventDefault={handleSubmit}>
                        <div class="modal-body">

                                <div class="mb-3">
                                    <label for="front-area" class="form-label">Front Area</label>
                                    <textarea bind:value={$CardStore.front} style="color:black"  class="form-control" id="front-area" rows="5" placeholder="Type in Markdown"></textarea>
                                </div>
                                <div class="mb-3">
                                    <label for="back-area" class="form-label">Back Area</label>
                                    <textarea bind:value={$CardStore.back} style="color:black" class="form-control" id="back-area" rows="10" placeholder="Type in Markdown"></textarea>
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

        <!-- Modal -->
        <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-xl">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="staticBackdropLabel">All history card</h1>
                    </div>
                    <div class="modal-body">
                        {#if HistoryStore}
                            <div class="container mt-3">
                                <div class="row">
                                    <h4>List history</h4>
                                    <div class="col-3 scrollable-column">

                                        <div class="list-group">
                                            {#each $HistoryStore as info}
                                                <button type="button" class="list-group-item list-group-item-action" on:click={() => changeIdHistory(info.history_id)}>{info.history_id}</button>
                                                {/each}
                                        </div>
                                    </div>
                                    <div class="col-9">
                                        <div class="row">
                                            <h4>Date: {history.history_date} </h4>
                                        </div>
                                        <div class="container mb-3">
                                            <div class="row">
                                                <h5 class="text-center">Front</h5>
                                                <div class="col">
                                                    <div class="card bg-secondary card-width ">
                                                        <div class="card-body">
                                                            <SvelteMarkdown source="{history.front}"/>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="container mb-3">

                                            <div class="row">
                                                <h5 class="text-center">Back</h5>
                                                <div class="col">
                                                    <div class="card bg-secondary card-width">
                                                        <div class="card-body">
                                                            <SvelteMarkdown source="{history.back}"/>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            {:else}
                                <p>Loading</p>
                            {/if}
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary">Change</button>
                    </div>
                </div>
            </div>
        </div>

    </div>
    {/if}

