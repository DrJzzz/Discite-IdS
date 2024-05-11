<script>
    import {House, CardsThree, Notebook} from "phosphor-svelte";

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
            </ul>
            <hr>
            <div class="dropdown">
                <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
                    <img src="https://github.com/mdo.png" alt="" width="32" height="32" class="rounded-circle me-2">
                    <strong>User</strong>
                </a>
                <ul class="dropdown-menu dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser1">
                    <li><a class="dropdown-item" href="/dashboard/user">Profile</a></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="/">Sign out</a></li>
                </ul>
            </div>
        </div>
        <div class="flex-1 p-8 col">
            <slot></slot>
        </div>
    </div>




</div>