<template>
    <div class="panel panel-success">
        <div class="panel-heading">Status:
            <h3 class="panel-title">Success!</h3>
        </div>

        <div class="panel-body">{{ success }}</div>
    </div>
</template>

<script>

    export default {
        props: ['success'],
        data() {
            return {

            }
        }
    }
</script>

<style>

</style>