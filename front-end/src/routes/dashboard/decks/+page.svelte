<script>
    import {CardStore} from "../../../card-store.js"
    import {onMount} from "svelte";
    import {NoteStore} from "../../../note-store.js";


    onMount(async function() {
        const endpoint = 'http://127.0.0.1:8000/cards/'
        const response = await fetch(endpoint)
        const data = await response.json()
        CardStore.set(data.results)
    });

</script>


<!-- component -->
<style>
    #journal-scroll::-webkit-scrollbar {
        width: 4px;
        cursor: pointer;
        /*background-color: rgba(229, 231, 235, var(--bg-opacity));*/

    }
    #journal-scroll::-webkit-scrollbar-track {
        background-color: rgba(229, 231, 235, var(--bg-opacity));
        cursor: pointer;
        /*background: red;*/
    }
    #journal-scroll::-webkit-scrollbar-thumb {
        cursor: pointer;
        background-color: #a0aec0;
        /*outline: 1px solid slategrey;*/
    }
</style>

<div class="container mx-auto py-10 flex justify-center h-screen">
    <div class="w-4/12 pl-4  h-full flex flex-col">
        <div class="bg-white text-sm text-gray-500 font-bold px-5 py-2 shadow border-b border-gray-300">
            Card list
        </div>

        <div class="w-full h-full overflow-auto shadow bg-white" id="journal-scroll">

            <table class="w-full">


                <tbody class="">

                {#each $CardStore as card}


                    <tr class="relative transform scale-100
                                        text-xs py-1 border-b-2 border-blue-100 cursor-default

                                bg-blue-500 bg-opacity-25">
                        <td class="pl-5 pr-3 whitespace-no-wrap">
                            <div class="text-gray-400">Last Modified</div>
                            <div>{card.modified}</div>
                        </td>

                        <td class="px-2 py-2 whitespace-no-wrap">
                            <div class="leading-5 text-gray-500 font-medium">Card {card.id}</div>
                            <div class="leading-5 text-gray-900">
                                <a class="text-blue-500 hover:underline" href="/card/{card.id}/">Watch card</a></div>
                            <div class="leading-5 text-gray-800">{card.subject}</div>
                        </td>

                    </tr>
                {/each}
                </tbody>
            </table>
        </div>
        ¿

    </div>
</div>