<script lang="ts">
    export let isOpen = false;

    function closeModal() {
        isOpen = false;
    }

    function stopPropagation(event : any) {
        event.stopPropagation();
    }
</script>

<div class="fixed bg-black/30 inset-0 flex items-center justify-center z-50 {isOpen ? 'flex': 'hidden'}">
    <div on:click={stopPropagation} class="bg-white rounded-lg shadow-lg p-6 flex flex-col">
        <div class="flex ml-auto"><button class="text-black"  on:click={closeModal}>
            X
        </button></div>
        <!-- Modal content goes here -->
        <slot></slot>
    </div>
</div>

