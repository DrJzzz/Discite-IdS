
<script>
    import NavBar from "../components/NavBar/NavBar.svelte";

    import Footer from "../components/Footer/Footer.svelte";
</script>

<NavBar />
<slot />

<div class="container">
    <div class="header">
        <h1 class="title">Learning Made Simple</h1>
        <p class="subtitle">
            Take notes and create flashcards using Markdown,
            then study them using spaced repetition.
        </p>
        <div class="actions">
            <a href="/signIn">
                <button class="button">Sign in</button>
            </a>
        </div>
    </div>
    <div class="image-placeholder">

        <img src="./images/anki.png" alt="Anki Card">
    </div>
</div>

<div class="dual-features">
    <div class="feature">
        <div class="feature-title">
            Your Learning Companion, Anywhere all the time
        </div>
        <p class="feature-description">
            Access your notes and flashcards from anywhere, all the time!
            Accses from your phone, tablet or computer.
        </p>
    </div>

    <div class="feature">
        <div class="feature-title">
            Focus on what matters
        </div>
        <p class="feature-description">
            Leave to us to remind you what to study and when, you just focus on learning.
            Thanks to our spaced repetition algorithm, you'll maximize your learning.
        </p>
    </div>
</div>

<div class="markdown-enabled-section">
    <div class="markdown-content">
        <h2 class="markdown-title">Easy export and import</h2>
        <p class="markdown-description">
            Evrything will be written and stored as markdown, 
            so you can easly export and import your notes and flashcards.
        </p>
    </div>

    <div class="markdown-content">
        <h2 class="markdown-title">Support for many formats</h2>
        <p class="markdown-description">
           Add images, videos and more easly to your notes and flashcards.
        </p>
    </div>
</div>






<style>
    .container {
        display: flex; /* Flexbox para el contenedor */
        justify-content: space-between; /* Espacio entre los elementos */
        align-items: center; /* Alinear los ítems verticalmente */
        padding: 100px; /* Espaciado alrededor del contenido */
        background-color: #1c1c1c; /* Fondo oscuro */
        color: white; /* Texto claro */
        margin-bottom: 32px;
    }

    .header {
        max-width: 50%; /* Máximo ancho para el contenido de texto */
    }

    .title {
        font-size: 48px; /* Tamaño de fuente grande para el título */
        margin: 0; /* Remover el margen por defecto */
        line-height: 1.2; /* Espaciado de línea para el título */
    }

    .subtitle {
        font-size: 20px; /* Tamaño de fuente para el subtítulo */
        margin: 20px 0; /* Espacio entre el título y los botones */
    }

    .actions {
        display: flex; /* Flexbox para los botones de acción */
        align-items: center; /* Alinear los ítems verticalmente */
    }

    .button {
        padding: 10px 20px; /* Espaciado interno del botón */
        margin-right: 10px; /* Espacio entre los botones */
        background-color: #333; /* Fondo de los botones */
        color: white; /* Color del texto del botón */
        border: none; /* Sin bordes */
        border-radius: 5px; /* Bordes redondeados */
        cursor: pointer; /* Cursor tipo puntero */
        text-transform: uppercase; /* Texto en mayúsculas */
        font-weight: bold; /* Texto en negrita */
    }

    .button:hover {
        background-color: #555; /* Cambio de color al pasar el ratón */
    }

    .link {
        color: #4b8bec; /* Color para el enlace 'Try it online' */
        text-decoration: none; /* Sin subrayado en el enlace */
        cursor: pointer;
    }

    .image-placeholder {
        display: flex;
        max-width: 600px;
        width: 50%;
        margin-left: 20px;
    }
    .image-placeholder img {
        width: 100%;
        height: auto;
    }

    /* Agrega estilos responsivos si es necesario */
    @media (max-width: 768px) {
        .container {
            flex-direction: column; /* Cambia a una columna para móviles */
        }

        .header, .image-placeholder {
            max-width: 100%; /* Ancho completo en móviles */
        }

        .actions {
            flex-direction: column; /* Botones en columna en móviles */
        }

        .button {
            margin-bottom: 10px; /* Espacio entre botones en móviles */
        }
    }

    /* Asegúrate de que el contenedor de tu sección ocupa toda la altura de la ventana gráfica para que todo esté centrado verticalmente también */
    .feature-section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 70vh;
        background-color: #1c1c1c; /* O el color exacto de tu diseño */
        color: white;
        font-family: 'Arial', sans-serif; /* Cambia esto por la fuente que estás utilizando */
        padding: 20px;
        box-sizing: border-box;
    }

    /* Aplica un tamaño de fuente más grande y otros estilos para el título para destacarlo */
    .feature-title {
        font-size: 4rem; /* Ajusta este tamaño según tus necesidades */
        font-weight: 700; /* Fuente en negrita */
        margin: 0 0 20px; /* Asegúrate de que no hay margen arriba del título y hay algo de espacio debajo */
    }

    /* Asegúrate de que la descripción también esté centrada y con un tamaño adecuado */
    .feature-description {
        font-size: 1.25rem; /* Ajusta este tamaño según tus necesidades */
        max-width: 800px; /* O el ancho máximo que prefieras */
        text-align: justify; /* Esto centrará el texto */
        margin: 0;
        padding: 0 20px; /* Para evitar que el texto toque los bordes de la pantalla */
        text-justify: inter-word;
    }

    .dual-features {
        display: flex; /* Usar flexbox para estructurar las dos columnas */
        justify-content: space-between; /* Espacio igual entre las columnas */
        background-color: #1c1c1c; /* El mismo fondo que la sección anterior */
        padding: 40px; /* Espaciado similar al de la sección anterior */
        color: white;
    }

    .feature {
        width: 48%; /* Dar a cada característica el 48% del ancho para dejar espacio entre */
    }

    .feature-icon {
        /* Estilos para los íconos, reemplazar con íconos reales */
        margin-right: 10px; /* Margen a la derecha del ícono */
        display: inline-block; /* Íconos en línea con el texto */
        vertical-align: middle; /* Alinear verticalmente con el texto */
    }

    .feature-title {
        font-size: 24px; /* Tamaño del título */
        margin: 0 0 10px 0; /* Margen debajo del título */
        display: flex; /* Flexbox para título e ícono */
        align-items: center; /* Alineación vertical del título e ícono */
    }

    .feature-description {
        font-size: 16px; /* Tamaño para la descripción */
    }



    /* Estilos para la nueva sección */
    .markdown-enabled-section {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 40px;
        background-color: #1a1a1a; /* O el color de fondo de tu elección */
        color: white;
    }

    .markdown-content {
        margin: 8px 16px; /* Margen interno para el contenido */
        flex: 1; /* Ocupa el espacio disponible en proporción */
        max-width: 50%; /* Máximo de ancho para el contenido del texto */
    }

    .markdown-title {
        font-size: 2rem; /* Tamaño de la fuente del título */
        margin-bottom: 0.5em;
    }

    .markdown-description {
        font-size: 1rem;
    }

    .markdown-image {
        flex: 1; /* Ocupa el espacio disponible en proporción */
        max-width: 50%; /* Máximo de ancho para la imagen */
        text-align: right; /* Alinea la imagen a la derecha */
    }

    .markdown-image img {
        max-width: 100%; /* Hace que la imagen sea responsive */
        height: auto; /* Mantiene la proporción de la imagen */
    }



    .attachment-section {
        display: flex;
        align-items: center; /* Alinea verticalmente el contenido */
        justify-content: space-between; /* Espacia los elementos hijos */
        padding: 40px;
        background-color: #1c1c1c; /* Ajusta el color de fondo según tu diseño */
        color: white; /* Ajusta el color del texto según tu diseño */
    }

    .attachment-content, .attachment-image {
        flex: 1; /* Esto dividirá el espacio disponible por igual entre el contenido y la imagen */
    }

    .attachment-title {
        font-size: 2rem; /* Ajusta el tamaño según necesites */
        margin-bottom: 0.5rem;
    }

    .attachment-description {
        font-size: 1rem; /* Ajusta el tamaño según necesites */
    }

    .attachment-image img {
        max-width: 100%; /* Asegúrate de que la imagen no se desborde de su contenedor */
        height: auto; /* Mantiene la proporción de la imagen */
    }




    .features-section {
        display: grid;
        grid-template-columns: repeat(4, 1fr); /* Cuatro columnas de igual ancho */
        gap: 20px; /* Espacio entre los elementos del grid */
        justify-content: center; /* Centra el grid en el contenedor */
        align-items: start; /* Alinea los elementos al inicio de sus respectivas celdas */
        padding: 40px 0;
        background-color: #1c1c1c; /* El color de fondo de tu sección */
        color: white;
    }

    .feature-item {
        text-align: center; /* Centra el texto dentro de cada bloque */
    }

    .icon {
        /* Añade estilos a tus íconos aquí. Asumiendo que usas emojis o texto como íconos */
        display: block;
        font-size: 2rem;
        margin-bottom: 10px;
    }

    .feature-title {
        font-size: 1.2rem;
        margin-bottom: 5px;
    }

    .feature-description {
        font-size: 0.9rem;
    }

    /* Asegúrate de que el contenido no es demasiado ancho en pantallas grandes */
    @media (max-width: 1200px) {
        .features-section {
            grid-template-columns: repeat(2, 1fr); /* Dos columnas en pantallas medianas */
        }
    }

    @media (max-width: 768px) {
        .features-section {
            grid-template-columns: 1fr; /* Una columna en pantallas pequeñas */
        }
    }

</style>