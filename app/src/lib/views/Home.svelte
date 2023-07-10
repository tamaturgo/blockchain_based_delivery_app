<script lang="ts">
    import SearchCard from "../components/SearchCard.svelte";
    import SearchField from "../components/SearchField.svelte";
    import AddCard from "../components/AddCard.svelte";
    import { setContext } from "svelte";

    let delivery = {
        'id': ''
    }
    
    let update : boolean = false

    let addCard : boolean = false

    setContext('home', { searchDelivery})

    $: expanded = addCard ? "w-80 flex flex-col mt-9" :"w-80 flex flex-col mt-40"
    function searchDelivery(id : string) {
        delivery['id'] = id
    }
</script>
<main class="min-h-screen w-screen bg-background flex flex-col items-center gap-10 text-black-text">
                <div class={expanded}>
    <div class="self-start cursor-pointer hover:font-semibold" on:click={() => addCard = true}>Adicionar encomenda</div>
    <img src="/src/assets/CRYPTOpost.svg" alt="Logo" class="p-10 stroke-none font-normal" on:click={() => window.location.reload()}/>
    <SearchField/>
            {#if delivery['id'] != '' && !addCard}
        <SearchCard id={delivery['id']} update={update}/>
        {#if update}
            
        <div class="flex justify-between">
            <div class="cursor-pointer hover:font-semibold" on:click={() => update = false}>Cancelar</div>
            <div class="cursor-pointer hover:font-semibold" on:click={() => update = true}>Editar</div>
        </div>

        {:else}
            <div class="self-end cursor-pointer hover:font-semibold" on:click={() => update = true}>Editar</div>
        {/if}
    {/if}
    {#if addCard}
        <AddCard/>
        <div class="flex justify-between">
            <div class="cursor-pointer hover:font-semibold" on:click={() => addCard = false}>Cancelar</div>
            <div class="cursor-pointer hover:font-semibold" on:click={() => addCard = true}>Adicionar</div>
        </div>
    {/if}
    </div>
</main>
