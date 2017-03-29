<template>
    <div style="display: block; margin: auto; position: relative">
        <div class="row col-md-6">
            <div class="form-group">
                <label>First Name</label>
                <input class="form-control" v-model="inputUser.data.attributes.firstName"/>
            </div>
            <div class="form-group">
                <label>Last Name</label>
                <input class="form-control" v-model="inputUser.data.attributes.lastName">
            </div>
            <div class="form-group">
                <label>Email</label>
                <input class="form-control" type="email" v-model="inputUser.data.attributes.email"/>
            </div>
            <div class="form-group">
                <label>Age</label>
                <input class="form-control" type="number" v-model="inputUser.data.attributes.age"/>
            </div>
            <div class="form-group">
                <label>Birth Date</label>
                <input class="form-control" type="date" v-model="inputUser.data.attributes.birthDate"/>
            </div>
            <div class="form-group">
                <label>Zip Code</label>
                <input class="form-control" type="number" v-model="inputUser.data.attributes.zipcode"/>
            </div>
            <div class="btn btn-group">
                <button @click="submit" class="btn btn-primary">Submit User</button>
                <button @click="updateUser" class="btn btn-warning">Update User</button>
            </div>
        </div>
        <div class="row col-md-5 pull-right" style="padding-top: 5px; display: inline-block">
            <ul class="list-group">
                <li class="list-group-item" style="padding-top: 5px">
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
                        <input class="form-control" type="number" v-model="id" min="1" :max="usersLength"/>
                    </div>
                </li>
                <div class="btn btn-group">
                    <button @click="fetchData" class="btn btn-primary">Get Data</button>
                    <button @click="deleteUser" class="btn btn-danger">Delete Currently Displayed User</button>
                </div>
            </ul>

        </div>
        <transition name="bounce">
            <app-panel :success="success" v-show="showSuccess"></app-panel>
        </transition>
    </div>
</template>

<script>
    import Panel from './panel.vue';
    export default {
        data() {
            return {

                inputUser: {
                    data: {
                        attributes: {
                            firstName: '',
                            lastName: '',
                            email: '',
                            age: null,
                            birthDate: '',
                            zipcode: null
                        },
                        id: null,
                        type: "users"
                    }
                },
                displayUser: {},
                emptyUser: {
                    data: {
                        attributes: {
                            firstName: '',
                            lastName: '',
                            email: '',
                            age: null,
                            birthDate: '',
                            zipcode: null
                        },
                        id: null,
                        type: "users"
                    }
                },
                users: [],
                id: 0,
                usersLength: 1,
                showSuccess: false,
                success: ''
            }
        },
        methods: {
            fetchData() {
                this.$http.get('http://localhost:5000/api/v1/users{/id}.json', {params: {id: this.id}})
                    .then(response => {
                        this.displayUser = response.body.data.attributes;
                    })
            },
            submit() {
                console.log(this.inputUser);
                this.$http.post('http://localhost:5000/api/v1/users.json', this.inputUser)
                    .then(response => {
                        console.log(response.data.id);
                    }, error => {
                        console.log(error);
                    });
                this.user = this.emptyUser;
                usersLengthFunc();
            },
            updateUser() {
                this.$http.patch('http://localhost:5000/api/v1/users{/id}.json', this.inputUser, {params: {id: this.id}})
                    .then(response => {
                        this.inputUser = this.emptyUser;
                        this.success = "Your user info has successfully been updated!";
                        this.showSuccess = true;
                    }, error => {
                        console.log(this.id);
                        console.log(error);
                    })
            },
            deleteUser() {
                this.$http.delete('http://localhost:5000/api/v1/users{/id}.json', {params: {id: this.id}})
                    .then(response => {
                        console.log(response);
                        this.displayUser = this.emptyUser;
                    }, error => {
                        console.log(error);
                    });
            },
        },

        mounted() {
            this.$http.get('http://localhost:5000/api/v1/users.json')
                .then(response => {
                    return response.body.data
                })
                .then(function (data) {
                    const resultArray = [];
                    for (let key in data) {
                        resultArray.push(data[key]);
                    }
                    this.usersLengthFunc = function () {
                        this.users = resultArray;
                        console.log(this.users);
                        this.usersLength = this.users.length;
                        console.log(this.usersLength);
                    };
                    usersLengthFunc();
                })
        },
        components: {
            appPanel: Panel
        }
    }

</script>

<style>

    .bounce-enter-active {
        animation: bounce-in 1s;
    }
    .bounce-leave-active {
        animation: bounce-out 1s;
    }
    @keyframes bounce-in {
        0% {
            transform: scale(0);
        }
        50% {
            transform: scale(1.5);
        }
        100% {
            transform: scale(1);
        }
    }
    @keyframes bounce-out {
        0% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.5);
        }
        100% {
            transform: scale(0);
        }
    }

</style>