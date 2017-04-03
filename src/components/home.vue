<template>
    <app-content></app-content>
</template>

<script>
    import Content from './content.vue';

    export default {
        name: 'app',
        data () {
            return {
                msg: 'Welcome to Your Vue.js App'
            }
        },
        components: {
            appContent: Content
        }
    }
</script>

<style>

</style>