<script lang="ts">
    import {getContext} from 'svelte'

    const placeholder:string = 'Pesquisar encomenda'
    let field : any
    let value : string = ''

    const { searchDelivery } = getContext('home')

    function handleSearch(e : KeyboardEvent) {
        if (e.key == 'Enter' && value != '') {
            searchDelivery(value)
        }
    }

</script>
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div on:click={() => field.focus()} class='w-80 h-16 p-4 gap-4 bg-[#FFFFFF] rounded-xl flex items-center hover:cursor-text'>
    <img src="/src/assets/Search.svg" alt="Search icon" on:click={() => searchDelivery(field)}/>
    <input placeholder={placeholder} bind:this={field} bind:value={value} on:keypress={handleSearch} class="border-none outline-none w-full h-full bg-[#FFF] text-black-text caret-blue-primary"/>
</div>

