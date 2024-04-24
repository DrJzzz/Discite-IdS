<script>


</script>
<div class="w-full h-full flex">
    <nav class="w-64 h-full border-r-[1px] bg-primaryBlue border-r-lightBlue text-gray-100">
        <ul class="flex flex-col">
            <a href="/dashboard" class="p-4 hover:bg-gray-700">Dashboard</a>
            <a href="/dashboard/decks" class="p-4 hover:bg-gray-700">My Decks</a>
            <a href="/notes" class="p-4 hover:bg-gray-700">My Notes</a>
            <a href="/dashboard/settings" class="p-4 hover:bg-gray-700">Settings</a>
            <a href="/dashboard/new-card" class="p-4 bg-gray-600 hover:bg-gray-500">Create a New Card</a>
        </ul>
    </nav>
    <div class="flex-1 p-8 bg-primaryBlue">
        <slot></slot>
    </div>
</div>