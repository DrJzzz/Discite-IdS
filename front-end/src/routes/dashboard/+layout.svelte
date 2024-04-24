<script>
    let isOpen = false;

    function toggleMenu() {
        isOpen = !isOpen;
    }
</script>

<style>
    .menu {
        top: 0;
        left: 0;
        transition: transform 0.3s ease-in-out;
        transform: translateX(-200px);
    }

    .menu.open {
        transform: translateX(0);
    }

    .content {
        margin-left: 200px;
        transition: margin-left 0.3s ease-in-out;
    }

    .content.open {
        margin-left: 0;
    }
</style>

<!-- Menu-->
<div class="w-[200px] h-[100vh] bg-[#2d3542] fixed menu {isOpen ? 'open' : ''}">
    <button on:click={toggleMenu}>Toggle Menu</button>
    
</div>

<!-- Content -->
<div class="content {isOpen ? 'open' : ''}">
    <button on:click={toggleMenu}>Toggle Menu</button>
    <slot />
</div>