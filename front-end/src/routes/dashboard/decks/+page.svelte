<script>

    import NewCard from "../../../components/Forms/NewCard.svelte";
    import SvelteMarkdown from "svelte-markdown";
    import {goto} from "$app/navigation";
    import {Plus} from "phosphor-svelte";
    import NewDeck from "../../../components/Forms/NewDeck.svelte";
    import {UsersStore} from "../../../users-store.js";
    import {writable} from "svelte/store";

    /** @type {import('./$types').PageData} */
    export let data;

    $UsersStore = [];

    console.log(data.users)

    let id_deck = 0;
    function navigateToCard(id) {
        goto(`/dashboard/decks/${id}`);
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

    function changeIdDeck(id){
        id_deck = id;
        console.log(id_deck)
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
                                <li><a class="dropdown-item text-warning-emphasis" href="#">Rename</a></li>
                                <li><a class="dropdown-item text-danger" href="#">Delete</a></li>
                            </ul>
                        </div>
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
</div>
