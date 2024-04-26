<script lang="ts">
	import SimpleBtn from "../Buttons/SimpleBtn.svelte";
  import FavIcon from "../../lib/images/favicon.png"
  import MenuToggle from "../../lib/images/menu-toggle.svg"
  import MenuToggleHm from "../../lib/images/menu-toggle-hm.svg"

  let isOpen = false;

  function toggleMenu() {
    isOpen = !isOpen;
  }
</script>


<nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark" >
  <div class="container-fluid">
    <a class="navbar-brand" href="/landing">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor04" aria-controls="navbarColor04" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarColor02">
      <ul class="navbar-nav me-auto">
        <li class="nav-item">
          <a class="nav-link active" href="/">Home
            <span class="visually-hidden"></span>
          </a>
        </li>
      </ul>


    </div>
    <div class="container-sm ms-auto" >
      <button type="button" class="btn btn-outline-dark"><a href="/login">Login</a></button>
      <button type="button" class="btn btn-outline-dark"><a href="/signIn">Sign In</a></button>
    </div>
  </div>
</nav>
