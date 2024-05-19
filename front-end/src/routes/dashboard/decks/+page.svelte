<script>

    import NewCard from "../../../components/Forms/NewCard.svelte";
    import SvelteMarkdown from "svelte-markdown";
    import {goto} from "$app/navigation";
    import {Plus, X} from "phosphor-svelte";
    import NewDeck from "../../../components/Forms/NewDeck.svelte";
    import {UsersStore} from "../../../users-store.js";
    import {CardStore} from "../../../card-store.js";
    import {writable} from "svelte/store";
    import {onMount} from "svelte";

    /** @type {import('./$types').PageData} */
    export let data;
    let id_deck = 0;
    let id_card = 0;
    let is_deck = false;
    let is_rename = false;
    let name = "";

    function navigateToCard(id) {
        goto(`/dashboard/decks/${id}`);
    }
    onMount(() => {
        CardStore.set(data.cards);
        console.log($CardStore)
        UsersStore.set([]);
    });

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


    const addUsers = (id) => {
        const user = data.users.find(user => user.id === id);
        console.log(user);
        if (user) {
            UsersStore.update(users => {
                if (!users.some(u => u.id === user.id)) {
                    return [...users, user];
                }
                return users;
            });
        }
    };



    function handleSelectChange(event) {
        const selectedOptions = Array.from(event.target.selectedOptions);
        const selectedValues = selectedOptions.map(option => option.value);
        selectedValues.forEach(value => addUsers(parseInt(value)));
        UsersStore.subscribe(value => {
            console.log('Items have changed:', value);});
        console.log($UsersStore)
    }


    function deleteUser(id){
        $UsersStore = $UsersStore.filter(item => item !== id);
    }

    function cancelSubmit(){
        $UsersStore = [];

    }

    async function handleSubmit() {

        $UsersStore.forEach(user => {

            invite(user);

        });

    }

    async function handleSubmitRename(){
        try {
            const csrftoken = getCookie('csrftoken');
            console.log(csrftoken)
            const info = { name}
            const endpoint = `http://localhost:8000/decks/${id_deck}/`;
            const response = await fetch(endpoint, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,  // Incluir el token CSRF en los encabezados
                },
                body: JSON.stringify(info),
                credentials: 'include'
            });
            if (response.ok) {
                console.log('Rename deck successfully!');
            } else {
                console.error('Failed to delete deck');
            }
        } catch (error) {
            console.error('An error occurred while deleting the deck:', error);
        }
    }

    function changeIdDeck(id){
        id_deck = id;
        is_deck = true;
    }
    function changeIdDeckRename(id){
        id_deck = id;
        is_rename= true;
    }

    function changeIdCard(id){
        id_card = id;
        is_deck = false;
    }

    async function invite(user){
        const sharer = `/users/${data.user.id}/`;
        const deck_shared = true;
        const deck = `/decks/${id_deck}/`;
        const recipient = `/users/${user.id}/`
        try {
            const info = {sharer, deck_shared, recipient , deck}
            const endpoint = "http://localhost:8000/shared/"
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(info),
                credentials: 'include'
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
    async function deleteDeck() {
        try {
            const csrftoken = getCookie('csrftoken');
            console.log(csrftoken)
            const endpoint = `http://localhost:8000/decks/${id_deck}/`;
            const response = await fetch(endpoint, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,  // Incluir el token CSRF en los encabezados
                },
                credentials: 'include'
            });
            if (response.ok) {
                console.log('Delete deck successfully!');
            } else {
                console.error('Failed to delete deck');
            }
        } catch (error) {
            console.error('An error occurred while deleting the deck:', error);
        }
    }
    async function deleteCard() {
        try {
            const csrftoken = getCookie('csrftoken');
            const endpoint = `http://localhost:8000/cards/${id_card}/`;
            const response = await fetch(endpoint, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,  // Incluir el token CSRF en los encabezados
                },
                credentials: 'include'
            });
            if (response.ok) {
                console.log('Delete card successfully!');
            } else {
                console.error('Failed to delete deck');
            }
        } catch (error) {
            console.error('An error occurred while deleting the deck:', error);
        }
    }
</script>

<style>
    .card-view{
        cursor: pointer;
    }


    .dropdown-menu {
        min-width: 100px !important;
    }

    .dropdown-item {
        font-size: 16px !important;
    }
    .btn-delete{
        max-width: 50px;
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
    {#if CardStore}
            <div class="accordion" id="accordionPanelsStayOpenExample">
            {#each $CardStore as info}
                <div class="accordion-item">
                    <h2 class="accordion-header row">
                        <button class="col accordion-button" type="button" data-bs-toggle="collapse" style="max-width: 60%;" data-bs-target="#panelsStayOpen-collapse{info.deck.id}" aria-expanded="true" aria-controls="panelsStayOpen-collapse{info.deck.id}">
                            {info.deck.name}
                        </button>
                        <div class="col btn-group "style="max-width: 50px;">
                            <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" data-bs-auto-close="false" aria-expanded="false">
                                Options
                            </button>
                            <ul class="dropdown-menu dropdown-menu-dark bg-dark" >
                                <li><a class="dropdown-item" data-bs-toggle="modal" data-bs-target="#inviteModal" on:click={() => changeIdDeck(info.deck.id)} >Invite</a></li>
                                <li><a class="dropdown-item text-warning-emphasis" role="button" href="#staticBackdrop" data-bs-toggle="modal" data-bs-target="#staticBackdrop"  on:click={() => changeIdDeckRename(info.deck.id)}>Rename</a></li>
                                <li><a class="dropdown-item text-danger" role="button" href="#staticBackdrop" data-bs-toggle="modal" data-bs-target="#staticBackdrop" on:click={() => changeIdDeck(info.deck.id)} >Delete</a></li>
                            </ul>
                        </div>
                    </h2>
                    <div id="panelsStayOpen-collapse{info.deck.id}" class="accordion-collapse collapse">
                        <div class="accordion-body">
                            <div class="list-group">
                                {#each info.cards as card}
                                    <div class="row">
                                        <a on:click={() => navigateToCard(card.id)}  style="max-width: 60%;"  class="list-group-item list-group-item-action active card-view" aria-current="true">
                                            <div class="d-flex w-100 justify-content-between">
                                                <SvelteMarkdown source="{card.front}"/>
                                            </div>
                                        </a>
                                        <button type="button" class="col  btn btn-outline-danger btn-delete " data-bs-toggle="modal" data-bs-target="#staticBackdrop" on:click={() => changeIdCard(card.id)}>
                                            <X/>
                                        </button>
                                    </div>
                                {/each}
                            </div>
                        </div>
                    </div>
                </div>
            {/each}
            </div>
        <!-- Modal Rename, delete -->
        <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    {#if is_rename}
                        <div class="modal-body text-center">
                            <h3>Rename deck</h3>
                        </div>
                        <form on:submit|preventDefault={handleSubmitRename}>
                            <div class="modal-body">
                                <div>
                                    <label class="col-form-label mt-4" for="inputDefault">New name</label>
                                    <input bind:value={name} type="text" class="form-control" placeholder="Type new name" id="inputDefault" spellcheck="false" data-ms-editor="true">
                                </div>

                            </div>

                            <div class="modal-footer">
                                <button  type="button" class="btn btn-secondary" data-bs-dismiss="modal" >Cancel</button>
                                <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
                            </div>
                        </form>
                    {:else }
                        <div class="modal-body text-center">
                            {#if is_deck}
                                <h3>¿Are you sure you want to delete this deck? </h3>
                            {:else }
                                <h3>¿Are you sure you want to delete this card? </h3>
                            {/if}
                        </div>
                        <div class="modal-footer" style="margin-right: 25%">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                            {#if is_deck}
                                <button type="button" class="btn btn-primary"  on:click={() => deleteDeck()}>Confirm</button>
                            {:else }
                                <button type="button" class="btn btn-primary"  on:click={() => deleteCard()}>Confirm</button>
                            {/if}
                        </div>
                    {/if}
                </div>
            </div>
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
    {#if UsersStore}
    <div class="modal fade" id="inviteModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Invite collaborators</h5>
                </div>
                <form on:submit|preventDefault={handleSubmit}>
                    <div class="modal-body">

                        <div>
                            <label for="listUser">User list</label>
                            <select id="listUser" class="form-select" multiple aria-label="Multiple select example" style="color: black;"  on:change={handleSelectChange}>
                                {#each data.users as user}
                                    <option value="{user.id}">
                                        <div>
                                            <p>{user.name}</p>
                                            <p><small>{user.email}</small></p>
                                        </div>
                                    </option>
                                {/each}
                            </select>
                        </div>
                        <h3>Users to invite</h3>
                        <div class="container-fluid" >

                            <div class="btn-group-vertical" role="group" aria-label="Vertical button group">
                                {#each $UsersStore as user}
                                    <button type="button" class="btn btn-outline-danger" on:click={() => deleteUser(user)} >{user.name}</button>
                                {/each}
                            </div>

                        </div>

                    </div>

                    <div class="modal-footer">
                        <button  type="button" class="btn btn-secondary" data-bs-dismiss="modal" on:click={()=>cancelSubmit()}>Cancel</button>
                        <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    {/if}
</div>
