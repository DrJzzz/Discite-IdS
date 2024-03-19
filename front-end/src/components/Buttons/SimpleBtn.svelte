<script lang="ts">
    export let text: string = 'Button';
    export let color: string = 'bg-[#f6f6f6]';
    export let type: "button" | "submit" | "reset" | null | undefined = 'button';
    export let width: string = 'w-auto';

</script>

<button 
    type={type} 
    class="{color} {width} text-[#333333] text-lg font-semibold py-2 px-4 rounded" 
    on:click>
    {text}
</button>
