<template>
    <div class="panel col-xs-12" :class="panelClasses" key="panel" style="position: absolute;">
        <div class="panel-heading" key="heading">Status:
            <h3 class="panel-title">{{ heading }}</h3>
        </div>

        <div class="panel-body" key="body">{{ message }}</div>
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
                message: '',
                heading: ''
            }
        },
        methods:{
            panelMessage: function () {
                if (this.success !== '') {
                    this.message = this.success;
                    this.heading = 'Success!';
                } else {
                    this.message = this.danger;
                    this.heading = 'Error!';
                }
            }
        },
        computed: {
            panelClasses: function() {
                return {
                    'panel-success': this.successClass,
                    'panel-danger': !this.successClass
                }
            }
        },
        created() {
            this.panelMessage();
        }
    }
</script>

<style>

</style>