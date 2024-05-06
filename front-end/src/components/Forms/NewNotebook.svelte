<script>
    let name = '';
    async function handleSubmit() {
        const owner = 1;

        const data = {name, owner };
        console.log(JSON.stringify(data))
        try {
            const response = await fetch('http://127.0.0.1:8000/notebook/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
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


</script>

<div>
    <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Add notebook</h5>
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