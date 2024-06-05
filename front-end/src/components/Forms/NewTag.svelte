<script>
    import {getCookie} from "../../utils/csrf.js";
    import {alertError, alertSuccess} from "../../utils/alerts.js";
    import {invalidateAll} from "$app/navigation";

    let name = '';
    async function handleSubmit() {
        try {
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');
            const info = {name}
            const response = await fetch('http://127.0.0.1:8000/tags/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                body: JSON.stringify(info),
                credentials : 'include'
            });

            if (response.ok) {
                alertSuccess('Added new tag successfully.');
                await invalidateAll();
            } else {
                alertError('Failed to add new tag.');
            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
            alertError('An error occurred while adding new tag.');
        }
    }
</script>


<div>
    <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Add tag</h5>
    </div>
    <form on:submit|preventDefault={handleSubmit}>
        <div class="modal-body">

            <div class="mb-3">
                <label for="title" class="form-label">Name</label>
                <input type="text" bind:value={name} style="color:black"  class="form-control" id="title" >
            </div>

        </div>

        <div class="modal-footer">
            <button type="button"  class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
        </div>
    </form>



</div>