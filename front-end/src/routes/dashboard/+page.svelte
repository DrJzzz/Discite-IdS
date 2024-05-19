<script>
    import {Brain} from "phosphor-svelte";
    import {goto} from "$app/navigation";

    /** @type {import('./$types').PageData} */
    export let data;

    import {DeckStore} from "../../deck-store.js";
    import {onMount} from "svelte";

    function navigateToCard() {
        goto(`/dashboard/study`);
    }
    let max_cards = [];

    onMount(() =>{
       $DeckStore = data.decks;
        max_cards = createArrayWithSize(0, 0);
       if ($DeckStore){
           max_cards = createArrayWithSize($DeckStore.length, 0);
       }

        console.log(max_cards.length)
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    export function createArrayWithSize(size, defaultValue) {
        return Array.from({ length: size }, () => defaultValue);
    }




    async function handleSubmit(){
        let index = 0;
        data.decks.forEach(deck => {
            sendMaxReviws(deck, index);
            index +=1;
        })

        navigateToCard()

    }

    async function sendMaxReviws(deck, index){

        console.log(deck)
        const url = `http://localhost:8000/decks/${deck.id}/update_review/`
        const max_reviews = max_cards[index];
        const info = {max_reviews}
        const csrftoken = getCookie('csrftoken');
        try {
            const response = await fetch(url, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                credentials : 'include',
                body: JSON.stringify(info),
            });

            if (response.ok) {

                console.log(max_cards[index])
            } else {
                alert('Somenthing went wrong, try again');
            }
        }catch (error){
            console.log(error)
        }
    }
</script>


<div>
    <button type="button" class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight" >
        <div class="d-flex align-items-center">
            <Brain />
            Study cards
        </div>
    </button>


    <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
        <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvasRightLabel">Select cards to study of each deck</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
            <form class="p-4" on:submit|preventDefault={handleSubmit}>
                    {#each $DeckStore as deck, index}
                        <div class="mb-3">
                            <label for="max-reviews" class="form-label">{deck.name}</label>
                            <input bind:value={max_cards[index]} type="number" class="form-control" id="max-reviews" min="1" style="color: black">
                        </div>
                    {/each}
                <button type="submit" class="btn btn-primary">Go to study</button>
            </form>
        </div>
    </div>
</div>

