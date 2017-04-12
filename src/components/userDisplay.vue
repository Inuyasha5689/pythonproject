<template>
    <div class="row col-xs-12 col-md-6" style="display: inline-block; position: relative;">
        <ul class="list-group">
            <li class="list-group-item">
                <h3>This is the user you pulled from the database</h3>
                <hr>
                <div class="">
                    <label>First Name:</label>    <p style="display: inline-block">{{ displayUser.firstName }}</p>
                </div>
                <br>
                <div>
                    <label>Last Name:</label> <p style="display: inline-block">{{ displayUser.lastName }}</p>
                </div>
                <br>
                <div>
                    <label>Email:</label> <p style="display: inline-block">{{ displayUser.email }}</p>
                </div>
                <br>
                <div>
                    <label>Age:</label> <p style="display: inline-block">{{ displayUser.age }}</p>
                </div>
                <br>
                <div>
                    <label>Birth Date:</label> <p style="display: inline-block">{{ displayUser.birthDate }}</p>
                </div>
                <br>
                <div>
                    <label>Zipcode:</label> <p style="display: inline-block">{{ displayUser.zipcode }}</p>
                </div>
            </li>
            <br>
            <li>
                <div class="form-group">
                    <label>Please enter the id number of the person's data that you wanna pull from the database</label>
                    <input class="form-control" type="number" v-model="id" min="1"/>
                </div>
            </li>
            <div class="btn btn-group" style="border-right: px">
                <button @click="fetchData" class="btn btn-primary">Get Data</button>
                <button @click="deleteUser" class="btn btn-danger">Delete Currently Displayed User</button>
            </div>
        </ul>
    </div>

</template>

<script>
    import { eventBus } from '../main';

    export default {
        data() {
            return {
                danger: '',
                successClass: true,
                showSuccess: false,
                displayUser: {},
                emptyUser:{},
                id: 1
            }
        },
        methods: {
            emitData(danger, successClass, showSuccess) {
                eventBus.$emit('danger', this.danger);
                this.successClass = successClass;
                eventBus.$emit('successClass', this.successClass);
                this.showSuccess = showSuccess;
                eventBus.$emit('showSuccess', this.showSuccess);
            },
            fetchData() {
                this.$http.get('http://vuejs.magicalexwuff.com:5000/api/v1/users{/id}.json', {params: {id: this.id}})
                    .then(response => {
                        this.displayUser = response.body.data.attributes;
                        eventBus.$emit('displayUser', this.displayUser);
                    }, error => {
                        this.danger = "User id not found!";
                        eventBus.emitData(this.danger, false, true);
                    });
                this.successClass = true;
            },
            deleteUser() {
                this.$http.delete('http://vuejs.magicalexwuff.com:5000/api/v1/users{/id}.json', {params: {id: this.id}})
                    .then(response => {
                        this.success = "You have successfully deleted the user from the database!";
                        eventBus.$emit('success', this.success);
                        this.showSuccess = true;
                        eventBus.$emit('showSuccess', this.showSuccess);
                        this.successClass = true;
                        eventBus.$emit('successClass', this.successClass);
                        this.displayUser = this.emptyUser;
                    }, error => {
                        this.danger = "unable to delete the user";
                        eventBus.emitData(this.danger, false, true);

                    });
                this.successClass = true;
            }
        },
        created() {
            eventBus.$on('displayUser', (user) => {
                this.displayUser = user;
            });
            eventBus.$on('emptyUser', (user) => {
                this.emptyUser = user;
            });
        }
    }

</script>

<style>

</style>