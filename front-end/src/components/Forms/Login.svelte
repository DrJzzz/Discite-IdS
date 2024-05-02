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
                localStorage.setItem('key', result.key);             
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
    <div class="container-fluid align-content-center " >
        <div class="row">
            <div class="col-md-4"></div>
            <div class="col-md-4">
                <h1 >Login</h1>
                <form on:submit|preventDefault={handleSubmit}>
                    <div class="mb-3" >
                        <label for="exampleInputEmail1" class="form-label">Email address</label>
                        <input  style="color: black;" bind:value={email} type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Password</label>
                        <input style="color: black;" bind:value={password} type="password" class="form-control" id="exampleInputPassword1">
                    </div>
                    <div class="mb-3 form-check">
                        <input type="checkbox" class="form-check-input" id="exampleCheck1">
                        <label class="form-check-label" for="exampleCheck1">Check me out</label>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
            <div class="col-md-4"></div>
        </div>

    </div>
</main>
