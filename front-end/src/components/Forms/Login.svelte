<script>
    import { goto } from '$app/navigation';
	import InputPassword from '../Inputs/InputPassword.svelte';
	import InputText from '../Inputs/InputText.svelte';

    let email = '';
    let password = '';

    async function handleSubmit() {
        const url = 'http://localhost:8000/rest-auth/login/';
        const data = {
            email,
            password
        };

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            
            if (response.ok) {                
                goto('/dashboard');
            } else {
                alert('Tu usuairo o contraseña son incorrectos, por favor intenta de nuevo.');
            }
            
        } catch (error) {
            alert("Bip bop, algo salió mal. Por favor intenta de nuevo.")
        }
    }
</script>

<main>
    <h1 class="text-2xl text-black">Login</h1>
    <form on:submit|preventDefault={handleSubmit}>
        <InputText label="Email" bind:value={email} placeholder="Email" required/>
        
        <InputPassword label="Password" bind:value={password} placeholder="Password" required/>
        
        <button type="submit">Login</button>
    </form>
</main>

<style>
    main {
        max-width: 400px;
        margin: 0 auto;
        padding: 2rem;
    }

    button {
        padding: 0.5rem 1rem;
        background-color: #007bff;
        color: #fff;
        border: none;
        cursor: pointer;
    }
</style>