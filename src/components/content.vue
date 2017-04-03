<template>
    <app-user-display></app-user-display>
</template>

<script>
    import UserDisplay from './userDisplay.vue';

    export default {
        data() {
            return {
                users: []
            }
        },
        methods: {

        },

        components: {
            appUserDisplay: UserDisplay,
        }
    }
</script>

<style>

</style>