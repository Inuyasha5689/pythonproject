<template>
    <div>
        <app-header></app-header>
        <app-content class="container"></app-content>
    </div>
</template>

<script>
    import Header from './header.vue';
    import Content from './content.vue';

    export default {
        name: 'app',
        data () {
            return {
                msg: 'Welcome to Your Vue.js App'
            }
        },
        components: {
            appHeader: Header,
            appContent: Content
        }
    }
</script>

<style>

</style>