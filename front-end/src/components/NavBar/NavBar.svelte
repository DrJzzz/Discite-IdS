<script lang="ts">
	import SimpleBtn from "../Buttons/SimpleBtn.svelte";
	import Login from "../Forms/Login.svelte";
	import Registro from "../Forms/Registro.svelte";
	import Modal from "../Modal/Modal.svelte";

  let isOpen = false;

  function toggleMenu() {
    isOpen = !isOpen;
  }

  function openLogin() {
    loginIsOpen = true;
  }

  function openRegistro() {
    registroIsOpen = true;
  }

  function closeLogin() {
    loginIsOpen = false;
  }

  function closeRegistro() {
    registroIsOpen = false;
  }

  let loginIsOpen = false;
  let registroIsOpen = false;
</script>


<nav class="flex items-center justify-between px-6 py-2 bg-[#2e2f31] text-[#eaeaea]">
  <Modal isOpen={loginIsOpen} on:close={closeLogin}>
    <slot>
      <Login />
    </slot>
  </Modal>

  <Modal isOpen={registroIsOpen} on:close={closeRegistro}>
    <slot> 
      <Registro isOpen={registroIsOpen}/>
    </slot>
  </Modal>

  <div class="flex items-center">
    <a href="/">
      <img src="favicon.png" alt="Logo" class="w-12 mx-4 bg-[#2e2f31]">
    </a>
  </div>
  
  <div class="md:flex hidden">
    <div class="mx-2">
      <SimpleBtn text="Log In" on:click={openLogin}/>
    </div>
          
      <SimpleBtn text="Sign In" on:click={openRegistro}/>
  </div>
  
<!-- Responsive Menu -->
  <div class="md:hidden">
    <button class="text-white" type="button" on:click={toggleMenu}>
      {#if isOpen}
        <img src="menu-toggle.svg" alt="Menu icon" />
      {:else}
      <img src="menu-toggle-hm.svg" alt="Menu icon" />
      {/if}
    </button>
    {#if isOpen}
      <div class="absolute mt-1 right-0 bg-[#2e2f31] w-full py-2 shadow-lg z-50">
        <div class="w-full flex flex-col">
          <div class="w-fit my-2 ml-auto mr-6">
            <SimpleBtn text="Sign In" on:click={openRegistro}/>
          </div>
          <div class="w-fit my-2 ml-auto mr-4">
            <SimpleBtn text="Log In" on:click={openLogin}/>
          </div>
          
        </div>
        
      </div>
    {/if}
  </div>
</nav>