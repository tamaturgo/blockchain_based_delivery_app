<script lang="ts">
    export let delivery;

    const style = "outline-none py-3 px-4 border-2 border-background rounded-lg bg-[#FFF] w-full focus:border-blue-primary" 

</script>
<main class="w-full rounded-lg bg-[#FFF] p-4 flex flex-col items-start gap-2">
    <h1 class="font-semibold text-xl">Encomenda</h1>
        <!-- svelte-ignore a11y-label-has-associated-control -->
        <label class="font-semibold">Nome do produto</label>
        <input required bind:value={delivery.product} class={style} placeholder="Nome do produto" />
        <!-- svelte-ignore a11y-label-has-associated-control -->
        <label class="font-semibold">Remetente e destinatário</label>
        <input required bind:value={delivery.sender} class={style} placeholder="Remetente" />
        <input required bind:value={delivery.receiver} class={style} placeholder="Destinatário" />
        <!-- svelte-ignore a11y-label-has-associated-control -->
        <label class="font-semibold">Quantidade</label>
        <input required min="1" max="1000" bind:value={delivery.amount} type="number" class={style}/>
</main>
