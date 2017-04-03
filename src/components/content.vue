<template>
    <app-user class=""></app-user>
</template>

<script>
    import User from './User.vue';

    export default {
        data() {
            return {
                users: []
            }
        },
        methods: {

        },

        components: {
            appUser: User
        }
    }
</script>

<style>

</style>