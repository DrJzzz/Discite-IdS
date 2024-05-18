<script>
    import {NoteStore} from '../../../note-store.js'
    import {onMount} from 'svelte'
    import { goto } from '$app/navigation';
    import { writable } from "svelte/store";
    import NewNote from "../../../components/Forms/NewNote.svelte";
    import SvelteMarkdown from "svelte-markdown";
    import {Plus} from "phosphor-svelte";
    import NewNotebook from "../../../components/Forms/NewNotebook.svelte";
    import {UsersStore} from "../../../users-store.js";

    /** @type {import('./$types').PageData} */
    export let data;
    $UsersStore = [];

    let id_notebook = 0;

    function navigateToNote(id) {
        goto(`/dashboard/notes/${id}`);
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
    }


    function deleteUser(id){
        $UsersStore = $UsersStore.filter(item => item !== id);
    }

    async function handleSubmit() {

        $UsersStore.forEach(user => {

            invite(user);

        });

    }

    function changeIdNotebook(id){
        id_notebook = id;
    }

    function cancelSubmit(){
        $UsersStore = [];

    }
    async function invite(user){
        const sharer = `/users/${data.user.id}/`;
        const notebook_shared = true;
        const notebook = `/notebooks/${id_notebook}/`;
        const recipient = `/users/${user.id}/`
        try {
            const info = {sharer, notebook_shared, recipient , notebook}
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
<!-- Botón que activa el modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
    <div class="d-flex align-items-center">
        <Plus />
        Add note
    </div>
</button>
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#notebookModal">
    <div class="d-flex align-items-center">
        <Plus />
        Add notebook
    </div>
</button>
{#if data}
    <div class="accordion" id="accordionPanelsStayOpenExample">
        {#each data.notes as info}
            <div class="accordion-item">
                <h2 class="accordion-header row">
                    <button style="max-width: 60%;"  class="col accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse{info.notebook.id}" aria-expanded="true" aria-controls="panelsStayOpen-collapse{info.notebook.id}">
                        {info.notebook.name}
                    </button>
                    <div class="col btn-group "style="max-width: 50px;">
                        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" data-bs-auto-close="false" aria-expanded="false">
                            Options
                        </button>
                        <ul class="dropdown-menu dropdown-menu-dark bg-dark" >
                            <li><a class="dropdown-item" data-bs-toggle="modal" data-bs-target="#inviteModal" on:click={() => changeIdNotebook(info.notebook.id)} >Invite</a></li>
                            <li><a class="dropdown-item text-warning-emphasis" href="#">Rename</a></li>
                            <li><a class="dropdown-item text-danger" href="#">Delete</a></li>
                        </ul>
                    </div>
                </h2>
                <div id="panelsStayOpen-collapse{info.notebook.id}" class="accordion-collapse collapse">
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
{:else }
    <div>
        <h3>Cargando..</h3>
    </div>
{/if}

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <NewNote/>
        </div>
    </div>
</div>

<div class="modal fade" id="notebookModal" tabindex="-1" aria-labelledby="notebookModal" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <NewNotebook/>
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