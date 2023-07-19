<script lang="ts">
    import {searchedDelivery} from '../../stores'
</script>

<main
    class="flex flex-col w-80 p-6 my-6 gap-6 items-start rounded-xl text-black-text bg-[#FFF]"
>
    <div class="text-xl font-semibold">Encomenda</div>

    <div class="flex">
        <div>{$searchedDelivery.sender} -> {$searchedDelivery.receiver}</div>
    </div>

    <div class="flex flex-col items-start h-10 gap-2">
        <h2 class="font-semibold text-sm">ID do produto</h2>
        {$searchedDelivery.id}
    </div>

    <div class="flex flex-col items-start h-10 gap-2">
        <h2 class="font-semibold text-sm">Nome do produto</h2>
        <div class="capitalize">{$searchedDelivery.name}</div>
    </div>

    <dl class="flex flex-col list-disc items-start">
    <h2 class="font-semibold text-sm">Status</h2>
    {#each $searchedDelivery.status as element}
            <dt class="capitalize">{element[0]}</dt>
            <dd class="text-sm">{new Date(element[1]).toLocaleString()}</dd>
    {/each}
    </dl>
</main>
