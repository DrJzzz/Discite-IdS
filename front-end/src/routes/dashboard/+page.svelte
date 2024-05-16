<script>
    import {Brain} from "phosphor-svelte";
    import {goto} from "$app/navigation";

    function navigateToCard() {
        goto(`/dashboard/study`);
    }
</script>


<div>
    <button type="button" class="btn btn-primary" on:click={() => navigateToCard()}  >
        <div class="d-flex align-items-center">
            <Brain />
            Study cards
        </div>
    </button>
</div>

