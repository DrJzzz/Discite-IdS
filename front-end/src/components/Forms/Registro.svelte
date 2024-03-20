<script>
    import { goto } from '$app/navigation';
	import InputPassword from '../Inputs/InputPassword.svelte';
	import InputText from '../Inputs/InputText.svelte';

    export let isOpen
    let name = '';
    let email = '';

    let password1 = '';
    let password2 = '';

    async function handleSubmit() {
        const url = 'http://localhost:8000/rest-auth/registration/';
        const data = {
            "name": name,
            email,
            "phone_number": "0000000000",
            "birth_date": "1999-04-09",
            "max_reviews" : 0, 
            password1,
            password2,
  
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
                alert('Usuario creado exitosamente');
                isOpen = false;
            } else {
                alert('Tu usuairo o contraseña son incorrectos, por favor intenta de nuevo.');
            }
            
        } catch (error) {
            alert("Bip bop, algo salió mal. Por favor intenta de nuevo.")
        }
    }
</script>

<main>
    <h1 class="text-2xl text-black">Registro</h1>
    <form on:submit|preventDefault={handleSubmit}>
        <InputText label="Name" bind:value={name} placeholder="Name"/>

        <InputText label="Email" bind:value={email} placeholder="Email"/>
        
        <InputPassword label="Password" bind:value={password1} placeholder="Password"/>
        <InputPassword label="Confirm Password" bind:value={password2} placeholder="Confirm Password"/>
        
        <button type="submit">Sign in</button>
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