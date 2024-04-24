<script>

</script>

<style>
    .container {
        display: flex; /* Flexbox para el contenedor */
        justify-content: space-between; /* Espacio entre los elementos */
        align-items: center; /* Alinear los ítems verticalmente */
        padding: 100px; /* Espaciado alrededor del contenido */
        background-color: #1c1c1c; /* Fondo oscuro */
        color: white; /* Texto claro */
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
        /* Reemplaza esto con tu imagen real */
        width: 50%; /* Ancho para la imagen */
        height: 300px; /* Altura para la imagen */
        background-color: #333; /* Fondo de ejemplo para la imagen */
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

<div class="container">
    <div class="header">
        <h1 class="title">Un espacio comodo para Aprender </h1>
        <p class="subtitle">
            Toma notas y crea tarjetas didácticas usando Markdown,
            luego estúdialos usando repeticiones espaciadas.

        </p>
        <div class="actions">
            <button class="button">Registrarse</button>
            <a> </a>
            <a class="link">Saber mas</a>
        </div>
    </div>
    <div class="image-placeholder">

        <img src="anki.png" alt="Descripción de la imagen">
    </div>
</div>

<div class="feature-section">
    <h2 class="feature-title">Poder en la sencillez </h2>
    <p class="feature-description">
        Simple pero poderoso, como un lienzo en blanco listo para capturar
        la complejidad de tus pensamientos e ideas.
    </p>
</div>

<div class="dual-features">
    <div class="feature">
        <div class="feature-title">
            <span class="feature-icon"> En linea</span>
            --- Siempre disponible
        </div>
        <p class="feature-description">
            Accede al conocimiento sin límites de tiempo o lugar, diseñado para acompañarte en cada paso
            de tu aprendizaje continuo, estés donde estés.
        </p>
    </div>

    <div class="feature">
        <div class="feature-title">
            <span class="feature-icon">Un Espacio Libre</span>
            -- Diseña tu propio espacio
        </div>
        <p class="feature-description">
            Disfruta creando tu espacio de estudio, segun tus necesidades, con ideas
            y conceptos que te ayuden a aprender y recordar.
        </p>
    </div>
</div>

<div class="markdown-enabled-section">
    <div class="markdown-content">
        <h2 class="markdown-title">Habilitado para Markdown</h2>
        <p class="markdown-description">
            Anota rápidamente notas y tarjetas al ritmo de markdown. Controles de formato y atajos también están disponibles si los necesitas. Aprende más sobre markdown.
        </p>
    </div>
    <div class="markdown-image">

        <img src="md.png" alt="Interfaz de usuario de markdown" />
    </div>
</div>

<div class="attachment-section">
    <div class="attachment-content">
        <h2 class="attachment-title">Archivos adjuntos</h2>
        <p class="attachment-description">
            Puedes insertar medios en sus notas o tarjetas, como imágenes, audio y video, arrastrándolos al editor.
        </p>
    </div>
    <div class="attachment-image">
        <!-- Coloca aquí tu imagen, esta es solo una referencia de ejemplo -->
        <img src="att.png" alt="Editor Image">
    </div>
</div>




<div class="features-section">
    <div class="feature-item">
        <span class="icon">🔠</span> <!-- Reemplaza con el ícono que prefieras -->
        <h3 class="feature-title">Auto-translate</h3>
        <p class="feature-description">
            Mochi uses state-of-the-art machine translation to automatically provide translations for words and phrases.
        </p>
    </div>
    <div class="feature-item">
        <span class="icon">🖼️</span> <!-- Reemplaza con el ícono que prefieras -->
        <h3 class="feature-title">Image search</h3>
        <p class="feature-description">
            Use the built-in image search to embed an image into your card based on some word or phrase.
        </p>
    </div>
    <div class="feature-item">
        <span class="icon">☁️</span> <!-- Reemplaza con el ícono que prefieras -->
        <h3 class="feature-title">Cloud syncing</h3>
        <p class="feature-description">
            With a Pro account you can sync your content and use Mochi across all of your devices, including mobile.
        </p>
    </div>
    <div class="feature-item">
        <span class="icon">🔌</span> <!-- Reemplaza con el ícono que prefieras -->
        <h3 class="feature-title">Full REST API</h3>
        <p class="feature-description">
            Mochi provides a robust REST API for interacting with your cards and decks. This allows for powerful integrations and custom workflows. Check out the API docs to get started.
        </p>
    </div>
</div>
