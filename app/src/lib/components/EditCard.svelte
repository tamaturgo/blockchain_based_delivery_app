<script lang="ts">
    import {updateDeliveryStatus} from '../../stores'
    export let id: string;
</script>

<div
    class="flex flex-col w-80 p-6 my-6 gap-6 items-start rounded-xl text-black-text bg-[#FFF]"
>
    <h1 class="text-xl font-semibold">Encomenda</h1>
    <div class="flex flex-col items-start h-10 gap-2">
        <h2 class="font-semibold text-sm">ID do produto</h2>
        {id}
    </div>
    <input
        bind:value={$updateDeliveryStatus}
        minlength="3"
        placeholder="Novo status"
        class="border-background border-2 rounded-lg p-4 outline-none w-full h-full bg-[#FFF] text-black-text caret-blue-primary focus:border-blue-primary"
    />
</div>
