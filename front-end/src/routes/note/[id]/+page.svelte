<script>
    import {NoteStore} from '../../../note-store'
    import { onMount } from "svelte";
    import SvelteMarkdown from 'svelte-markdown';

    export let data;
    /**
	 * @type {{ title: any; content: any; } | null}
	 */
    let note;

    onMount(async function() {
        if ($NoteStore.length) {
            note = $NoteStore.find(film => film.id == data.id)
        } else {
            const endpoint = `http://localhost:8000/notes/notes/${data.id}/`
            let response = await fetch(endpoint)
            if (response.status == 200) {
                note = await response.json()
            } else {
                note = null;
            }
        }
    })

    const source = `
  # This is a header

This is a paragraph.

* This is a list
* With two items
  1. And a sublist
  2. That is ordered
    * With another
    * Sublist inside

| And this is | A table |
|-------------|---------|
| With two    | columns |`





    
</script>
<SvelteMarkdown {source} />

<div class="row mt-4">
    {#if note }
        <h2 class="mb-4">{ note.title }</h2>
        <div class="col-12 col-md-4">
            
        </div>
        <div class="col-12 col-md-8">
            <p>{ note.content }</p>
        </div>
    {:else }
        <p>No film was found with ID {data.id}</p>
    {/if }
</div>