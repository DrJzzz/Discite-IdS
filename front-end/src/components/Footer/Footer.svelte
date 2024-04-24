<script>
    // JavaScript
    let currentYear = new Date().getFullYear();
</script>

<style>
    #footer {
        background-color: #333; /* Color de fondo*/
        padding: 2rem 0;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        align-items: flex-start;
    }

    #footer section {
        margin: 1rem;
    }

    .about {
        color:aliceblue;
        flex-grow: 1;
    }

    .about .h5 {
        color: aliceblue;
        font-size: 1.25rem;
        margin-bottom: 0.5rem;
    }

    .about div {
        margin-bottom: 0.25rem;
    }

    .footer-links a {
        display: block;
        color: #007bff;
        text-decoration: none;
        margin-bottom: 0.25rem;
    }

    .footer-links a:hover {
        text-decoration: underline;
    }

    .copyright {
        font-size: 0.875rem;
        color: #6a747c;
    }
</style>

<div id="footer">
    <section>
        <img src="favicon.png" width="40" height="40" alt="Mochi logo"/>
    </section>
    <section class="about">
        <span class="h5">AnkiCards</span>
        <div>
            Anki Cards la mejor opción para aprender
        </div>
        <div class="copyright">
            © <span id="current-year">2024</span> Anki Cards, Inc
        </div>
    </section>
    <section class="footer-links">
        <!-- Enlaces del pie de página aquí -->

    </section>
    <section class="footer-links">
        <!-- Más enlaces aquí -->

    </section>
</div>