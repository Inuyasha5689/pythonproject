<template>
    <div>
        <app-user-display @listofusers="users = $event"></app-user-display>

    </div>
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