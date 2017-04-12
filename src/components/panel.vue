<template>
    <div class="panel panel-default col-xs-12 col-md-6npm"  :class="panelClasses" key="panel" style="">
        <div class="panel-heading" :class="panelClasses">Status:
            <h3 class="panel-title" :class="panelClasses">{{ heading }}</h3>
        </div>

        <div class="panel-body" key="body">{{ message }}</div>
    </div>
</template>

<script>

    export default {
        props: [
            'status',
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
                if (this.status !== '') {
                    this.message = this.status[1];
                    this.heading = this.status[0];
                } else {
                    this.message = this.status[1];
                    this.heading = this.status[0];
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