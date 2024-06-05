<script>
    import {UserStore} from "../../stores.js";
    import {getCookie} from "../../utils/csrf.js";
    import {alertError, alertSuccess} from "../../utils/alerts.js";
    import {invalidate, invalidateAll} from "$app/navigation";
    import {DeckStore} from "../../stores.js";
    import {Plus, X} from "phosphor-svelte";
    import {TagStore} from "../../stores.js";
    import FilePond, { registerPlugin, supported } from 'svelte-filepond';
    import FilePondPluginImageExifOrientation from 'filepond-plugin-image-exif-orientation';
    import FilePondPluginImagePreview from 'filepond-plugin-image-preview';
    import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.css';
    import FilePondPluginImageResize from 'filepond-plugin-image-resize';
    import FilePondPluginImageTransform from 'filepond-plugin-image-transform';
    registerPlugin(FilePondPluginImageExifOrientation, FilePondPluginImagePreview, FilePondPluginImageResize, FilePondPluginImageTransform);

    let front = '';
    let back = '';
    let id_deck = "";
    let templateOption = "";

    let decks = [];




    function resetTemplate(){
        templateOption = "";
        id_deck = "";
    }

    let user;

    if (UserStore){

        user = $UserStore;
    }

     async function handleSubmit() {
        const deck = '/decks/'+id_deck+'/'
         const tags = buttons
             .filter(button => button.color === 'btn-danger')
             .map(button => button.url);
        const template = parseInt(templateOption, 10);
        const data = { front, back, deck, tags, template};
        console.log(JSON.stringify(data))
        try {
            const token = localStorage.getItem('key');
            const csrftoken = getCookie('csrftoken');
            const response = await fetch('http://127.0.0.1:8000/cards/', {
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
                alertSuccess('Added new card successfully.');
                await invalidateAll().then(() => {

                });
                await invalidate('/dashboard/decks');
            } else {
                alertError('Failed to add new card.');
            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
            alertError('An error occurred while adding a card.')
        }
    }

    let buttons = [];

    // Suscribirse a TagStore y actualizar los botones cuando cambie
    const unsubscribe = TagStore.subscribe($TagStore => {
        buttons = $TagStore.map(data => ({
            ...data,
            color: 'btn-primary', // Color azul de Bootstrap
            icon: Plus // Icono de Phosphor Icons
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

    // a reference to the component, used to call FilePond methods
    let pond;

    // pond.getFiles() will return the active files

    // the name to use for the internal file input
    let name = 'filepond';



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
        back = '<img src="'+ imageUrl + '" alt="drawing" width="400"/>'
    }
</script>

<div>
    <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Add card</h5>
    </div>
    <form on:submit|preventDefault={handleSubmit}>
        <div class="modal-body">
            <div class="mb-3">
                <label for="front-area" class="form-label">Template</label>
                <select bind:value={templateOption} class="form-select" style="color:black" aria-label="Select template">
                    <option value="" disabled selected>Open to select template</option>
                    <option value="1">Basic</option>
                    <option value="2">Latex</option>
                    <option value="3">Image</option>
                </select>
            </div>
            {#if templateOption != 0}
                <div class="mb-3">
                    <label for="front-area" class="form-label">Deck</label>
                    <select bind:value={id_deck}  class="form-select" style="color:black" aria-label="Select template">
                        <option value="" disabled selected>Open to select a deck</option>
                        {#each $DeckStore as deck}
                        <option value="{deck.id}">{deck.name}</option>
                            {/each}
                    </select>
                </div>
            {/if}

            {#if templateOption === '1'}

                <div class="mb-3">
                    <label for="front-area" class="form-label">Front Area</label>
                    <textarea bind:value={front} style="color:black"  class="form-control" id="front-area" rows="5" placeholder="Type in Markdown"></textarea>
                </div>
                <div class="mb-3">
                    <label for="back-area" class="form-label">Back Area</label>
                    <textarea bind:value={back} style="color:black" class="form-control" id="back-area" rows="10" placeholder="Type in Markdown"></textarea>
                </div>
                {:else if templateOption === '2'}
                <div class="mb-3">
                    <label for="front-area" class="form-label">Front Area</label>
                    <textarea bind:value={front} style="color:black"  class="form-control" id="front-area" rows="5" placeholder="Type in latex"></textarea>
                </div>
                <div class="mb-3">
                    <label for="back-area" class="form-label">Back Area</label>
                    <textarea bind:value={back} style="color:black" class="form-control" id="back-area" rows="10" placeholder="Type in latex"></textarea>
                </div>
                {:else if templateOption === '3'}
                <div class="mb-3">
                    <label for="front-area" class="form-label">Front Area</label>
                    <textarea bind:value={front} style="color:black"  class="form-control" id="front-area" rows="5" placeholder="Type in Markdown"></textarea>
                </div>
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
            <button on:click={resetTemplate} type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            {#if templateOption != 0}
                <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
            {/if}
        </div>
    </form>



</div>