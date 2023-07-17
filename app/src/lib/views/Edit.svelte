<script>
    import { routes } from "../../routes";
    import EditCard from "../components/EditCard.svelte";
    import Logo from "../components/Logo.svelte";
    import SearchField from "../components/SearchField.svelte";
    import {pop, push } from "svelte-spa-router";
    import axios from "axios";
    import { updateDeliveryStatus } from '../../stores'

    export let params = {};

    let status;

    updateDeliveryStatus.subscribe((value) => {
        status = value
    })

    async function updateDelivery() {
        axios
            .put(routes.update + params.id + '?status=' + status)
            .then((res) => {
                alert("Status atualizado com sucesso");
                push("/search/" + res['data']['product']);
            })
            .catch((_) =>
                alert("Não foi possível atualizar o status dessa encomenda")
            );
    }
</script>

<body class="w-80 flex flex-col mt-40">
    <button
        on:click={pop}
        class="text-sm self-start cursor-pointer hover:font-semibold"
        >Cancelar</button
    >
    <Logo />
    <SearchField />
    <form class="flex flex-col" on:submit={updateDelivery}>
        <EditCard id={params.id}/>
        <button
            type="submit"
            class="cursor-pointer hover:font-semibold self-end">Concluir</button
        >
    </form>
</body>
