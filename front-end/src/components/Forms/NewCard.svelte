<script>
	import SimpleBtn from "../Buttons/SimpleBtn.svelte";

    let front = '';
    let back = '';
    let deck = '';

    /* async function handleSubmit() {
        const data = { front, back, deck };

        try {
            const response = await fetch('https://api.endpoint', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                console.log('Form submitted successfully!');
            } else {
                console.error('Failed to submit form');
            }
        } catch (error) {
            console.error('An error occurred while submitting the form:', error);
        }
    } */
</script>

<form class="flex flex-col mx-auto" on:submit|preventDefault={() => {}}>
    <label
        for="front"
        class="text-lg font-semibold"
    >
        Content in the front of the card
    </label>
    <textarea class="w-4/5 max-w-[800px] mb-6" bind:value={front}></textarea>
    
    <label
        for="front"
        class="text-lg font-semibold mb-6"
    >
        Content in the back of the card
    </label>
    <textarea class="w-4/5 max-w-[800px] mb-6" bind:value={back}></textarea>
    
    <label
        for="front"
        class="text-lg font-semibold"
    >
        Select the deck where you want to add the card
    </label>
    <select class="w-4/5 max-w-[800px] mb-6" bind:value={deck}>
        <option value="option1">Option 1</option>
        <option value="option2">Option 2</option>
        <option value="option3">Option 3</option>
    </select>
    
    <SimpleBtn width="w-4/5 max-w-[800px]" text="Create" type="submit" />
</form>