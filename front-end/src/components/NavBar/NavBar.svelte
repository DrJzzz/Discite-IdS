<script lang="ts">
	import SimpleBtn from "../Buttons/SimpleBtn.svelte";
	import Login from "../Forms/Login.svelte";
	import Registro from "../Forms/Registro.svelte";
	import Modal from "../Modal/Modal.svelte";

  let isOpen = false;

  function toggleMenu() {
    isOpen = !isOpen;
  }

  let modal1isOpen = false;
  let modal2isOpen = false;
</script>


<nav class="flex items-center justify-between px-6 py-2 bg-[#2e2f31] text-[#eaeaea]">
  <Modal isOpen={modal1isOpen}>
    <slot>
      <Login />
    </slot>
  </Modal>
  <Modal isOpen={modal2isOpen}>
    <slot> 
      <Registro/>
    </slot>
  </Modal>
  <div class="flex items-center">
    <a href="/">
      <img src="favicon.png" alt="Logo" class="w-12 mx-4 bg-[#2e2f31]">
    </a>
  </div>
  
  <div class="md:flex hidden">
    <SimpleBtn text="Log In" on:click={() => modal1isOpen = true}/>
          
          
      <SimpleBtn text="Log In" on:click={() => modal2isOpen = true}/>
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
        <div class="w-full flex">
          
            <SimpleBtn text="Sign In" on:click={() => {modal2isOpen = true; isOpen = false}}/>
            <SimpleBtn text="Log In" on:click={() => {modal1isOpen = true; isOpen = false}}/>
          
        </div>
        
      </div>
    {/if}
  </div>
</nav>