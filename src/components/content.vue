<template>
    <div>
        <app-user-display @listofusers="users = $event"></app-user-display>
        <app-user-input :users="users"></app-user-input>
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