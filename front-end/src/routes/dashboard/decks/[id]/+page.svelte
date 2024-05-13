<script>
    import { onMount } from "svelte";
    import {page} from "$app/stores";
    import SvelteMarkdown from "svelte-markdown";
    import NewCard from "../../../../components/Forms/NewCard.svelte";
    import {Pencil} from "phosphor-svelte";

    export let data;

    let card;
    let decks = [];

    let id_deck = "";

    console.log(data.id)



    async function handleSubmit() {

        console.log(JSON.stringify(data.card))
        try {
            const response = await fetch(`http://127.0.0.1:8000/fcards/${data.id}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data.card)
            });

            if (response.ok) {
                console.log('Form submitted successfully!');

            } else {
                console.error('Failed to submit form');
            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
        }
    }

</script>

{#if data}
    <div>
        <!-- Botón que activa el modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            <div class="d-flex align-items-center">
                <Pencil/>
                Edit card
            </div>

        </button>
        <div class="row">
            <div class="container-sm col">
                <div class="text-center mb-3"><p>Front</p></div>
                <div class="card bg-secondary mb-3" style="width: 30rem;margin-left: 20%;min-height: 300px">
                    <div class="card-body">
                        <SvelteMarkdown source="{data.card.front}"/>
                    </div>
                </div>
            </div>
            <div class="container-sm col">
                <div class="text-center mb-3"><p>Back</p></div>
                <div class="card bg-secondary mb-3" style="width: 30rem;margin-left: 20%;min-height: 300px">
                    <div class="card-body">
                        <SvelteMarkdown source="{data.card.back}"/>
                    </div>
                </div>
            </div>
        </div>
        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Edit card</h5>
                    </div>
                    <form on:submit|preventDefault={handleSubmit}>
                        <div class="modal-body">

                                <div class="mb-3">
                                    <label for="front-area" class="form-label">Front Area</label>
                                    <textarea bind:value={data.card.front} style="color:black"  class="form-control" id="front-area" rows="5" placeholder="Type in Markdown"></textarea>
                                </div>
                                <div class="mb-3">
                                    <label for="back-area" class="form-label">Back Area</label>
                                    <textarea bind:value={data.card.back} style="color:black" class="form-control" id="back-area" rows="10" placeholder="Type in Markdown"></textarea>
                                </div>


                        </div>

                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                                <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>

                        </div>
                    </form>
                </div>
            </div>
        </div>

    </div>
    {/if}

