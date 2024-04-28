<script>
    import {NoteStore} from '../../../../note-store.js'
    import {onMount} from 'svelte'

    onMount(async function() {
        const endpoint = 'http://127.0.0.1:8000/notes/'
        const response = await fetch(endpoint)
        const data = await response.json()
        console.log(data)
        console.log(data.results.length)
        NoteStore.set(data.results)

    } )

</script>

<h1> Displaying notes </h1>

<div>
    <h2>Notes List</h2>
    
    <div>
        {#each $NoteStore as note}
       
        <div class="col-12 col-sm-6 col-md-4">
            
            <div class="card w-100 h-100">
            
                <div class="card-body d-flex flex-column justify-content-between gap-4">
					<div>
                        <h5 class="card-title">{ note.title }</h5>
                       
                    </div>
                    <div>
                        <a href="/note/{note.id}/" class="btn btn-primary" >View</a>
					</div>
                </div>
              </div>

        </div>
        {/each}
    </div>
    
</div>