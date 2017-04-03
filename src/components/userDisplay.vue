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
                displayUser: {}
            }
        },
        methods: {
            fetchData() {
                this.$http.get('http://vuejs.magicalexwuff.com:5000/api/v1/users{/id}.json', {params: {id: this.id}})
                    .then(response => {
                        this.displayUser = response.body.data.attributes;
                        eventBus.$emit('displayUser', this.displayUser);
                    }, error => {
                        console.log(error);
                        this.danger = "User id not found!";
                        eventBus.$emit('danger', this.danger);
                        this.successClass = false;
                        eventBus.$emit('successClass', this.successClass);
                        this.showSuccess = true;
                        eventBus.$emit('showSuccess', this.showSuccess);
                    });
                this.successClass = true;
            }
        },
        created() {
            eventBus.$on('displayUser', (user) => {
                this.displayUser = user;
            })
        }
    }

</script>

<style>

</style>