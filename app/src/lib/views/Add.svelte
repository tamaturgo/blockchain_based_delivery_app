<script lang="ts">
    import { link } from "svelte-spa-router";
    import AddCard from "../components/AddCard.svelte";
</script>

<main class="mt-40 w-80 flex flex-col items-center">
    <a
        href="/"
        use:link
        class="text-sm self-start cursor-pointer hover:font-semibold"
        >Cancelar</a
    >
    <img src="/src/assets/CRYPTOpost.svg" alt="Logo" class="my-6" />
    <AddCard />
    <div class="cursor-pointer hover:font-semibold self-end mt-6">
        Adicionar
    </div>
</main>
