<script>
    import {NoteStore} from '../../../note-store.js';
    import {onMount} from 'svelte';
    import { goto } from '$app/navigation';
    import { writable } from "svelte/store";
    import NewNote from "../../../components/Forms/NewNote.svelte";
    import SvelteMarkdown from "svelte-markdown";
    import {Gear, LockKey, LockSimpleOpen, Pencil, Plus, Trash, UserPlus, X} from "phosphor-svelte";
    import NewNotebook from "../../../components/Forms/NewNotebook.svelte";
    import {UsersStore} from "../../../users-store.js";
    import {UserStore} from "../../../user-store.js";
    import {getCookie} from "../../../utils/csrf.js";
    import {alertSuccess, alertError} from "../../../utils/alerts.js";
    import {invalidateAll} from "$app/navigation";
    import NewTag from "../../../components/Forms/NewTag.svelte";

    /** @type {import('./$types').PageData} */
    export let data;

    let usersList = [];
    let id_notebook = 0;
    let id_note = 0;
    let is_notebook = false;
    let is_rename = false;
    let name = "";



    onMount(() => {
        NoteStore.set(data.notes);
        UsersStore.set([]);
        console.log(data.users)
    });

    function navigateToNote(id) {
        goto(`/dashboard/notes/${id}`);
    }

    const addUsers = (id) => {
        const user = data.users.find(user => user.id === id);
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
        const selectedValues = selectedOptions.map(option => parseInt(option.value));
        selectedValues.forEach(value => addUsers(value));
    }

    function deleteUser(id) {
        UsersStore.update(users => users.filter(user => user.id !== id));
        console.log($UserStore)
    }

    async function handleSubmit() {
        const usersToInvite = [];
        const unsubscribe = UsersStore.subscribe(users => {
            usersToInvite.push(...users);
        });
        unsubscribe();

        for (const user of usersToInvite) {
            await invite(user);
        }
        UsersStore.set([]); // Reset after submission
        await invalidateAll();
    }

    async function handleSubmitRename(){
        try {
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');
            console.log(csrftoken)
            const info = { name}
            const endpoint = `http://localhost:8000/notebooks/${id_notebook}/`;
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
                alertSuccess('Rename notebook successfully.');
                await invalidateAll();
            } else {
                alertError('Failed to rename notebook')
            }
        } catch (error) {
            console.error('An error occurred while renaming the notebook:', error);
            alertError('An error occurred while renaming the notebook.')
        }
    }

    function changeIdNotebookRename(id) {
        id_notebook = id;
        is_rename = true;
    }

    function changeIdNotebook(id) {
        id_notebook = id;
        is_notebook = true;
    }

    function changeIdNote(id) {
        id_note = id;
        is_notebook = false;
    }

    function cancelSubmit() {
        UsersStore.set([]);
    }

    async function invite(user) {
        const sharer = `/users/${data.user.id}/`;
        const notebook_shared = true;
        const notebook = `/notebooks/${id_notebook}/`;
        const recipient = `/users/${user.id}/`;
        try {
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');
            const info = {sharer, notebook_shared, recipient, notebook};
            const endpoint = "http://localhost:8000/shared/";
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

    async function deleteNotebook() {
        try {
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');
            console.log(csrftoken)
            const endpoint = `http://localhost:8000/notebooks/${id_notebook}/`;
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
                alertSuccess('Delete notebook successfully.');
                await invalidateAll();
            } else {
                alertError('Failed to delete notebook');
            }
        } catch (error) {
            console.error('An error occurred while deleting the notebook:', error);
            alertError('An error occurred while deleting the notebook.');
        }
    }

    async function deleteNote() {
        try {
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');
            const endpoint = `http://localhost:8000/notes/${id_note}/`;
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
                alertSuccess('Delete note successfully.');
                await invalidateAll()
            } else {
                alertError('Failed to delete note');
            }
        } catch (error) {
            console.error('An error occurred while deleting the note:', error);
            alertError('An error occurred while deleting the note.')
        }
    }

    async function changePublic(id, state){

        try {
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');
            let endpoint = '';
            if (!state) {
                endpoint = `http://localhost:8000/notebooks/${id}/set_public/`;
            }else{
                endpoint = `http://localhost:8000/notebooks/${id}/set_private/`;
            }
            const response = await fetch(endpoint, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                credentials: 'include'
            });
            if (response.ok) {
                alertSuccess('Change state deck successfully.');
                await invalidateAll();
            } else {
                alertError('Failed to change state deck');
            }
        } catch (error) {
            console.error('An error occurred while change state of the deck:', error);
            alertError('An error occurred while change state of the deck.');
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
        max-width: 460px;
        padding-bottom: 20px;
    }
</style>
<div class="button-div">
<!-- Botón que activa el modal -->
<button type="button" class="btn btn-primary btn-action-color" data-bs-toggle="modal" data-bs-target="#exampleModal">
    <div class="d-flex align-items-center">
        <Plus />
        Add note
    </div>
</button>
<button type="button" class="btn btn-primary btn-action-color" data-bs-toggle="modal" data-bs-target="#notebookModal">
    <div class="d-flex align-items-center">
        <Plus />
        Add notebook
    </div>
</button>
<button type="button" class="btn btn-primary btn-action-color" data-bs-toggle="modal" data-bs-target="#tagModal">
    <div class="d-flex align-items-center">
        <Plus />
        Add tag
    </div>
</button>
</div>
{#if NoteStore}
    <div class="accordion" id="accordionPanelsStayOpenExample" style="padding-top: 20px;">
        {#each $NoteStore as info}
            <div class="accordion-item">
                <h2 class="accordion-header row" style="padding-bottom: 20px;">
                    <button style="max-width: 60%;"  class="col accordion-button  accordion-button-custom" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse{info.notebook.id}" aria-expanded="true" aria-controls="panelsStayOpen-collapse{info.notebook.id}">
                        {info.notebook.name}
                    </button>
                    <div class="col btn-group "style="max-width: 50px;">
                        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" data-bs-auto-close="false" aria-expanded="false">
                            <Gear size={24}/>
                        </button>
                        <ul class="dropdown-menu dropdown-menu-dark bg-dark" >
                            <li><a class="dropdown-item" data-bs-toggle="modal"  role="button" href="#inviteModal" data-bs-target="#inviteModal" on:click={() => changeIdNotebook(info.notebook.id)} >
                                <div class="d-flex align-items-center">
                                    <UserPlus size={20}/>
                                    Invite
                                </div>
                            </a></li>
                            {#if !info.notebook.public}
                                <li><a class="dropdown-item text-primary-emphasis" on:click={() => changePublic(info.notebook.id, false)} >
                                    <div class="d-flex align-items-center">
                                        <LockSimpleOpen size={20} />
                                        Public
                                    </div>
                                </a></li>
                            {:else }
                                <li><a class="dropdown-item text-primary-emphasis" on:click={() => changePublic(info.notebook.id, true)} >
                                    <div class="d-flex align-items-center">
                                        <LockKey size={20}/>
                                        Private
                                    </div>
                                </a></li>
                            {/if}
                            <li><a class="dropdown-item text-warning-emphasis" role="button" href="#staticBackdrop" data-bs-toggle="modal" data-bs-target="#staticBackdrop"  on:click={() => changeIdNotebookRename(info.notebook.id)}>
                                <div class="d-flex align-items-center">
                                    <Pencil size={20} />
                                    Rename
                                </div>
                            </a></li>
                            <li><a class="dropdown-item text-danger" role="button" href="#staticBackdrop" data-bs-toggle="modal" data-bs-target="#staticBackdrop" on:click={() => changeIdNotebook(info.notebook.id)} >
                                <div class="d-flex align-items-center">
                                    <Trash size={20}/>
                                    Delete
                                </div>
                            </a></li>
                        </ul>
                    </div>
                </h2>
                <div id="panelsStayOpen-collapse{info.notebook.id}" class="accordion-collapse collapse">
                    <div class="accordion-body" style="max-width: 60%;" >
                        <div>
                            <table class="table table-hover">
                                <thead>
                                <tr>
                                    <th scope="col">List</th>
                                    <th scope="col">Tags</th>
                                    <th scope="col"></th>
                                </tr>
                                </thead>
                                <tbody>
                                {#each info.notes as note}
                                    <tr class="table-borders">
                                        <th scope="row">
                                            <div class="card-view">
                                                <a on:click={() => navigateToNote(note.id)} style="max-width: 60%;"   class="col list-group-item list-group-item-action active card-view" aria-current="true">
                                                    <div class="d-flex w-100 justify-content-between">
                                                        {note.title}
                                                    </div>
                                                </a>
                                            </div>
                                        </th>
                                        <td>{note.tags}</td>
                                        <td>
                                            <button type="button" class="col  btn btn-outline-danger btn-delete " data-bs-toggle="modal" data-bs-target="#staticBackdrop" on:click={() => changeIdNote(note.id)}>
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

    <!-- Modal Rename, delete-->
    <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                {#if is_rename}
                    <div class="modal-body text-center">
                        <h3>Rename Notebook</h3>
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
                        {#if is_notebook}
                            <h3>¿Are you sure you want to delete this notebook? </h3>
                        {:else }
                            <h3>¿Are you sure you want to delete this note? </h3>
                        {/if}
                    </div>
                    <div class="modal-footer" style="margin-right: 25%">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                        {#if is_notebook}
                            <button type="button" class="btn btn-primary" data-bs-dismiss="modal" on:click={() => deleteNotebook()}>Confirm</button>
                        {:else }
                            <button type="button" class="btn btn-primary" data-bs-dismiss="modal" on:click={() => deleteNote()}>Confirm</button>
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
                                <button type="button" class="btn btn-outline-danger" on:click={() => deleteUser(user.id)} >{user.name}</button>
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
