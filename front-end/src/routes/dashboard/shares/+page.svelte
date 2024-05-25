<script>
    import {onMount} from "svelte";
    import {NoteStore} from "../../../note-store.js";
    import {CardStore} from "../../../card-store.js";
    import {Plus} from "phosphor-svelte";
    import {goto} from "$app/navigation";
    import SvelteMarkdown from "svelte-markdown";
    import NewNote from "../../../components/Forms/NewNote.svelte";
    import NewCard from "../../../components/Forms/NewCard.svelte";
    import {getCookie} from "../../../utils/csrf.js";

    /** @type {import('./$types').PageData} */
    export let data;

    let title = '';
    let content = '';
    let id_notebook = "";
    let front = '';
    let back = '';
    let id_deck = "";
    let template = "";




    function resetTemplate(){
        template = "";
        id_deck = "";
    }

    onMount(() =>{
        $NoteStore = data.notes;
        $CardStore = data.cards;
        console.log($CardStore)
    })

    function navigateToCard(id) {
        goto(`/dashboard/decks/${id}`);
    }

    function navigateToNote(id) {
        goto(`/dashboard/notes/${id}`);
    }

    async function handleSubmit() {
        const notebook_ref = '/notebooks/'+id_notebook+'/'
        const data = { title, content, notebook_ref };
        console.log(JSON.stringify(data))
        try {
            const token = localStorage.getItem('key');
            const csrftoken = getCookie('csrftoken');
            const response = await fetch('http://127.0.0.1:8000/notes/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                body: JSON.stringify(data),
                credentials : 'include'
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
    async function handleSubmitCard() {
        console.log(id_deck)
        const deck = '/decks/'+id_deck+'/'
        const data = { front, back, deck };
        console.log(JSON.stringify(data))
        try {
            const token = localStorage.getItem('key');
            const csrftoken = getCookie('csrftoken');
            const response = await fetch('http://127.0.0.1:8000/fcards/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                body: JSON.stringify(data),
                credentials : 'include'
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

</script>
<style>
    .card-view{
        cursor: pointer;
    }
</style>
<div>
    <h3>Decks shared</h3>

    {#if CardStore}
        <!-- Botón que activa el modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            <div class="d-flex align-items-center">
                <Plus />
                Add card
            </div>
        </button>
        <div class="accordion" id="accordionPanelsStayOpenExample">
            {#each $CardStore as info}
                <div class="accordion-item">
                    <h2 class="accordion-header row">
                        <button class="col accordion-button" type="button" data-bs-toggle="collapse" style="max-width: 60%;" data-bs-target="#panelsStayOpen-collapse{info.deck.id}" aria-expanded="true" aria-controls="panelsStayOpen-collapse{info.deck.id}">
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

        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Add card</h5>
                    </div>
                    <form on:submit|preventDefault={handleSubmitCard}>
                        <div class="modal-body">
                            <div class="mb-3">
                                <label for="front-area" class="form-label">Template</label>
                                <select bind:value={template}  class="form-select" style="color:black" aria-label="Select template">
                                    <option value="" disabled selected>Open to select template</option>
                                    <option value="1">Basic</option>
                                </select>
                            </div>
                            {#if template != 0}
                                <div class="mb-3">
                                    <label for="front-area" class="form-label">Deck</label>
                                    <select bind:value={id_deck}  class="form-select" style="color:black" aria-label="Select template">
                                        <option value="" disabled selected>Open to select a deck</option>
                                        {#each $CardStore as value}
                                            <option value="{value.deck.id}">{value.deck.name}</option>
                                        {/each}
                                    </select>
                                </div>
                            {/if}
                            {#if template == 1}

                                <div class="mb-3">
                                    <label for="front-area" class="form-label">Front Area</label>
                                    <textarea bind:value={front} style="color:black"  class="form-control" id="front-area" rows="5" placeholder="Type in Markdown"></textarea>
                                </div>
                                <div class="mb-3">
                                    <label for="back-area" class="form-label">Back Area</label>
                                    <textarea bind:value={back} style="color:black" class="form-control" id="back-area" rows="10" placeholder="Type in Markdown"></textarea>
                                </div>
                            {/if}


                        </div>

                        <div class="modal-footer">
                            <button on:click={resetTemplate} type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                            {#if template != 0}
                                <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
                            {/if}
                        </div>
                    </form>
                </div>
            </div>
        </div>
    {:else }
        <div>
            <h3>Loading Decks...</h3>
        </div>
    {/if}
    <br/>
    <h3>Notebooks shared</h3>

    {#if NoteStore}
        <!-- Botón que activa el modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            <div class="d-flex align-items-center">
                <Plus />
                Add note
            </div>
        </button>
        <div class="accordion" id="accordionPanelsStayOpenExample">
            {#each $NoteStore as info}
                <div class="accordion-item">
                    <h2 class="accordion-header row">
                        <button style="max-width: 60%;"  class="col accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse-note{info.notebook.id}" aria-expanded="true" aria-controls="panelsStayOpen-collapse{info.notebook.id}">
                            {info.notebook.name}
                        </button>
                    </h2>
                    <div id="panelsStayOpen-collapse-note{info.notebook.id}" class="accordion-collapse collapse">
                        <div class="accordion-body">
                            <div class="list-group">
                                {#each info.notes as note}
                                    <a on:click={() => navigateToNote(note.id)}    class="list-group-item list-group-item-action active card-view" aria-current="true">
                                        <div class="d-flex w-100 justify-content-between">
                                            <SvelteMarkdown source="{note.title}"/>
                                        </div>
                                    </a>
                                {/each}
                            </div>
                        </div>
                    </div>
                </div>
            {/each}
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
                                <input type="text" bind:value={title} style="color:black"  class="form-control" id="title"  placeholder="Type in Markdown">
                            </div>
                            <div class="mb-3">
                                <label for="content" class="form-label">Content</label>
                                <textarea bind:value={content} style="color:black" class="form-control" id="content" rows="10" placeholder="Type in Markdown"></textarea>
                            </div>
                            <div class="mb-3">
                                <label for="front-area" class="form-label">Notebooks</label>
                                <select bind:value={id_notebook}  class="form-select" style="color:black" aria-label="Select template">
                                    <option value="" disabled selected>Open to select a notebook</option>
                                    {#each $NoteStore as value}
                                        <option value="{value.notebook.id}">{value.notebook.name}</option>
                                    {/each}
                                </select>
                            </div>

                        </div>

                        <div class="modal-footer">
                            <button type="button"  class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                            <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    {:else }
        <div>
            <h3>Laading..</h3>
        </div>
    {/if}



</div>