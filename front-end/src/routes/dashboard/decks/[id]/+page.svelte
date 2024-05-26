<script>
    import { onMount } from "svelte";
    import {page} from "$app/stores";
    import SvelteMarkdown from "svelte-markdown";
    import NewCard from "../../../../components/Forms/NewCard.svelte";
    import {Pencil, ClockCounterClockwise} from "phosphor-svelte";
    import {HistoryStore} from "../../../../history-store.js";
    import {CardStore} from "../../../../card-store.js";
    import {getCookie} from "../../../../utils/csrf.js";
    /** @type {import('./$types').PageData} */
    export let data;

    let card;
    let decks = [];

    let id_deck = "";

    let id_history = 0;
    let modalHistory;

    let history = {id : 0 , front : '' , back : '', history_date : "", history_id : 0} ;

    onMount(()=>{
        CardStore.set(data.card);
        HistoryStore.set(data.history.history);

        history = $HistoryStore[id_history];
        console.log(history)
        import('bootstrap').then(({ Modal }) => {
            modalHistory = new Modal(document.getElementById('staticBackdrop'));
        });
    })

    const closeModal = () => {
        modalHistory.hide();
    };
    async function handleSubmit() {

        console.log(JSON.stringify($CardStore))
        try {
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');
            const response = await fetch(`http://127.0.0.1:8000/fcards/${data.id}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': `${csrftoken}`,
                    'Authorization': `Token ${token}`
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


    function changeIdHistory(id){
        id_history = id;
        HistoryStore.subscribe(cards =>{
            // Encontrar el objeto con el mismo history_id
            history = cards.find(card => card.history_id === id);
        });
    }

    async function handleChangeHistory(){
        try {
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');

            const id = history.history_id;
            const info = {id};
            console.log(JSON.stringify(info))
            const response = await fetch(`http://127.0.0.1:8000/cards/${data.id}/revert_to/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': `${csrftoken}`,
                    'Authorization': `Token ${token}`
                },
                credentials : 'include',
                body: JSON.stringify(info)
            });

            if (response.ok) {
                console.log('Form submitted successfully!');
                closeModal();
            } else {
                console.error('Failed to submit form');
            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
        }
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
                        {#if $HistoryStore}
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
                                            <h4>Date: {history.history_date}</h4>
                                        </div>
                                        <div class="container mb-3">
                                            <div class="row">
                                                <h5 class="text-center">Front</h5>
                                                <div class="col">
                                                    <div class="card bg-secondary card-width">
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
                        <button type="button" class="btn btn-primary" on:click={handleChangeHistory}>Change</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {/if}

