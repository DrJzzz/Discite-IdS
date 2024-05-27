<script>
    import {UserStore} from "../../user-store.js";
    import {getCookie} from "../../utils/csrf.js";
    import {alertSuccess, alertError} from "../../utils/alerts.js";
    import {invalidateAll} from "$app/navigation";
    import {Plus, X} from "phosphor-svelte";
    import {TagStore} from "../../tag-store.js";
    let name = '';
    let user;

    if (UserStore){

        user = $UserStore;
    }
    async function handleSubmit() {
        const owner = user.id;
        const tags = buttons
            .filter(button => button.color === 'btn-danger')
            .map(button => button.id);
        const data = {name, owner, tags };
        console.log(JSON.stringify(data))
        try {
            const token = localStorage.getItem('key');
            const csrftoken = getCookie('csrftoken');
            const response = await fetch('http://127.0.0.1:8000/decks/', {
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
                alertSuccess('Added new deck.');
                await invalidateAll();
            } else {
                alertError('Failed to add new deck.');
            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
            alertError('An error occurred while adding new deck.');
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

    
</script>

<div>
    <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Add deck</h5>
    </div>
    <form on:submit|preventDefault={handleSubmit}>
        <div class="modal-body">
            <div class="form-floating mb-3">
                <input bind:value={name} type="text" class="form-control" id="floatingInput" placeholder="name" style="color:black" >
                <label for="floatingInput" style="color:black" >Name</label>
            </div>
            
            <div class="mb-3">
                <h4>Tags</h4>
                <hl>
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
            <button  type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
        </div>
    </form>



</div>