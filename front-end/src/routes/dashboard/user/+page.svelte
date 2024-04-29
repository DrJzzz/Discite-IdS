<script>
    import {onMount} from "svelte";

    let user;

    onMount(async function() {
        const endpoint = `http://localhost:8000/users/1/`;
        try {
            let response = await fetch(endpoint);
            if (response.status == 200) {
                user = await response.json();
                console.log(user);
            } else {
                user = null;
            }
        } catch (error) {
            console.error('Error al cargar la carta:', error);
            user = null;
        }
    });
</script>

{#if user}
    <div class="container py-5 ">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-md-12 col-xl-4">

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

            </div>
        </div>
    </div>
    {:else }
    <h3>User not found</h3>
    {/if}

