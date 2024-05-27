<script>
    import {Brain} from "phosphor-svelte";
    import {goto} from "$app/navigation";

    /** @type {import('./$types').PageData} */
    export let data;
    import { getCookie } from '../../utils/csrf';
    import {DeckStore} from "../../deck-store.js";
    import {HomeStore} from "../../home-stote.js";
    import {onMount} from "svelte";

    function navigateToCard() {
        goto(`/dashboard/study`);
    }
    let max_cards = [];

    onMount(() =>{
       $DeckStore = data.decks;
       HomeStore.set(data.users);
       max_cards = createArrayWithSize(0, 0);
       if ($DeckStore){
           max_cards = createArrayWithSize($DeckStore.length, 0);
       }
    });


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
        const token = localStorage.getItem('key');
        try {
            const response = await fetch(url, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': `${csrftoken}`,
                    'Authorization': `Token ${token}`
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

    // Datos de ejemplo para el usuario
    let user = {
        profileImage: 'https://via.placeholder.com/150'
    };

</script>


<div>
    <button type="button" class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight" >
        <div class="d-flex align-items-center">
            <Brain />
            Study cards
        </div>
    </button>

    {#if HomeStore}

            <div class="row">
                {#each $HomeStore as info}
                <div class="card col" style="max-width: 480px">
                    <div class="card-header d-flex align-items-center">
                        <img src={user.profileImage} alt="Profile Image" class="rounded-circle me-3" style="width: 50px; height: 50px;">
                        <div>
                            <h5 class="card-title mb-0">{info.user.name}</h5>
                            <p class="card-text"><small class="text-muted">{info.user.email}</small></p>
                        </div>
                    </div>
                    <div class="card-body">
                        <div class="accordion" id="accordion-deck-{info.user.id}">
                            <div class="accordion-item">
                                <h2 class="accordion-header" id="heading-deck-{info.user.id}">
                                    <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-deck-{info.user.id}" aria-expanded="false" aria-controls="collapse-deck-{info.user.id}">
                                        Decks
                                    </button>
                                </h2>
                                <div id="collapse-deck-{info.user.id}" class="accordion-collapse collapse" aria-labelledby="heading-deck-{info.user.id}" data-bs-parent="#accordion-deck-{info.user.id}">
                                    <div class="accordion-body">
                                        <table class="table">
                                            <thead>
                                            <tr>
                                                <th scope="col">Name</th>
                                                <th scope="col">Cards</th>
                                                <th scope="col">Tags</th>
                                                <th scope="col"></th>
                                            </tr>
                                            </thead>
                                            <tbody>
                                            {#each info.decks as deck}
                                                <tr>
                                                    <td>{deck.name}</td>
                                                    <td>{deck.card_count}</td>
                                                    <td>{deck.tags}</td>
                                                    <td><button class="btn btn-primary btn-sm">Follow</button></td>
                                                </tr>
                                            {/each}
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                            <div class="accordion-item">
                                <h2 class="accordion-header" id="heading-note-{info.user.id}">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-note-{info.user.id}" aria-expanded="false" aria-controls="collapse-note-{info.user.id}">
                                        Notebooks
                                    </button>
                                </h2>
                                <div id="collapse-note-{info.user.id}" class="accordion-collapse collapse" aria-labelledby="heading-{info.user.id}" data-bs-parent="#accordion-note-{info.user.id}">
                                    <div class="accordion-body">
                                        <table class="table">
                                            <thead>
                                            <tr>
                                                <th scope="col">Name</th>
                                                <th scope="col">Notes</th>
                                                <th scope="col">Tags</th>
                                                <th scope="col">Action</th>
                                            </tr>
                                            </thead>
                                            <tbody>
                                            {#each info.notebooks as notebook}
                                                <tr>
                                                    <td>{notebook.name}</td>
                                                    <td>{notebook.note_count}</td>
                                                    <td>{notebook.tags}</td>
                                                    <td><button class="btn btn-primary btn-sm">Follow</button></td>
                                                </tr>
                                            {/each}
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                {/each}
            </div>

        {/if}




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

