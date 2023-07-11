<script lang="ts">
    import { push } from "svelte-spa-router";
    const placeholder: string = "Pesquisar encomenda";
    let field: any;
    let value: string = "";

    function handleSearch(e: KeyboardEvent) {
        if (e.key == "Enter") {
            push("/search/" + value);
        }
    }
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div
    on:click={() => field.focus()}
    class="w-full h-16 p-4 gap-4 bg-[#FFFFFF] rounded-lg flex items-center hover:cursor-text"
>
    <img
        src="/src/assets/Search.svg"
        on:keypress={handleSearch}
        alt="Search icon"
    />
    <input
        {placeholder}
        bind:this={field}
        bind:value
        on:keypress={handleSearch}
        class="border-none outline-none w-full h-full bg-[#FFF] text-black-text caret-blue-primary"
    />
</div>
