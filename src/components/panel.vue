<template>
    <div class="panel panel-default"  :class="panelClasses" key="panel" style="">
        <div class="panel-heading" :class="panelClasses">Status:
            <h3 class="panel-title" :class="panelClasses">{{ heading }}</h3>
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

<style scoped="true">
    .panel {
        padding-left: 0px;
        padding-right: 0px;
    }

</style>