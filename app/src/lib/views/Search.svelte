<script>
    import SearchCard from "../components/SearchCard.svelte";
    import SearchField from "../components/SearchField.svelte";
    import { link } from "svelte-spa-router";

    export let params = {};
</script>

<body class="w-80 flex flex-col mt-40">
    <a
        use:link
        href="/add"
        class="text-sm self-start cursor-pointer hover:font-semibold"
        >Adicionar</a
    >
    <img src="/src/assets/CRYPTOpost.svg" alt="Logo" class="my-6" />
    <SearchField />
    <SearchCard id={params.id} />
    <a
        href={"/edit/" + params.id}
        use:link
        class="cursor-pointer hover:font-semibold self-end">Editar</a
    >
</body>
