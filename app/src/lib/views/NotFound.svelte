<script>
    import Logo from "../components/Logo.svelte";
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
    <Logo />
    <SearchField />
    <div class="text-9xl mt-20 mb-14 opacity-50">:(</div>
    <div class="opacity-50">Encomenda não encontrada</div>
</body>
