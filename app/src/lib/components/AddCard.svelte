<script lang="ts">
    export let delivery;

    const style = "outline-none py-3 px-4 border-2 border-background rounded-lg bg-[#FFF] w-full focus:border-blue-primary" 

</script>
<main class="w-full rounded-lg bg-[#FFF] p-6 flex flex-col items-start gap-4">
    <h1 class="font-semibold text-xl">Encomenda</h1>
        <input required bind:value={delivery.product} class={style} placeholder="Nome do produto" />
        <input required bind:value={delivery.product_id} class={style} placeholder="ID do produto" />
        <input required bind:value={delivery.sender} class={style} placeholder="ID do remetente" />
        <input required bind:value={delivery.receiver} class={style} placeholder="ID do destinatário" />
        <input required min="1" max="1000" bind:value={delivery.amount} type="number" class={style} placeholder="Quantia" />
</main>
