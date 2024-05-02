<script>
    import { goto } from '$app/navigation';
	import InputPassword from '../Inputs/InputPassword.svelte';
	import InputText from '../Inputs/InputText.svelte';

    let name = '';
    let email = '';

    let password1 = '';
    let password2 = '';
    let phone_number = ""
    let birthdate = ""

    async function handleSubmit() {
        const url = 'http://localhost:8000/rest-auth/registration/';
        const data = {
            name,
            email,
            phone_number,
            birthdate,
            "max_reviews" : 0, 
            password1,
            password2,
  
        };
        console.log(data)
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
                goto('/login')
            } else {
                console.log(response.statusText)
                alert('Tu usuairo o contraseña son incorrectos, por favor intenta de nuevo.');
            }
            
        } catch (error) {
            alert("Bip bop, algo salió mal. Por favor intenta de nuevo.")
        }
    }
</script>

<main>
    <h1 class="">Sign in</h1>
    <form on:submit|preventDefault={handleSubmit}>
        <div class="mb-3" >
            <label for="name" class="form-label">Name</label>
            <input style="color: black;" bind:value={name} type="text" class="form-control" id="name" >
        </div>
        <div class="mb-3" >
            <label for="exampleInputEmail1" class="form-label">Email address</label>
            <input style="color: black;"  bind:value={email} type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
            <label for="phoneNumber" class="form-label">Phone Number</label>
            <input style="color: black;" type="tel" class="form-control" id="phoneNumber" bind:value={phone_number} placeholder="Enter your phone number">
        </div>
        <div class="mb-3">
            <label for="dob" class="form-label">Birthdate</label>
            <input style="color: black;" type="date" class="form-control" id="dob" bind:value={birthdate}>
        </div>
        <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input style="color: black;"  bind:value={password1} type="password" class="form-control" id="exampleInputPassword1">
        </div>
        <div class="mb-3">
            <label for="exampleInputPassword2" class="form-label">Confirm Password</label>
            <input style="color: black;" bind:value={password2} type="password" class="form-control" id="exampleInputPassword2">
        </div>
        
        <button class="btn btn-primary" type="submit">Sign in</button>
    </form>
</main>

<style>
    main {
        max-width: 400px;
        margin: 0 auto;
        padding: 2rem;
    }

</style>