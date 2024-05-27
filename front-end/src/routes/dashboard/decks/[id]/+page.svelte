<script>
    import { onMount } from "svelte";
    import {page} from "$app/stores";
    import SvelteMarkdown from "svelte-markdown";
    import NewCard from "../../../../components/Forms/NewCard.svelte";
    import {Pencil, ClockCounterClockwise, X, Plus} from "phosphor-svelte";
    import {HistoryStore} from "../../../../history-store.js";
    import {SingleCardStore} from "../../../../single-card-store.js";
    import {getCookie} from "../../../../utils/csrf.js";
    import {alertSuccess, alertError} from "../../../../utils/alerts.js";
    import {invalidateAll} from "$app/navigation";
    import {TagStore} from "../../../../tag-store.js";
    import {SingleNoteStore} from "../../../../single-note-store.js";
    /** @type {import('./$types').PageData} */
    export let data;

    let card;
    let decks = [];

    let id_deck = "";


    let id_history = 0;
    let modalHistory;

    let history = {id : 0 , front : '' , back : '', history_date : "", history_id : 0} ;

    onMount(()=>{
        SingleCardStore.set(data.card);
        HistoryStore.set(data.history.history);

        history = $HistoryStore[id_history];
        console.log(history)
    })


    async function handleSubmit() {

        console.log(JSON.stringify($SingleCardStore))
        try {
            const tags = buttons
                .filter(button => button.color === 'btn-danger')
                .map(button => button.url);
            const front = $SingleCardStore.front;
            const back = $SingleCardStore.back;
            const deck = $SingleCardStore.deck;
            const info = {deck, front, back, tags};
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
                body: JSON.stringify(info)
            });

            if (response.ok) {
                alertSuccess('Updated card successfully.');
                await invalidateAll();
            } else {
                alertError('Failed to updated note.');
            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
            alertError('An error occurred while updating note');
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
                alertSuccess('Change history successfully.');
                await invalidateAll();
            } else {
                alertError('Failed to change history');
            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
            alertError('An error occurred while changing history');
        }
    }

    let buttons = [];

    // Suscribirse a TagStore y actualizar los botones cuando cambie
    const unsubscribe = TagStore.subscribe($TagStore => {
        buttons = $TagStore.map(data => ({
            ...data,
            color: $SingleCardStore.tags.includes(data.url) ? 'btn-danger' : 'btn-primary', // Inicializa con color según la URL
            icon: $SingleCardStore.tags.includes(data.url) ? X : Plus // Inicializa con icono según la URL
        }));
    });

    // Función para manejar el clic en los botones
    function toggleButtonState(index) {
        buttons = buttons.map((button, i) =>
            i === index
                ? {
                    ...button,
                    color: button.color === 'btn-primary' ? 'btn-danger' : 'btn-primary',
                    icon: button.icon === Plus ? X : Plus
                }
                : button
        );
        console.log(buttons)
    }




    let tag_name = '';
    async function createTag(){

        const data = {'name': `${tag_name}`};
        console.log(JSON.stringify(data))
        try {
            const token = localStorage.getItem('key');
            const csrftoken = getCookie('csrftoken');
            const response = await fetch('http://127.0.0.1:8000/tags/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                body: JSON.stringify(data),
                credentials : 'include',
            });

            if (response.ok) {
                alertSuccess('Added new Tag.');
                await invalidateAll();
            } else {
                alertError('Failed to add new Tag.');
            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
            alertError('An error occurred while adding new deck.');
        }
    }
</script>
{#if SingleCardStore}
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
                        <SvelteMarkdown source="{$SingleCardStore.front}"/>
                    </div>
                </div>
            </div>
            <div class="container-sm col">
                <div class="text-center mb-3"><p>Back</p></div>
                <div class="card bg-secondary mb-3 card-width" >
                    <div class="card-body">
                        <SvelteMarkdown source="{$SingleCardStore.back}"/>
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
                                    <textarea bind:value={$SingleCardStore.front} style="color:black"  class="form-control" id="front-area" rows="5" placeholder="Type in Markdown"></textarea>
                                </div>
                                <div class="mb-3">
                                    <label for="back-area" class="form-label">Back Area</label>
                                    <textarea bind:value={$SingleCardStore.back} style="color:black" class="form-control" id="back-area" rows="10" placeholder="Type in Markdown"></textarea>
                                </div>
                            <div class="mb-3">
                                <h4>Tags</h4>
                                <div class="form-floating mb-3">
                                    <input bind:value={tag_name} type="text"
                                           class="form-control" id="floatingInput"
                                           placeholder="name" style="color:black" >
                                    <label for="floatingInput" style="color:black" >
                                        Tag Name
                                    </label>
                                </div>

                                <button  type="button"
                                         class="btn btn-secondary"

                                         on:click={createTag}>
                                    Add
                                </button>


                                <div class="scrollable">
                                    <div class="button-container">
                                        {#each buttons as button, index}
                                            <div class="button-item">
                                                <button
                                                        class="btn {button.color} my-1"
                                                        on:click={() => toggleButtonState(index)}
                                                        type="button"
                                                >
                                                    <svelte:component this={button.icon} size={24} />
                                                    {button.name}
                                                </button>
                                            </div>
                                        {/each}
                                    </div>
                                </div>

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
                        <button type="button" class="btn btn-primary" on:click={handleChangeHistory} data-bs-dismiss="modal">Change</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
{/if}

