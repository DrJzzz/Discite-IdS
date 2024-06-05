<script>
    import {onMount} from "svelte";
    import {UserStore} from "../../../stores.js";
    import {getCookie} from "../../../utils/csrf.js";
    import {CameraPlus} from "phosphor-svelte";
    import {invalidateAll} from '$app/navigation';
    import {alertSuccess, alertError} from "../../../utils/alerts.js";


    export let data;
    let img = 'http://localhost:8000/media/blank-user-picture.jpg';
    onMount(() => {
        UserStore.set(data.user)
        img = data.img;
        console.log(img)
    })


    let imageFile = null;

    // Función para manejar el evento de cambio del input file
    function handleImageChange(event) {
        const file = event.target.files[0];
        if (file) {
            imageFile = file;
            handleImageUpload(imageFile)
        }
    }

    
    // Función para manejar el envío del archivo (por ejemplo, subirlo a un servidor)
    async function handleImageUpload(imageFile) {
        if (imageFile) {
            const formData = new FormData();
            formData.append('picture', imageFile);

            try {
                const token = localStorage.getItem('key');
                const csrftoken = getCookie('csrftoken');
                const response = await fetch('http://localhost:8000/users/4/set_user_picture/', {
                    method: 'PATCH',
                    headers: {
                        'Authorization': `Token ${token}`,
                        'X-CSRFToken': `${csrftoken}`
                    },
                    body: formData
                });

                if (response.ok) {
                    await invalidateAll();
                    alertSuccess('Change image successfully.');
                } else {
                    console.error('Error al subir el archivo');
                    alertError('Error changing the image.')
                }
            } catch (error) {
                console.error('Error al enviar el archivo:', error);
            }
        } else {
            console.error('No hay archivo seleccionado');
            alertError('Image file was empty.')
        }
    }
    async function handleSubmit() {
        try {
            const token = localStorage.getItem('key');
            const csrftoken = getCookie('csrftoken');
            const name = $UserStore.name;
            const birthdate = $UserStore.birthdate;
            const phone_number = $UserStore.phone_number;
            const email = $UserStore.email;
            const info = {name, birthdate, phone_number, email};
            const response = await fetch(`http://127.0.0.1:8000/rest-auth/user/`, {
                method: 'PUT',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                body: JSON.stringify(info)
            });


            if (response.ok) {
                alertSuccess('Updated user information.')
                await invalidateAll();

            } else {
                console.error('Failed to submit form');
                alertError('Error updating user information.')
            }
        } catch (error) {
            console.error('An error occurred while submitting the form.', error);
            alertError('An error occurred while updating user information.')
        }
    }

</script>

<style>
    .profile-img-container{
        position: relative;
    }


    .image{
        cursor: pointer;
        opacity: 1;
        width: 100%;
        height: auto;
        transition: .5s ease;
        backface-visibility: hidden;
    }

    .profile-img-container:hover .image{
        opacity: 0.3;
    }

    .profile-img-container:hover .midlle{
        opacity: 1;
    }

    .icon-img {
        color: white;
        font-size: 30px;
        padding: 16px 32px;
    }
    .midlle{
        transition: .5s ease;
        opacity: 0;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        -ms-transform: translate(-50%, -50%);
        text-align: center;
    }

</style>
{#if UserStore}
    <div class="container py-5 ">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-md-12 col-xl-4">
                <a class="button-edit" data-bs-toggle="modal" data-bs-target="#exampleModal">Edit profile</a>
                <div class="card" style="border-radius: 15px;">
                    <div class="card-body text-center">
                        <div class="profile-img-container">
                            <label for="uploadImage" >
                                <img src="{$UserStore.picture}"  alt="avatar"
                                     class="rounded-circle img-fluid image" style="width: 200px;">
                                <div class="midlle ">
                                    <div class="icon-img">
                                        <CameraPlus/>
                                    </div>

                                    <p class="text-secondary">Change image</p>
                                    <input on:change={handleImageChange} type="file" id="uploadImage" style="display:none">
                                </div>
                            </label>
                        </div>
                        <h4 class="mb-2">{$UserStore.name}</h4>
                        <p class="text-muted mb-4">@Email <span class="mx-2">|</span> <a
                                href="#!">{$UserStore.email}</a></p>
                        <div class="d-flex justify-content-between text-center mt-5 mb-2">
                            <div>
                                <p class="text-muted mb-0">Birthdate</p>
                                <p class="mb-2 h5">{$UserStore.birthdate}</p>

                            </div>
                            <div class="px-3">
                                <p class="text-muted mb-0">Phone Number</p>
                                <p class="mb-2 h5">{$UserStore.phone_number}</p>

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
                                        <input style="color: black;" bind:value={$UserStore.name} type="text" class="form-control" id="name" >
                                    </div>
                                    <div class="mb-3">
                                        <label for="phoneNumber" class="form-label">Phone Number</label>
                                        <input style="color: black;" type="tel" class="form-control" id="phoneNumber" bind:value={$UserStore.phone_number} placeholder="Enter your phone number">
                                    </div>
                                    <div class="mb-3">
                                        <label for="dob" class="form-label">Birthdate</label>
                                        <input style="color: black;" type="date" class="form-control" id="dob" bind:value={$UserStore.birthdate}>
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

