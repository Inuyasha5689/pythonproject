<template>
    <app-user-display></app-user-display>
</template>

<script>
    import UserDisplay from './userDisplay.vue';
    import List from './list.vue';

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
            appList: List
        }
    }
</script>

<style>

</style>