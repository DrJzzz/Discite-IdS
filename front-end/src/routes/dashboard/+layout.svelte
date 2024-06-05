<script>
    import {House, CardsThree, Notebook, ShareFat} from "phosphor-svelte";
    import {UserStore} from "../../stores.js";
    import {getCookie} from "../../utils/csrf.js";
    import { derived } from 'svelte/store';
    import { page } from '$app/stores';
    /** @type {import('./$types').LayoutData} */
    export let data;
    // Derived store to get the current path
    const currentPath = derived(page, $page => $page.url.pathname);

    let activePath = '';

    $: {
        currentPath.subscribe(value => {
            activePath = value;
        });
    }

    async function logout(){
        try {
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');
            const endpoint = `http://localhost:8000/rest-auth/logout/`;
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': `${csrftoken}`, // Incluir el token CSRF en los encabezados
                    'Authorization': `Token ${token}`,
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
<style>
    .bg-dark {
        background-color: #212529 !important;
    }

    .nav-link.active {
        background-color: #5b62f4 !important;
    }

    .vh-100 {
        height: 100vh;
    }

    @media (max-width: 767.98px) {
        .col-md-3 {
            max-width: 100%;
        }
    }
</style>
<div class="container-fluid vh-100">
    <div class="row h-100">
        <div class="col-12 col-md-3 bg-dark text-white p-3 d-flex flex-column justify-content-between">
            <div>
                <!-- Botón de despliegue para pantallas pequeñas -->
                <button class="navbar-toggler d-md-none" type="button" data-bs-toggle="collapse" data-bs-target="#dashboardMenu" aria-controls="dashboardMenu" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse d-md-block" id="dashboardMenu">
                    <a href="/dashboard" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none">
                        <svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
                        <span class="fs-4">Dashboard</span>
                    </a>
                    <hr>
                    <ul class="nav nav-pills flex-column mb-auto">
                        <li class="nav-item">
                            <a href="/dashboard" class="nav-link {activePath === '/dashboard' ? 'active' : ''}">
                                <div class="d-flex align-items-center">
                                    <House />
                                    Home
                                </div>
                            </a>
                        </li>
                        <li>
                            <a href="/dashboard/decks" class="nav-link {activePath === '/dashboard/decks' ? 'active' : ''} text-white">
                                <div class="d-flex align-items-center">
                                    <CardsThree />
                                    My decks
                                </div>
                            </a>
                        </li>
                        <li>
                            <a href="/dashboard/notes" class="nav-link {activePath === '/dashboard/notes' ? 'active' : ''} text-white">
                                <div class="d-flex align-items-center">
                                    <Notebook />
                                    My notes
                                </div>
                            </a>
                        </li>
                        <li>
                            <a href="/dashboard/shares" class="nav-link {activePath === '/dashboard/shares' ? 'active' : ''} text-white">
                                <div class="d-flex align-items-center">
                                    <ShareFat />
                                    My Shares
                                </div>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="dropdown">
                {#if $UserStore}
                    <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
                        <img src="{$UserStore.picture}" alt="" width="32" height="32" class="rounded-circle me-2">
                        <strong>{$UserStore.name}</strong>
                    </a>
                {:else}
                    <strong>Cargando...</strong>
                {/if}
                <ul class="dropdown-menu dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser1">
                    <li><a class="dropdown-item" href="/dashboard/user">Profile</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="/" on:click={logout}>Sign out</a></li>
                </ul>
            </div>
        </div>
        <div class="col-12 col-md-9 p-3">
            <slot></slot>
        </div>
    </div>
</div>