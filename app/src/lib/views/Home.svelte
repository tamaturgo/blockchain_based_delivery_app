<script lang="ts">
    import { link } from "svelte-spa-router";
    import SearchField from "../components/SearchField.svelte";
    import { setContext } from "svelte";
    import Logo from "../components/Logo.svelte";

    let delivery = {
        id: "",
    };

    setContext("home", { searchDelivery });

    function searchDelivery(id: string) {
        delivery["id"] = id;
    }
</script>

<main class="w-80 flex flex-col mt-40 items-center">
    <a
        href="/add"
        use:link
        class="text-sm self-start cursor-pointer hover:font-semibold"
        >Adicionar</a
    >
    <Logo />
    <SearchField />
</main>
