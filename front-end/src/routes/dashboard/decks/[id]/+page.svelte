<script>
    import { onMount } from "svelte";
    import SvelteMarkdown from "svelte-markdown";
    import {Pencil, ClockCounterClockwise, X, Plus} from "phosphor-svelte";
    import {HistoryStore} from "../../../../stores.js";
    import {SingleCardStore} from "../../../../stores.js";
    import {getCookie} from "../../../../utils/csrf.js";
    import {alertSuccess, alertError} from "../../../../utils/alerts.js";
    import {invalidateAll} from "$app/navigation";
    import {TagStore} from "../../../../stores.js";
    import Katex from 'svelte-katex'
    import FilePond, { registerPlugin, supported } from 'svelte-filepond';
    import FilePondPluginImageExifOrientation from 'filepond-plugin-image-exif-orientation';
    import FilePondPluginImagePreview from 'filepond-plugin-image-preview';
    import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.css';
    import FilePondPluginImageResize from 'filepond-plugin-image-resize';
    import FilePondPluginImageTransform from 'filepond-plugin-image-transform';
    import {formatDate} from "../../../../utils/date.js";

    registerPlugin(FilePondPluginImageExifOrientation, FilePondPluginImagePreview, FilePondPluginImageResize, FilePondPluginImageTransform);

    /** @type {import('./$types').PageData} */
    export let data;

    let card;
    let decks = [];

    let id_deck = "";
    const math3 = "V=\\frac{1}{3}\\pi r^2 h";

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

    // the name to use for the internal file input
    let name = 'filepond';

    // a reference to the component, used to call FilePond methods
    let pond;

    const process = (fieldName, file, metadata, load, error, progress, abort) => {

        const csrftoken = getCookie('csrftoken');
        const token = localStorage.getItem('key');
        const formData = new FormData();
        formData.append('image', file); // Cambia 'file' al nombre deseado
        const request = new XMLHttpRequest();
        request.open('POST', 'http://localhost:8000/img/');


        request.setRequestHeader('X-CSRFToken', csrftoken);
        request.setRequestHeader('Authorization', `Token ${token}`);
        // Configura la solicitud para enviar cookies automáticamente
        request.withCredentials = true;

        request.upload.onprogress = (e) => {
            progress(e.lengthComputable, e.loaded, e.total);
        };

        request.onload = function() {
            if (request.status >= 200 && request.status < 300) {
                try {
                    const urlImg = JSON.parse(request.response); // Convertir a JSON
                    setBackImage(urlImg.url);
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

    function setBackImage(imageUrl){
        $SingleCardStore.back = '<img src="'+ imageUrl + '" alt="drawing" width="400"/>'
    }
</script>

<style>
    .button-div {
        display: flex;
        justify-content: space-between;
        max-width: 300px;
        padding-bottom: 20px;
        margin-left: 20px;
    }
</style>


{#if SingleCardStore}
    <div>
        <div class="button-div">
        <!-- Botón que activa el modal edit-->
        <button type="button" class="btn btn-primary btn-action-color" data-bs-toggle="modal" data-bs-target="#exampleModal">
            <div class="d-flex align-items-center">
                <Pencil/>
                Edit card
            </div>

        </button>
        <!-- Botón que activa el modal history-->
        <button type="button" class="btn btn-primary btn-action-color" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
            <div class="d-flex align-items-center">
                <ClockCounterClockwise/>
                See history
            </div>

        </button>
    </div>

        <div class="row">
            <div class="container-sm col">
                <div class="text-center mb-3"><p>Front</p></div>
                <div class="card bg-secondary mb-3 card-width" >
                    <div class="card-body">
                        {#if $SingleCardStore.template == 2}
                            <Katex>{$SingleCardStore.front}</Katex>
                        {:else }
                            <SvelteMarkdown source="{$SingleCardStore.front}"/>
                        {/if}
                    </div>
                </div>
            </div>
            <div class="container-sm col">
                <div class="text-center mb-3"><p>Back</p></div>
                <div class="card bg-secondary mb-3 card-width" >
                    <div class="card-body">
                        {#if $SingleCardStore.template == 2}
                            <Katex>{$SingleCardStore.back}</Katex>
                        {:else }
                            <SvelteMarkdown source="{$SingleCardStore.back}"/>
                        {/if}
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
                                {#if $SingleCardStore.template === 1}
                                    <div class="mb-3">
                                        <label for="back-area" class="form-label">Back Area</label>
                                        <textarea bind:value={$SingleCardStore.back} style="color:black" class="form-control" id="back-area" rows="10" placeholder="Type in Markdown"></textarea>
                                    </div>
                                {:else if $SingleCardStore.template === 2}
                                    <div class="mb-3">
                                        <label for="back-area" class="form-label">Back Area</label>
                                        <textarea bind:value={$SingleCardStore.back} style="color:black" class="form-control" id="back-area" rows="10" placeholder="Type in latex"></textarea>
                                    </div>
                                {:else if $SingleCardStore.template === 3}
                                    <div class="mb-3">
                                        <label for="back-area" class="form-label">Back Area</label>
                                        <FilePond
                                                bind:this={pond}
                                                {name}
                                                server={{ process }}
                                                allowMultiple={false}
                                                allowImagePreview={true}
                                                allowImageResize={true}
                                                imageResizeTargetWidth={300}
                                                imageResizeTargetHeight={300}
                                                imageResizeMode="cover"
                                                allowImageTransform={true}
                                        />
                                    </div>
                                {/if}
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
                                            <h4>Date: {formatDate(history.history_date)}</h4>
                                        </div>
                                        <div class="container mb-3">
                                            <div class="row">
                                                <h5 class="text-center">Front</h5>
                                                <div class="col">
                                                    <div class="card bg-secondary card-width">
                                                        <div class="card-body">
                                                            {#if $SingleCardStore.template == 2}
                                                                <Katex>{history.front}</Katex>
                                                            {:else }
                                                                <SvelteMarkdown source="{history.front}"/>
                                                            {/if}
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
                                                            {#if $SingleCardStore.template == 2}
                                                                <Katex>{history.back}</Katex>
                                                            {:else }
                                                                <SvelteMarkdown source="{history.back}"/>
                                                            {/if}
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

