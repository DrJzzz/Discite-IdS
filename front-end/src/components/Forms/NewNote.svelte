<script>
    import {onMount} from "svelte";
    import {UserStore} from "../../user-store.js";
    import {ImagesStore} from "../../images-store.js";
    import FilePond, { registerPlugin, supported } from 'svelte-filepond';
    import FilePondPluginImageExifOrientation from 'filepond-plugin-image-exif-orientation'
    import FilePondPluginImagePreview from 'filepond-plugin-image-preview'
    import {UsersStore} from "../../users-store.js";
    import {getCookie} from "../../utils/csrf.js";
    import {alertSuccess, alertError} from "../../utils/alerts.js";
    import {invalidateAll} from "$app/navigation";
    import {NotebookStore} from "../../notebook-store.js";

    registerPlugin(FilePondPluginImageExifOrientation, FilePondPluginImagePreview);

    let title = '';
    let content = '';
    let id_notebook = "";

    let user;

    if (UserStore){
        user = $UserStore;
    }

    async function handleSubmit() {
        const notebook = '/notebooks/'+id_notebook+'/'
        const data = { title, content, notebook };
        console.log(JSON.stringify(data))
        try {
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');
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
                alertSuccess('Added new note successfully.');
                await invalidateAll();
            } else {
                alertError('Failed to add new note.');
            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
            alertError('An error occurred while adding new note.');
        }
    }

    let notebooks = [];

    onMount(() => {
        ImagesStore.set([]);
    });
    // a reference to the component, used to call FilePond methods
    let pond;

    // pond.getFiles() will return the active files

    // the name to use for the internal file input
    let name = 'filepond';



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



<div>
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
                    {#each $NotebookStore as notebook}
                        <option value="{notebook.id}">{notebook.name}</option>
                    {/each}
                </select>
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
                        bind:this={pond}
                        {name}
                        server={{ process }}
                        allowMultiple={true}
                />

            </div>

        </div>

        <div class="modal-footer">
            <button type="button"  class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
        </div>
    </form>



</div>
