<script>
    import NewCard from "../../../components/Forms/NewCard.svelte";
    import {goto} from "$app/navigation";
    import {Plus, X, Gear, LockKey,LockSimpleOpen,Pencil, Trash, UserPlus} from "phosphor-svelte";
    import NewDeck from "../../../components/Forms/NewDeck.svelte";
    import {UsersStore} from "../../../stores.js";
    import {CardStore} from "../../../stores.js";
    import {onMount} from "svelte";
    import {getCookie} from "../../../utils/csrf.js";
    import {alertSuccess, alertError} from "../../../utils/alerts.js";
    import {invalidateAll} from "$app/navigation";
    import NewTag from "../../../components/Forms/NewTag.svelte";

    /** @type {import('./$types').PageData} */
    export let data;
    let id_deck = 0;
    let id_card = 0;
    let is_deck = false;
    let is_rename = false;
    let name = "";
    let unsubscribe;
    const localhost = 'http://localhost:8000/';

    function navigateToCard(id) {
        goto(`/dashboard/decks/${id}`);
    }
    onMount(() => {
        console.log($CardStore)
        UsersStore.set([]);
    });


    unsubscribe = CardStore.subscribe(value => {
        if (value) {
            console.log('Received event:', value);
            // Maneja el evento aquí
        }
        console.log("change")
    });

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
        await invalidateAll();
    }

    async function handleSubmitRename(){
        try {
            const token = localStorage.getItem('key');
            const csrftoken = getCookie('csrftoken');
            console.log(csrftoken)
            const info = { name}
            const endpoint = `http://localhost:8000/decks/${id_deck}/`;
            const response = await fetch(endpoint, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                body: JSON.stringify(info),
                credentials: 'include'
            });
            if (response.ok) {
                alertSuccess('Rename deck successfully.');
                await invalidateAll().then(() => {
                        CardStore.set(data.cards);
                        console.log($CardStore)
                        UsersStore.set([]);
                });
            } else {
                console.error('');
                alertError('Something failed to rename deck');
            }
        } catch (error) {
            console.error('An error occurred while deleting the deck:', error);
            alertError('An error occurred while renaming the deck');
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
            const token = localStorage.getItem('key');
            const csrftoken = getCookie('csrftoken');
            const info = {sharer, deck_shared, recipient , deck}
            const endpoint = "http://localhost:8000/shared/"
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                body: JSON.stringify(info),
                credentials: 'include'
            });
            if (response.ok) {
                alertSuccess(`Invitation send to ${user.name}`);
            } else {
                alertError(`Failed sending invitation to ${user.name}`);
            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
            alertError('An error occurred while sending invitation');
        }
    }
    async function deleteDeck() {
        try {
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');
            const endpoint = `http://localhost:8000/decks/${id_deck}/`;
            const response = await fetch(endpoint, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                credentials: 'include'
            });
            if (response.ok) {
                alertSuccess('Delete deck successfully.');
                await invalidateAll().then(() => {
                    CardStore.set(data.cards);
                    console.log($CardStore)
                    UsersStore.set([]);
                });
            } else {
                alertError('Failed to delete deck');
            }
        } catch (error) {
            console.error('An error occurred while deleting the deck:', error);
            alertError('An error occurred while deleting the deck');
        }
    }
    async function deleteCard() {
        try {
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');
            const endpoint = `http://localhost:8000/cards/${id_card}/`;
            const response = await fetch(endpoint, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                credentials: 'include'
            });
            if (response.ok) {
                alertSuccess('Delete card successfully.');
                await invalidateAll().then(() => {
                    CardStore.set(data.cards);
                    console.log($CardStore)
                    UsersStore.set([]);
                });
            } else {
                alertError('Failed to delete card.');
            }
        } catch (error) {
            console.error('An error occurred while deleting the deck:', error);
            alertError('An error occurred while deleting the deck.')
        }
    }

    async function changePublic(id, state){

            try {
                const csrftoken = getCookie('csrftoken');
                const token = localStorage.getItem('key');
                let endpoint = '';
                if (!state) {
                    endpoint = `http://localhost:8000/decks/${id}/set_public/`;
                }else{
                    endpoint = `http://localhost:8000/decks/${id}/set_private/`;
                }
                const response = await fetch(endpoint, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': `${csrftoken}`,  // Incluir el token CSRF en los encabezados
                        'Authorization': `Token ${token}`
                    },
                    credentials: 'include'
                });
                if (response.ok) {
                    alertSuccess('Change state deck successfully.');
                    await invalidateAll().then(() => {
                        CardStore.set(data.cards);
                        console.log($CardStore)
                        UsersStore.set([]);
                    });
                } else {
                    alertError('Failed to change state deck.');
                }
            } catch (error) {
                console.error('An error occurred while change state of the deck:', error);
                alertError('An error occurred while change state of the deck.')
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
    
    .button-div {
        display: flex;
        justify-content: space-between;
        max-width: 420px;
        padding-bottom: 20px;
    }
</style>


<div>
    <div class="button-div">
    <!-- Botón que activa el modal -->
    <button type="button" class="btn btn-primary btn-action-color" data-bs-toggle="modal" data-bs-target="#exampleModal" style="padding-bottom: 20px;">
        <div class="d-flex align-items-center">
            <Plus />
            Add card
        </div>
    </button>
    <!-- Botón que activa el modal -->
    <button type="button" class="btn btn-primary btn-action-color" data-bs-toggle="modal" data-bs-target="#deckModal" style="padding-bottom: 20px;">
        <div class="d-flex align-items-center">
            <Plus />
            Add deck
        </div>
    </button>
    <button type="button" class="btn btn-primary btn-action-color" data-bs-toggle="modal" data-bs-target="#tagModal" style="padding-bottom: 20px;">
        <div class="d-flex align-items-center">
            <Plus />
            Add tag
        </div>
    </button>

    </div>
    {#if CardStore}
        <div class="accordion" id="accordionPanelsStayOpenExample" style="padding-top: 20px;">
            {#each $CardStore as info}
                <div class="accordion-item" style="padding-bottom: 20px;">
                    <h2 class="accordion-header row">
                        <button class="col accordion-button accordion-button-custom" type="button" data-bs-toggle="collapse" style="max-width: 60%;" data-bs-target="#panelsStayOpen-collapse{info.deck.id}" aria-expanded="true" aria-controls="panelsStayOpen-collapse{info.deck.id}">
                            {info.deck.name}
                        </button>
                        <div class="col btn-group" style="max-width: 50px;">
                            <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" data-bs-auto-close="false" aria-expanded="false">
                                <Gear size={24}/>
                            </button>
                            <ul class="dropdown-menu dropdown-menu-dark bg-dark">
                                <li><a class="dropdown-item" data-bs-toggle="modal" data-bs-target="#inviteModal" on:click={() => changeIdDeck(info.deck.id)}>
                                    <div class="d-flex align-items-center">
                                        <UserPlus size={20}/>
                                        Invite
                                    </div>
                                </a></li>
                                {#if !info.deck.public}
                                    <li><a class="dropdown-item text-primary-emphasis" on:click={() => changePublic(info.deck.id, false)}>
                                        <div class="d-flex align-items-center">
                                            <LockSimpleOpen size={20} />
                                            Public
                                        </div>
                                    </a></li>
                                {:else}
                                    <li><a class="dropdown-item text-primary-emphasis" on:click={() => changePublic(info.deck.id, true)}>
                                        <div class="d-flex align-items-center">
                                            <LockKey size={20}/>
                                            Private
                                        </div>
                                    </a></li>
                                {/if}
                                <li><a class="dropdown-item text-warning-emphasis" role="button" href="#staticBackdrop" data-bs-toggle="modal" data-bs-target="#staticBackdrop" on:click={() => changeIdDeckRename(info.deck.id)}>
                                    <div class="d-flex align-items-center">
                                        <Pencil size={20} />
                                        Rename
                                    </div>
                                </a></li>
                                <li><a class="dropdown-item text-danger" role="button" href="#staticBackdrop" data-bs-toggle="modal" data-bs-target="#staticBackdrop" on:click={() => changeIdDeck(info.deck.id)}>
                                    <div class="d-flex align-items-center">
                                        <Trash size={20}/>
                                        Delete
                                    </div>
                                </a></li>
                            </ul>
                        </div>
                    </h2>
                    <div id="panelsStayOpen-collapse{info.deck.id}" class="accordion-collapse collapse">
                        <div class="accordion-body" style="max-width: 60%;">
                            <div>
                                <table class="table table-hover table-borders">
                                    <thead class="table-header-custom">
                                    <tr>
                                        <th scope="col">List</th>
                                        <th scope="col">Tags</th>
                                        <th scope="col"></th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    {#each info.cards as card, index}
                                        <tr class=" table-borders">
                                            <th scope="row">
                                                <div class="card-view">
                                                    <a on:click={() => navigateToCard(card.id)} class="list-group-item list-group-item-action active " aria-current="true">
                                                        <div class="d-flex w-100 justify-content-between">
                                                            Card {index+1}
                                                        </div>
                                                    </a>
                                                </div>

                                            </th>
                                            <td class="tags-column">{card.tags}</td>
                                            <td>
                                                <button type="button" class="col btn btn-outline-danger btn-delete"  data-bs-toggle="modal" data-bs-target="#staticBackdrop" on:click={() => changeIdCard(card.id)}>
                                                    <X/>
                                                </button>
                                            </td>
                                        </tr>
                                    {/each}
                                    </tbody>
                                </table>
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
                                <button type="button" class="btn btn-primary" data-bs-dismiss="modal"  on:click={() => deleteDeck()}>Confirm</button>
                            {:else }
                                <button type="button" class="btn btn-primary" data-bs-dismiss="modal" on:click={() => deleteCard()}>Confirm</button>
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
    <div class="modal fade" id="tagModal" tabindex="-1" aria-labelledby="tagModal" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <NewTag/>
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
                                    <button type="button" class="btn btn-outline-danger" on:click={() => deleteUser(user)} >
                                            <div class="card-header d-flex align-items-center">
                                                <img src={localhost + user.picture} alt="Profile Image" class="rounded-circle me-3" style="width: 50px; height: 50px;">
                                                <div>
                                                    <h5 class="card-title mb-0">{user.name}</h5>
                                                    <p class="card-text"><small class="text-muted">{user.email}</small></p>
                                                </div>
                                            </div>
                                        </button>
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
