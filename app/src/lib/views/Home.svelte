<script lang="ts">
    import {link} from 'svelte-spa-router'
    import SearchField from "../components/SearchField.svelte";
    import { setContext } from "svelte";

    let delivery = {
        'id': ''
    }
    
    setContext('home', { searchDelivery})

    function searchDelivery(id : string) {
        delivery['id'] = id
    }
</script>

<body class="w-80 flex flex-col mt-40">
    <a use:link={'/add'} class="text-sm self-start cursor-pointer hover:font-semibold">Adicionar</a>
    <img src="/src/assets/CRYPTOpost.svg" alt="Logo" class="my-6"/>
    <SearchField/>
</body>

