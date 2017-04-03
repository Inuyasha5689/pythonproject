<template>
    <ul>
        hello
        <li v-for="user in users">
            <p>{{ user.attributes.firstName }}</p>
            <p>{{ user.attributes.lastName }}</p>
            <p>{{ user.attributes.email }}</p>
            <p>{{ user.attributes.age }}</p>
            <p>{{ user.attributes.id }}</p>
        </li>
    </ul>
</template>

<script>
    import { eventBus } from '../main';
export default {
    props: [
        'usersArray'
    ],
    data() {
        return {
            users: []
        }
    },
    methods: {
       log() {
           console.log(this.users);
       }
    },
    beforeUpdate() {
        eventBus.$on('usersArray', users => {
            this.users = users;
            console.log(users);
        });
    }
}
</script>

<style>

</style>