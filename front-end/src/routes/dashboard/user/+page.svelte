<script>
    import {onMount} from "svelte";

    let user;

    onMount(async function() {
        const token = localStorage.getItem('key');
        console.log(token);
        const endpoint = `http://localhost:8000/rest-auth/user/`;
        try {
            let response = await fetch(endpoint, {
                method: 'GET',
                credentials :'include'
            });

            if (response.ok) {
                // Convertir la respuesta a JSON
                const userData = await response.json();
                // Asignar los datos del usuario a la variable user
                user = userData;
                console.log(user)
            } else {
                // Mostrar un mensaje de error si la solicitud no fue exitosa
                console.error('Error al cargar el usuario:', response.statusText);
                user = null;
            }
        } catch (error) {
            // Mostrar un mensaje de error si hay un error en la solicitud
            console.error('Error al cargar el usuario:', error);
            user = null;
        }
    });

    async function handleSubmit() {
        console.log(JSON.stringify(user))
        try {
            const token = localStorage.getItem('key');
            const response = await fetch(`http://127.0.0.1:8000/users/${user.id}/`, {
                method: 'PUT',
                credentials :'include'
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

{#if user}
    <div class="container py-5 ">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-md-12 col-xl-4">
                <a class="button-edit" data-bs-toggle="modal" data-bs-target="#exampleModal">Edit profile</a>
                <div class="card" style="border-radius: 15px;">
                    <div class="card-body text-center">
                        <div class="mt-3 mb-4" style="margin-left: 35%">
                            <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava2-bg.webp"
                                 class="rounded-circle img-fluid" style="width: 100px;" />
                        </div>
                        <h4 class="mb-2">{user.name}</h4>
                        <p class="text-muted mb-4">@Email <span class="mx-2">|</span> <a
                                href="#!">{user.email}</a></p>
                        <div class="d-flex justify-content-between text-center mt-5 mb-2">
                            <div>
                                <p class="text-muted mb-0">Birthdate</p>
                                <p class="mb-2 h5">{user.birthdate}</p>

                            </div>
                            <div class="px-3">
                                <p class="text-muted mb-0">Phone Number</p>
                                <p class="mb-2 h5">{user.phone_number}</p>

                            </div>
                        </div>
                        <div class="d-flex justify-content-between text-center mt-5 mb-2">
                            <div>
                                <p class="mb-2 h5">3</p>
                                <p class="text-muted mb-0">Cards</p>
                            </div>
                            <div class="px-3">
                                <p class="mb-2 h5">12</p>
                                <p class="text-muted mb-0">Decks</p>
                            </div>
                            <div>
                                <p class="mb-2 h5">10</p>
                                <p class="text-muted mb-0">Notes</p>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Modal -->
                <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="exampleModalLabel">Edit card</h5>
                            </div>
                            <form on:submit|preventDefault={handleSubmit}>
                                <div class="modal-body">

                                    <div class="mb-3" >
                                        <label for="name" class="form-label">Name</label>
                                        <input style="color: black;" bind:value={user.name} type="text" class="form-control" id="name" >
                                    </div>
                                    <div class="mb-3">
                                        <label for="phoneNumber" class="form-label">Phone Number</label>
                                        <input style="color: black;" type="tel" class="form-control" id="phoneNumber" bind:value={user.phone_number} placeholder="Enter your phone number">
                                    </div>
                                    <div class="mb-3">
                                        <label for="dob" class="form-label">Birthdate</label>
                                        <input style="color: black;" type="date" class="form-control" id="dob" bind:value={user.birthdate}>
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
        </div>
    </div>
    </div>
    {:else}
    <h3>User not found</h3>
{/if}

