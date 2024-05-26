<script>
	import SimpleBtn from "../Buttons/SimpleBtn.svelte";
    import {UserStore} from "../../user-store.js";
    import {getCookie} from "../../utils/csrf.js";

    let front = '';
    let back = '';
    let id_deck = "";
    let template = "";

    let decks = [];




    function resetTemplate(){
        template = "";
        id_deck = "";
    }

    let user;

    if (UserStore){

        user = $UserStore;
    }

    async function getDecks() {
        try {
            const token = localStorage.getItem('key');
            const csrftoken = getCookie('csrftoken');
            const response = await fetch(`http://127.0.0.1:8000/users/${user.id}/decks/`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
            });

            if (response.ok) {

                decks =await  response.json()
            } else {
                console.error('Failed decks');
            }
        } catch (error) {
            console.error('An error occurred while getting decks: ', error);
        }
    }

     async function handleSubmit() {
        const deck = '/decks/'+id_deck+'/'
        const data = { front, back, deck };
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
                console.log('Form submitted successfully!');
            } else {
                console.error('Failed to submit form');
            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
        }
    }

    getDecks()
</script>

<div>
    <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Add card</h5>
    </div>
    <form on:submit|preventDefault={handleSubmit}>
        <div class="modal-body">
            <div class="mb-3">
                <label for="front-area" class="form-label">Template</label>
                <select bind:value={template}  class="form-select" style="color:black" aria-label="Select template">
                    <option value="" disabled selected>Open to select template</option>
                    <option value="1">Basic</option>
                </select>
            </div>
            {#if template != 0}
                <div class="mb-3">
                    <label for="front-area" class="form-label">Deck</label>
                    <select bind:value={id_deck}  class="form-select" style="color:black" aria-label="Select template">
                        <option value="" disabled selected>Open to select a deck</option>
                        {#each decks.decks as deck}
                        <option value="{deck.id}">{deck.name}</option>
                            {/each}
                    </select>
                </div>
            {/if}
            {#if template == 1}

                <div class="mb-3">
                    <label for="front-area" class="form-label">Front Area</label>
                    <textarea bind:value={front} style="color:black"  class="form-control" id="front-area" rows="5" placeholder="Type in Markdown"></textarea>
                </div>
                <div class="mb-3">
                    <label for="back-area" class="form-label">Back Area</label>
                    <textarea bind:value={back} style="color:black" class="form-control" id="back-area" rows="10" placeholder="Type in Markdown"></textarea>
                </div>
            {/if}


        </div>

        <div class="modal-footer">
            <button on:click={resetTemplate} type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            {#if template != 0}
                <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
            {/if}
        </div>
    </form>



</div>