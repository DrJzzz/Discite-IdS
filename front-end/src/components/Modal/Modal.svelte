<script lang="ts">
    export let isOpen = false;

    function closeModal() {
        isOpen = false;
    }

    function stopPropagation(event : any) {
        event.stopPropagation();
    }
</script>

<div class="fixed bg-black/30 inset-0 flex items-center justify-center z-50" style="display: {isOpen ? 'flex' : 'none'};">
    <div on:click={stopPropagation} class="bg-white rounded-lg shadow-lg p-6">
        <!-- Modal content goes here -->
        <slot></slot>

        <button class="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600" on:click={closeModal}>
            Close
        </button>
    </div>
</div>

