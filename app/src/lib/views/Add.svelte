<script lang="ts">
    import { link } from "svelte-spa-router";
    import AddCard from "../components/AddCard.svelte";
    import Logo from "../components/Logo.svelte";

    let delivery = {
        product: '',
        product_id: '',
        sender: '',
        receiver: '',
        amount: 0
    }
    
    async function addDelivery() {
        if (
            Object.entries(delivery).every(
                (value) => value != null && value != undefined
            )
        ) {
            await fetch("http://localhost:5000/delivery", {
                method: 'POST',
                body: JSON.stringify(delivery),
            }).then((res) => console.log(res.body));
        }
    }
</script>

<main class="mt-40 w-80 flex flex-col items-center">
    <a
        href="/"
        use:link
        class="text-sm self-start cursor-pointer hover:font-semibold"
        >Cancelar</a
    >
    <Logo/>
    <form name="add" class="w-full flex flex-col" on:submit|preventDefault={addDelivery}>
    <AddCard {delivery} />
    <input
        type="submit"
        value="Adicionar"
        class="cursor-pointer hover:font-semibold self-end mt-6"/>
    </form>
</main>
