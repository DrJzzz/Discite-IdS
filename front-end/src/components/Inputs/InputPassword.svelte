<script lang="ts">
    export let value = '';
    export let placeholder = '';
    export let label = '';
    export let required = false;

    function handleChange(event: any) {
        value = event.target.value;
    }
</script>


<div class="flex flex-col mx-2 my-4">
    <p class="text-black">{label}</p>
    <input type="password" 
        required={required}
        class="rounded-sm text-black"
        bind:value={value} 
        placeholder={placeholder} 
        on:input={handleChange} />
</div>

<style>
    input {
        border: 1px solid #CFCFCF;
        padding: 3px 10px;
    }

    input::placeholder {
        color: #ADADAD;
        font-size: 14px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        margin-left: 2px;
    }

</style>