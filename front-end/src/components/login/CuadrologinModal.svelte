<script>
  import { createEventDispatcher } from 'svelte';

  let showModal = true;
  let username = '';
  let email = '';
  let password='';

  const dispatch = createEventDispatcher();

  function toggleModal() {
    showModal = !showModal;
  }

  function handleSubmit() {
    // Aquí puedes enviar los datos del formulario al servidor
    const formData = {
      username,
      email
    };
    console.log('Datos enviados:', formData);

    // Aquí puedes cerrar el modal o realizar otras acciones después del envío exitoso
    toggleModal();
  }
</script>


{#if showModal}
  <div class="modal">
    <div class="modal-content">
      <span class="close" on:click={toggleModal}>&times;</span>
      <h2>Registro</h2>

     <!-- <form on:submit|preventDefault={handleSubmit}>-->


    <form on:submit={handleSubmit}>
        <label>   <!--esto lo que hace es asociar a que viene un campo de entrada o un formulario -->
        Nombre de usuario:
        <input type="text" bind:value={username} required />   <!--el tipo de entrada que viene-->
        </label>
        <label>
        Correo electrónico:
        <input type="email" bind:value={email} required />   <!--{email es la variable que guarda el }-->
        </label>
        <label>
        Contraseña:
        <input type="password" bind:value={password} required />
        </label>
        <button type="submit">Registrarse</button>
  </form>

    </div>
  </div>
{/if}



<style>
    /* Estilos para el formulario, puedes personalizarlos según tus necesidades */
    form {
     /* padding-top: 10%;
      padding-bottom:10% ;*/
      max-width: 400px;  /**Esto es el ancho del texto*/
      margin: 0 auto;
    }

    h2{
        position: relative;
        right: -20%;
    }

    label {
      
      display: block;
      margin-bottom: 0.5rem;
    }
    input {
      width: 100%;
      padding: 0.5rem;
      margin-bottom: 1rem;
    }
    button {
      padding: 0.5rem 1rem;
      background-color: #007bff;
      color: white;
      border: none;
      cursor: pointer;
    }



    .modal {
      display: block;
      position: fixed;
      z-index: 1;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      overflow: auto;
      /*background-color: rgba(0, 0, 0, 0.5);*/
      /*border-radius: 50%;*/
    
    }




        
    .modal-content {
        background-color: rgb(109, 113, 114);
        margin: 10% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 40%;   /**Esto es el ancho del modal */
    }


    .close {
      color: red;
    float: right;
    font-size: 28px;
    font-weight: bold;
  }

  .close:hover,
  .close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
  }
  </style>






