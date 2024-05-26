<script>
	import { page } from '$app/stores';
	import NavBar from '../components/NavBar/NavBar.svelte';
</script>

<NavBar />
{#if $page.status === 404}
    <div>
        <h1>Ups... Page not found, want to go <a href="/">home?</a></h1>
    </div>
    
{:else}
    {#if $page.error}
        <h1>Ups... {$page.status}: {$page.error.message}</h1>
    {/if}
    <p>Want to go <a href="/">home?</a></p>
{/if}
    
<style>
    h1 {
        margin-top: 16px;
        text-align: center;
        margin-bottom: auto;
    }
</style>