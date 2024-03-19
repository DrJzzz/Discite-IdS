<script>
    // Para añadir scripts 
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


    .feature-section {
    background-color: #1c1c1c; /* Un poco más claro que el header para diferenciar secciones */
    color: white;
    padding: 40px; /* Añadir algo de espacio alrededor del texto */
    text-align: center; /* Centrar el texto horizontalmente */
  }

  .feature-title {
    font-size: 32px; /* Un tamaño de fuente destacado para el título */
    margin: 0 0 10px 0; /* Un poco de margen debajo del título */
  }

  .feature-description {
    font-size: 18px; /* Un tamaño de fuente legible para el cuerpo del texto */
    max-width: 600px; /* Una anchura máxima para mantener la legibilidad */
    margin: auto; /* Centrar automáticamente el párrafo dentro de la sección */
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


  </style>
  
  <div class="container">
    <div class="header">
      <h1 class="title">Spaced repetition made easy</h1>
      <p class="subtitle">
        Take notes and make flashcards using markdown,
        then study them using spaced repetition.
      </p>
      <div class="actions">
        <button class="button">Download for Linux</button>
        <span>Or </span>
        <a> </a>
        <a class="link">Try it online</a>
      </div>
    </div>
    <div class="image-placeholder">
      <!-- Coloca aquí tu imagen -->
      <!-- <img src="/path-to-your-image.jpg" alt="Descripción de la imagen"> -->
    </div>
  </div>

  <div class="feature-section">
    <h2 class="feature-title">Powerfully simple.</h2>
    <p class="feature-description">
      Mochi comes with batteries included, loaded with tons of features to make creating and 
      reviewing cards as simple and easy as possible.
    </p>
  </div>
  
<div class="dual-features">
  <div class="feature">
    <div class="feature-title">
      <span class="feature-icon">// Ícono aquí</span>
      Spaced Repetition
    </div>
    <p class="feature-description">
      Mochi uses a spaced repetition algorithm to maximize retention and minimize study time. 
      Learn more about spaced repetition
    </p>
  </div>
  
  <div class="feature">
    <div class="feature-title">
      <span class="feature-icon">// Ícono aquí</span>
      Offline first
    </div>
    <p class="feature-description">
      Mochi is offline first. That means you can use it without ever signing up. All of your data is stored 
      locally first before it's synced to the cloud.
    </p>
  </div>
</div>