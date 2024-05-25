<script>
    import {NoteStore} from '../../../../note-store.js'
    import { onMount } from "svelte";
    import SvelteMarkdown from 'svelte-markdown';
    import {ClockCounterClockwise, Pencil} from "phosphor-svelte";
    import {ImagesStore} from "../../../../images-store.js";
    import FilePond, { registerPlugin, supported } from 'svelte-filepond';
    import FilePondPluginImageExifOrientation from 'filepond-plugin-image-exif-orientation'
    import FilePondPluginImagePreview from 'filepond-plugin-image-preview'
    import {HistoryStore} from "../../../../history-store.js";

    registerPlugin(FilePondPluginImageExifOrientation, FilePondPluginImagePreview);
    /** @type {import('./$types').PageData} */
    export let data;


    let id_history = 0;

    let history = {id : 0 , title : '' , content : '', history_date : ""} ;


    const note = data.note;

    onMount(() =>{
        ImagesStore.set([]);
        NoteStore.set(data.note);
        HistoryStore.set(data.history.history);
        history = $HistoryStore[id_history];
        console.log(history)
    })


    async function handleSubmit() {
        console.log(JSON.stringify(note))
        try {
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');
            const response = await fetch(`http://127.0.0.1:8000/notes/${note.id}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                    'Authorization': `Token ${token}`
                },
                credentials : 'include',
                body: JSON.stringify(note)
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
        history = $HistoryStore[id_history-1];
    }

    const title = `# Title:`

    // the name to use for the internal file input
    let name = 'filepond';

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

    const process = (fieldName, file, metadata, load, error, progress, abort) => {

        const csrftoken = getCookie('csrftoken');
        const formData = new FormData();
        formData.append('image', file); // Cambia 'file' al nombre deseado
        const request = new XMLHttpRequest();
        request.open('POST', 'http://localhost:8000/img/');


        request.setRequestHeader('X-CSRFToken', csrftoken);
        // Configura la solicitud para enviar cookies automáticamente
        request.withCredentials = true;

        request.upload.onprogress = (e) => {
            progress(e.lengthComputable, e.loaded, e.total);
        };

        request.onload = function() {
            if (request.status >= 200 && request.status < 300) {
                try {
                    const urlImg = JSON.parse(request.response); // Convertir a JSON
                    addImageStore(urlImg);
                } catch (e) {
                    error('Error parsing response as JSON');
                }
            } else {
                error('Error uploading file');
            }
        };

        request.onerror = function() {
            error('Error uploading file');
        };

        request.onabort = function() {
            abort();
        };

        request.send(formData);

        return {
            abort: () => {
                request.abort();
                abort();
            }
        };
    };

    const addImageStore = (image) => {
        console.log(image)
        ImagesStore.update(images => {
            if (!images.some(u => u.url === image.url)) {
                return [...images, image];
            }
            return images;
        });

    };

    
</script>

<style>
    /* Hacer que la primera columna sea scrollable */
    .scrollable-column {
        height: 100%;
        max-height: 500px; /* Ajusta según sea necesario */
        overflow-y: auto;
    }

    .scrollable-column-note {
        height: 100%;
        max-height: 800px; /* Ajusta según sea necesario */
        overflow-y: auto;
    }
</style>

{#if NoteStore}
    <div class="container-md" >
        <!-- Botón que activa el modal edit-->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            <div class="d-flex align-items-center">
                <Pencil/>
                Edit note
            </div>
        </button>
        <!-- Botón que activa el modal history-->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
            <div class="d-flex align-items-center">
                <ClockCounterClockwise/>
                See history
            </div>
        </button>
            <div>
                <div class="card bg-secondary mb-3 scrollable-column-note" style="max-width: 900px;min-width: 720px;min-height: 400px;">
                    <div class="card-header">
                        <div class="d-flex align-items-center">
                            <SvelteMarkdown source="{title}" />
                            <SvelteMarkdown source="{$NoteStore.title}" />
                        </div>

                    </div>
                    <div class="card-body">
                        <SvelteMarkdown source="{$NoteStore.content}" />
                    </div>
                </div>
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
                                <input type="text" bind:value={$NoteStore.title} style="color:black"  class="form-control" id="title"  placeholder="Type in Markdown">
                            </div>
                            <div class="mb-3">
                                <label for="content" class="form-label">Content</label>
                                <textarea bind:value={$NoteStore.content} style="color:black" class="form-control" id="content" rows="10" placeholder="Type in Markdown"></textarea>
                            </div>
                            <div class="mb-3">
                                <h6> Links images in markdown</h6>
                                {#each $ImagesStore as image, index}
                                    <p>![Image {index+1}](<a href="{image.url}">{image.url}</a> "Your title image")</p>
                                {/each}
                            </div>

                            <div class="app">
                                <h6>Upload images</h6>
                                <FilePond
                                        {name}
                                        server={{ process }}
                                        allowMultiple={true}
                                />

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
        <!-- Modal History-->
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
                                        <div>
                                            <div class="card bg-secondary mb-3 scrollable-column-note" style="max-width: 900px;min-width: 720px;min-height: 400px;">
                                                <div class="card-header">
                                                    <div class="d-flex align-items-center">
                                                        <SvelteMarkdown source="{title}" />
                                                        <SvelteMarkdown source="{history.title}" />
                                                    </div>

                                                </div>
                                                <div class="card-body">
                                                    <SvelteMarkdown source="{history.content}" />
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
    {:else }
        <h2>No se encontro la nota con id: {data.id}</h2>
    {/if}

