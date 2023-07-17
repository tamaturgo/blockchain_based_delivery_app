<script lang="ts">
    import SearchCard from "../components/SearchCard.svelte";
    import SearchField from "../components/SearchField.svelte";
    import {searchedDelivery} from "../../stores"
    import { link } from "svelte-spa-router";
    import Logo from "../components/Logo.svelte";

</script>

<main class="w-80 flex flex-col items-center mt-20">
    <a
        use:link
        href="/add"
        class="text-sm self-start cursor-pointer hover:font-semibold"
        >Adicionar</a
    >
    <Logo />
    <SearchField />
    <SearchCard />
    <a
        href={"/edit/" + $searchedDelivery.name}
        use:link
        class="cursor-pointer hover:font-semibold self-end">Editar</a
    >
</main>
