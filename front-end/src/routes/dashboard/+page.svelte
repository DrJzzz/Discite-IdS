<script>
    import {Brain, Eye} from "phosphor-svelte";
    import {goto} from "$app/navigation";
    import { getCookie } from '../../utils/csrf';
    import {DeckStore} from "../../deck-store.js";
    import {HomeStore} from "../../home-stote.js";
    import {onMount} from "svelte";
    import SvelteMarkdown from "svelte-markdown";
    import {alertSuccess, alertError} from "../../utils/alerts.js";
    import {HistoryStore} from "../../history-store.js";
    import {TagStore} from "../../tag-store.js";
    import { get } from 'svelte/store';

    /** @type {import('./$types').PageData} */
    export let data;


    let isDeck = true;
    let tagDict = {};

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
       $TagStore.forEach(tag => {
           tagDict[tag.id] = tag.name;
       });
       let info = get(HomeStore);
       HomeStore.set(replaceTagIdsWithNames(info, tagDict ));
       console.log($HomeStore);
       console.log($TagStore);
       HomeStore.set(info);
    });


    export function createArrayWithSize(size, defaultValue) {
        return Array.from({ length: size }, () => defaultValue);
    }

    // Función para reemplazar ids por nombres
    function replaceTagIdsWithNames(data, tagDict) {
        data.forEach(item => {
            item.decks.forEach(deck => {
                deck.tags = deck.tags.map(tagId => tagDict[tagId]);
            });
            item.notebooks.forEach(notebook => {
                notebook.tags = notebook.tags.map(tagId => tagDict[tagId]);
            });
        });
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

    async function fetchDeck(id){
        isDeck = true;
        try{
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');
            const cardsEndpoint = `http://localhost:8000/decks/${id}/cards/`;
            const cardsRes = await fetch(cardsEndpoint, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': `${csrftoken}`,
                    'Authorization': `Token ${token}`
                },
                credentials: 'include'
            });

            if (cardsRes.ok){
                deck = await cardsRes.json();
                card = deck.cards[0];
            }else {
                alertError('Failed to load deck data');
            }

        }catch (error){
            console.error('An error occurred while submitting the form:', error);
            alertError('An error occurred while getting deck data');
        }
    }

    async function fetchNotebook(id){
        isDeck = false;
        try{
            const csrftoken = getCookie('csrftoken');
            const token = localStorage.getItem('key');
            const cardsEndpoint = `http://localhost:8000/notebooks/${id}/notes/`;
            const decksRes = await fetch(cardsEndpoint, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': `${csrftoken}`,
                    'Authorization': `Token ${token}`
                },
                credentials: 'include'
            });

            if (decksRes.ok){
                infoNotebook = await decksRes.json();
                note = infoNotebook.notes[0];
            }else {
                alertError('Failed to load deck data');
            }

        }catch (error){
            console.error('An error occurred while submitting the form:', error);
            alertError('An error occurred while getting deck data');
        }
    }
    let deck = {
        deck: {id: 0, name: ''},  cards : [{ id : 1, due : '2024-01-20', front : '', back: '' },
            { id : 1, due : '2024-01-20', front : '', back: '' }]
    }

    let infoNotebook = {
        notebook: {id : 0, name: ''},
        notes : [{id: 0, title: '', content: '',dateCreated : ''}]
    }


    let card = deck.cards[0];
    let note = infoNotebook.notes[0];

    function changeCard(id) {
        card =deck.cards.find(card => card.id === id);
    }

    function changeNote(id){
        note = infoNotebook.notes.find(note => note.id === id);
    }

    const title = '# Title:'

    const localhost = 'http://localhost:8000'
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
                        <img src={localhost+ info.picture} alt="Profile Image" class="rounded-circle me-3" style="width: 50px; height: 50px;">
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
                                        <table class="table table-hover">
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
                                                    <td>
                                                        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop" on:click={() => fetchDeck(deck.id)}>
                                                            <div class="d-flex align-items-center">
                                                                <Eye/>
                                                                View
                                                            </div>
                                                        </button>
                                                    </td>
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
                                                    <td>
                                                        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop" on:click={fetchNotebook(notebook.id)}>
                                                            <div class="d-flex align-items-center">
                                                                <Eye/>
                                                                View
                                                            </div>
                                                        </button>
                                                    </td>
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
        <!-- Modal Deck-->
        <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-xl">
                <div class="modal-content">
                    {#if isDeck}
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="staticBackdropLabel">{deck.deck.name}</h1>
                    </div>
                    <div class="modal-body">
                            <div class="container mt-3">
                                <div class="row">
                                    <h4>List Cards</h4>
                                    <div class="col-3 scrollable-column">
                                        <div class="list-group">
                                            {#each deck.cards as info}
                                                <button type="button" class="list-group-item list-group-item-action" on:click={() => changeCard(info.id)}>{info.id}</button>
                                            {/each}
                                        </div>
                                    </div>
                                    <div class="col-9">
                                        <div class="row">
                                            <h4>Date: {card.due}</h4>
                                        </div>
                                        <div class="container mb-3">
                                            <div class="row">
                                                <h5 class="text-center">Front</h5>
                                                <div class="col">
                                                    <div class="card bg-secondary card-width">
                                                        <div class="card-body">
                                                            <SvelteMarkdown source="{card.front}"/>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="container mb-3">
                                            <div class="row">
                                                <h5 class="text-center">Back</h5>
                                                <div class="col">
                                                    <div class="card bg-secondary card-width">
                                                        <div class="card-body">
                                                            <SvelteMarkdown source="{card.back}"/>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                    </div>
                    {:else}
                        <div class="container mt-3">
                            <div class="row">
                                <h4>List history</h4>
                                <div class="col-3 scrollable-column">

                                    <div class="list-group">
                                        {#each infoNotebook.notes as note}
                                            <button type="button" class="list-group-item list-group-item-action" on:click={() => changeNote(note.id)}>{note.id}</button>
                                        {/each}
                                    </div>
                                </div>
                                <div class="col-9">
                                    <div class="row">
                                        <h4>Date: {note.dateCreated} </h4>
                                    </div>
                                    <div>
                                        <div class="card bg-secondary mb-3 scrollable-column-note" style="max-width: 900px;min-width: 720px;min-height: 400px;">
                                            <div class="card-header">
                                                <div class="d-flex align-items-center">
                                                    <SvelteMarkdown source="{title}" />
                                                    <SvelteMarkdown source="{note.title}" />
                                                </div>

                                            </div>
                                            <div class="card-body">
                                                <SvelteMarkdown source="{note.content}" />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    {/if}
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
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

