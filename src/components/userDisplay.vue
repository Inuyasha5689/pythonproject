<template>
    <div style="display: block;">
        <div class="row col-md-6">
            <div class="form-group has-icon has-icon-right">
                <label>First Name</label>
                <input class="form-control" v-validate:firstName="'required|alpha|min:3|max:20'" name="firstName" type="text"
                       v-model="inputUser.data.attributes.firstName" :class="{'input': true, 'is-danger': errors.has('firstName') }"/>
                <i v-show="errors.has('firstName')" class="fa fa-warning"></i>
                <span v-show="errors.has('firstName')" class="help is-danger">{{ errors.first('firstName') }}</span>
            </div>
            <div class="form-group has-icon has-icon-right">
                <label>Last Name</label>
                <input class="form-control" v-validate:lastName="'required|alpha|min:3|max:20'" name="lastName" type="text"
                       v-model="inputUser.data.attributes.lastName" :class="{'input': true, 'is-danger': errors.has('lastName') }">
                <i v-show="errors.has('lastName')" class="fa fa-warning"></i>
                <span v-show="errors.has('lastName')" class="help is-danger">{{ errors.first('lastName') }}</span>
            </div>
            <div class="form-group has-icon has-icon-right">
                <label>Email</label>
                <input class="form-control" v-validate:email="'required|email|max:50'" name="email" type="email"
                       v-model="inputUser.data.attributes.email" :class="{'input': true, 'is-danger': errors.has('email') }"/>
                <i v-show="errors.has('email')" class="fa fa-warning"></i>
                <span v-show="errors.has('email')" class="help is-danger">{{ errors.first('email') }}</span>
            </div>
            <div class="form-group has-icon has-icon-right">
                <label>Age</label>
                <input class="form-control" v-validate:age="'required|max_value:99'" name="age" type="number"
                       v-model="inputUser.data.attributes.age" min="1" max="99" :class="{'input': true, 'is-danger': errors.has('age') }"/>
                <i v-show="errors.has('age')" class="fa fa-warning"></i>
                <span v-show="errors.has('age')" class="help is-danger">{{ errors.first('age') }}</span>
            </div>
            <div class="form-group has-icon has-icon-right">
                <label>Birth Date</label>
                <input class="form-control" v-validate:birthDate="'required|date_format:YYYY-MM-DD'" name="birthDate"
                       type="date" v-model="inputUser.data.attributes.birthDate" :class="{'input': true, 'is-danger': errors.has('birthDate') }"/>
                <i v-show="errors.has('birthDate')" class="fa fa-warning"></i>
                <span v-show="errors.has('birthDate')" class="help is-danger">{{ errors.first('birthDate') }}</span>
            </div>
            <div class="form-group has-icon has-icon-right">
                <label>Zip Code</label>
                <input class="form-control" v-validate:zipcode="'required|numeric|min:4'" name="zipcode" type="number"
                       v-model="inputUser.data.attributes.zipcode" :class="{'input': true, 'is-danger': errors.has('zipcode') }"/>
                <i v-show="errors.has('zipcode')" class="fa fa-warning"></i>
                <span v-show="errors.has('zipcode')" class="help is-danger">{{ errors.first('zipcode') }}</span>
            </div>
            <div class="btn btn-group">
                <button @click="submit" class="btn btn-primary">Submit User</button>
                <button @click="updateUser" class="btn btn-warning">Update User</button>
            </div>
        </div>
        <transition name="bounce" mode="out-in" @afterEnter="afterEnter" class="row">
            <app-panel :success="success" :successClass="successClass" :danger="danger" v-if="showSuccess" key="component" style="position: relative"></app-panel>
        </transition>
        <div class="row col-md-5 pull-right" style="padding-top: 5px; display: inline-block; position: relative;">
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

    </div>
</template>

<script>
    import Panel from './panel.vue';
    import {eventBus} from  '../main';
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
                success: '',
                danger: [],
                successClass: true,
                User: new eventBus.methods.UserClass().User.constructor
            }
        },
        methods: {
            fetchData() {
                this.$http.get('http://vuejs.magicalexwuff.com:5000/api/v1/users{/id}.json', {params: {id: this.id}})
                    .then(response => {
                        this.displayUser = response.body.data.attributes;
                    })
            },
            submit() {
                console.log(this.inputUser);
                this.$http.post('http://vuejs.magicalexwuff.com:5000/api/v1/users.json', this.inputUser)
                    .then(response => {
                        this.inputUser = this.emptyUser;
                        this.success = "You have successfully added your user info to the database! If you would like to change or delete it later please use the id number: "+ response.attributes.id;
                        this.showSuccess = true;
                    }, error => {
                        console.log(error);
                    });
                this.user = this.emptyUser;
                usersLengthFunc();
            },
            updateUser() {
                this.$http.patch('http://vuejs.magicalexwuff.com:5000/api/v1/users{/id}.json', this.inputUser, {params: {id: this.id}})
                    .then(response => {
                        this.inputUser = this.emptyUser;
                        this.success = "";
                        this.showSuccess = true;
                    }, error => {
                        for (let i = 0; i < error.body.error.errors.length; i++){
                            this.danger.push(error.body.error.errors[i].detail);
                        }
                        this.successClass = false;
                        this.showSuccess = true;
                    });
            },
            deleteUser() {
                this.$http.delete('http://vuejs.magicalexwuff.com:5000/v1/users{/id}.json', {params: {id: this.id}})
                    .then(response => {
                        console.log(response);
                        this.displayUser = this.emptyUser;
                    }, error => {
                        console.log(error);
                    });
            },
            afterEnter(el) {
                let vm = this;
                setTimeout(function () {
                    vm.showSuccess = false;
                }, 3000)
            }
        },
        computed: {
            firstName() {return this.inputUser.data.attributes.firstName;},
            lastName() {return this.inputUser.data.attributes.lastName;},
            email() {return this.inputUser.data.attributes.email;},
            age() {return this.inputUser.data.attributes.age;},
            birthDate() {console.log(this.inputUser.data.attributes.birthDate); return this.inputUser.data.attributes.birthDate;},
            zipcode() {return this.inputUser.data.attributes.zipcode}

        },

        mounted() {
            this.$http.get('http://vuejs.magicalexwuff.com:5000/api/v1/users.json')
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
                    this.usersLengthFunc();
                })
        },
        created() {
          console.log(this.User);
        },
        components: {
            appPanel: Panel
        }
    }

</script>

<style scoped="true">

    .is-danger {
        border-color: red;
    }

    .bounce-enter-active {
        animation: bounce-in 1s;
    }

    .bounce-leave-active {
        animation-delay: 3s;
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
            opacity: 1;
        }
        50% {
            transform: scale(1.5);
            opacity: .5;
        }
        100% {
            transform: scale(0);
            opacity: 0;
        }
    }

</style>