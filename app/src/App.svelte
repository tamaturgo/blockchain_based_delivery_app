<script>
import {Router, Route} from 'svelte-routing'
import Home from './lib/views/Home.svelte'

export let url = '/'
</script>

<Router {url}>
    <div>
        <Route path='/'><Home/></Route>
    </div>
</Router>
