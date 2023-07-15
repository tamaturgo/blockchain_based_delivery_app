<script lang="ts">
    export let delivery;

</script>
<main class="w-full rounded-lg bg-[#FFF] p-6 flex flex-col items-start gap-4">
    <h1 class="font-semibold text-xl">Encomenda</h1>
        <input required bind:value={delivery.product} class="outline-none py-3 px-4 border-2 border-background rounded-lg bg-[#FFF] w-full" placeholder="Nome do produto" />
        <input required bind:value={delivery.product_id} class="outline-none py-3 px-4 border-2 border-background rounded-lg bg-[#FFF] w-full" placeholder="ID do produto" />
        <input required bind:value={delivery.sender} class="outline-none py-3 px-4 border-2 border-background rounded-lg bg-[#FFF] w-full" placeholder="ID do remetente" />
        <input required bind:value={delivery.receiver} class="outline-none py-3 px-4 border-2 border-background rounded-lg bg-[#FFF] w-full" placeholder="ID do destinatário" />
        <input required min="1" max="1000" bind:value={delivery.amount} type="number" class="outline-none py-3 px-4 border-2 border-background rounded-lg bg-[#FFF] w-full" placeholder="Quantia" />
</main>
