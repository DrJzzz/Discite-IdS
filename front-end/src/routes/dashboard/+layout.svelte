<script>
    import {House, CardsThree, Notebook, ShareFat} from "phosphor-svelte";
    import {onMount} from "svelte";
    import {UserStore} from "../../user-store.js";

    /** @type {import('./$types').LayoutData} */
    export let data;

    onMount(()=>{
        UserStore.set(data.user)
    })

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    async function logout(){
        try {
            const csrftoken = getCookie('csrftoken');

            const endpoint = `http://localhost:8000/rest-auth/logout/`;
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken // Incluir el token CSRF en los encabezados
                },
                credentials: 'include'
            });
            if (response.ok) {
                console.log('Logout successfully!');
            } else {
                console.error('Failed to logout');
            }
        } catch (error) {
            console.error('An error occurred while logout:', error);
        }
    }

</script>
<div class="container-fluid vh-100">
    <div class="row">
        <div class="container col" style="max-width: 280px;">
            <a href="/dashboard" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none">
                <svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
                <span class="fs-4">Dashboard</span>
            </a>
            <hr>
            <ul class="nav nav-pills flex-column mb-auto">
                <li class="nav-item">
                    <a href="/dashboard" class="nav-link active" aria-current="page">
                        <div class="d-flex align-items-center">
                            <House />
                            Home
                        </div>

                    </a>
                </li>
                <li>
                    <a href="/dashboard/decks" class="nav-link text-white">
                        <div class="d-flex align-items-center">
                            <CardsThree />
                            My decks
                        </div>
                    </a>
                </li>
                <li>
                    <a href="/dashboard/notes" class="nav-link text-white">
                        <div class="d-flex align-items-center">
                            <Notebook />
                            My notes
                        </div>
                    </a>
                </li>
                <li>
                    <a href="/dashboard/shares" class="nav-link text-white">
                        <div class="d-flex align-items-center">
                            <ShareFat />
                            My Shares
                        </div>
                    </a>
                </li>
            </ul>
            <hr>
            <div class="dropdown">
                <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
                    <img src="https://github.com/mdo.png" alt="" width="32" height="32" class="rounded-circle me-2">
                    {#if UserStore}
                        <strong>{$UserStore.name}</strong>
                    {:else }
                        <strong>Cargando..</strong>
                    {/if}
                </a>
                <ul class="dropdown-menu dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser1">
                    <li><a class="dropdown-item" href="/dashboard/user">Profile</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="/" on:click={() =>logout()}>Sign out</a></li>
                </ul>
            </div>
        </div>
        <div class="flex-1 p-8 col">
            <slot></slot>
        </div>
    </div>




</div>