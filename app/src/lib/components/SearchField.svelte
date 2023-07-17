<script lang="ts">
    import axios from "axios";
    import { replace } from "svelte-spa-router";
    import { routes } from "../../routes";
    import { searchedDelivery } from "../../stores.js";
    const placeholder: string = "Pesquisar encomenda";
    let value: string = "";

    function parseDelivery(data) {
        let delivery = {
            id: "",
            name: "",
            status: "",
        };
        delivery.status = data.map((block: Object) => [
            block["data"]["status"],
            block["timestamp"],
        ]);
        delivery.id = data[0]["data"]["product_id"];
        delivery.name = data[0]["data"]["product"];
        return delivery;
    }

    function handleSearch() {
        axios
            .get(routes.search + value)
            .then((res) => ($searchedDelivery = parseDelivery(res["data"])))
            .then((_) => replace("/search/" + $searchedDelivery.name))
            .catch((_) =>
                replace("/not-found").then((_) => ($searchedDelivery = {}))
            );
    }
</script>

<form
    on:submit={handleSearch}
    class="w-full h-16 p-4 gap-4 bg-[#FFFFFF] rounded-lg flex items-center hover:cursor-text"
>
    <button type="submit">
        <img src="Search.svg" alt="Search icon" />
    </button>
    <input
        {placeholder}
        minlength="2"
        bind:value
        class="border-none outline-none w-full h-full bg-[#FFF] text-black-text caret-blue-primary"
    />
</form>
