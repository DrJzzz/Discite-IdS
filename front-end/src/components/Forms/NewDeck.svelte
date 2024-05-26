<script>
    import {UserStore} from "../../user-store.js";
    import {getCookie} from "../../utils/csrf.js";
    import {alertSuccess, alertError} from "../../utils/alerts.js";
    import {invalidateAll} from "$app/navigation";

    let name = '';
    let user;

    if (UserStore){

        user = $UserStore;
    }
    async function handleSubmit() {
        const owner = user.id;

        const data = {name, owner };
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



        </div>

        <div class="modal-footer">
            <button  type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
        </div>
    </form>



</div>