<script>
    import {onMount} from "svelte";

    let title = '';
    let content = '';
    let id_notebook = "";

    async function handleSubmit() {
        const notebook_ref = '/notebooks/'+id_notebook+'/'
        const data = { title, content, notebook_ref };
        console.log(JSON.stringify(data))
        try {
            const response = await fetch('http://127.0.0.1:8000/notes/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
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

    let notebooks = [];

    async function getNotebooks() {
        try {
            const response = await fetch('http://127.0.0.1:8000/users/2/notebooks/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                },
                credentials : 'include'
            });

            if (response.ok) {

                const data =await  response.json()
                notebooks = data.notebooks

            } else {
                console.error('Failed decks');
            }
        } catch (error) {
            console.error('An error occurred while getting decks: ', error);
        }
    }
    onMount(getNotebooks);
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
                    {#each notebooks as notebook}
                        <option value="{notebook.id}">{notebook.name}</option>
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