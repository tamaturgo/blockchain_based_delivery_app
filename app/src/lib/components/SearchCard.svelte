<script lang="ts">
    export let id: string;
    export let name: string;
    export let status: [string];
</script>

<main
    class="flex flex-col w-80 p-6 my-6 gap-6 items-start rounded-xl text-black-text bg-[#FFF]"
>
    <h1 class="text-xl font-semibold">Encomenda</h1>

    <div class="flex justify-between" />
    <div class="flex flex-col items-start h-10 gap-2">
        <h2 class="font-semibold text-sm">ID do produto</h2>
        {id}
    </div>

    <div class="flex flex-col items-start h-10 gap-2">
        <h2 class="font-semibold text-sm">Nome do produto</h2>
        {name}
    </div>

    <h2 class="font-semibold text-sm">Status</h2>
    <dl class="flex flex-col list-disc items-start">
    {#each status as element}
            <dt class="capitalize">{element[0]}</dt>
            <dd class="text-sm">{new Date(element[1]).toLocaleString()}</dd>
    {/each}
    </dl>
</main>
