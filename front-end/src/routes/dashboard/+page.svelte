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

    // Datos de ejemplo para el usuario
    let user = {
        name: 'John Doe',
        email: 'john.doe@example.com',
        profileImage: 'https://via.placeholder.com/150'
    };

    let user2 = {
        name: 'Nicholas Med',
        email: 'nicholas@example.com',
        profileImage: 'https://via.placeholder.com/150'
    };
    // Datos de ejemplo para Decks y Notebooks
    let decks = [
        { name: 'Deck 1', number: 10, tags: 'tag1, tag2' },
        { name: 'Deck 2', number: 20, tags: 'tag3, tag4' }
    ];

    let notebooks = [
        { name: 'Notebook 1', number: 5, tags: 'tag5, tag6' },
        { name: 'Notebook 2', number: 15, tags: 'tag7, tag8' }
    ];
</script>


<div>
    <button type="button" class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight" >
        <div class="d-flex align-items-center">
            <Brain />
            Study cards
        </div>
    </button>
    <div class="row">
        <div class="card col" style="max-width: 720px">
            <div class="card-header d-flex align-items-center">
                <img src={user.profileImage} alt="Profile Image" class="rounded-circle me-3" style="width: 50px; height: 50px;">
                <div>
                    <h5 class="card-title mb-0">{user.name}</h5>
                    <p class="card-text"><small class="text-muted">{user.email}</small></p>
                </div>
            </div>
            <div class="card-body">
                <div class="accordion" id="accordionExample">
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="headingOne">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                                Decks
                            </button>
                        </h2>
                        <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <table class="table">
                                    <thead>
                                    <tr>
                                        <th scope="col">Name</th>
                                        <th scope="col">Cards</th>
                                        <th scope="col">Tags</th>
                                        <th scope="col">Action</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    {#each decks as deck}
                                        <tr>
                                            <td>{deck.name}</td>
                                            <td>{deck.number}</td>
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
                        <h2 class="accordion-header" id="headingTwo">
                            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                                Notebooks
                            </button>
                        </h2>
                        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
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
                                    {#each notebooks as notebook}
                                        <tr>
                                            <td>{notebook.name}</td>
                                            <td>{notebook.number}</td>
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
        <div class="card col" style="max-width: 720px">
            <div class="card-header d-flex align-items-center">
                <img src={user2.profileImage} alt="Profile Image" class="rounded-circle me-3" style="width: 50px; height: 50px;">
                <div>
                    <h5 class="card-title mb-0">{user2.name}</h5>
                    <p class="card-text"><small class="text-muted">{user2.email}</small></p>
                </div>
            </div>
            <div class="card-body">
                <div class="accordion" id="accordionExample">
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="headingOne">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                                Decks
                            </button>
                        </h2>
                        <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <table class="table">
                                    <thead>
                                    <tr>
                                        <th scope="col">Name</th>
                                        <th scope="col">Cards</th>
                                        <th scope="col">Tags</th>
                                        <th scope="col">Action</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    {#each decks as deck}
                                        <tr>
                                            <td>{deck.name}</td>
                                            <td>{deck.number}</td>
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
                        <h2 class="accordion-header" id="headingTwo">
                            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                                Notebooks
                            </button>
                        </h2>
                        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
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
                                    {#each notebooks as notebook}
                                        <tr>
                                            <td>{notebook.name}</td>
                                            <td>{notebook.number}</td>
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
    </div>



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

