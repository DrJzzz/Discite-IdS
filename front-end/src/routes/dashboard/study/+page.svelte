<script>
    import SvelteMarkdown from "svelte-markdown";
    import {Eye} from "phosphor-svelte";
    import {goto} from "$app/navigation";

    export let data;

    const front = "# Prubea"
    const back = "# Prubea back"
    let watch = false;

    let card;

    let i = 0;

    if (data.cards){
        card = data.cards[i];
    }

    function navigateToHome() {
        goto(`/dashboard`);
    }

    async function handleSubmit(id, dificulty) {

        try {
            const response = await fetch(`http://127.0.0.1:8000/cards/${id}/set_new_rating/${dificulty}/`, {
                method: 'POST',
                credentials : 'include'
            });

            if (response.ok) {
                console.log('Form submitted successfully!');

            } else {
                console.error('Failed to submit form');

                if( i < data.cards.length-1){
                    i += 1;
                    watch = false;
                    card = data.cards[i];

                }
                else {
                    alert("Your study has been finished");
                    navigateToHome();
                }

            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
        }
    }


    function watchBack() {
        watch = true
    }
</script>

{#if data}
    <div>
        <div class="row">
            <div class="container-sm col">
                <div class="text-center mb-3"><p>Front</p></div>
                <div class="card bg-secondary mb-3" style="width: 30rem;margin-left: 20%;min-height: 300px">
                    <div class="card-body">
                        <SvelteMarkdown source="{card.front}"/>
                    </div>
                </div>
            </div>
            <div class="container-sm col">
                <div class="text-center mb-3"><p>Back</p></div>
                <div class="card bg-secondary mb-3" style="width: 30rem;margin-left: 20%;min-height: 300px">
                    <div class="card-body">
                        {#if !watch}
                            <button on:click={() => watchBack()} type="button" class="btn btn-outline-info" style="margin-left: 30%;margin-top: 20%">
                                <div class="d-flex align-items-center">
                                    <Eye />
                                    Watch card
                                </div>
                            </button>
                        {:else }
                                <SvelteMarkdown source="{card.back}"/>
                        {/if}

                    </div>
                </div>
            </div>
        </div>
        <div class="row container" style="max-width: 720px;margin-left: 30%">
            <div class="col">
                <button type="button" class="btn btn-outline-danger" on:click={() => handleSubmit(2, 1)}>Again</button>
            </div>
            <div class="col">
                <button type="button" class="btn btn-outline-primary" on:click={() => handleSubmit(2, 3)}>Good</button>
            </div>
            <div class="col">
                <button type="button" class="btn btn-outline-success" on:click={() => handleSubmit(2, 4)}>Easy</button>
            </div>
            <div class="col">
                <button type="button" class="btn btn-outline-warning" on:click={() => handleSubmit(2, 2)}>Hard</button>
            </div>
        </div>

    </div>
{/if}