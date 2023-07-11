<script>
import Router from 'svelte-spa-router'
    import Home from './lib/views/Home.svelte'
import Add from './lib/views/Add.svelte';
    import SearchField from './lib/components/SearchField.svelte';
    import Search from './lib/views/Search.svelte';
    import Edit from './lib/views/Edit.svelte';
    import NotFound from './lib/views/NotFound.svelte';

const routes = {
    '/': Home,
    '/add': Add,
    '/search/:id': Search,
    '/edit/:id': Edit,
    '*': NotFound
}
</script>

<main class="min-h-screen w-screen bg-background flex flex-col items-center gap-10 text-black-text">
    <Router {routes}/>
</main>
