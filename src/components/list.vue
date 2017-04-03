<template>
    <ul>
        <li v-for="user in users"></li>
    </ul>
</template>

<script>
    import { eventBus } from '../main';
export default {
    data() {
        return {
            users: []
        }
    },
    created() {
        eventBus.$on('usersArray', (users) => {
            this.users = users;
        })
    }
}
</script>

<style>

</style>