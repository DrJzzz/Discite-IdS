<script>
    import SvelteMarkdown from "svelte-markdown";
    import {Eye} from "phosphor-svelte";
    import {goto} from "$app/navigation";
    import {StudyCards} from "../../../stores.js";
    import {getCookie} from "../../../utils/csrf.js";
    import {alertSuccess, alertError,alertEndStudy} from "../../../utils/alerts.js";
    import {onMount} from "svelte";
    import Katex from "svelte-katex";
    import {invalidateAll} from "$app/navigation";

    export let data;

    const front = "# Prubea"
    const back = "# Prubea back"
    let watch = false;


    let i = 0;

    onMount(() => {
        if (data.cards.length > 0){
            StudyCards.set(data.cards);
            console.log($StudyCards)
        }else{
            alertEndStudy('No more cards to study, comeback later.', 'warning');
            navigateToHome();
        }
    })



    function navigateToHome() {
        goto(`/dashboard`);
    }

    async function handleSubmit(id, rating) {

        try {
            const token = localStorage.getItem('key');
            const csrftoken = getCookie('csrftoken');
            const info ={rating} ;
            console.log(JSON.stringify(info))
            const response = await fetch(`http://127.0.0.1:8000/cards/${$StudyCards[i].id}/set_new_rating/`, {
                method: 'POST',
                credentials : 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                    'X-CSRFToken': `${csrftoken}`
                },
                body: JSON.stringify(info)
            });

            if (response.ok) {

                if( i < data.cards.length-1){
                    i += 1;
                    watch = false;
                    alertSuccess('Study card successfully')
                }
                else {
                    await invalidateAll().then( () => {
                        if ($StudyCards.length === 0){
                            alertEndStudy("No more cards to study", 'success');
                            navigateToHome();
                        }
                    });
                }
            } else {
                alertError('Failed to study card, retry');
            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
            alertError('An error occurred while studying the card');
        }
    }


    function watchBack() {
        watch = true
    }

</script>

{#if $StudyCards.length > 0}
    <div>
        <div class="row container" style="max-width: 720px;margin-left: 10%">
            <div class="col">
                <button type="button" class="btn btn-outline-danger" on:click={() => handleSubmit(2, 1)}>Again</button>
            </div>
            <div class="col">
                <button type="button" class="btn btn-outline-warning" on:click={() => handleSubmit(2, 2)}>Hard</button>
            </div>
            <div class="col">
                <button type="button" class="btn btn-outline-primary" on:click={() => handleSubmit(2, 3)}>Good</button>
            </div>
            <div class="col">
                <button type="button" class="btn btn-outline-success" on:click={() => handleSubmit(2, 4)}>Easy</button>
            </div>
            
        </div>
        <div class="row">
            <div class="container-sm col">
                <div class="text-center mb-3"><p>Front</p></div>
                <div class="card bg-secondary mb-3" style="width: 30rem;margin-left: 20%;min-height: 300px">
                    <div class="card-body">
                        <SvelteMarkdown source="{$StudyCards[i].front}"/>
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
                                    <Eye size={24} />
                                    Watch card
                                </div>
                            </button>
                        {:else }
                            {#if $StudyCards[i].template === 2}
                                <Katex>{$StudyCards[i].back}</Katex>
                            {:else }
                                <SvelteMarkdown source="{$StudyCards[i].back}"/>
                            {/if}
                        {/if}

                    </div>
                </div>
            </div>
        </div>
    </div>
{/if}