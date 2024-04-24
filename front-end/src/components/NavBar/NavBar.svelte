<script lang="ts">
	import SimpleBtn from "../Buttons/SimpleBtn.svelte";
  let isOpen = false;

  function toggleMenu() {
    isOpen = !isOpen;
  }
</script>

<nav class="flex items-center justify-between px-6 py-2 bg-primaryBlue text-[#eaeaea]">

  <div class="flex items-center">
    <a href="/">
      <img src="favicon.png" alt="Logo" class="w-12 mx-4 bg-[#2e2f31]">
    </a>
  </div>
  
  <div class="md:flex hidden">
    <a href="/login" class="mx-2">
      <SimpleBtn text="Log In"/>
    </a>
       <a href="/signIn" class="mx-2">   
      <SimpleBtn text="Sign In"/>
    </a>
        
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
      <div class="absolute mt-1 right-0 bg-primaryBlue w-full py-2 shadow-lg z-50">
        <div class="w-full flex flex-col">
          <div class="w-fit my-2 ml-auto mr-6">
            <SimpleBtn text="Sign In"/>
          </div>
          <div class="w-fit my-2 ml-auto mr-6">
            <SimpleBtn text="Log In"/>
          </div>
          
        </div>
        
      </div>
    {/if}
  </div>
</nav>