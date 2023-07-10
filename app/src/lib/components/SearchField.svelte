<script lang="ts">
    const placeholder:string = 'Pesquisar encomenda'
    let field:any
</script>
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
<form on:click={() => field.focus()} class='w-80 h-16 p-4 gap-4 bg-[#FFFFFF] rounded-xl flex items-center hover:cursor-text'>
    <img src="/src/assets/Search.svg" alt="Search icon"/>
    <input placeholder={placeholder} bind:this={field} class="border-none outline-none w-full h-full bg-[#FFF] text-black-text caret-blue-primary"/>
</form>
