<script lang="ts">
    import { onMount } from "svelte";
    import SearchCard from "../components/SearchCard.svelte";
    import SearchField from "../components/SearchField.svelte";
    import { link, replace } from "svelte-spa-router";
    import Logo from "../components/Logo.svelte";

    export let params:any = {};

    let status: any;
    let id: string;
    let name: string;

    onMount(async () => {
        const response = await fetch(
            "http://localhost:5000/delivery/search?product=" + params.id
        );

        if (response.status != 200) replace("/");

        const blocks = await response.json();
        status = blocks.map((block:Object) => [
            block["data"]["status"],
            block["timestamp"],
        ]);
        id = blocks[0]["data"]["product_id"];
        name = blocks[0]["data"]["product"];
    });

    $: params && document.location.reload()
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
    {#if status != undefined}
        <SearchCard {id} {name} {status} />
        <a
            href={"/edit/" + params.id}
            use:link
            class="cursor-pointer hover:font-semibold self-end">Editar</a
        >
    {/if}
</body>
