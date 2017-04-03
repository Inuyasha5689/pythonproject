<template>
    <div>
        <app-header></app-header>
        <app-content></app-content>
    </div>
</template>

<script>
    import Content from './content.vue';
    import Header from './header.vue';

    export default {
        name: 'app',
        data () {
            return {
                msg: 'Welcome to Your Vue.js App'
            }
        },
        components: {
            appContent: Content,
            appHeader: Header
        }
    }
</script>

<style>

</style>