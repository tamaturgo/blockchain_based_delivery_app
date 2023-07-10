<script lang="ts">
    export let id : string
    export let update : boolean
</script>
    <main class="flex flex-col w-80 p-6 my-6 gap-6 items-start rounded-xl text-black-text bg-[#FFF]">
    <h1 class="text-xl font-semibold">Encomenda</h1>
    <div class="flex flex-col items-start h-10 gap-2">
        <h2 class="font-semibold text-sm">ID do produto</h2>
        {id}
    </div>
    {#if update}
        <div class="flex flex-col items-start gap-2 w-full">
        <div class="text-sm">Novo status:</div>
       <input class="bg-[#FFF] w-full p-4 outline-none border-background border-2 rounded-lg text-sm" placeholder="Novo status" />
        </div>
    {/if}
</main>
