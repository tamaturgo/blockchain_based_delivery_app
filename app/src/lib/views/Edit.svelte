<script>
    import EditCard from "../components/EditCard.svelte";
    import Logo from "../components/Logo.svelte";
    import SearchField from "../components/SearchField.svelte";
    import { link, pop } from "svelte-spa-router";

    export let params = {};
</script>

<body class="w-80 flex flex-col mt-40">
    <button
        on:click={pop}
        class="text-sm self-start cursor-pointer hover:font-semibold"
        >Cancelar</button
    >
    <Logo />
    <SearchField />
    <EditCard id={params.id} />
    <a
        href={"/edit/" + params.id}
        use:link
        class="cursor-pointer hover:font-semibold self-end">Concluir</a
    >
</body>
