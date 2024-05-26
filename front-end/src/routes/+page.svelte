
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
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 100px;
        background-color: #1c1c1c;
        color: white;
        margin-bottom: 32px;
    }
    .header {
        max-width: 50%;
    }
    .title {
        font-size: 48px;
        margin: 0;
        line-height: 1.2;
    }
    .subtitle {
        font-size: 20px;
        margin: 20px 0;
    }
    .actions {
        display: flex;
        align-items: center;
    }
    .button {
        padding: 10px 20px;
        margin-right: 10px;
        background-color: #333;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-transform: uppercase;
        font-weight: bold;
    }
    .button:hover {
        background-color: #555;
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
    @media (max-width: 768px) {
        .container {
            flex-direction: column;
        }
        .header, .image-placeholder {
            max-width: 100%;
        }
        .actions {
            flex-direction: column;
        }
        .button {
            margin-bottom: 10px;
        }
    }

    .feature-title {
        font-size: 4rem;
        font-weight: 700;
        margin: 0 0 20px;
    }
    .feature-description {
        font-size: 1.25rem;
        max-width: 800px;
        text-align: justify;
        margin: 0;
        padding: 0 20px;
        text-justify: inter-word;
    }
    .dual-features {
        display: flex;
        justify-content: space-between;
        background-color: #1c1c1c;
        padding: 40px;
        color: white;
    }
    .feature {
        width: 48%;
    }

    .feature-title {
        font-size: 24px;
        margin: 0 0 10px 0;
        display: flex;
        align-items: center;
    }
    .feature-description {
        font-size: 16px;
    }
    .markdown-enabled-section {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 40px;
        background-color: #1a1a1a;
        color: white;
    }
    .markdown-content {
        margin: 8px 16px;
        flex: 1;
        max-width: 50%;
    }
    .markdown-title {
        font-size: 2rem;
        margin-bottom: 0.5em;
    }
    .markdown-description {
        font-size: 1rem;
    }
  
    .feature-title {
        margin-bottom: 5px;
    }
    .feature-description {
        font-size: 0.9rem;
    }

</style>
