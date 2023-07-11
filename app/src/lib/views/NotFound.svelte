<script>
    import SearchField from "../components/SearchField.svelte";
    import { link } from "svelte-spa-router";
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
    <div class="text-9xl mt-20 mb-14 opacity-50">:(</div>
    <div class="opacity-50">Encomenda não encontrada</div>
</body>
