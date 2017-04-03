<template>
    <div><app-user-display></app-user-display>
    <app-user-input></app-user-input></div>
</template>

<script>
    import UserDisplay from './userDisplay.vue';
    import UserInput from './userInput.vue';
    import { eventBus } from '../main';

    export default {
        data() {
            return {

            }
        },
        components: {
            appUserDisplay: UserDisplay,
            appUserInput: UserInput
        }
    }

</script>

<style>

</style>