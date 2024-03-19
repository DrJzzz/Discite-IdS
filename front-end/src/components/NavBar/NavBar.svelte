<script lang="ts">
	import { onMount } from "svelte";
	import SimpleBtn from "../Buttons/SimpleBtn.svelte";


  let isOpen = false;

  function toggleMenu() {
    isOpen = !isOpen;
  }
</script>


<nav class="flex items-center justify-between px-6 py-2 bg-[#2e2f31] text-[#eaeaea]">
  <div class="flex items-center">
    <a href="/">
      <img src="favicon.png" alt="Logo" class="w-12 mx-4 bg-[#2e2f31]">
    </a>
  </div>
  
  <div class="md:flex hidden">
    <div class="flex lg:ml-4">
      </div>
  </div>
  <a href="#contact-form" class="md:flex hidden">
    <SimpleBtn text="Log In" />
  </a>
  

  <div class="md:hidden">
    <button class="text-white" type="button" on:click={toggleMenu}>
      {#if isOpen}
        <img src="menu-toggle.svg" alt="Menu icon" />
      {:else}
      <img src="menu-toggle-hm.svg" alt="Menu icon" />
      {/if}
    </button>
    {#if isOpen}
      <div class="absolute mt-4 right-0 bg-[#2e2f31] w-full py-2 shadow-lg z-50">
        <div class="w-full flex">
          <a href="" class="ml-auto mr-3">
          <SimpleBtn text="Log In"/>
        </a>
        </div>
        
      </div>
    {/if}
  </div>
</nav>