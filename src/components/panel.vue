<template>
    <div class="panel col-xs-12" :class="panelClasses" key="panel" style="position: absolute;">
        <div class="panel-heading" key="heading">Status:
            <h3 class="panel-title">Success!</h3>
        </div>

        <div class="panel-body" key="body">{{ danger }}</div>
    </div>
</template>

<script>

    export default {
        props: [
            'success',
            'danger',
            'successClass'
        ],
        data() {
            return {

            }
        },
        methods:{

        },
        computed: {
            panelClasses: function() {
                return {
                    'panel-success': this.successClass,
                    'panel-danger': !this.successClass
                }
            }
        }
    }
</script>

<style>

</style>