<template>
    <div class="myclass">
        <div class="row col-xs-12 col-md-6" style="display: inline-block; position: relative;">
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
            <div class="btn btn-group zipcode">
                <button @click="submit" class="btn btn-primary">Submit User</button>
                <button @click="updateUser" class="btn btn-warning">Update User</button>
            </div>
        </div>
        <transition name="bounce" mode="out-in" @afterEnter="afterEnter">
            <app-panel :successClass="successClass" :status="status" v-if="showSuccess" class=" col-xs-12 col-md-6" key="component" ></app-panel>
        </transition>
    </div>
</template>

<script>
    import Panel from './panel.vue';
    import { ErrorBag } from 'vee-validate';
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
                dangerArray: [],
                successClass: true,
                nextPostId: [],
                status: []
            }
        },
        methods: {
            emitData(status, successClass, showSuccess) {
                eventBus.$emit('status', status);
                this.successClass = successClass;
                eventBus.$emit('successClass', this.successClass);
                this.showSuccess = showSuccess;
                eventBus.$emit('showSuccess', this.showSuccess);
            },
            submit() {
                this.$http.post('http://vuejs.magicalexwuff.com:5000/api/v1/users.json', this.inputUser)
                    .then(response => {
                        this.inputUser = this.emptyUser;
                        this.status = ["Success","You have successfully added your user info to the database! If you would like to change or delete it later please use the id number: "+ response.data.data.id];
                        this.emitData(this.status, true, true);
                    }, error => {
                        this.status=["Error","Make sure all the fields are filled before you submit!"];
                        this.emitData(this.status, false, true);
                    })
                    .then(() => {
                        this.errors.clear();
                    });
                this.$emit('clear');
                this.user = this.emptyUser;
                this.usersLengthFunc();
            },
            updateUser() {
                this.$http.patch('http://vuejs.magicalexwuff.com:5000/api/v1/users{/id}.json', this.inputUser, {params: {id: this.id}})
                    .then(response => {
                        this.inputUser = this.emptyUser;
                        this.status = ["Success","You have successfully updated the selected user!"];
                        this.emitData(this.status, true, true);

                    }, error => {
                        this.status = ["Error","1 or more fields have not been entered. Please make sure all fields are filled."];
                        this.emitData(this.status, false, true);
                    });
                this.successClass = true;
            },
            afterEnter(el) {
                let vm = this;
                setTimeout(function () {
                    vm.showSuccess = false;
                }, 4000)
            },
            displayError(error) {
                let vm = this;
                vm.danger = error.data.message;
                vm.successClass = false;
                vm.showSuccess = true;
            }
        },
        computed: {
            firstName() {return this.inputUser.data.attributes.firstName;},
            lastName() {return this.inputUser.data.attributes.lastName;},
            email() {return this.inputUser.data.attributes.email;},
            age() {return this.inputUser.data.attributes.age;},
            birthDate() {return this.inputUser.data.attributes.birthDate;},
            zipcode() {return this.inputUser.data.attributes.zipcode}

        },

        mounted() {
            this.$http.get('http://vuejs.magicalexwuff.com:5000/api/v1/users.json')
                .then(response => {
                    return response.body.data
                }, error =>{
                    this.displayError(error);
                })
                .then(function (data) {
                    const resultArray = [];
                    for (let key in data) {
                        resultArray.push(data[key]);
                    }
                    this.usersLengthFunc = function () {
                        this.users = resultArray;
                        this.$set(this.users, this.users);
                        this.usersLength = this.users.length;
                        eventBus.$emit('usersArray', this.users);

                    };
                    this.usersLengthFunc();
                    eventBus.$emit('emptyUser', this.emptyUser);

                })


        },
        created() {
          eventBus.$on('status', (status) => {
              this.status = status;
          });
          eventBus.$on('successClass', (successClass) => {
              this.successClass = successClass;
          });
          eventBus.$on('showSuccess', (showSuccess) => {
              this.showSuccess = showSuccess;
          });
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

    .myclass {
        margin-left: 10px;
    }

    .zipcode {
        margin-left: -12px;
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