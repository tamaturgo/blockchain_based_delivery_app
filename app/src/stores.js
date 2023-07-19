import { writable } from "svelte/store";

export const updateDeliveryStatus = writable('')

export const searchedDelivery = writable({
    id: '',
    name: '',
    status: [],
    sender: '',
    receiver: ''
})
