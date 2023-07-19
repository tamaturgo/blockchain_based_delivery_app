<script lang="ts">
    import { link, push } from "svelte-spa-router";
    import AddCard from "../components/AddCard.svelte";
    import Logo from "../components/Logo.svelte";
    import { routes } from "../../routes";
    import axios from "axios";

    let delivery = {
        product: "",
        product_id: 0,
        sender: "",
        receiver: "",
        amount: 1,
    };

    async function addDelivery() {
        axios
            .post(routes.add, delivery)
            .then((res) =>
                push("/search/" + res["data"]["product_id"]).then((_) =>
                    alert("Encomenda adicionada com sucesso")
                )
            )
            .catch((_) => {
                alert("Não foi possível adicionar a encomenda");
                push("/");
            });
    }
</script>

<main class="mt-40 w-80 flex flex-col items-center">
    <a
        href="/"
        use:link
        class="text-sm self-start cursor-pointer hover:font-semibold"
        >Cancelar</a
    >
    <Logo />
    <form
        name="add"
        class="w-full flex flex-col"
        on:submit|preventDefault={addDelivery}
    >
        <AddCard {delivery} />
        <input
            type="submit"
            value="Adicionar"
            class="cursor-pointer hover:font-semibold self-end mt-6"
        />
    </form>
</main>
