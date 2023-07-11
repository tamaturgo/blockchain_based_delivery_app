
<script>
    import EditCard from "../components/EditCard.svelte";
import SearchCard from "../components/SearchCard.svelte";
    import SearchField from "../components/SearchField.svelte";
    import { link } from "svelte-spa-router";

    export let params = {};
</script>

<body class="w-80 flex flex-col mt-40">
    <a
        use:link
        href="/"
        class="text-sm self-start cursor-pointer hover:font-semibold"
        >Cancelar</a
    >
    <img src="/src/assets/CRYPTOpost.svg" alt="Logo" class="my-6" />
    <SearchField />
    <EditCard id={params.id}/>
    <a
        href={"/edit/" + params.id}
        use:link
        class="cursor-pointer hover:font-semibold self-end">Concluir</a
    >
</body>
